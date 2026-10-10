# 决策历史与来源边界

## 2026-10-10 / 原方案

之前的备忘录把“分布式修订后的持续恢复＋选择下一份通信/计算”列为主问题，主观潜力约8。提出40个任务、4个Agent及程序化SQL/代码场景。它尚未执行模型实验。

原文件保持在对话附件，不覆盖：

- research_memo.md SHA256: `1e5fe5da5a3c1f6f65ef5892f14dab00fa33e8e1f4bb34e264ab258134a363a8`
- LiC_multiagent_assessment_20261010.zip SHA256: `be69d0efe52828c26616e60a8bfbbcf719ae60e3f1f86f5bb6654cd6380e6f4f`

这些是本轮对已挂载文件计算的完整性标识，不是可信时间戳，也不是仓库内可下载文件的承诺。本仓库不收录旧ZIP、原论文或审查对话全文。

## 2026-10-10 / 第一轮修订（v0.1.0）

接受拥挤度与任务范围批评：补上直接近邻；将宽方向降为备用。D4改为“同渠道、同有效纠正、不同授权操作”的成对安全—效用研究。D1仅保留暴露语义依赖不完整及stale reintroduction问题；D2暂停；D3诊断性。

四项引文纠错经本轮核对不成立（PropUQ接收备注、Hi-Agreement v1、MAST赛道、Spark方法段）；StateWise确属单Agent。详见review-response.md。

第一轮拟用3个真正调用的LLM peers、40个开发任务、3轮、4防御×2分支×2重复。所有初始状态、分支结果、成本与拒绝分别报告。模型与正式推断参数尚未冻结。

## 2026-10-10 / 第二轮：外部检索与方案 v0.2.0

**检索方法与限制。** 只能使用网页检索索引：WebFetch 对所有主机 DNS 失败，沙盒代理拒绝 arxiv.org、export.arxiv.org、aclanthology.org、api.semanticscholar.org。没有打开任何页面、PDF 或版本历史。新增来源全部标为 `search_index_only`，其数字视为作者自报或二手转述。

**复核结果。** S01–S30 的题名与编号全部在索引中找到，未发现虚构或错配来源。状态更新：S01 补充 arXiv 预印本 2505.11556 与旧题名；S09 找到 AAAI 论文集条目；S16、S17 补充 ACL 页码与 arXiv 预印本；S19 找到 ICLR 2026 论文集页面（解决上一轮未复核的会议问题）；S27 经 ICLR 博客确认为 ICLR 2026 Outstanding Paper；S30 确认为 NeurIPS 2024 D&B。S13 有一处未解决的数字差异（第三方 62.9%/51.5% vs 上一轮读图 63.9%/52.7%），引用前重读。S02 的 EMNLP 接收备注本轮无法在索引中再次看到，也未见反证，维持“作者自报”。S04 的 spotlight 仍只有二手来源。

**新增近邻（S31–S51）。** 最影响 D4 的是：ARGUS（同一观察中良性与注入跨度分开，按完整良性因果链放行动作）[S31]；Abdelnabi & Bagdasarian（严格数据／指令分离会损害情境合理行为）[S32]；CaMeL 与 FIDES（控制流／数据流按设计分离）[S33,S34]；AgentSentry（净化时保留任务证据）[S35]；ControlValve（多 Agent 中对齐检查可被控制流劫持绕过）[S38]；The Attacker Moves Second（自适应攻击绕过多数已发表防御）[S39]；The Price of Safety（防御的良性情形成本）[S40]；One Axis, No Brake 与 Most LLM Conformity Needs No Speaker（事后过滤的自知上限、无发言者底线）[S41,S42]；以及多 Agent 消息级防御 G-Safeguard、SAC、Challenger/Inspector [S43,S44,S46]。

**决策。**

1. D4 拥挤度由中度上调为中高；主问题收窄为 D4′：真实 peer 转述的、需改变后续动作的有效纠正。伞问题保留。
2. 新增 B4 按设计分离防御臂（CaMeL／FIDES 式）与 H4。理由：原方法候选“证据候选／操作请求分路”是其特例，不先与它比较就无法主张任何分路收益。防御臂由 4 个增至 5 个，主网格上限由 5,760 增至 7,200 次 peer 生成。
3. 40 个任务按纠正类型分层（契约预授权／需改变动作，各 20）。这是 H4 的直接检验；每层只作描述。
4. 新增无发言者诊断（8 个开发任务、B0、两分支、2 次重复，上限 288 次 peer 生成），把 peer 署名效应作为高于内容底线的增量报告。
5. B2 改正：PIGuard／PromptGuard 2 是独立分类器，不是同一 peer 模型上的提示，成本单独计。B3 候选池扩为 Task Shield、ActGuard、AgentSentry、MELON、ARGUS、AlignmentCheck；选纯对齐检查时须报告 ControlValve 的已知绕过。
6. 统计：离线检查器加入精确条件 McNemar 功效。n=40、q=0.30 时 80% 功效的最小差值约 0.243，与粗式 0.243 一致；该检验实际第一类错误率约 0.024；5pp 效应约需 980 对（粗式 942）。修正审查回复中“约 25pp”的不一致表述为约 24pp。
7. 主观潜力由约 7/10 下调为约 6/10（有条件），仍高于 D1/D2/D3。
8. 平衡准确率的表述改为：二元决策恰为 1/2，允许 defer 且记为未正确时最多 1/2。

实验状态不变：未运行 LLM、作者复现或现有 harness 接入；新颖性仍为 not_established。

## 研究与工程状态分开

- work_status: plan_revised (v0.2.0)
- claim_status: untested
- novelty_status: not_established
- dataset_role: development
- llm_experiment_run: false
- author_reproduction_run: false
- existing_harness_integrated: false
- source_access: S01–S30 prior_round_direct_read；S31–S51 search_index_only
- public_content: 自有研究计划、文献定位、纯Python离线检查；无凭据、无私人数据、无原论文全文。

离线检查验证文档/配置与逻辑控制，不验证论文结论、不估计攻击发生率。任何后续运行应另存run_id、模型快照、命令、数据哈希、前史哈希、成本和原始输出；不得将本轮测试计作前瞻有效性证据。
