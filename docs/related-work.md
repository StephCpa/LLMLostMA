# 近邻、引文核验与拥挤度

日期：2026-10-10（第二轮）。定向检索，不是穷尽普查。未运行作者实验。官方发表、作者自报接收、预印本与继承阅读记录分别标记。机器可读原始记录见[../sources.json](../sources.json)。

## 本轮核验方法与限制

- 第一轮（S01–S30）按各条“核对范围”直接阅读了摘要、方法段或 PDF 指定页。
- 第二轮只能使用网页检索索引：WebFetch 对所有主机 DNS 失败，沙盒代理拒绝 arxiv.org、export.arxiv.org、aclanthology.org 与 api.semanticscholar.org。因此本轮**没有打开任何页面、PDF 或版本历史**；结论来自检索摘要与二手概述，`access_level` 字段区分 `prior_round_direct_read` 与 `search_index_only`。
- 复核结果：S01–S30 的题名与编号全部在索引中找到，未发现虚构或错配的来源；S01、S09、S16、S17、S19、S27、S30 有发表状态更新；S13 存在一处未解决的数字差异（第三方概述 62.9%/51.5%，第一轮读图 63.9%/52.7%，可能是不同汇总口径），引用前须重读 Fig. 4。
- 新增 S31–S51 均为 `search_index_only`：只采信其摘要级定位，数字一律视为作者自报或二手转述，运行前须直接阅读。

## 决策

D1 广义修订恢复与 D2 通信选择均中度至高度拥挤；D3 已有直接基准。第二轮把 D4 的拥挤度从“中度”上调为**中高**：

- “严格的数据/指令分离会损害情境上合理的行为”已有专门论证。[S32]
- “同一观察中保留良性字段、阻断由注入跨度驱动的动作”已有跨度级因果来源审计与配套基准。[S31]
- “净化上下文时保留任务相关证据”已有方法和 Utility Under Attack 指标。[S35]
- “证据候选与操作请求分路”是控制流/数据流按设计分离的特例。[S33,S34]
- 多 Agent 场景中，对齐检查可被控制流劫持绕过，安全与功能目标冲突已被明确提出。[S38]
- 防御的良性情形效用成本已被单独测量。[S40]

D4 只保留一个更窄、待验证的交叉点（D4′）：**由真实 peer 转述的、需要改变后续动作的有效纠正，与同一纠正附加越权指令的成对版本，在按设计分离、行动对齐审计与跨度级来源审计下各自落在安全—纠正效用边界的什么位置。** 不能称“首次研究过度防御”“首次在多 Agent 中区分纠正与注入”或“没有直接近邻”。

检索覆盖所给 arXiv ID、correction/injection/legitimate corrections/multi-agent overblocking/task alignment/benign utility/Byzantine/conformity 等关键词；非论文新闻与聚合站没有用作科学结论依据。引用少见或尚未复现的预印本用于定义查新边界，不等于采信其全部效应。

## D4′ 与最近邻的特征对照

✓ = 摘要级可见；部分 = 只覆盖一部分；✗ = 摘要级可见地不覆盖；未核 = 本轮无法判断。依据仅为各来源的“对候选的约束”和复核记录，不是全文审读。

| 来源 | 渠道 | 同一消息含有效内容＋越权指令 | 真实多跳 peer | 同一纠正的成对 C/X | 纠正需改变后续动作 | 报告良性效用 |
|---|---|---|---|---|---|---|
| S13 Easier to Mislead | 模拟 peer 答案 | ✗ | ✗ | ✗（不同初始子群） | ✗（QA） | ✓ |
| S14 Utility Under Attack | 记忆检索 | ✗（明确不是指令注入） | ✗ | ✗ | ✗ | ✓ |
| S15 Trust Propagation | 管线 Agent＋检索文档 | 部分（伪造批准） | ✓ | 未核 | 未核 | ✓ |
| S17 Task Shield | 工具返回 | 部分 | ✗ | ✗ | ✗ | ✓ |
| S18 ActGuard | 工具返回 | ✓（掩蔽触发跨度） | ✗ | ✗ | 未核 | 未核 |
| S31 ARGUS | 运行时跨度 | ✓ | ✗ | 未核 | 部分（情境依赖任务） | ✓ |
| S33 CaMeL | 工具返回 | 按设计阻断 | ✗ | ✗ | ✗（数据不能改控制流） | ✓ |
| S35 AgentSentry | 工具返回 | ✓（保留任务证据） | ✗ | ✗ | 未核 | ✓ |
| S38 ControlValve | 多 Agent 编排消息 | 部分 | ✓ | 未核 | 未核 | ✓ |
| S40 Price of Safety | 记忆 | ✗ | ✗ | ✗（仅良性） | ✗ | ✓ |
| S43 G-Safeguard | 多 Agent 话语图 | 未核 | ✓ | ✗ | 未核 | ✓ |
| S44 SAC | 多 Agent 消息 | ✗（拜占庭答案） | ✓ | ✗ | ✗ | ✓ |
| S45 Prompt Infection | 多 Agent 消息 | ✓ | ✓ | ✗ | 未核 | 未核 |

