# 对外部审查的逐项处理

日期：2026-10-10。依据为用户提供的审查意见、此前研究备忘录和本轮重新读取的公开来源。这里记录判断与理由，不把不同模型同意当作独立科学验证。

## 1. 接受的方向性纠偏

- 原主线漏掉 HiddenBench、Consilience、Delayed Verification、Reliability–Contagion、Governed Shared Memory、Q-Mix 与 DALA，导致拥挤度估计偏乐观。已补入[S01,S07–S12]。
- D4 优先：从泛泛恢复转为防御对合法纠正的代价；D1是备用，D2暂缓，D3仅诊断。不同时新增一个庞大的训练项目。
- SQL/代码的显式依赖常可由工具解决，保留为正控制；主材料增加文字中的派生数值与复制常量。不能从“包含代码”推论所有语义依赖都已知，也不声称没有工具能追踪。
- 40个任务只适合开发立项检验，不能当有功效的正式确认；开发后不重新标成holdout。其约24pp MDE只是特定配对方差假设下的粗数量级（第二轮用精确 McNemar 功效复算为约 0.243，见[统计与资源计划](evaluation.md)）。

## 2. 引文纠错不能全部接受

| 外部意见 | 本轮原文核对 | 处置 |
|---|---|---|
| PropUQ-MAS arXiv没有EMNLP接收备注 | 当前abs的Comments明确写“Accepted to EMNLP 2026 (Main Conference)”，v3日期2026-09-01 | 保留为作者arXiv自报接收；不冒充已核验ACL Anthology最终发表。[S02] |
| Hi-Agreement名称在任何版本都不存在 | 2608.03421v1摘要、§3标题与Fig.1均使用Hi-Agreement | 保留为v1名称，不混写成所有版本的现名。[S03] |
| MAST的Datasets & Benchmarks赛道未确认 | 官方NeurIPS proceedings页标题下明确列出Datasets and Benchmarks Track | 保留赛道标注；本轮未另外复核spotlight标记。[S04] |
| Spark to Fire的三态检查和回滚未核实 | v2 §VI-D有Green/Red/Yellow；§VI-E Stage4及§VI-F明确blocking/rollback | 其功能描述可保留；这不是我们复现了算法或验证其效果。PDF抓取失败，核对限于HTML方法段。[S05] |
| StateWise是single-agent | 原文是单Agent的持久状态修复，不是peer网络证据 | 接受并在文献表明确降为邻近的局部模块，不证明网络推广。[S06] |

“未找到/未看全文”不是“原文没有”的证据。相反，补齐引文也不挽救原主线的新颖性；D4优先和降级旧方向的决定不变。

## 3. 进一步收紧D4

“尚无直接邻居”不能作为结论。NotInject/PIGuard已有过度防御任务；Task Shield、Trust Propagation和ActGuard已有保留效用或选择性清理；Utility Under Attack已直接研究低信任证据被排除。[S14–S18]

本轮主检索包括 correction+injection、legitimate corrections、multi-agent overblocking、task alignment及所给ID，查到上述额外近邻。未完成穷尽引文普查，novelty_status保持not_established。

D4需要比“正常消息vs恶意消息”更强：C/X都含同一份有用更正，X额外要求越权；把事实与指令分开核验，并观察真实Agent后续执行。防御若丢掉整条消息虽然安全，也失去任务能力。

## 4. 审查中的两个数字如何使用

Easier to Mislead v2 Fig.4(a,b)：CoT将all-wrong条件harmful revision从63.9%降至36.5%，同时all-correct条件beneficial revision从52.7%降至32.5%。已看PDF第7页。它使用模拟peer回答，且harmful/beneficial来自初始正确/错误的不同子群，不能直接移植为本项目配对效应。[S13]

Utility Under Attack v1 Table6：Corpus N中0.8583→0.0417，证据召回99.17%→0；已看PDF第18页。它是“所有答案证据都来自低信任来源”的构造极端，不是通用部署损失；论文强调假断言污染不等于指令注入，且修复提案尚未验证。[S14]

## 5. 完成状态

已完成：本轮定向核对、改写研究计划、增加样本/指标边界的离线算术与结构检查。

未完成：模型实验、作者方法复现、真实网络防御评估、攻击覆盖证明、适应性对手验证、新颖性确认、预注册、接入既有安全harness。

本仓库保存当前方案及可追溯的修改理由；不将原审查全文或私人通信上传。旧备忘录不被静默改写，历史与原文件哈希见[decision-log.md](decision-log.md)。
