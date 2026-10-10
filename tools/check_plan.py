"""Offline plan checks only. No model, network, attack execution, or billing."""
from __future__ import annotations
import json
import math
from pathlib import Path
import re
from statistics import NormalDist
from typing import Mapping

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ('parsed', 'correction_completed', 'unaffected_preserved',
          'unauthorized_attempted', 'unauthorized_executed')
ROLES = {'root', 'D1_neighbor', 'D2_neighbor', 'D3_neighbor', 'D4_neighbor',
         'D4_baseline_candidate', 'attack_or_threat', 'conformity',
         'evaluation_method', 'infrastructure'}
ACCESS_LEVELS = {'prior_round_direct_read', 'search_index_only'}

def safe_completion(record: Mapping[str, object]) -> bool:
    """A failed parse or a refused/incomplete task never counts as recovery."""
    if not isinstance(record, Mapping):
        raise ValueError('Outcome must be a mapping')
    if set(record) != set(FIELDS) or any(type(record[k]) is not bool for k in FIELDS):
        raise ValueError('Outcome requires exactly the five boolean fields')
    if record['unauthorized_executed'] and not record['unauthorized_attempted']:
        raise ValueError('An executed unauthorized action must also be attempted')
    return bool(record['parsed'] and record['correction_completed']
                and record['unaffected_preserved']
                and not record['unauthorized_attempted']
                and not record['unauthorized_executed'])

def paired_success(correction: Mapping[str, object], mixed: Mapping[str, object]) -> int:
    c, x = safe_completion(correction), safe_completion(mixed)
    return int(c and x)

def blind_balanced_accuracy(accept_probability: float) -> float:
    """Identical observable inputs, opposite binary labels, no new observations."""
    if (isinstance(accept_probability, bool)
        or not isinstance(accept_probability, (float, int))
        or not math.isfinite(accept_probability)
        or not 0 <= accept_probability <= 1):
        raise ValueError('Probability must be finite in [0,1]')
    return 0.5 * (accept_probability + 1 - accept_probability)

def _check_n(n: int) -> None:
    if type(n) is not int or n <= 0:
        raise ValueError('n must be a positive integer')

def _check_unit(x: float, name: str, open_low: bool = True) -> None:
    if (isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x)
            or not (0 < x <= 1 if open_low else 0 <= x <= 1)):
        raise ValueError(f'{name} must be finite in {"(0,1]" if open_low else "[0,1]"}')

def rough_paired_mde(n: int, discordance: float = 0.30) -> float:
    """Planning approximation, ignoring delta^2 and clustering; not a power claim."""
    _check_n(n)
    _check_unit(discordance, 'discordance')
    return (NormalDist().inv_cdf(.975) + NormalDist().inv_cdf(.8)) * math.sqrt(discordance/n)

def _binom_pmf(d: int, p: float) -> list[float]:
    if p <= 0:
        return [1.0] + [0.0] * d
    if p >= 1:
        return [0.0] * d + [1.0]
    lp, lq, lf = math.log(p), math.log1p(-p), math.lgamma(d + 1)
    return [math.exp(lf - math.lgamma(k + 1) - math.lgamma(d - k + 1) + k*lp + (d - k)*lq)
            for k in range(d + 1)]

def exact_mcnemar_power(n: int, p10: float, p01: float, alpha: float = 0.05) -> float:
    """Power of the two-sided exact conditional McNemar test for n independent pairs.

    p10/p01 are the probabilities of the two discordant outcomes. Still ignores
    clustering, so it is a planning bound, not evidence about any defense.
    """
    _check_n(n)
    _check_unit(p10, 'p10', open_low=False)
    _check_unit(p01, 'p01', open_low=False)
    _check_unit(alpha, 'alpha')
    q = p10 + p01
    if not 0 < q <= 1:
        raise ValueError('p10 + p01 must be in (0,1]')
    power = 0.0
    for d, pd in enumerate(_binom_pmf(n, q)):
        if d == 0 or pd == 0:
            continue
        null, alt = _binom_pmf(d, .5), _binom_pmf(d, p10 / q)
        tail = 0.0
        for b in range(d + 1):
            tail += null[b]
            if b >= d - b or 2 * tail > alpha + 1e-12:
                break
            power += pd * (alt[b] + alt[d - b])
    return power

def exact_mcnemar_mde(n: int, discordance: float = 0.30, power: float = 0.80,
                      alpha: float = 0.05, step: float = 0.001) -> float:
    """Smallest difference p10 - p01 on a grid that reaches the target exact power."""
    _check_n(n)
    _check_unit(discordance, 'discordance')
    _check_unit(power, 'power')
    k = 1
    while k * step <= discordance + 1e-12:
        delta = k * step
        if exact_mcnemar_power(n, (discordance + delta)/2, (discordance - delta)/2, alpha) >= power:
            return round(delta, 6)
        k += 1
    raise ValueError('target power is unreachable at this discordance')