读法：每一列单独都有人做过；本轮未见同时满足“真实 peer 转述＋同一纠正成对＋需改变动作＋两侧共同成功”的已核工作。这只是摘要级的组合空缺，D4′ 的贡献最多是条件化测量与评价工具，而不是新机制；若全文审读发现 S31/S38 已覆盖，即按[研究方案](research-plan.md) §8 收缩。

两条由近邻直接推出、必须在实验中检验而非假设的预测：

1. 按设计分离（S33/S34）在“契约预先授权的纠正”上应几乎无代价；代价集中在“需要改变后续动作的纠正”，因为此时有效信息必须影响控制流。[S32,S33]
2. 只看内容的事后过滤难以区分有益与有害修订，除非在修订前提供可核验信息（S41）；而鲁棒聚合（S44）与边级隔离（S43）在结构上会压低只由一个 peer 持有的信息，恰好是单一合法纠正所在位置（参见 S01 的分散信息失败）。

## 未登记线索

以下仅在检索结果中见到题名，未见可靠摘要，不分配 S 编号、不支持任何结论，运行前逐条判断是否纳入：

- Right Answers, Wrong States: Hidden Information Failures in Multi-Agent Collaboration — https://arxiv.org/abs/2610.01244
- When Evidence Changes: Evaluating Memory Repair and Re-reading in Language-Model Agents — https://arxiv.org/abs/2610.03902
- The Evaluator Is Part of the Experiment: Measuring Open-Ended LLM Conformity — https://arxiv.org/abs/2608.04463
- TEPA: Revoking Stale Memories for Conflict-Robust Language Agents — https://arxiv.org/abs/2608.07429
- SIEVE: Selective Integrity Verification and Escalation for Defending LLM Agents against Indirect Prompt Injection — https://arxiv.org/abs/2512.06716
- Delegation Without Trust: An Empirical Gap Analysis of Identity, Authorization, and Runtime Governance in Multi-Agent LLM Systems — https://arxiv.org/abs/2609.00267
- Adversarial Attacks in Multi-Agent LLM Pipelines: Unveiling Structural Vulnerabilities in Agentic AI Architectures — https://arxiv.org/abs/2608.00718
- Meta “Agents Rule of Two”（2025-10-31 博客，仅见二手概述）

## 来源登记

字段：入口、状态、核对范围（该来源最近一次直接阅读的范围）、对候选的约束、访问层级、本轮复核、用途。用途词表：`root`、`D1_neighbor`、`D2_neighbor`、`D3_neighbor`、`D4_neighbor`、`D4_baseline_candidate`、`attack_or_threat`、`conformity`、`evaluation_method`、`infrastructure`。

### S01 · Systematic Failures in Collective Reasoning under Distributed Information in Multi-Agent LLMs (HiddenBench)

- 入口：https://proceedings.mlr.press/v306/li26ej.html
- 状态：ICML 2026 official proceedings (PMLR 306); arXiv preprint 2505.11556, earlier titled "HiddenBench: Assessing Collective Reasoning in Multi-Agent LLMs via Hidden Profile Tasks"
- 核对范围：Official abstract and bibliographic metadata
- 对候选的约束：65 tasks; reported 30.1% distributed-group vs 80.7% full-information single-agent accuracy. Not a matched-cost superiority claim. Structured protocol already proposed.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Index confirms PMLR v306 entry, ICML 2026 poster page, authors Li/Naito/Shirado, 65 tasks and 30.1% vs 80.7%.
- 用途：D3_neighbor, D2_neighbor

### S02 · PropUQ-MAS: Propagation-Aware Uncertainty Quantification for LLM Multi-Agent Systems

- 入口：https://arxiv.org/abs/2608.22130v3
- 状态：arXiv v3; author comments report EMNLP 2026 Main acceptance
- 核对范围：abs Comments and version history
- 对候选的约束：The acceptance note exists. Final proceedings not fetched. UQ metrics do not by themselves establish correction utility.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed via index. The EMNLP 2026 acceptance comment was not visible in snippets and no lab or proceedings listing was found; no contradiction either. Keep as author-reported only.
- 用途：D3_neighbor

