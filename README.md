# LLMLostMA

## 保留纠错能力的多智能体安全评估

**主线 D4：合法纠正与越权指令经由同一通信渠道到达时，防御能否保留有用证据、拒绝越权操作，并完成修订后的任务？**

这是 Meta-method v0.4 下的研究计划与离线检查，不是已验证的防御算法。状态日期：2026-10-10；计划版本：0.1.0。未运行 LLM、API、网络攻击或训练实验，未完成预注册或新颖性确认。

## 本轮决策

- D4 为首个立项检验：优先评估混合消息中的**有效纠正保留**，不以“首次发现过度防御”为主张。
- D1 降为备用：只研究暴露的工具无法直接恢复的语义依赖，不宣称所有代码依赖都不可追踪。
- D2 通信动作选择暂不开发；D3 跨轮／跨节点分片只作诊断控制，不独立立项。
- 复用既有多智能体安全项目的威胁模型和日志规范；本仓库尚未取得该项目的执行接口，因此只定义适配契约，**没有宣称已接入现有 harness**。

## 文件入口

| 文档 | 用途 |
|---|---|
| [研究方案](docs/research-plan.md) | D4 主张、竞争解释、分阶段实验与退出条件 |
| [威胁模型与成对世界](docs/threat-model.md) | 授权、真实性、来源、信息可辨性和安全边界 |
| [近邻与拥挤度](docs/related-work.md) | 已核对来源、阅读深度、已有覆盖与剩余问题 |
| [逐项审查回复](docs/review-response.md) | 接受哪些意见、拒绝哪些引文纠错、怎样改变方案 |
| [统计与资源计划](docs/evaluation.md) | 配对单位、指标、40 任务开发试验、预算与确认条件 |
| [历史与状态](docs/decision-log.md) | 原方案的保留／改写范围和未执行事项 |
| [开发配置](configs/stage0.json) | 尚未运行的参数模板，不会自动调用 API |

## 离线检查

Python 3.10+，只使用标准库：

```bash
python tools/check_plan.py
python -m unittest discover -s tests -v
```

检查仅覆盖文档链接、协议一致性、指标算术及信息不足控制。测试通过不表示防御有效、论文可发表或样本量足够。没有 API runner、模型权重、原论文全文、凭据或真实敏感任务。

## English summary

LLMLostMA studies correction-preserving security in LLM networks. Its first proposed experiment pairs a legitimate correction with a message carrying the same useful evidence plus an unauthorized directive, delivered through the same peer channel. The objective is to preserve justified updates without laundering instruction authority. We separate factual validity, permission, provenance, and observability; include strong over-defense and task-alignment baselines; and treat complete refusal as lost utility rather than successful recovery. Only offline protocol checks have been executed. No novelty or deployment guarantee is claimed.

本次不替仓库所有者选择或变更许可证；第三方论文与代码仍受各自条款约束。
