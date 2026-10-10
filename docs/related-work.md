# 近邻、引文核验与拥挤度

日期：2026-10-10。定向检索，不是穷尽普查。未运行作者实验。官方发表、作者自报接收、预印本与继承阅读记录分别标记。机器可读原始记录见[../sources.json](../sources.json)。

## 决策

D1广义修订恢复与D2通信选择均中度至高度拥挤；D3已有直接基准。D4只保留一个待验证的交叉点：**混合消息中同一份必要纠正能否被安全保留，并在真实peer后续互动中完成任务**。不能称“首次研究过度防御”“没有直接近邻”。近期D4直接相邻包括S13–S18和S29。

检索覆盖所给arXiv ID、correction/injection/legitimate corrections/multi-agent overblocking/task alignment等关键词；非论文新闻与聚合站没有用作科学结论依据。引用少见或尚未复现的预印本用于定义查新边界，不等于采信其全部效应。

## 来源登记


### S01 · Systematic Failures in Collective Reasoning under Distributed Information in Multi-Agent LLMs (HiddenBench)

- 入口：https://proceedings.mlr.press/v306/li26ej.html
- 状态：ICML 2026 official proceedings
- 本轮核对：Official abstract and bibliographic metadata
- 对候选的约束：65 tasks; reported 30.1% distributed-group vs 80.7% full-information single-agent accuracy. Not a matched-cost superiority claim. Structured protocol already proposed.

### S02 · PropUQ-MAS: Propagation-Aware Uncertainty Quantification for LLM Multi-Agent Systems

- 入口：https://arxiv.org/abs/2608.22130v3
- 状态：arXiv v3; author comments report EMNLP 2026 Main acceptance
- 本轮核对：abs Comments and version history
- 对候选的约束：The acceptance note exists. Final proceedings not fetched. UQ metrics do not by themselves establish correction utility.

### S03 · When Truth Is Distributed: Misinformation Derails Collective Fact Recovery in LLM-Based Multi-Agent Systems

- 入口：https://arxiv.org/html/2608.03421v1
- 状态：arXiv v1 inspected for historical name
- 本轮核对：Abstract, section 3, paired conditions and source propagation
- 对候选的约束：Hi-Agreement explicitly appears in v1. Honest/deceptive worlds and false-root persistence already studied; not a proof of natural attack prevalence.

### S04 · Why Do Multi-Agent LLM Systems Fail?

- 入口：https://papers.nips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html
- 状态：NeurIPS 2025 Datasets and Benchmarks Track
- 本轮核对：Official proceedings heading and abstract
- 对候选的约束：The track is explicitly listed. Spotlight separately not rechecked this turn.

### S05 · From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration

- 入口：https://arxiv.org/html/2603.04474v2
- 状态：arXiv v2
- 本轮核对：HTML VI-D/VI-E/VI-F and limitations; PDF request failed
- 对候选的约束：Tri-state Green/Red/Yellow, lineage, external verification, blocking and rollback are in the method. No implementation reproduction.

### S06 · StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions

- 入口：https://arxiv.org/html/2610.05241v1
- 状态：arXiv v1
- 本轮核对：Abstract, paired state tests and limitations
- 对候选的约束：Single-agent persistent operational-state repair. Adjacent module, not evidence for peer-network repair.

### S07 · Consilience: Conformally Calibrated Communication Control for Hidden-Profile Multi-Agent Reasoning

- 入口：https://arxiv.org/abs/2608.20564v1
- 状态：arXiv v1
- 本轮核对：Abstract
- 对候选的约束：Selects challenge/clarify/seek evidence/route and speaker. Round-conditional marginal guarantee is not simultaneous multi-round or arbitrary distribution-shift safety.

### S08 · Agent Q-Mix: Selecting the Right Action for LLM Multi-Agent Systems through Reinforcement Learning

- 入口：https://arxiv.org/abs/2604.00344v1
- 状态：arXiv v1
- 本轮核对：Abstract
- 对候选的约束：Learns decentralized communication with centralized training, topology-aware state and token-cost tradeoff. General communication action selection is crowded.

### S09 · Cost-Effective Communication: An Auction-based Method for Language Agent Interaction (DALA)