### S03 · When Truth Is Distributed: Misinformation Derails Collective Fact Recovery in LLM-Based Multi-Agent Systems

- 入口：https://arxiv.org/html/2608.03421v1
- 状态：arXiv v1 inspected for historical name
- 核对范围：Abstract, section 3, paired conditions and source propagation
- 对候选的约束：Hi-Agreement explicitly appears in v1. Honest/deceptive worlds and false-root persistence already studied; not a proof of natural attack prevalence.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed; snippets showed only prompt/schema text, so findings were not re-checked this round.
- 用途：D3_neighbor, D4_neighbor

### S04 · Why Do Multi-Agent LLM Systems Fail?

- 入口：https://papers.nips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html
- 状态：NeurIPS 2025 Datasets and Benchmarks Track
- 核对范围：Official proceedings heading and abstract
- 对候选的约束：The track is explicitly listed. Spotlight separately not rechecked this turn.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: NeurIPS 2025 D&B listing and mlanthology entry confirmed (Cemri et al.; 1,600+ traces, 14 failure modes). Spotlight is asserted only by a secondary blog and remains unconfirmed.
- 用途：D3_neighbor

### S05 · From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration

- 入口：https://arxiv.org/html/2603.04474v2
- 状态：arXiv v2
- 核对范围：HTML VI-D/VI-E/VI-F and limitations; PDF request failed
- 对候选的约束：Tri-state Green/Red/Yellow, lineage, external verification, blocking and rollback are in the method. No implementation reproduction.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed (Xie et al.). alphaXiv lists v2 dated 2026-05-11. v1 abstract reports defense success 0.32 to >0.89; v2 wording reportedly differs (final infection prevented in >=89% of runs). Quote numbers per version.
- 用途：D1_neighbor, D3_neighbor

### S06 · StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions

- 入口：https://arxiv.org/html/2610.05241v1
- 状态：arXiv v1
- 核对范围：Abstract, paired state tests and limitations
- 对候选的约束：Single-agent persistent operational-state repair. Adjacent module, not evidence for peer-network repair.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed (Peng et al., submitted 2026-10-04): record-level counterfactual replanning, hierarchical resolver, independent state-action check; 150 executable coding-agent cases.
- 用途：D1_neighbor

### S07 · Consilience: Conformally Calibrated Communication Control for Hidden-Profile Multi-Agent Reasoning

- 入口：https://arxiv.org/abs/2608.20564v1
- 状态：arXiv v1
- 核对范围：Abstract
- 对候选的约束：Selects challenge/clarify/seek evidence/route and speaker. Round-conditional marginal guarantee is not simultaneous multi-round or arbitrary distribution-shift safety.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed (posted 2026-08-20 per secondary coverage); 12 models on HiddenBench-style tasks per news summary, not verified.
- 用途：D2_neighbor

### S08 · Agent Q-Mix: Selecting the Right Action for LLM Multi-Agent Systems through Reinforcement Learning

- 入口：https://arxiv.org/abs/2604.00344v1
- 状态：arXiv v1
- 核对范围：Abstract
- 对候选的约束：Learns decentralized communication with centralized training, topology-aware state and token-cost tradeoff. General communication action selection is crowded.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed (2026-04-01): QMIX-based CTDE over per-agent communication actions with accuracy/token-cost reward.
- 用途：D2_neighbor

### S09 · Cost-Effective Communication: An Auction-based Method for Language Agent Interaction (DALA)

- 入口：https://arxiv.org/abs/2511.13193v2
- 状态：arXiv v2, 2026-04-24; AAAI proceedings entry located (ojs.aaai.org article 40182)
- 核对范围：Abstract and version history
- 对候选的约束：Auction-based speaking selection. Not every action in the old proposal is identical, but cost-aware communication is occupied.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: AAAI OJS entry found via index; volume and year not opened this round.
- 用途：D2_neighbor

### S10 · Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement

- 入口：https://arxiv.org/abs/2606.27409v2
- 状态：arXiv v2, 2026-09-16
- 核对范围：Abstract and revision notes
- 对候选的约束：Updated version limits oscillation interpretation: grounded factual answering eliminates the effect. Do not universalize signed-belief instability.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed (single author Itkin, submitted 2026-06-25); greedy (1-1/e) corrector placement does not imply optimal static MSE.
- 用途：D3_neighbor

### S11 · Reliability-Contagion Feasibility in LLM Multi-Agent Networks