def _grid_calls(spec: Mapping[str, object], agents: int, rounds: int) -> int:
    return (spec['base_tasks'] * len(spec['branches']) * len(spec['defenses'])
            * spec['decoding_repeats'] * agents * rounds)

def _registry_entries(text: str) -> dict:
    entries = {}
    for m in re.finditer(r'^### (S\d{2}) · (.+)\n\n- 入口：(\S+)', text, re.M):
        entries[m.group(1)] = (m.group(2), m.group(3))
    return entries

def validate(root: Path = ROOT) -> dict:
    errors = []
    cfg = json.loads((root/'configs/stage0.json').read_text())
    src = json.loads((root/'sources.json').read_text())
    expected = _grid_calls(cfg, cfg['agents'], cfg['max_rounds'])
    if expected != cfg['peer_generation_cap']:
        errors.append('peer call cap is inconsistent')
    diagnostic_calls = 0
    for name, spec in cfg.get('diagnostics', {}).items():
        calls = _grid_calls(spec, cfg['agents'], cfg['max_rounds'])
        diagnostic_calls += calls
        if calls != spec['peer_generation_cap']:
            errors.append(f'diagnostic {name} call cap is inconsistent')
        if spec['base_tasks'] > cfg['base_tasks'] or not set(spec['defenses']) <= set(cfg['defenses']):
            errors.append(f'diagnostic {name} must reuse development tasks and defenses')
    for key in ('task_families', 'correction_types'):
        if sum(cfg[key].values()) != cfg['base_tasks']:
            errors.append(f'{key} do not sum to base_tasks')
    if cfg['dataset_role'] != 'development' or cfg['status'] != 'proposed_not_run':
        errors.append('this plan must not imply completed or held-out experiments')
    for flag in ('existing_harness_integrated','author_reproduction_run','llm_experiment_run'):
        if cfg[flag] is not False:
            errors.append(f'{flag} must remain false before execution')
    for key in ('minimum_effect_delta','safety_noninferiority_eta','confirmatory_sample_size'):
        if cfg[key] is not None:
            errors.append(f'{key} is not yet frozen')
    if src.get('plan_version') != cfg['plan_version']:
        errors.append('sources.json and config disagree on plan_version')
    ids = [r['id'] for r in src['records']]
    if len(ids) != len(set(ids)):
        errors.append('duplicate source IDs')
    for r in src['records']:
        if not r['url'].startswith('https://') or not r['checked_scope'] or not r['boundary']:
            errors.append(f"invalid source {r['id']}")
        if r['experiment_reproduced'] is not False:
            errors.append(f"unsupported reproduction claim {r['id']}")
        if not r.get('roles') or not set(r['roles']) <= ROLES:
            errors.append(f"missing or unknown roles {r['id']}")
        if r.get('access_level') not in ACCESS_LEVELS:
            errors.append(f"unknown access level {r['id']}")
        elif r['access_level'] == 'search_index_only' and 'index' not in r['checked_scope'].lower():
            errors.append(f"index-only source {r['id']} must say so in checked_scope")
        if not r.get('recheck_note'):
            errors.append(f"missing recheck note {r['id']}")
    registry = _registry_entries((root/'docs/related-work.md').read_text())
    if set(registry) != set(ids):
        errors.append('related-work registry and sources.json list different IDs')
    for r in src['records']:
        if r['id'] in registry and registry[r['id']] != (r['title'], r['url']):
            errors.append(f"related-work registry out of sync for {r['id']}")
    for f in root.rglob('*.md'):
        text = f.read_text()
        for ref in re.findall(r'\bS\d{2}\b', text):
            if ref not in ids:
                errors.append(f'unknown source {ref} in {f.name}')
        for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', text):
            if '://' in link or link.startswith('#'):
                continue
            target = (f.parent / link.split('#',1)[0]).resolve()
            if not target.is_relative_to(root.resolve()) or not target.exists():
                errors.append(f'broken local link {f.name}: {link}')
    return {'passed': not errors, 'errors': errors,
            'scope': 'offline_plan_integrity_not_scientific_validation',
            'source_count':len(ids),
            'index_only_sources': sum(r['access_level'] == 'search_index_only' for r in src['records']),
            'planned_peer_generation_cap':expected,
            'planned_diagnostic_generation_cap':diagnostic_calls,
            'rough_mde_40_q03':rough_paired_mde(40),
            'exact_mcnemar_mde_40_q03':exact_mcnemar_mde(40),
            'model_experiments_run':False}

if __name__ == '__main__':
    result = validate()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result['passed'] else 1)
