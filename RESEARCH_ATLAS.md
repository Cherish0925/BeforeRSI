# RSI 三条路线：数量、团队与研究方向

**调查仍在进行。以下是已核对的重点案例，不是最终领域总数。**

[离线 HTML](research/atlas/index.html) · [简明 PDF](output/pdf/beforersi-research-atlas.pdf)

原 8/2/2 是未完成调查时选出的12个案例；既没有证明其余工作低质，也不能代表全球有价值工作的数量。此次补入14项机制审查，其中7项进入重点案例；仍不宣称完成全领域筛选。

| 路线 | 重点案例 | 工业独立 | 学术独立 | 产学联合 |
|---|---:|---:|---:|---:|
| Harness | 12 | 2 | 1 | 9 |
| Model | 5 | 3 | 0 | 2 |
| Model × Harness | 2 | 1 | 0 | 1 |

按论文首页署名机构分类；产学联合单列，一项只计一次。不是按经费、作者人数或主导权计数。STOP 按署名计为联合，研究期间在微软的脚注保留。

## 三条路线分别在推进什么

### Harness

让经验和代码改变下一次执行或研发。 从提示与记忆，扩展到整套 agent、改进器和评价流程。

- 工业应用目标：减少人工维护，提高可靠性，降低调用与执行成本。
- 研究问题：哪些改动能迁移？后继是否更会产生下一代改进？
- 当前证据：已有提示、代码、经验库和评价流程的更新实例；强度从任务适应到改进器自改不等。
- 判断边界：自动 harness 研发不自动等于递归能力增长；SoL-Pi 将新 harness 反哺后继研发列为未来方向。

**已核对重点名单：** STOP、Promptbreeder、SICA、DGM、HyperAgents、RRSI、AIDE²、HGM、ACE、SoL-Pi、ModularRSI、Red Queen Gödel Machine

### Model

让模型产生的训练信号更新模型，并进入后续学习。 从自生成样本，走向策略、评价器、验证器的反馈闭环。

- 工业应用目标：扩展高质量训练信号，减少标注瓶颈，提升推理与 agent 能力。
- 研究问题：反馈如何跟上模型？哪些条件下自训练改善、饱和或退化？
- 当前证据：已核对70B迭代偏好/评价训练、DeepSeek证明验证循环和Kimi自评价RL；不是只有两个70B案例。
- 判断边界：ReST-EM、SIMA 2、GPT-Red 的机制应被保留；公开参数不足时另列，不当作低价值淘汰。

**已核对重点名单：** Self-Rewarding LM、Self-Taught Evaluators、Iterative RPO、DeepSeekMath-V2、Kimi K2 · 自评价 RL

### Model × Harness

harness 改变可学轨迹，参数更新再改变 harness 的可行设计。 把数据产生、外部工作流和权重学习放进同一迭代流程。

- 工业应用目标：用可承担的模型规模完成更强的科研或企业 agent 任务。
- 研究问题：双向适配何时有正收益？如何避免模仿失配与跨任务回退？
- 当前证据：MASS 报告两轮工作流/SFT交替；Salesforce工作主要证明一次联合适配。
- 判断边界：本次仅两项通过重点审查，不是全领域只有两项。EvoTrainer规模仍待核准；Co-Harness证据审查未完。

**已核对重点名单：** MASS、On-policy M–H Co-evolution

目标与方向为对所列论文的综合判断，不是全行业意见调查，也不是按论文数量推算的趋势。

## 调查账本

完整目录 127 项；其中 38 项有机制审查卡片，67 项仍待审，另有 16 项历史材料与 6 项背景。已审卡片中只有 19 项进入重点视图。

另有 4 项已审机制但规模待核准；6 项关键前身/支撑；6 项低于27B的机制参考；3 项评测/形式工具。

Model / 混合规模门槛保留。AlphaProof 的3B主网络说明：不满足门槛不等于研究劣质。

## 原文与审查记录

- [逐项研究卡片](research/atlas/core-cards.md)
- [完整参考索引](research/atlas/references.md)
- [待审和筛选理由](research/atlas/review-queue.md)
- [分类原理附录](research/atlas/classification.md)