- 入口：https://arxiv.org/abs/2607.21912v1
- 状态：arXiv v1
- 核对范围：Abstract
- 对候选的约束：Topology findings depend on fixed exposure per edge vs fixed sender budget. Simulations and controlled LLM experiments are distinct evidence.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed (Niu, Shu, Zhao); correction-aware susceptible/exposed/infectious/corrected model; authors call the empirical scope deliberately small.
- 用途：D3_neighbor

### S12 · Governed Shared Memory for Multi-Agent LLM Systems

- 入口：https://arxiv.org/abs/2606.24535v1
- 状态：arXiv v1
- 核对范围：Abstract
- 对候选的约束：Temporal supersession, scoped retrieval, provenance and production governance; explicitly not a baseline comparison.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed (Margalit et al., 2026-06-23): MemClaw service and ArgusFleet harness; no baseline comparison by design.
- 用途：D1_neighbor

### S13 · Easier to Mislead Than to Correct: Harmful and Beneficial Revision in LLM Conformity

- 入口：https://arxiv.org/html/2606.01637v2
- 状态：arXiv v2, 2026-06-06
- 核对范围：Main protocol, 3.5, 4.3; PDF page 7 Figure 4 inspected
- 对候选的约束：Simulated peers; harmful and beneficial rates condition on different initial-answer subsets. CoT 63.9 to 36.5 harmful, 52.7 to 32.5 beneficial under respective conditions; not our D4 paired estimate.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed (Qu, Fu, Hu; 2026-06-01). A third-party overview reports 62.9% harmful (all-wrong) vs 51.5% beneficial (all-correct), which differs from the 63.9/52.7 pair read from Fig. 4 last round; may be a different aggregation. Unresolved: re-read Fig. 4 before quoting either pair.
- 用途：D4_neighbor, conformity

### S14 · Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening and Provenance Ranking

- 入口：https://arxiv.org/html/2608.21230v1
- 状态：arXiv v1
- 核对范围：Protocol, Table 6, limitations; PDF page 18 inspected
- 对候选的约束：Corpus N accuracy 0.8583 to 0.0417 with provenance weight, a constructed worst case. Plain false assertions are explicitly not instruction injections. Proposed occupancy remedy not evaluated.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed. Secondary coverage describes a separate LongMemEval experiment (1.2% poisoning, 0.850 to 0.300) and 0/360 detection by write-time screening; distinct from the Table 6 figure cited here.
- 用途：D4_neighbor

### S15 · Trust propagation and structural containment in Multi-agent LLM pipelines

- 入口：https://arxiv.org/html/2609.17648v1
- 状态：arXiv v1
- 核对范围：Authorization and independent-policy sections, Observer methods; parsed PDF; screenshot unavailable
- 对候选的约束：Already separates source authentication from permission and measures legitimate-task overblocking. Do not claim signed action binding or utility-preserving sanitization as new.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID/authors confirmed (Safin, Zisad, Shatabda, Hasan): 4-agent LangGraph pipeline; with authorization a compromised Validator reaches 100% judgment bypass but 0% unsafe action; Observer cuts hijack false positives 49% to 7%; 3 seeds, 60 labeled tasks.
- 用途：D4_neighbor, D4_baseline_candidate

### S16 · PIGuard: Prompt Injection Guardrail via Mitigating Overdefense for Free

- 入口：https://aclanthology.org/2025.acl-long.1468/
- 状态：ACL 2025 official proceedings (pp. 30420-30437); preprint arXiv 2410.22770 titled "InjecGuard"
- 核对范围：Official abstract and metadata
- 对候选的约束：NotInject tests benign trigger-rich samples. General over-defense and benign retention are not new; corrections-in-network is a narrower proposed test.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Confirmed. NotInject has 339 benign trigger-word samples. PIGuard is a separate DeBERTa-v3 classifier with public weights (code leolee99/PIGuard), not a prompt on the peer model.
- 用途：D4_neighbor, D4_baseline_candidate

### S17 · The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents

- 入口：https://aclanthology.org/2025.acl-long.1435/
- 状态：ACL 2025 official proceedings (pp. 29680-29697); preprint arXiv 2412.16682
- 核对范围：Official abstract and metadata
- 对候选的约束：Task-alignment checking with safety/utility tradeoff. Required strong baseline for permission and action claims.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Confirmed (Jia, Wu, Qin, Squicciarini). Authors report AgentDojo/GPT-4o ASR 2.07% with 69.79% utility.
- 用途：D4_baseline_candidate

### S18 · ActGuard: Pre-execution Action Auditing against Indirect Prompt Injection in LLM Agents

