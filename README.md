# LLMLostMA

## 保留纠错能力的多智能体安全评估

**主线 D4：合法纠正与越权指令经由同一通信渠道到达时，防御能否保留有用证据、拒绝越权操作，并完成修订后的任务？**

**收窄后的主问题 D4′：当由真实 peer 转述的有效纠正要求改变后续动作时，按设计分离、行动对齐审计与跨度级来源审计各自落在安全—纠正效用边界的什么位置？**

这是 Meta-method v0.4 下的研究计划与离线检查，不是已验证的防御算法。状态日期：2026-10-10；计划版本：0.2.0。未运行 LLM、API、网络攻击或训练实验，未完成预注册或新颖性确认。

## 本轮决策

- D4 为首个立项检验：优先评估混合消息中的**有效纠正保留**，不以“首次发现过度防御”为主张。第二轮检索后 D4 拥挤度上调为中高：同一观察中分离良性与注入跨度（ARGUS）、控制流／数据流按设计分离（CaMeL、FIDES）、净化时保留任务证据（AgentSentry）、多 Agent 对齐检查可被绕过（ControlValve）都已有直接工作。
- 新增第五个防御臂 B4（按设计分离）与假说 H4：契约预授权的纠正应可无代价完成，缺口预计集中在需要改变动作的纠正上。40 个开发任务按这两类各 20 个分层。
- 新增无发言者诊断，把 peer 署名效应作为高于内容底线的增量报告。
- D1 降为备用：只研究暴露的工具无法直接恢复的语义依赖，不宣称所有代码依赖都不可追踪。
- D2 通信动作选择暂不开发；D3 跨轮／跨节点分片只作诊断控制，不独立立项。
- 复用既有多智能体安全项目的威胁模型和日志规范；本仓库尚未取得该项目的执行接口，因此只定义适配契约，**没有宣称已接入现有 harness**。

## 文件入口

| 文档 | 用途 |
|---|---|
| [研究方案](docs/research-plan.md) | D4′ 主张、H1–H4、分阶段实验与退出条件 |
| [威胁模型与成对世界](docs/threat-model.md) | 授权、真实性、来源、信息可辨性和安全边界 |
| [近邻与拥挤度](docs/related-work.md) | 51 条来源、核验层级、D4′ 特征对照与未登记线索 |
| [逐项审查回复](docs/review-response.md) | 接受哪些意见、拒绝哪些引文纠错、怎样改变方案 |
| [统计与资源计划](docs/evaluation.md) | 配对单位、指标、40 任务开发试验、精确功效、预算与确认条件 |
| [历史与状态](docs/decision-log.md) | 原方案、两轮修订的保留／改写范围和未执行事项 |
| [开发配置](configs/stage0.json) | 尚未运行的参数模板，不会自动调用 API |
| [来源登记](sources.json) | 机器可读来源记录，与近邻文档由检查器保持一致 |

## 文献核验层级

S01–S30 在第一轮按各条记录的范围直接阅读过。第二轮在只有网页检索索引可用的环境中复核：30 条题名与编号全部找到，无虚构来源，7 条有发表状态更新，1 条数字差异未解决（S13）。新增 S31–S51 只做了检索索引级核对，标为 `search_index_only`，运行前须直接阅读。

## 离线检查

Python 3.10+，只使用标准库：

```bash
python tools/check_plan.py
python -m unittest discover -s tests -v
```

检查覆盖文档链接、来源登记与文档一致性、协议与配置算术、指标定义、信息不足控制，以及精确条件 McNemar 功效的规划计算。测试通过不表示防御有效、论文可发表或样本量足够。没有 API runner、模型权重、原论文全文、凭据或真实敏感任务。

## English summary

LLMLostMA studies correction-preserving security in LLM agent networks. The first proposed experiment pairs a legitimate correction with a message carrying the same useful evidence plus an unauthorized directive, both delivered through the same peer channel. The goal is to keep justified updates without letting the message launder instruction authority. The design separates factual validity, permission, provenance and observability, and it counts complete refusal as lost utility rather than successful recovery.

Plan v0.2.0 follows a second literature pass. That pass re-located all 30 earlier sources and added 21 neighbors at search-index level. Each component of the original idea already has close prior work: span-level provenance auditing (ARGUS), control/data-flow separation by design (CaMeL, FIDES), evidence-preserving purification (AgentSentry), and bypasses of alignment checks in multi-agent systems (ControlValve). The plan therefore narrows its question to peer-relayed corrections that require changing downstream actions. It adds a by-design separation baseline, stratifies tasks by correction type, adds a speaker-free diagnostic, and uses exact McNemar power for planning (a 40-pair pilot reliably detects only differences of about 0.24 or larger). Only offline protocol checks have been executed. No novelty or deployment guarantee is claimed.

本次不替仓库所有者选择或变更许可证；第三方论文与代码仍受各自条款约束。
