# 决策历史与来源边界

## 2026-10-10 / 原方案

之前的备忘录把“分布式修订后的持续恢复＋选择下一份通信/计算”列为主问题，主观潜力约8。提出40个任务、4个Agent及程序化SQL/代码场景。它尚未执行模型实验。

原文件保持在对话附件，不覆盖：

- research_memo.md SHA256: `1e5fe5da5a3c1f6f65ef5892f14dab00fa33e8e1f4bb34e264ab258134a363a8`
- LiC_multiagent_assessment_20261010.zip SHA256: `be69d0efe52828c26616e60a8bfbbcf719ae60e3f1f86f5bb6654cd6380e6f4f`

这些是本轮对已挂载文件计算的完整性标识，不是可信时间戳，也不是仓库内可下载文件的承诺。本仓库不收录旧ZIP、原论文或审查对话全文。

## 2026-10-10 / 本轮修订

接受拥挤度与任务范围批评：补上直接近邻；将宽方向降为备用。D4改为“同渠道、同有效纠正、不同授权操作”的成对安全—效用研究。D1仅保留暴露语义依赖不完整及stale reintroduction问题；D2暂停；D3诊断性。

四项引文纠错经本轮核对不成立（PropUQ接收备注、Hi-Agreement v1、MAST赛道、Spark方法段）；StateWise确属单Agent。详见review-response.md。

第一轮拟用3个真正调用的LLM peers、40个开发任务、3轮、4防御×2分支×2重复。所有初始状态、分支结果、成本与拒绝分别报告。模型与正式推断参数尚未冻结。

## 研究与工程状态分开

- work_status: plan_revised
- claim_status: untested
- novelty_status: not_established
- dataset_role: development
- llm_experiment_run: false
- author_reproduction_run: false
- existing_harness_integrated: false
- public_content: 自有研究计划、文献定位、纯Python离线检查；无凭据、无私人数据、无原论文全文。

离线检查验证文档/配置与逻辑控制，不验证论文结论、不估计攻击发生率。任何后续运行应另存run_id、模型快照、命令、数据哈希、前史哈希、成本和原始输出；不得将本轮测试计作前瞻有效性证据。