- 入口：https://arxiv.org/abs/2609.14987
- 状态：2026-09-14 preprint; version not pinned this turn
- 核对范围：Primary abstract
- 对候选的约束：Audits proposed actions, localizes triggering evidence and masks confirmed malicious spans. Selective sanitization is not vacant.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed (posted 2026-09): chunk-level influence scoring on the proposed action, flag-and-mask re-evaluation. Benchmark numbers not seen in snippets.
- 用途：D4_baseline_candidate

### S19 · Unlocking the Power of Multi-Agent LLM for Reasoning: From Lazy Agents to Deliberation

- 入口：https://arxiv.org/abs/2511.02303v1
- 状态：ICLR 2026 official proceedings; arXiv v1 2511.02303
- 核对范围：Abstract; prior method reading not rerun
- 对候选的约束：Direct LiC-in-two-agent restart already exists. This turn did not rerun venue proof or experiment.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: ICLR 2026 proceedings page and poster located via index (Zhang et al.); resolves the venue question left open last round.
- 用途：root, D1_neighbor

### S20 · When Memory Updates but Behavior Does Not: Repairing Implicit Stale Dependencies in Personalized Agent Responses (StateAuditor)

- 入口：https://arxiv.org/abs/2608.01619v1
- 状态：arXiv v1
- 核对范围：Abstract and limitations
- 对候选的约束：Provenance/chronology verification is not semantic supersession. Already uses state-to-draft audits; external effects have explicit bounds.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed (Sun and He, 2026-08-03). StateAuditor targets the implicit policy adaptation gap defined by STALE [S50]; .686 to .736 under STALE strict protocol; no gain on a harder authored set.
- 用途：D1_neighbor

### S21 · Grounded Continuation: A Linear-Time Runtime Verifier for LLM Conversations

- 入口：https://arxiv.org/abs/2605.14175v3
- 状态：arXiv v3, 2026-10-05
- 核对范围：Latest abstract and version history
- 对候选的约束：Dependency/retraction engine plus Interpreter; v3 reports raw-text update extraction. Not merely an oracle graph baseline. Proof depends on map semantics.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed (He, Dong, Huang; v1 2026-05-13). v3 date not visible in snippets; keep last round's version pin.
- 用途：D1_neighbor

### S22 · From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents

- 入口：https://arxiv.org/abs/2608.10502v1
- 状态：arXiv v1
- 核对范围：Abstract
- 对候选的约束：Single-agent memory/action rollback is a direct D1 neighbor, not an untouched multi-agent solution.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed. Self-reported 85.3% vs 77.3% recovery on 150 cases and 68.0% vs 54.0% on a 50-case LongMemEval-V2 stress set; cannot undo irreversible side effects.
- 用途：D1_neighbor

### S23 · Invalidation Contracts for Cross-Episode Agent Memory

- 入口：https://arxiv.org/abs/2609.00243v1
- 状态：arXiv v1
- 核对范围：Abstract and declared scope
- 对候选的约束：Already separates validity from planner compliance; fine-grained versioning and retained cache utility. Oracle validity must not be confused with learned behavior.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed (Wu and Canedo): about 9,400 episodes across seven models; first-try compliance varies strongly by model while validity is protocol-determined.
- 用途：D1_neighbor

### S24 · How does Adversarial Influence Scale in Multi-Agent Systems?

- 入口：https://arxiv.org/abs/2609.30028v1
- 状态：arXiv v1
- 核对范围：Abstract
- 对候选的约束：Adversarial scale is neighboring, not a warrant to add topology and attacker search to Stage 0.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed (Wu, Cekinmez, Liao, Narasimhan, Griffiths; 2026-09-24): defection rises linearly with deceiver proportion; LLM agents defect even when deceivers are a minority; groups of 2-21.
- 用途：attack_or_threat, conformity

### S25 · From Process Loss to Assembly Bonus: Human-Grounded Diagnosis of Multi-Agent LLM Collaboration

- 入口：https://arxiv.org/abs/2609.13261v1
- 状态：arXiv v1
- 核对范围：Abstract
- 对候选的约束：Distributed collaboration diagnosis already studied; no head-to-head reproduction this turn.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed; human baseline of 500 groups; snippet table values truncated.
- 用途：D3_neighbor

### S26 · LLM Agents for Deliberative Collaboration: A Study on Joint Decision Making Under Partial Observability

- 入口：https://arxiv.org/abs/2607.06157v1
- 状态：arXiv v1
- 核对范围：Abstract
- 对候选的约束：Joint decision-making under partial observability is an existing task class.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed (Wang et al., 2026-07-07): joint decisions under asymmetric observations; deliberation can enable error correction.
- 用途：D3_neighbor

