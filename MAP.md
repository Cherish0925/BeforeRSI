# RSI 核心知识图与阅读路径

当前主图以 [中文研究地图](RESEARCH_ATLAS.md) 为入口，逐项资料见 [核心卡片](research/atlas/core-cards.md)。本次将主题相关性与研究价值判断分开；不再把完整目录中的候选一并放入主图。

![核心知识树](assets/atlas/knowledge-tree.png)

## 七个机制问题

| 分支 | 要解释的问题 |
|---|---|
| 改进器与研发流程自修改 | 谁产生改动；后继是否更会继续研发？ |
| 学习更新与训练过程 | 哪种干预使学习者在实际训练后更好？ |
| 课程、技能与环境共演 | 新信息从何而来，下一轮任务分布如何形成？ |
| 评价器、奖励与对手共演 | 反馈为何可信，代际分数如何保持可比？ |
| 模型与 harness 匹配 | 外部能力如何内化；为何可能负迁移？ |
| 可复用软件与成本机制 | 哪些修改跨任务保留，研发代价能否摊销？ |
| 比较、反例与形式边界 | 哪个观察支持哪一层结论？ |

![反馈与继承](assets/atlas/feedback-map.png)

## 图的语义

- `curated_membership`：本项目将限定贡献归入机制分支，不表示历史传承。
- `explicit_extension`：原文明确扩展先行工作；当前记录 DGM → HyperAgents。
- `explicit_comparison`：原文明示对照；当前记录 DGM → HGM，不声称代码直接继承。
- `analytical_comparison`：我们的比较阅读关系，不表示已核实引用。

[data/knowledge-graph.json](data/knowledge-graph.json) 只含 23 项核心工作与 7 个机制节点。
关系的来源和定位见 [data/quality-review.json](data/quality-review.json)；整合卡片和完整目录见 [data/research-atlas.json](data/research-atlas.json)。

## 历史与全目录放在哪里

16 项历史与机制参考在离线地图的独立页中按年份排列；时间先后不是因果传承。完整 123 项参考、所有候选及来源链接在 [参考索引](research/atlas/references.md)。两者均不充作主图中已确认的当代 RSI 成果。

阅读顺序可从 SEAL / DERL 的学习价值开始，接到 DGM / HGM / HyperAgents 的改进与谱系，再读 AIDE² 的后继接管比较；最后用 MASS、on-policy co-evolution 和 Rethinking Evaluation 检验迁移、代价与负结果。

## 对模型的要求

M/H/D 记录工件；解释必须指明信息、学习、选择和继承发生在哪里。改进者是系统承担的角色，不必是独立模块。任务、评价、资源和人的参与均需显式声明。系统分数、改进能力与多代继续价值是不同量。

通用表示尚不是普适预测。主图为理论提出具体约束，不证明所有工作已经被统一解释；详见 [THEORY.md](THEORY.md)、[MECHANISMS.md](MECHANISMS.md) 与 [研究计划](PROGRAM.md)。