- 入口：https://arxiv.org/abs/2511.13193v2
- 状态：arXiv v2, 2026-04-24
- 本轮核对：Abstract and version history
- 对候选的约束：Auction-based speaking selection. Not every action in the old proposal is identical, but cost-aware communication is occupied.

### S10 · Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement

- 入口：https://arxiv.org/abs/2606.27409v2
- 状态：arXiv v2, 2026-09-16
- 本轮核对：Abstract and revision notes
- 对候选的约束：Updated version limits oscillation interpretation: grounded factual answering eliminates the effect. Do not universalize signed-belief instability.

### S11 · Reliability-Contagion Feasibility in LLM Multi-Agent Networks

- 入口：https://arxiv.org/abs/2607.21912v1
- 状态：arXiv v1
- 本轮核对：Abstract
- 对候选的约束：Topology findings depend on fixed exposure per edge vs fixed sender budget. Simulations and controlled LLM experiments are distinct evidence.

### S12 · Governed Shared Memory for Multi-Agent LLM Systems

- 入口：https://arxiv.org/abs/2606.24535v1
- 状态：arXiv v1
- 本轮核对：Abstract
- 对候选的约束：Temporal supersession, scoped retrieval, provenance and production governance; explicitly not a baseline comparison.

### S13 · Easier to Mislead Than to Correct: Harmful and Beneficial Revision in LLM Conformity

- 入口：https://arxiv.org/html/2606.01637v2
- 状态：arXiv v2, 2026-06-06
- 本轮核对：Main protocol, 3.5, 4.3; PDF page 7 Figure 4 inspected
- 对候选的约束：Simulated peers; harmful and beneficial rates condition on different initial-answer subsets. CoT 63.9 to 36.5 harmful, 52.7 to 32.5 beneficial under respective conditions; not our D4 paired estimate.

### S14 · Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening and Provenance Ranking

- 入口：https://arxiv.org/html/2608.21230v1
- 状态：arXiv v1
- 本轮核对：Protocol, Table 6, limitations; PDF page 18 inspected
- 对候选的约束：Corpus N accuracy 0.8583 to 0.0417 with provenance weight, a constructed worst case. Plain false assertions are explicitly not instruction injections. Proposed occupancy remedy not evaluated.

### S15 · Trust propagation and structural containment in Multi-agent LLM pipelines

- 入口：https://arxiv.org/html/2609.17648v1
- 状态：arXiv v1
- 本轮核对：Authorization and independent-policy sections, Observer methods; parsed PDF; screenshot unavailable
- 对候选的约束：Already separates source authentication from permission and measures legitimate-task overblocking. Do not claim signed action binding or utility-preserving sanitization as new.

### S16 · PIGuard: Prompt Injection Guardrail via Mitigating Overdefense for Free

- 入口：https://aclanthology.org/2025.acl-long.1468/
- 状态：ACL 2025 official proceedings
- 本轮核对：Official abstract and metadata
- 对候选的约束：NotInject tests benign trigger-rich samples. General over-defense and benign retention are not new; corrections-in-network is a narrower proposed test.

### S17 · The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents

- 入口：https://aclanthology.org/2025.acl-long.1435/
- 状态：ACL 2025 official proceedings
- 本轮核对：Official abstract and metadata
- 对候选的约束：Task-alignment checking with safety/utility tradeoff. Required strong baseline for permission and action claims.

### S18 · ActGuard: Pre-execution Action Auditing against Indirect Prompt Injection in LLM Agents

- 入口：https://arxiv.org/abs/2609.14987
- 状态：2026-09-14 preprint; version not pinned this turn
- 本轮核对：Primary abstract
- 对候选的约束：Audits proposed actions, localizes triggering evidence and masks confirmed malicious spans. Selective sanitization is not vacant.

### S19 · Unlocking the Power of Multi-Agent LLM for Reasoning: From Lazy Agents to Deliberation

- 入口：https://arxiv.org/abs/2511.02303v1
- 状态：arXiv v1; prior assessment has ICLR 2026 record
- 本轮核对：Abstract; prior method reading not rerun
- 对候选的约束：Direct LiC-in-two-agent restart already exists. This turn did not rerun venue proof or experiment.