### S27 · LLMs Get Lost In Multi-Turn Conversation

- 入口：https://arxiv.org/abs/2505.06120
- 状态：ICLR 2026 Outstanding Paper (ICLR blog, 2026-04-23); arXiv 2505.06120
- 核对范围：Inherited prior analysis, not fully reread this turn
- 对候选的约束：Temporal instruction splitting is not a per-edge failure probability. Same-network extension alone is not a contribution.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Award confirmed via the ICLR blog announcement; 39% average multi-turn drop across six tasks; 200k+ simulated conversations.
- 用途：root

### S28 · Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation

- 入口：https://arxiv.org/abs/2602.07338v1
- 状态：arXiv v1
- 核对范围：Abstract
- 对候选的约束：Mediator/assistant separation already addresses intent consolidation.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed (Liu et al., 2026-02).
- 用途：root

### S29 · AgentVisor: Defending LLM Agents Against Prompt Injection via Semantic Virtualization

- 入口：https://arxiv.org/abs/2604.24118
- 状态：2026 preprint; version not pinned this turn
- 核对范围：Primary abstract
- 对候选的约束：Semantic privilege separation and one-shot correction already studied; not equivalent to this network experiment.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Title/ID confirmed: Guest proposes tool calls, Visor audits them without seeing raw external context. A secondary write-up reports 0.65% ASR at 1.45% utility cost (unverified).
- 用途：D4_baseline_candidate

### S30 · AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents

- 入口：https://arxiv.org/abs/2406.13352
- 状态：NeurIPS 2024 Datasets and Benchmarks Track (official proceedings); arXiv 2406.13352
- 核对范围：Abstract
- 对候选的约束：Dynamic tool-agent security/utility evaluation exists. Reuse only license-permitted artifacts with explicit adaptation.
- 访问层级：prior_round_direct_read
- 本轮复核：2026-10-10 index recheck: Official proceedings entry confirmed; 97 tasks; models solve <66% of tasks without attack.
- 用途：infrastructure

### 第二轮新增（仅检索索引级）

### S31 · ARGUS: Defending LLM Agents Against Context-Aware Prompt Injection

- 入口：https://arxiv.org/abs/2605.03378
- 状态：arXiv v1, 2026-05
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：Causal-provenance auditor: each state-changing action must be supported by a complete benign causal chain over runtime spans; AgentLure (4 domains, 8 attack vectors; one summary reports 320 samples) targets context-dependent tasks. Already occupies "keep benign fields of the same observation, block actions driven by injected spans" for single-agent tool returns; D4 must differ through live peer relay and the paired same-correction design.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D4_neighbor, D4_baseline_candidate

### S32 · AI Agents May Always Fall for Prompt Injections

- 入口：https://arxiv.org/abs/2605.17634
- 状态：arXiv v1, 2026-05-17 (Abdelnabi and Bagdasarian)
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：Argues data-instruction separation both misses contextual-manipulation attacks and degrades contextually appropriate behavior; reframes injection with Contextual Integrity (misrepresented flows, manipulated norms, mixed flows). "Strict separation loses legitimate behavior" is therefore an existing argument, not a D4 finding. A secondary "impossibility" framing is not confirmed in the abstract.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D4_neighbor

### S33 · Defeating Prompt Injections by Design (CaMeL)

- 入口：https://arxiv.org/abs/2503.18813
- 状态：arXiv v2, 2025
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：Extracts control and data flow from the trusted query so untrusted data cannot change program flow; capabilities enforce policy at tool calls. v2 abstract: 77% of AgentDojo tasks with provable security vs 84% undefended (v1 reported 67%). The proposed evidence/operation split is a special case of this design and needs a faithful-adaptation comparison first. Code: google-research/camel-prompt-injection.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D4_baseline_candidate

### S34 · Securing AI Agents with Information-Flow Control (FIDES)

- 入口：https://arxiv.org/abs/2505.23643
- 状态：arXiv v2, 2025-09-03
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：Planner that tracks confidentiality and integrity labels, deterministically enforces policies and selectively hides information; formal model of planner expressiveness. Integrity labels on peer-relayed evidence are an existing mechanism. Code: microsoft/fides.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D4_baseline_candidate

### S35 · AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification

- 入口：https://arxiv.org/abs/2602.22724
- 状态：arXiv v1, 2026-02-26
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：Counterfactual re-execution at tool-return boundaries locates takeover points; purification removes attacker-induced deviations while keeping task-relevant evidence; self-reported Utility Under Attack 74.55% on AgentDojo. Evidence-preserving purification is occupied for single-agent tool use.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D4_neighbor, D4_baseline_candidate

