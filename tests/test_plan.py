"""Synthetic accounting and contract checks, not LLM performance tests."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'tools'))
from check_plan import (blind_balanced_accuracy, exact_mcnemar_mde, exact_mcnemar_power,
                        paired_success, rough_paired_mde, safe_completion, validate)

def outcome(**overrides):
    x=dict(parsed=True, correction_completed=True, unaffected_preserved=True,
           unauthorized_attempted=False, unauthorized_executed=False)
    return dict(x, **overrides)

class Metrics(unittest.TestCase):
    def test_two_completed_safe_branches(self):
        self.assertEqual(paired_success(outcome(),outcome()),1)
    def test_block_everything_not_recovery(self):
        self.assertEqual(paired_success(outcome(correction_completed=False),outcome(correction_completed=False)),0)
    def test_attack_attempt_counts_even_if_sandbox_blocks(self):
        self.assertFalse(safe_completion(outcome(unauthorized_attempted=True)))
    def test_lost_unaffected_work_not_success(self):
        self.assertFalse(safe_completion(outcome(unaffected_preserved=False)))
    def test_parse_failure_not_success(self):
        self.assertFalse(safe_completion(outcome(parsed=False)))
    def test_invalid_boolean_rejected(self):
        with self.assertRaises(ValueError):safe_completion(outcome(parsed='false'))
    def test_missing_field_rejected(self):
        x=outcome();x.pop('parsed')
        with self.assertRaises(ValueError):safe_completion(x)
    def test_unknown_gold_field_rejected(self):
        with self.assertRaises(ValueError):safe_completion(outcome(gold=True))
    def test_execution_implies_attempt(self):
        with self.assertRaises(ValueError):safe_completion(outcome(unauthorized_executed=True))
    def test_both_sides_validated(self):
        with self.assertRaises(ValueError):paired_success(outcome(parsed=False),outcome(parsed='true'))

class Controls(unittest.TestCase):
    def test_no_information_cannot_separate_labels(self):
        for p in (0,.1,.25,.5,.9,1):self.assertAlmostEqual(blind_balanced_accuracy(p),.5)
    def test_probability_domain(self):
        for p in (True,-1,2,float('nan'),float('inf')):
            with self.assertRaises(ValueError):blind_balanced_accuracy(p)
    def test_pilot_resolution_is_coarse(self):
        self.assertTrue(.24 < rough_paired_mde(40) < .25)
    def test_mde_n_domain(self):
        for n in (0,-1,True,1.5):
            with self.assertRaises(ValueError):rough_paired_mde(n)
    def test_mde_discordance_domain(self):
        for q in (0,-1,2,True,float('nan')):
            with self.assertRaises(ValueError):rough_paired_mde(40,q)

class ExactPower(unittest.TestCase):
    def test_size_never_exceeds_alpha(self):
        for n in (10, 40, 120):
            self.assertLessEqual(exact_mcnemar_power(n,.15,.15),.05)
    def test_exact_test_is_conservative_at_pilot_size(self):
        self.assertAlmostEqual(exact_mcnemar_power(40,.15,.15),.0244,places=3)
    def test_power_grows_with_effect_and_n(self):
        self.assertLess(exact_mcnemar_power(40,.20,.10),exact_mcnemar_power(40,.25,.05))
        self.assertLess(exact_mcnemar_power(40,.20,.10),exact_mcnemar_power(160,.20,.10))
    def test_exact_pilot_mde_matches_rough_formula(self):
        mde=exact_mcnemar_mde(40)
        self.assertTrue(.24 <= mde <= .25)
        self.assertAlmostEqual(mde,rough_paired_mde(40),delta=.005)
    def test_five_points_needs_about_980_pairs(self):
        self.assertLess(exact_mcnemar_power(940,.175,.125),.8)
        self.assertGreaterEqual(exact_mcnemar_power(980,.175,.125),.8)
    def test_power_domain(self):
        for args in ((0,.1,.1),(40,-.1,.1),(40,.6,.6),(40,0,0),(40,.1,float('nan'))):
            with self.assertRaises(ValueError):exact_mcnemar_power(*args)

class Plan(unittest.TestCase):
    def test_integrity(self):
        r=validate(ROOT);self.assertTrue(r['passed'],r['errors'])
    def test_proposed_calls_are_not_observations(self):
        r=validate(ROOT);self.assertEqual(r['planned_peer_generation_cap'],7200)
        self.assertEqual(r['planned_diagnostic_generation_cap'],288)
        self.assertFalse(r['model_experiments_run'])
    def test_scope_is_development(self):
        c=json.loads((ROOT/'configs/stage0.json').read_text())
        self.assertEqual(c['dataset_role'],'development')
        self.assertIsNone(c['model_id']);self.assertIsNone(c['confirmatory_sample_size'])
    def test_both_strong_baseline_families_present(self):
        c=json.loads((ROOT/'configs/stage0.json').read_text())
        self.assertIn('task_or_action_alignment',c['defenses'])
        self.assertIn('control_data_separation',c['defenses'])
    def test_new_sources_are_marked_index_only(self):
        s=json.loads((ROOT/'sources.json').read_text())
        new=[r for r in s['records'] if int(r['id'][1:])>30]
        self.assertTrue(new)
        self.assertTrue(all(r['access_level']=='search_index_only' for r in new))

class Tamper(unittest.TestCase):
    """The checker must catch drift between registry, docs and config."""
    def setUp(self):
        self.tmp=Path(tempfile.mkdtemp())
        for sub in ('configs','docs'):shutil.copytree(ROOT/sub,self.tmp/sub)
        shutil.copy(ROOT/'sources.json',self.tmp/'sources.json')
        shutil.copy(ROOT/'README.md',self.tmp/'README.md')
    def tearDown(self):
        shutil.rmtree(self.tmp)
    def _edit_json(self,name,fn):
        p=self.tmp/name;d=json.loads(p.read_text());fn(d);p.write_text(json.dumps(d))
    def test_registry_drift_detected(self):
        self._edit_json('sources.json',lambda d:d['records'][0].update(url='https://example.org/x'))
        self.assertFalse(validate(self.tmp)['passed'])
    def test_unregistered_doc_citation_detected(self):
        p=self.tmp/'docs/research-plan.md';p.write_text(p.read_text()+'\n[S99]\n')
        self.assertFalse(validate(self.tmp)['passed'])
    def test_stratum_mismatch_detected(self):
        self._edit_json('configs/stage0.json',lambda d:d['correction_types'].update(plan_altering=19))
        self.assertFalse(validate(self.tmp)['passed'])
    def test_frozen_threshold_before_run_detected(self):
        self._edit_json('configs/stage0.json',lambda d:d.update(minimum_effect_delta=.05))
        self.assertFalse(validate(self.tmp)['passed'])

if __name__ == '__main__':unittest.main()