### S20 · When Memory Updates but Behavior Does Not: Repairing Implicit Stale Dependencies in Personalized Agent Responses (StateAuditor)

- 入口：https://arxiv.org/abs/2608.01619v1
- 状态：arXiv v1
- 本轮核对：Abstract and limitations
- 对候选的约束：Provenance/chronology verification is not semantic supersession. Already uses state-to-draft audits; external effects have explicit bounds.

### S21 · Grounded Continuation: A Linear-Time Runtime Verifier for LLM Conversations

- 入口：https://arxiv.org/abs/2605.14175v3
- 状态：arXiv v3, 2026-10-05
- 本轮核对：Latest abstract and version history
- 对候选的约束：Dependency/retraction engine plus Interpreter; v3 reports raw-text update extraction. Not merely an oracle graph baseline. Proof depends on map semantics.

### S22 · From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents

- 入口：https://arxiv.org/abs/2608.10502v1
- 状态：arXiv v1
- 本轮核对：Abstract
- 对候选的约束：Single-agent memory/action rollback is a direct D1 neighbor, not an untouched multi-agent solution.

### S23 · Invalidation Contracts for Cross-Episode Agent Memory

- 入口：https://arxiv.org/abs/2609.00243v1
- 状态：arXiv v1
- 本轮核对：Abstract and declared scope
- 对候选的约束：Already separates validity from planner compliance; fine-grained versioning and retained cache utility. Oracle validity must not be confused with learned behavior.

### S24 · How does Adversarial Influence Scale in Multi-Agent Systems?

- 入口：https://arxiv.org/abs/2609.30028v1
- 状态：arXiv v1
- 本轮核对：Abstract
- 对候选的约束：Adversarial scale is neighboring, not a warrant to add topology and attacker search to Stage 0.

### S25 · From Process Loss to Assembly Bonus: Human-Grounded Diagnosis of Multi-Agent LLM Collaboration

- 入口：https://arxiv.org/abs/2609.13261v1
- 状态：arXiv v1
- 本轮核对：Abstract
- 对候选的约束：Distributed collaboration diagnosis already studied; no head-to-head reproduction this turn.

### S26 · LLM Agents for Deliberative Collaboration: A Study on Joint Decision Making Under Partial Observability

- 入口：https://arxiv.org/abs/2607.06157v1
- 状态：arXiv v1
- 本轮核对：Abstract
- 对候选的约束：Joint decision-making under partial observability is an existing task class.

### S27 · LLMs Get Lost In Multi-Turn Conversation

- 入口：https://arxiv.org/abs/2505.06120
- 状态：Original root paper; prior official ICLR 2026 award check
- 本轮核对：Inherited prior analysis, not fully reread this turn
- 对候选的约束：Temporal instruction splitting is not a per-edge failure probability. Same-network extension alone is not a contribution.

### S28 · Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation

- 入口：https://arxiv.org/abs/2602.07338v1
- 状态：arXiv v1
- 本轮核对：Abstract
- 对候选的约束：Mediator/assistant separation already addresses intent consolidation.

### S29 · AgentVisor: Defending LLM Agents Against Prompt Injection via Semantic Virtualization

- 入口：https://arxiv.org/abs/2604.24118
- 状态：2026 preprint; version not pinned this turn
- 本轮核对：Primary abstract
- 对候选的约束：Semantic privilege separation and one-shot correction already studied; not equivalent to this network experiment.

### S30 · AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents

- 入口：https://arxiv.org/abs/2406.13352
- 状态：Historical evaluation infrastructure (2024)
- 本轮核对：Abstract
- 对候选的约束：Dynamic tool-agent security/utility evaluation exists. Reuse only license-permitted artifacts with explicit adaptation.


## 下一次真正运行之前

重新核验S15/S17/S18的代码与可用接口；冻结一个同预算强行动审计基线。复查是否出现同渠道纠正/注入的直接成对研究；如已有完整等价工作，收敛为复现或任务迁移，不能靠换框架名立论。

D1还须核对最新Grounded Continuation v3；不能继续只对比早期的结构化oracle版本。Delayed Verification v2也缩小了振荡主张，应以修订版而非标题当证据。