### S36 · MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents

- 入口：https://proceedings.mlr.press/v267/zhu25z.html
- 状态：ICML 2025 official proceedings (PMLR 267); arXiv 2502.05174
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：Masked re-execution with tool-call comparison flags actions that persist when the user task is masked. A legitimate peer correction that changes required actions may or may not trip this signal; test rather than assume. Code: kaijiezhu11/MELON.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D4_baseline_candidate

### S37 · LlamaFirewall: An open source guardrail system for building secure AI agents

- 入口：https://arxiv.org/abs/2505.03574
- 状态：arXiv v1, 2025-05 (Meta)
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：PromptGuard 2 (86M/22M BERT-style classifier), experimental AlignmentCheck chain-of-thought auditor, and CodeShield. Secondary sources report AgentDojo ASR about 17.6% to 1.7% (unverified). Open weights make it a practical B2/B3 option, subject to the bypass results in S38.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D4_baseline_candidate

### S38 · Breaking and Fixing Defenses Against Control-Flow Hijacking in Multi-Agent Systems (ControlValve)

- 入口：https://arxiv.org/abs/2510.17276
- 状态：ICLR 2026 (poster listing); arXiv v2, 2026-03
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：Control-flow hijacking evades alignment checks of inter-agent messages (e.g. LlamaFirewall) even with strong LLM checkers; argues safety and functionality goals conflict in multi-agent systems; proposes permitted control-flow graphs plus zero-shot per-invocation rules. Directly constrains any alignment-check arm and the D4 premise.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D4_neighbor, D4_baseline_candidate, attack_or_threat

### S39 · The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections

- 入口：https://arxiv.org/abs/2510.09023
- 状态：arXiv v1, 2025-10-10; USENIX Security 2026 listing
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：Adaptive attacks (gradient, RL, random search, human-guided) bypassed 12 recent defenses with >90% ASR for most, many of which had reported near-zero ASR. Frozen one-shot attack results in this plan are non-adaptive lower bounds on attack success.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：attack_or_threat, evaluation_method

### S40 · The Price of Safety: Benign-Case Utility and Token Overhead of Memory-Poisoning Defenses in LLM Agents

- 入口：https://arxiv.org/abs/2609.22818
- 状态：arXiv v1, 2026-09
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：Write-time defenses showed no resolvable benign-case cost (95% CI about +/-4.5 pts); a read-time reranker cost -4.4 pts (CI [-9.0,-0.05], McNemar p=0.064) and falsely quarantined legitimate memories on 33.6% of adjudicated items. Small study (5 conversations x 3 runs). Benign-case cost of defenses is already measured; intercept position matters.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D4_neighbor, evaluation_method

### S41 · One Axis, No Brake: Self-Knowledge Limits the Filtering of Harmful Peer Conformity in LLMs

- 入口：https://arxiv.org/abs/2609.18998
- 状态：arXiv v1, 2026-09
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：Argues a post-hoc filter that keeps beneficial and blocks harmful peer revisions needs knowledge of initial correctness (self-knowledge AUROC about 0.64-0.89 across six families); steering moves harmful and beneficial revisions together; adding information before revision helps. Predicts content-only filters cannot separate valid from invalid peer updates without host-verifiable evidence.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D4_neighbor, conformity

### S42 · Most LLM Conformity Needs No Speaker: Measuring the Speaker-Free Floor in Peer-Pressure Benchmarks

- 入口：https://arxiv.org/abs/2607.05545
- 状态：arXiv v1, 2026-07
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：A speaker-free conflicting answer causes harmful revision in 66.5% of initially correct cases vs 10.3% under a plain re-ask (six open-weight LLMs, seven datasets); source attribution should be measured as an increment over this floor. Motivates the speaker-free diagnostic added in plan v0.2.0.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：conformity, evaluation_method

### S43 · G-Safeguard: A Topology-Guided Security Lens and Treatment on LLM-based Multi-agent Systems

- 入口：https://aclanthology.org/2025.acl-long.359/
- 状态：ACL 2025 official proceedings (pp. 7261-7276); arXiv 2502.11127
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：GNN anomaly detection on the multi-agent utterance graph plus topological intervention; reports >40% performance recovery under prompt injection. Message- or edge-level isolation is a natural over-defense case for a lone peer correction; the exact intervention was not confirmed this round.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D4_baseline_candidate

### S44 · Robust Multi-Agent LLMs under Byzantine Faults

