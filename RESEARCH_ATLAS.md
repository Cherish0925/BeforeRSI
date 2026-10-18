# BeforeRSI 中文研究地图

更新：2026-10-18。这是可核对的当前研究底稿，不是“全领域已经调研完”的宣告。

**先看 [图文导读 PDF](output/pdf/beforersi-research-atlas.pdf)，或下载打开 [可搜索离线地图](research/atlas/index.html)。** HTML 默认只显示核心；候选须主动切换，不能混入核心知识树。

![核心知识树](assets/atlas/knowledge-tree.png)

## 目前实际收集与筛选结果

| 层级 | 数量 | 如何使用 |
|---|---:|---|
| 核心命题 | 23 | 方法/证据或形式定义有定位，明确说明纳入价值；只进入这部分的主图 |
| 候选待审 | 78 | 不等于低质量，也不作为已确认价值的核心文献；需进一步深读 |
| 历史与机制参考 | 16 | 包括 14 个基础条目及 Good / Gödel Machine；单列溯源 |
| 背景移出 | 6 | 普通模型训练与外围背景，不作为直接 RSI 成果 |
| 已具名判为低价值 | 0 | 本轮未完成这种判定，不表示所有工作优质 |

另有 **567 个去重 arXiv 发现线索**，来自四份文献 README 快照。它们与 123 条目录存在重叠，不能相加为 690，也不能作为质量或覆盖率分母。发现线索不进入核心图。

旧目录的 63 直接主题 / 30 支撑 / 7 评测 / 3 理论 / 14 基础 / 6 背景是**相关性分类**；此处 23 / 78 / 16 / 6 是**图谱纳入决定**，两套统计用途不同。

## 质量门槛与阅读边界

- 原始方法/关键对照或完整定义有可定位依据；仅摘要不进入核心图。
- 有可明确陈述的机制差异、可靠反例、形式边界或真实研发用途，能够改变研究判断。
- 支持强度与纳入命题匹配；系统设计不能冒充因果实证，局部结果不能冒充一般规律。
- 模型/任务/训练/部署/资源与人的参与分别记录；未核准处明确留空或写未核准。
- 不按机构、GPU 数或是否 AI 辅助写作直接判质量；小规模限制外推，不自动抹去机制价值。

核心卡片是有理由的研究选择，仍不是独立复现或整篇质量认证。EvoTrainer 按训练侧系统设计纳入；GAI 按形式区分纳入，不能读成因果效果或增长定理。其余卡片也只支持各自写明的命题。

新增 56 项中的 46 项最初仅做摘要筛查，均未直接升级为主图文献。原有目录也不一律视为全文精读。每项的新阅读记录在卡片中给出。

## 七条机制线

| 分支 | 核心问题 | 代表工作 |
|---|---|---|
| 改进器与研发流程自修改 | 谁来产生下一代改进？ | DGM、HGM、HyperAgents、AIDE²、Frontis-MA1 / OpenMLE |
| 学习更新与训练过程 | 怎样的改动让学习者真正学得更好？ | SEAL、DERL、EvoTrainer、Automated Alignment Researchers |
| 课程、技能与环境共演 | 下一轮该学什么，从哪里获得新信息？ | Dr. Zero、Skill Self-Play、RLAnything |
| 评价器、奖励与对手共演 | 反馈为什么可信，如何跟上能力变化？ | Self-Taught Evaluators、GPT-Red、Red Queen Gödel Machine |
| 模型与 harness 的匹配 | 外部能力如何转成可学习、可迁移的能力？ | MASS、On-policy M–H Co-evolution |
| 可复用软件与成本机制 | 什么修改能跨任务保留，代价是多少？ | RRSI、ModularRSI、SoL-Pi |
| 比较、反例与形式边界 | 怎样知道系统真的改善了？ | Harness Updating ≠ Benefit、Rethinking Harness Evaluation、Generalized Agent Iteration |

![反馈与继承分析图](assets/atlas/feedback-map.png)

## 关系的含义

关系数据区分 **原文明示扩展**、**原文明示比较**、**我们的机制比较**。当前只记录 2 条经本轮定位确认的论文关系和 6 条分析关系；这不是已经构建完的引文网络。`data/knowledge-graph.json` 现在仅含核心工作；完整书目留在独立目录。图中机制归类与分析比较不是引用关系。

| 两项工作 | 关系与依据 |
|---|---|
| DGM / HyperAgents | 原文明确以 DGM 为基础扩展元层可编辑性；[定位](https://arxiv.org/html/2603.19461v1) §3；本文本轮核对 |
| DGM / HGM | 原文明示比较，并改变后代价值估计与搜索分配；[定位](https://arxiv.org/html/2510.21614v1) §2–4；并非声称代码直接继承 |
| SEAL / DERL | 我们的比较：均按学习后的价值评价生成的干预；不表示已核实引用关系 |
| HyperAgents / AIDE² | 我们的比较：元层可编辑与固定外层加独立接管测试 |
| MASS / On-policy M–H Co-evolution | 我们的比较：轨迹内化及学习者不匹配/负迁移 |
| Self-Taught Evaluators / Red Queen Gödel Machine | 我们的比较：可学习评价器及校准来源 |
| RRSI / Rethinking Harness Evaluation | 我们的比较：迁移选择与预算竞争 |
| SoL-Pi / AIDE² | 我们的比较：运行节约是否进入后继研发能力 |

## 对当前理论的约束

1. **描述对象不等于解释机制。** M/H/D 可记录工件，真正比较的是干预如何改变信息、学习、选择与后续改进。
2. **固定外层并不排除有价值学习。** 但它与后继接管外层是不同命题；AIDE² 为此另设测试。
3. **协同收益不预设为正。** MASS 的回退及 on-policy 研究的模仿退化要求显式记录不匹配。
4. **反馈来源是理论的一部分。** 搜索引入外部信息，构造标签提供锚点，对手与评价器改变评分语义。
5. **成本至少分研发、目标训练、部署与评价。** token、GPU 小时、动作数、墙钟时间不能无转换地横比。
6. **通用性要落实到预测。** 这些工作要求的机制已被整理，但尚未证明一个统一模型能定量预测全部家族。

## 深读的次序

先用 **SEAL → DERL → AIDE²** 分清“学会回答、学会构造更新、学会继续研发”；再用 **HyperAgents / HGM** 理解元层与延续价值；用 **Skill-SP / GPT-Red / RQGM** 理解协同反馈；最后用 **MASS / On-policy co-evolution / Rethinking Evaluation** 检验负迁移与成本。箭头只表示建议阅读顺序。

## 文件入口

- [23 项中文研究卡片](research/atlas/core-cards.md)：原理、差异、证据、规模、边界、思想与路线含义。
- [123 项完整参考索引](research/atlas/references.md)：有稳定编号、纳入状态和全部原文链接。
- [候选与暂不纳入理由](research/atlas/review-queue.md)：按每一项给出决定，不以“未读”冒充“低质”。
- [质量与纳入数据](data/quality-review.json)、[整合图谱数据](data/research-atlas.json)。
- [旧机制目录](research/mechanism-map.md)、[相关性目录](research/scope-catalog.md)、[理论](THEORY.md)。