- 入口：https://arxiv.org/abs/2605.09076
- 状态：arXiv v1, 2026-05-09; ICML 2026 listing
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：Self-Anchored Consensus filters unreliable messages with (F+1)-robustness graph conditions. Robust aggregation structurally discounts information held by one peer, which is exactly where a lone valid correction sits (cf. S01); candidate network-level filter arm.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D4_baseline_candidate, D3_neighbor

### S45 · Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems

- 入口：https://arxiv.org/abs/2410.07283
- 状态：arXiv v1, 2024-10
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：Self-replicating injection across agents; LLM Tagging reduces spread when combined with other safeguards; handcrafted attacks, mainly GPT-family. Peer-to-peer injection propagation is established.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：attack_or_threat

### S46 · On the Resilience of LLM-Based Multi-Agent Collaboration with Faulty Agents

- 入口：https://proceedings.mlr.press/v267/huang25ay.html
- 状态：ICML 2025 official proceedings (PMLR 267, pp. 26202-26226); arXiv 2408.00989
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：AutoTransform/AutoInject create faulty agents and message errors; hierarchical structure is most resilient; Challenger and Inspector recover up to 96.4% of errors. Figures differ between arXiv v3 and ICML; cite the ICML numbers.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D3_neighbor, D4_baseline_candidate

### S47 · Can LLMs Separate Instructions From Data? And What Do We Even Mean By That?

- 入口：https://arxiv.org/abs/2403.06833
- 状态：ICLR 2025 (arXiv v3 camera-ready)
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：Formal and empirical instruction-data separation measure with the SEP dataset (9,160 examples); all tested models fail to reach high separation; prompt engineering and fine-tuning barely help or hurt utility.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D4_neighbor, evaluation_method

### S48 · The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions

- 入口：https://arxiv.org/abs/2404.13208
- 状态：arXiv v1, 2024-04-19 (OpenAI)
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：Trains models to ignore lower-privileged conflicting instructions, with robustness gains and minimal capability loss on GPT-3.5. Privilege-by-source is an existing model-level concept; it does not decide whether lower-privilege factual corrections should be used.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D4_neighbor

### S49 · Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations

- 入口：https://arxiv.org/abs/2411.00640
- 状态：arXiv v1, 2024-11
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：Super-population framing, clustered standard errors, paired differences and power analysis for LM evaluations. Adopted as the analysis reference for task-clustered paired estimates; specific formulas not re-read this round.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：evaluation_method

### S50 · STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?

- 入口：https://arxiv.org/abs/2605.06527
- 状态：arXiv v1, 2026-05
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：400 implicit-conflict scenarios with three probes including Implicit Policy Adaptation; best model 55.2% overall; large gap between retrieving updated evidence and acting on it; CUPMem prototype. Direct D1 neighbor and origin of the gap targeted by S20.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D1_neighbor

### S51 · SoK: When Safe Agents Fail Together: The Security of Multi Agent LLM Systems

- 入口：https://arxiv.org/abs/2609.00595
- 状态：arXiv v1, 2026-09
- 核对范围：Search-index snippets and abstract summaries only; page not opened this round
- 对候选的约束：Only the reference list was visible via the index; abstract not seen. Used solely as a pointer for further MAS-security neighbors (e.g. GAM-BIT, identity-failure "Echoing") to mine before execution; no claims taken from it.
- 访问层级：search_index_only
- 本轮复核：2026-10-10: first registered this round; WebFetch and direct arXiv/ACL access were unavailable.
- 用途：D4_neighbor

## 下一次真正运行之前

1. 在可直接访问 arXiv/ACL 的环境中，逐条打开 S31–S51 的摘要页与版本历史，把 `access_level` 改为直接阅读并记录范围；重读 S13 Fig. 4 解决数字差异。
2. 全文审读 S31 ARGUS/AgentLure 与 S38 ControlValve：若其中已有“同一有效纠正＋越权指令”的成对设计或真实多跳 peer 转述，D4′ 收缩为复现或任务迁移。
3. 重新核验 S15/S17/S18/S33/S34/S35/S37 的代码、许可与可用接口；冻结 B3（行动对齐/审计）与 B4（按设计分离）各一个同预算实现，并写明是 faithful adaptation 还是作者代码。
4. 复查 S51 的参考文献，判断 GAM-BIT 等多 Agent 安全基准是否已有同渠道纠正/注入成对任务；复查“未登记线索”。
5. D1 还须核对最新 Grounded Continuation v3、STALE（S50）与 StateAuditor（S20）；不能继续只对比早期的结构化 oracle 版本。Delayed Verification v2 也缩小了振荡主张，应以修订版而非标题当证据。
