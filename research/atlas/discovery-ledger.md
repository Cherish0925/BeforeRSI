# 检索线索与范围判断

> 此页保留早期快照，分类、阅读状态和取舍以 [全量审查说明](reading-audit.md) 与当前 HTML 为准；不能把此页旧统计作为最终结论。

这是一份逐条处理的文献入口表。只有对应目录的工作具有其卡片注明的研读范围；其余条目依据原始摘要判断相关性，没有依据摘要、参数或机构作质量淘汰。

| 类别 | 条数 |
|---|---:|
| 评测 / 理论候选 | 64 |
| 方法候选，待全文研读 | 240 |
| 综述 / 路线图 | 17 |
| 使能方法 / 背景 | 133 |
| 已对应目录 | 86 |
| 当前图谱范围外 | 27 |

## 逐条记录

| arXiv | 文献 | 范围判断 | 理由 |
|---|---|---|---|
| [2609.05677](https://arxiv.org/abs/2609.05677v1) | Who Maintains Agent Skills? A Longitudinal Study of Human-Governed, AI-Assisted Skill Maintenance | 评测 / 理论候选 | 对技能仓库真实提交做纵向治理与维护分析，提供自动技能维护的人类基线；不是自主RSI成果，但可检验实际部署中的更新与责任边界。 |
| [2609.05019](https://arxiv.org/abs/2609.05019v1) | TROVE: Adaptive Agent Skill Orchestration via Trace-Grounded Route Validation and Editing | 方法候选，待全文研读 | 离线把搜索轨迹沉淀成技能与条件转移图，在线按证据局部编辑执行路线；具有可复用结构，但需区别持久技能学习与单次计划调整。 |
| [2609.11873](https://arxiv.org/abs/2609.11873v3) | The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement | 综述 / 路线图 | 提出从执行自主到递归元改进的路线及HCI分析，主要贡献是领域框架与挑战归纳；工业实例和初步实验需分别识别，不能当作单一RSI系统。 |
| [2609.04697](https://arxiv.org/abs/2609.04697v1) | SQL-Zero: Self-Evolving Text-to-SQL | 方法候选，待全文研读 | 出题者与SQL求解者交替GRPO，数据库执行给出反馈并限制重复模板；直接属于可验证课程共演化，且摘要明确后期迁移可能随规模退化。 |
| [2609.08944](https://arxiv.org/abs/2609.08944v1) | SkillAdam: Stable and Efficient Skill Evolution for Agents | 方法候选，待全文研读 | 以优化记忆积累修改方向，并按近期改善波动调整技能编辑幅度，持续优化冻结模型的技能文档；需验证Adam类比与真实优化收益的边界。 |
| [2609.08228](https://arxiv.org/abs/2609.08228v2) | SE-GoS: Self-Evolving Graph-of-Skills for Skill Library at Scale | 方法候选，待全文研读 | 固定技能内容和检索算法，仅依据执行轨迹修改检索图边、权重与节点描述；有留出迁移且多轮不再改善，适合明确图状态进化的能力边界。 |
| [2609.09646](https://arxiv.org/abs/2609.09646v2) | RobustSGPO: Search-Space Control for Agent Harness Evolution | 方法候选，待全文研读 | 控制harness补丁的修改范围、检查执行性并保留候选起点，以任务反馈继续搜索；属于执行结构搜索，须核对留出集和保留开销。 |
| [2609.09153](https://arxiv.org/abs/2609.09153v1) | Procedural Graphs: Self-Evolving Execution Structures for LLM Agents | 方法候选，待全文研读 | 由成功失败轨迹对比修改程序图拓扑和属性，以留出验证决定提交，并保存拒绝记录；具备持久执行结构改进，值得复核图演化与迁移。 |
| [2609.08183](https://arxiv.org/abs/2609.08183v2) | NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness | 方法候选，待全文研读 | 路由记录与能力评估改变下一轮训练混合，结合SFT和on-policy蒸馏形成模型更新候选；摘要未证明路由harness自身也被训练或改写。 |
| [2609.06396](https://arxiv.org/abs/2609.06396v2) | MetaRSI / RSI2: A Meta-Recursive Self-Improving System for Recursive Self-Improving Systems Themselves | 方法候选，待全文研读 | 明确组合数据、harness编辑与参数训练，并以元策略调整算子顺序及提案策略，直接涉及改进过程优化；闭环强度与理论假设须全文核实。 |
| [2609.04665](https://arxiv.org/abs/2609.04665v1) | Harness-agnostic detection and immunization of reward hacking in self-evolving language models | 评测 / 理论候选 | 为自进化闭环检测代理分数与真实能力偏离，并用保密对照及候选重选干预奖励投机；属于跨路线评价机制，需核实检测假设和选择偏差。 |
| [2609.08599](https://arxiv.org/abs/2609.08599v1) | Graph-Based Personalized Memory for LLM Agents: Representation, Evolution, Retrieval, and Evaluation | 综述 / 路线图 | 综述个性化图记忆的表示、更新、检索和评价，可补充长期状态分类；重点是用户信息管理，不应把所有记忆更新都统计为能力自进化。 |
| [2609.04869](https://arxiv.org/abs/2609.04869v1) | From Interaction Traces to Persistent Skills: Online Evolution for Computer-Use Agents | 方法候选，待全文研读 | 将GUI轨迹和评价反馈转为版本化技能库，每轮使用固定快照、下轮继承更新；明确有持续状态和空库对照，也报告重复修改未必修复失败。 |
| [2609.08919](https://arxiv.org/abs/2609.08919v1) | Experience Funnel: A State-Policy Alternating Loop for Self-Evolving Agents | 方法候选，待全文研读 | 先把交互经验转成可编辑文本状态，再将跨版本仍有效行为蒸馏进参数，更新后再采集经验；明确连接状态适应和policy巩固的交替闭环。 |
| [2609.08404](https://arxiv.org/abs/2609.08404v1) | Environments as Scaffold: Enriching Feedback to Bootstrap Self-Evolving Agents in Long-Horizon Tasks | 使能方法 / 背景 | 通过环境反馈丰富化帮助长程RL并内化指导，直接关联训练环境设计；摘要未明确环境规则由agent自主更新，不能仅据适应一词认定混合RSI。 |
| [2609.11677](https://arxiv.org/abs/2609.11677v2) | Ecdysis: Efficient and Effective Training of Runtime Harnesses for LLM Agents | 方法候选，待全文研读 | 聚合跨任务重复失败后才修改运行时harness，以减少对单个模型错误的过度补偿；直接研究更新证据与跨模型泛化，需复核因果消融。 |
| [2609.04865](https://arxiv.org/abs/2609.04865v2) | CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution | 方法候选，待全文研读 | 共享骨干联合训练推理与Meta-Skill角色，同时改进层级技能库；参数和外部技能通过任务效果耦合，是混合路线的重要全文候选。 |
| [2609.11682](https://arxiv.org/abs/2609.11682v1) | COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization | 方法候选，待全文研读 | 上下文bandit分配技能候选评估预算，再用执行证据修改技能种群；同时涉及搜索策略和技能产物，需阅读全文确认样本效率及目标模型自优化。 |
| [2609.09134](https://arxiv.org/abs/2609.09134v1) | Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.08832](https://arxiv.org/abs/2609.08832v1) | Closing the Consistency Gap: Self-Evolving Agents That Learn to Stay on Course | 方法候选，待全文研读 | 对同任务多次执行的不稳定步骤做诊断，将针对性指导写入记忆供以后运行使用；以重复成功率而非仅平均分评价，属于持久经验改进。 |
| [2507.21046](https://arxiv.org/abs/2507.21046v4) | A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence | 综述 / 路线图 | 按进化对象、时机和方法组织模型、记忆、工具与架构研究，可补充检索与分类；这是综述，不应与原创系统重复计入成果数量。 |
| [2508.07407](https://arxiv.org/abs/2508.07407v2) | A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems | 综述 / 路线图 | 用输入、agent、环境、优化器四要素统一自进化反馈，综述不同更新对象和领域应用；应作为来源导航，不能与被综述工作重复计数。 |
| [2501.07278](https://arxiv.org/abs/2501.07278v2) | Lifelong Learning of Large Language Model based Agents: A Roadmap | 综述 / 路线图 | 将持续学习的感知、记忆与行动模块及遗忘问题系统整理，提供长期学习背景；路线图与概念建议不等于已经实现的递归改进系统。 |
| [2607.13104](https://arxiv.org/abs/2607.13104v1) | Self-Improvements in Modern Agentic Systems: A Survey | 综述 / 路线图 | 以模型与运行支架构成系统配置、用自发更新算子描述持久改进，综述按对象与反馈分类；适合作分类参照而不计作独立实证系统。 |
| [2601.12538](https://arxiv.org/abs/2601.12538v2) | A Survey of Agentic Reasoning for Large Language Models: Towards Recursively Self-Improving and Collective Agents | 综述 / 路线图 | 覆盖基础推理、自进化及集体智能，并区分上下文适应和参数后训练；适合检查分类遗漏，但一般多智能体协作不自动属于RSI。 |
| [2303.17651](https://arxiv.org/abs/2303.17651v2) | Self-Refine: Iterative Refinement with Self-Feedback | 使能方法 / 背景 | 同一模型生成反馈并反复改写当前答案，无额外训练；摘要未说明反馈或策略跨任务保留，应列推理时自修订方法而非直接持续自进化。 |
| [2303.11366](https://arxiv.org/abs/2303.11366v4) | Reflexion: Language Agents with Verbal Reinforcement Learning | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2304.03442](https://arxiv.org/abs/2304.03442v2) | Generative Agents: Interactive Simulacra of Human Behavior | 使能方法 / 背景 | 从经历形成记忆和高层反思来生成可信社会行为，但主要目标是行为模拟，摘要未证明改进自身任务能力的闭环；保留为记忆架构背景。 |
| [2310.08560](https://arxiv.org/abs/2310.08560v2) | MemGPT: Towards LLMs as Operating Systems | 使能方法 / 背景 | 通过分层记忆与中断管理长期上下文，是持久状态基础设施；摘要未明确以任务反馈优化记忆机制本身，需区别记住用户与提升改进能力。 |
| [2305.16291](https://arxiv.org/abs/2305.16291v2) | Voyager: An Open-Ended Embodied Agent with Large Language Models | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2310.03714](https://arxiv.org/abs/2310.03714v1) | DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines | 使能方法 / 背景 | 将语言模型流水线编译为指标驱动的提示、示例与可选微调优化，提供自动改进基础设施；支持多种算子不代表同一实验已联合自进化。 |
| [2211.01910](https://arxiv.org/abs/2211.01910v2) | Large Language Models Are Human-Level Prompt Engineers | 使能方法 / 背景 | 由LLM提出指令候选并按另一个模型的任务得分选择，是早期自动提示搜索；提供AI优化AI的基础机制，未表明优化器自身递归改善。 |
| [2309.03409](https://arxiv.org/abs/2309.03409v3) | Large Language Models as Optimizers | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2309.16797](https://arxiv.org/abs/2309.16797v1) | Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2406.07496](https://arxiv.org/abs/2406.07496v1) | TextGrad: Automatic "Differentiation" via Text | 使能方法 / 背景 | 用语言反馈沿计算图改进提示和代码等变量，是自动优化复合AI的通用工具；应用也含分子与治疗计划，须筛出真正改变AI系统的案例。 |
| [2203.14465](https://arxiv.org/abs/2203.14465v2) | STaR: Bootstrapping Reasoning With Reasoning | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2310.02304](https://arxiv.org/abs/2310.02304v3) | Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2401.10020](https://arxiv.org/abs/2401.10020v3) | Self-Rewarding Language Models | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2402.16823](https://arxiv.org/abs/2402.16823v3) | Language Agents as Optimizable Graphs | 方法候选，待全文研读 | 把agent表示为可组合计算图，同时优化节点提示与边连接，直接作用于模型外部执行结构；应核实图优化反馈、跨代保留及预算。 |
| [2408.08435](https://arxiv.org/abs/2408.08435v2) | Automated Design of Agentic Systems | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2410.10762](https://arxiv.org/abs/2410.10762v4) | AFlow: Automating Agentic Workflow Generation | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2502.04180](https://arxiv.org/abs/2502.04180v2) | Multi-agent Architecture Search via Agentic Supernet | 方法候选，待全文研读 | 优化架构分布而非单一工作流，再按查询采样计算与工具配置；是自适应结构搜索候选，需核实更新信号及训练与推理阶段界限。 |
| [2410.06153](https://arxiv.org/abs/2410.06153v3) | AgentSquare: Automatic LLM Agent Search in Modular Design Space | 方法候选，待全文研读 | 将计划、推理、工具和记忆模块统一接口，用模块进化与重组搜索agent，并以代理预测省评估；直接属于harness设计空间优化。 |
| [2502.02533](https://arxiv.org/abs/2502.02533v2) | Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies | 方法候选，待全文研读 | 交替优化局部提示、全局拓扑及工作流提示，利用前阶段结果搜索下一阶段；直接涉及系统配置优化，需检查反馈闭环与跨任务迁移。 |
| [2410.11782](https://arxiv.org/abs/2410.11782v3) | G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks | 使能方法 / 背景 | 以图自编码器为任务生成通信拓扑，是学习式架构配置方法；摘要强调适配与效率，但没有说明部署经验持续改变设计器，暂作方法背景。 |
| [2406.14228](https://arxiv.org/abs/2406.14228v3) | EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms | 方法候选，待全文研读 | 以既有agent作个体，经变异、交叉和选择形成多agent配置，符合系统结构搜索范围；是否跨任务持续改善而非单题集成须全文确认。 |
| [2309.17288](https://arxiv.org/abs/2309.17288v3) | AutoAgents: A Framework for Automatic Agent Generation | 使能方法 / 背景 | 根据当前任务生成角色团队并用观察者反思计划和回答，属于动态协作机制；摘要未说明学到的配置跨任务继承，暂不当作持续自进化成果。 |
| [2503.03686](https://arxiv.org/abs/2503.03686v1) | MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems | 使能方法 / 背景 | 在查询—系统代码配对数据上训练架构生成模型，可降低配置成本；摘要描述离线数据构造和单次生成，尚无执行反馈反复更新生成器证据。 |
| [2504.15257](https://arxiv.org/abs/2504.15257v1) | FlowReasoner: Reinforcing Query-Level Meta-Agents | 方法候选，待全文研读 | 通过执行表现、复杂度和效率奖励训练生成多agent系统的meta-agent；学习对象是架构设计能力，需分清查询级临时结构与跨任务继承。 |
| [2502.04306](https://arxiv.org/abs/2502.04306v1) | ScoreFlow: Mastering LLM Agent Workflows via Score-based Preference Optimization | 方法候选，待全文研读 | 以量化反馈的Score-DPO优化生成工作流的能力，连接模型训练与agent结构设计；需核对实际被训练参数及生成结构如何被执行和保留。 |
| [2507.22606](https://arxiv.org/abs/2507.22606v1) | MetaAgent: Automatically Constructing Multi-Agent Systems Based on Finite State Machines | 方法候选，待全文研读 | 用有限状态机表达并优化多agent系统，自动设计角色行为及状态转移；属于架构搜索候选，摘要尚不足判断优化是否基于持续执行反馈。 |
| [2510.02669](https://arxiv.org/abs/2510.02669v1) | AutoMaAS: Self-Evolving Multi-Agent Architecture Search for Large Language Models | 方法候选，待全文研读 | 根据性能成本生成、融合和删除操作符，并以在线反馈继续调整架构；属于agent结构进化候选，需验证在线与长期继承的具体实现。 |
| [2603.22791](https://arxiv.org/abs/2603.22791v1) | ABSTRAL: Automatic Design of Multi-Agent Systems Through Iterative Refinement and Topology Optimization | 方法候选，待全文研读 | 把系统架构作为可修改自然语言文档，通过对比轨迹迭代发现角色和拓扑，并测试设计文档跨域迁移；有明确可保留的系统级改进对象。 |
| [2602.06511](https://arxiv.org/abs/2602.06511v4) | EvoMAS: Evolutionary Generation of Multi-Agent Systems | 方法候选，待全文研读 | 执行轨迹驱动配置空间中的变异和交叉，并迭代维护种群与经验记忆；有明确持久结构搜索，需复核可执行率、预算和跨任务比较。 |
| [2509.11079](https://arxiv.org/abs/2509.11079v5) | Difficulty-Aware Agentic Orchestration for Query-Specific Multi-Agent Workflows | 方法候选，待全文研读 | 根据执行成功更新难度估计，再调操作符分配和模型路由以生成查询级工作流；存在反馈适应候选，但持久更新范围需阅读全文确定。 |
| [2604.01658](https://arxiv.org/abs/2604.01658v3) | CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery | 使能方法 / 背景 | 持续多agent协作和共享记忆用于外部数学、算法、系统发现，具有可复用搜索机制；摘要未证明进化产物是自身agent，不能直接等同强RSI。 |
| [2608.09629](https://arxiv.org/abs/2608.09629v1) | Rethinking Self-Evolving Agents: Do We Still Need Prescribed Optimization Pipelines? | 方法候选，待全文研读 | 固定目标、权限、数据和预算，让优化agent自主组织证据采集与产物修改过程；直接研究改进策略自主性及其对优化模型能力的依赖。 |
| [2510.07841](https://arxiv.org/abs/2510.07841v1) | Self-Improving LLM Agents at Test-Time | 方法候选，待全文研读 | 先找模型不确定样本，再自产相似训练例并做测试时微调，直接形成参数自适应；需分开同模型TT-SI与强教师TT-D，核查监督可靠性。 |
| [2607.21461](https://arxiv.org/abs/2607.21461v3) | AREX: Towards a Recursively Self-Improving Agent for Deep Research | 使能方法 / 背景 | 内外循环主要验证并修订当前研究答案，模型另经mid-training和RL训练；须区分答案递归精化与跨任务自改进，摘要未充分证明后者。 |
| [2510.13220](https://arxiv.org/abs/2510.13220v2) | EvoTest: Evolutionary Test-Time Learning for Self-Improving Agentic Systems | 方法候选，待全文研读 | 每局后由evolver改提示、记忆、超参和工具例程，下一局actor继承配置；J-TTL专门测跨回合学习，是直接harness候选兼评价线索。 |
| [2504.07952](https://arxiv.org/abs/2504.07952v1) | Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory | 方法候选，待全文研读 | 模型自行提炼策略与代码片段到持久cheatsheet，跨查询调用并更新，权重冻结；是经验状态进化候选，须核查题目顺序与评估泄漏控制。 |
| [2504.16084](https://arxiv.org/abs/2504.16084v3) | TTRL: Test-Time Reinforcement Learning | 方法候选，待全文研读 | 用无标签测试题的多数票作为RL奖励更新参数，是直接测试时自训练；投票奖励可能自强化错误，须区分测试分布适应与未知任务泛化。 |
| [2601.15808](https://arxiv.org/abs/2601.15808v2) | Inference-Time Scaling of Verification: Self-Evolving Deep Research Agents via Test-Time Rubric-Guided Verification | 使能方法 / 背景 | rubric verifier反馈促使当前答案多轮精化且不额外训练，是验证器与推理时计算扩展；摘要未描述跨任务保留改进，不能仅依标题算RSI。 |
| [2505.19590](https://arxiv.org/abs/2505.19590v5) | Learning to Reason without External Rewards | 方法候选，待全文研读 | 以模型自身置信度替换GRPO外部奖励，提供内生反馈的参数自训练候选；摘要无法证明置信度可靠或长期稳定，需要核查校准和塌缩消融。 |
| [2601.21268](https://arxiv.org/abs/2601.21268v1) | Reinforcement Learning from Meta-Evaluation: Aligning Language Models Without Ground-Truth Labels | 使能方法 / 背景 | 利用评审器对自然语言元问题的正面判断概率训练生成器，属于无金标准AI反馈方法；摘要未说明评审器也学习或反馈过程自主改进。 |
| [2507.19457](https://arxiv.org/abs/2507.19457v2) | GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2510.04618](https://arxiv.org/abs/2510.04618v3) | Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2601.16175](https://arxiv.org/abs/2601.16175v2) | Learning to Discover at Test Time | 方法候选，待全文研读 | 对当前科学问题的探索经验做测试时RL，参数真实更新而非仅冻结模型搜索；重点是求单个优秀解，不能据此推断跨问题通用持续递归。 |
| [2305.10250](https://arxiv.org/abs/2305.10250v3) | MemoryBank: Enhancing Large Language Models with Long-Term Memory | 使能方法 / 背景 | 通过遗忘、强化及历史交互总结维持用户记忆，主要研究长期陪伴和个性化；内容状态更新不必然代表自优化学习机制，列记忆背景。 |
| [2508.16153](https://arxiv.org/abs/2508.16153v2) | Memento: Fine-tuning LLM Agents without Fine-tuning LLMs | 方法候选，待全文研读 | 以环境反馈改写情节记忆并通过case选择影响决策，基础LLM固定；属于在线记忆策略适应，需核对神经检索策略与非参数版本的差别。 |
| [2509.04439](https://arxiv.org/abs/2509.04439v3) | ArcMemo: Abstract Reasoning Composition with Lifelong LLM Memory | 方法候选，待全文研读 | 将推理轨迹压成概念级模块记忆并在后续题目中检索、更新，比较动态库与静态库；直接检验跨查询积累，需复核ARC评估协议。 |
| [2507.06229](https://arxiv.org/abs/2507.06229v5) | Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving | 使能方法 / 背景 | 聚合不同框架轨迹成共享知识库，以计划和诊断检索提升任务表现；可支撑集体经验学习，但摘要未说明库按后续结果持续修订的闭环。 |
| [2601.08605](https://arxiv.org/abs/2601.08605v2) | ExpSeek: Self-Triggered Experience Seeking for Web Agents | 使能方法 / 背景 | 用步骤熵主动触发经验检索与介入，可提高固定agent利用经验的能力；摘要未明确经验生成器或库持续进化，暂列选择与调用机制背景。 |
| [2602.15902](https://arxiv.org/abs/2602.15902v1) | Doc-to-LoRA: Learning to Instantly Internalize Contexts | 使能方法 / 背景 | 超网络学习把文档一次映射成LoRA适配器，是快速参数内化与元学习方法；摘要没有自产经验反复改善更新器的闭环，可作为模型路线支撑。 |
| [2606.04536](https://arxiv.org/abs/2606.04536v1) | Scaling Self-Evolving Agents via Parametric Memory | 方法候选，待全文研读 | 显式记忆提炼出在线LoRA训练信号，同时RL训练如何提炼和行动，形成慢基座、快权重与外部状态耦合；单回合与跨回合继承须核实。 |
| [2603.18620](https://arxiv.org/abs/2603.18620v1) | Learning to Self-Evolve | 方法候选，待全文研读 | 以编辑上下文后下游表现的改善训练编辑策略，并用树引导演化，直接学习如何自改进；需分清优化者参数与被编辑目标模型是否共同更新。 |
| [2512.24695](https://arxiv.org/abs/2512.24695v1) | Nested Learning: The Illusion of Deep Learning Architectures | 方法候选，待全文研读 | 提出多层优化视角及学习自身更新规则的序列模块，直接触及学习机制自修改；需阅读全文区分元训练能力、在线更新与强递归的实证层次。 |
| [2602.07755](https://arxiv.org/abs/2602.07755v1) | Learning to Continually Learn via Meta-learning Agentic Memory Designs | 方法候选，待全文研读 | Meta Agent搜索可执行的数据库schema、记忆检索与更新代码，优化的是学习经验的机制本身；直接补足记忆内容之外的记忆设计进化路线。 |
| [2610.11373](https://arxiv.org/abs/2610.11373v1) | From a Prompt to Repertoires: Evolving Functional REpertoires Enable LLM Continual Learning | 方法候选，待全文研读 | 顺序任务中把单提示改为可扩展函数库，兼容更新修订旧函数、冲突更新新增函数，旨在防遗忘；属于持久结构适应，需核查通用性。 |
| [2605.08703](https://arxiv.org/abs/2605.08703v2) | RewardHarness: Self-Evolving Agentic Post-Training | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2508.19005](https://arxiv.org/abs/2508.19005v6) | Building Self-Evolving Agents via Experience-Driven Lifelong Learning: A Framework and Benchmark | 评测 / 理论候选 | 提出经验探索、记忆、技能与内化框架及StuLife长期任务基准；摘要不足证明四项都已闭环实现，适合作评价候选并补读方法正文。 |
| [2601.18226](https://arxiv.org/abs/2601.18226v2) | Yunjue Agent Tech Report: A Fully Reproducible, Zero-Start In-Situ Self-Evolving Agent System for Open-Ended Tasks | 方法候选，待全文研读 | 将连续任务反馈转为可复用工具，迭代合成、优化并保留工具，另有并行进化和迁移评估；属于工具能力扩张，需验证反馈可靠性。 |
| [2606.06741](https://arxiv.org/abs/2606.06741v1) | OpenSkill: Open-World Self-Evolution for LLM Agents | 方法候选，待全文研读 | 从开放文档与仓库获取知识和验证锚点，自建练习任务后优化可迁移技能，直接涉及验证环境的自构造；目标答案隔离与验证可靠性需核实。 |
| [2603.01145](https://arxiv.org/abs/2603.01145v2) | AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution | 方法候选，待全文研读 | 从对话互动抽象技能并持续维护、按需注入后续请求，参数不重训；直接对应持久可迁移技能层，需核查更新采纳规则和长期效果。 |
| [2604.17308](https://arxiv.org/abs/2604.17308v1) | SkillFlow:Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents | 评测 / 理论候选 | 以顺序任务、技能发现、修补及库继承评估长期演化，既报告收益也报告退化；直接补足技能使用率不等于技能效用的评价维度。 |
| [2603.02766](https://arxiv.org/abs/2603.02766v1) | EvoSkill: Automated Skill Discovery for Multi-Agent Systems | 方法候选，待全文研读 | 按执行失败生成或修改技能文件夹，以留出性能和Pareto选择保留，模型权重固定；有明确持久产物及零样本迁移证据，优先阅读全文。 |
| [2602.08234](https://arxiv.org/abs/2602.08234v2) | SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2604.08377](https://arxiv.org/abs/2604.08377v2) | SkillClaw: Let Skills Evolve Collectively with Agentic Evolver | 方法候选，待全文研读 | 汇聚跨用户长期轨迹，由evolver修订或扩展技能并同步共享仓库，属于集体技能演化；需核查反馈来源、验证隔离和跨用户迁移证据。 |
| [2603.16060](https://arxiv.org/abs/2603.16060v2) | ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical Reinforcement Learning | 方法候选，待全文研读 | 同一策略承担技能管理与解题，成功轨迹更新技能库，层级奖励同时推动推理与库质量；明确参数和可复用外部技能共同演化。 |
| [2510.15863](https://arxiv.org/abs/2510.15863v2) | PolySkill: Learning Generalizable Skills Through Polymorphic Abstraction | 方法候选，待全文研读 | 将技能抽象目标与具体执行解耦，持续提炼技能并改善自主探索课程；有跨网站迁移候选，需核对目标修改、技能继承与实际反馈来源。 |
| [2509.18133](https://arxiv.org/abs/2509.18133v4) | Self-Evolving LLMs via Continual Instruction Tuning | 使能方法 / 背景 | 任务专属与共享LoRA配合对抗学习支持连续指令训练和抗遗忘，工业价值可单独评估；摘要未显示训练数据或学习方案由系统自生成优化。 |
| [2505.14970](https://arxiv.org/abs/2505.14970v4) | Self-Evolving Curriculum for LLM Reasoning | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2608.20920](https://arxiv.org/abs/2608.20920v2) | ForeDreamer: A Self-Evolving Dual-Agent Memory Architecture for Future Event Prediction | 方法候选，待全文研读 | 区分单次预测事实状态与跨事件经验记忆，分别改进预测决策和记忆构建；存在持久经验更新，需全文核查反馈真值与跨时间测试隔离。 |
| [2308.10144](https://arxiv.org/abs/2308.10144v3) | ExpeL: LLM Agents Are Experiential Learners | 方法候选，待全文研读 | 自动收集任务经验并抽取语言规则，在以后任务中回忆经验与洞察，模型权重不变；属于持久经验学习，需核对规则更新和跨域转移。 |
| [2605.06614](https://arxiv.org/abs/2605.06614v1) | SkillOS: Learning Skill Curation for Self-Evolving Agents | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2602.02474](https://arxiv.org/abs/2602.02474v2) | MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2512.17102](https://arxiv.org/abs/2512.17102v2) | Reinforcement Learning for Self-Improving Agent with Skill Library | 方法候选，待全文研读 | 顺序任务rollout把生成技能持续加入库，技能奖励训练生成和调用能力；模型学习与外部技能积累相互作用，适合混合路线全文核查。 |
| [2505.03335](https://arxiv.org/abs/2505.03335v3) | Absolute Zero: Reinforced Self-play Reasoning with Zero Data | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2508.05004](https://arxiv.org/abs/2508.05004v4) | R-Zero: Self-Evolving Reasoning LLM from Zero Data | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2506.24119](https://arxiv.org/abs/2506.24119v3) | SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning | 方法候选，待全文研读 | 模型与持续变强的自身版本进行多轮零和博弈，以角色条件优势估计训练，形成自动对手课程；是模型层自博弈与迁移候选。 |
| [2511.16043](https://arxiv.org/abs/2511.16043v2) | Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2603.09206](https://arxiv.org/abs/2603.09206v1) | MM-Zero: Self-Evolving Multi-Model Vision Language Models From Zero Data | 方法候选，待全文研读 | Proposer、视觉代码生成者和Solver均由同一基座初始化并用GRPO训练，生成可验证视觉任务构成自举信号；不是仅在推理时修改答案。 |
| [2509.15194](https://arxiv.org/abs/2509.15194v3) | Evolving Language Models without Labels: Majority Drives Selection, Novelty Promotes Variation | 方法候选，待全文研读 | 多数票提供选择锚点、推理新颖性奖励维持探索，针对无标签自训练的熵塌缩；有直接模型更新候选，但长期开放任务稳定性仍待全文验证。 |
| [2510.27072](https://arxiv.org/abs/2510.27072v1) | Towards Understanding Self-play for LLM Reasoning | 评测 / 理论候选 | 以Absolute Zero为对象分析自博弈的权重更新稀疏性、熵和奖励设计，并与RLVR及SFT比较；属于自改进动力学证据，不是新系统数量。 |
| [2602.21320](https://arxiv.org/abs/2602.21320v1) | Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2608.19197](https://arxiv.org/abs/2608.19197v3) | SPADE: Self-Play in Adaptive Synthetic Executable Environments | 方法候选，待全文研读 | 单一模型分任可执行环境设计者和求解者，按提示辅助前后的regret共同强化学习；同时改变训练环境与模型，须全文确认环境继承及训练稳定性。 |
| [2605.09959](https://arxiv.org/abs/2605.09959v1) | G-Zero: Self-Play for Open-Ended Generation from Zero Data | 方法候选，待全文研读 | 以自生提示引起的预测分布变化作为内在信号，GRPO训练提案者、DPO训练生成者，形成双模型闭环；理论依赖探索覆盖及标签噪声假设。 |
| [2607.23802](https://arxiv.org/abs/2607.23802v2) | From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open-Ended LLM Self-Improvement | 方法候选，待全文研读 | 把开放任务变成间谍博弈，通过预先确定身份产生可验证奖励并训练模型；关键待核查点是代理奖励如何迁移到真实开放任务质量。 |
| [2601.07055](https://arxiv.org/abs/2601.07055v2) | Dr. Zero: Self-Evolving Search Agents without Training Data | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2511.00602](https://arxiv.org/abs/2511.00602v4) | OpenSIR: Open-Ended Self-Improving Reasoner | 方法候选，待全文研读 | 同一模型轮换教师和学生，从单种子生成并求解问题，以多样性奖励和难度校准维持课程；需核查无外部验证时奖励如何避免自证。 |
| [2608.03392](https://arxiv.org/abs/2608.03392v4) | Self-Evolving Coding Agents | 综述 / 路线图 | 按框架、记忆、技能、工作流和环境等持久更新目标综述编码agent自演化，并讨论反馈、泛化与成本；用于扩充文献与边界，不计独立实验成果。 |
| [2410.04444](https://arxiv.org/abs/2410.04444v4) | Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2505.14738](https://arxiv.org/abs/2505.14738v2) | R&D-Agent: An LLM-Agent Framework Towards Autonomous Data Science | 使能方法 / 背景 | 将机器学习工程拆成研发阶段与组件并在MLE-Bench验证，直接涉及AI研究自动化；摘要没有证明研究agent本身随研发成果持续升级。 |
| [2601.07348](https://arxiv.org/abs/2601.07348v5) | Controlled Self-Evolution for Algorithmic Code Optimization | 使能方法 / 背景 | 进化对象主要是算法题解代码，使用反馈引导交叉变异和跨题经验记忆；可支撑研究agent的程序优化，但摘要未显示它改进自身改进器或AI系统。 |
| [2510.06261](https://arxiv.org/abs/2510.06261v2) | AlphaApollo: A System for Deep Agentic Reasoning | 使能方法 / 背景 | 结合工具推理的逐轮RL和测试时答案改写，具有模型与系统联合设计价值；摘要未显示更新后的harness反过来训练后继，递归边界待正文确认。 |
| [2603.15707](https://arxiv.org/abs/2603.15707v1) | SEMAG: Self-Evolutionary Multi-Agent Code Generation | 使能方法 / 背景 | 按题目难度调整多agent工作流并选择外部最新模型，属于配置与路由适配；摘要未显示其自主训练模型或将改进器更新持久继承。 |
| [2505.22954](https://arxiv.org/abs/2505.22954v3) | Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2506.13131](https://arxiv.org/abs/2506.13131v1) | AlphaEvolve: A coding agent for scientific and algorithmic discovery | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2506.03136](https://arxiv.org/abs/2506.03136v2) | Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning | 方法候选，待全文研读 | 编码者与单元测试者根据交互结果共同RL，测试者从编码错误学习并为编码者提供信号；属于模型协同训练，不以实验模型规模排除。 |
| [2510.21614](https://arxiv.org/abs/2510.21614v3) | Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2511.02864](https://arxiv.org/abs/2511.02864v3) | Mathematical exploration and discovery at scale | 使能方法 / 背景 | AlphaEvolve用于67项数学构造并联用证明系统，展示程序进化的外部科学价值；改进目标是数学成果，不能直接记成AI系统自身升级。 |
| [2509.19349](https://arxiv.org/abs/2509.19349v1) | ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.19526](https://arxiv.org/abs/2609.19526v1) | Self Improvement via Fast Tree-search | 方法候选，待全文研读 | 自修改代码树结合LLM成对补丁评判与Bradley-Terry排序，只给高潜力节点昂贵任务评测；需核查评判误差、全预算与留出泛化。 |
| [2609.25510](https://arxiv.org/abs/2609.25510v2) | Hill Sampling for Test-Time Scaling: A Simple and Better Alternative to Repeated Sampling, Evolution, and Training | 评测 / 理论候选 | 在相同科学程序问题比较保留最佳解的采样、进化及测试时权重更新，直接检验复杂改进机制是否必要；对象不是自身agent，作为对照证据。 |
| [2511.13646](https://arxiv.org/abs/2511.13646v3) | Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly? | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2607.07663](https://arxiv.org/abs/2607.07663v2) | Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops | 综述 / 路线图 | 综述按改进对象和闭环程度组织1250项arXiv记录，并突出评价信号；有助发现遗漏，数量是综述语料范围，不能当成1250个严格RSI成果。 |
| [2609.13406](https://arxiv.org/abs/2609.13406v1) | Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.15802](https://arxiv.org/abs/2609.15802v1) | The Economics of Recursive Self-Improvement | 使能方法 / 背景 | 以研发反馈图和环路弹性分析自加速，区分狭窄研发指标与经济能力；是机制与测量框架，校准结论并非运行中的RSI系统实证。 |
| [2609.00137](https://arxiv.org/abs/2609.00137v1) | Recursive Criticality of AI Self-Improvement | 使能方法 / 背景 | 用研发反馈、继承效率、周期和研究难度定义递归再生数，讨论机构间传播；这是参数化理论模型，不是观察到能力越过某阈值的事实。 |
| [2609.14858](https://arxiv.org/abs/2609.14858v2) | Dream-RSI: Recursive Self-Improvement through Evolving Worlds | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.14857](https://arxiv.org/abs/2609.14857v2) | ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2608.13951](https://arxiv.org/abs/2608.13951v1) | HELIX: Model-Harness Co-evolution for Recursive Self-Improvement | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2608.24735](https://arxiv.org/abs/2608.24735v1) | Meta$^n$: Recursive Self-Improvement through Emergent Depth | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2608.07645](https://arxiv.org/abs/2608.07645v1) | Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative Evolution | 方法候选，待全文研读 | 自修改编码agent利用多任务轨迹及跨谱系同题轨迹，扩展单失败轨迹变异；有继承与比较反馈，需复核理论加性景观假设及迁移设置。 |
| [2606.26294](https://arxiv.org/abs/2606.26294v3) | The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.15364](https://arxiv.org/abs/2609.15364v2) | RSIAgent: Autonomous Exploration for Recursive Self-improvement in New Environments | 方法候选，待全文研读 | 课程、执行与验证agent先广后深探索环境，保留可复用因果知识并冻结供下游使用；是无权重训练的持久记忆自改进候选。 |
| [2607.28568](https://arxiv.org/abs/2607.28568v1) | Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2606.20657](https://arxiv.org/abs/2606.20657v3) | A-Evolve-Training: Autonomous Post-Training of a 30B Model | 方法候选，待全文研读 | 报告多轮自主后训练30B模型并修订误导性开发指标下的搜索策略；还报告更大模型管线，需区分闭环基础设施与有人工基线的效果证据。 |
| [2605.27276](https://arxiv.org/abs/2605.27276v2) | SIA: Self Improving AI with Harness & Weight Updates | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2608.08466](https://arxiv.org/abs/2608.08466v1) | Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Harnesses | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2605.15871](https://arxiv.org/abs/2605.15871v2) | Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.18094](https://arxiv.org/abs/2609.18094v4) | Agora: Git as Shared Memory for Collective AutoResearch | 使能方法 / 背景 | Git记录多研究agent的假说、验证和贡献DAG，实测合作完成权重迁移；支撑AI4AI协作研究，但无匹配对照或研究者自身递归升级证据。 |
| [2603.19461](https://arxiv.org/abs/2603.19461v1) | Hyperagents | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.26457](https://arxiv.org/abs/2609.26457v1) | Recursive self-improvement of AI research agents | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2604.05142](https://arxiv.org/abs/2604.05142v2) | A mathematical theory of evolution for self-designing AIs | 使能方法 / 背景 | 以有向后继设计树替代随机突变，推导有界适应度与额外锁定条件下的极限；是RSI理论背景，结论必须连同假设而非普遍演化规律呈现。 |
| [2510.04399](https://arxiv.org/abs/2510.04399v3) | On The Statistical Limits of Self-Improving Agents | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2510.10232](https://arxiv.org/abs/2510.10232v2) | SGM: A Statistical Godel Machine for Risk-Controlled Recursive Self-Modification | 使能方法 / 背景 | 以e值和浓度界审核自修改，并分配跨轮全局错误预算，直接支撑可靠RSI接受规则；统计保证的独立性及自适应条件须全文核查。 |
| [2603.26499](https://arxiv.org/abs/2603.26499v2) | AIRA_2: Overcoming Bottlenecks in AI Research Agents | 使能方法 / 背景 | 通过异步GPU池、隐藏一致评估和交互式操作器提升机器学习研究搜索；属于AI4AI研究基础，摘要未说明研究agent自身后继接管循环。 |
| [2606.20683](https://arxiv.org/abs/2606.20683v1) | From Question Answering to Task Completion: A Survey on Agent System and Harness Design | 综述 / 路线图 | 从model-harness耦合梳理观察、上下文、控制、动作、状态和验证等运行职责；适合校正知识图谱分类，不能作为已实现协同进化的实验。 |
| [2606.09498](https://arxiv.org/abs/2606.09498v3) | Self-Harness: Harnesses That Improve Themselves | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2608.07545](https://arxiv.org/abs/2608.07545v1) | DarwinX: Evolving Agent Harnesses Through Natural Selection | 方法候选，待全文研读 | 冻结模型、种群选择harness，以保留旧能力并扩展覆盖的契约接纳变体，档案支持重组；需核查无回归门控如何与真正留出评测隔离。 |
| [2608.25593](https://arxiv.org/abs/2608.25593v2) | JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution | 方法候选，待全文研读 | 训练专用模型即时生成、修复任务harness，并从历史配置的表现继续蒸馏；模型学习和harness档案形成耦合，需核查真实多轮与外推。 |
| [2608.02276](https://arxiv.org/abs/2608.02276v1) | Harness-R1: Learning to Edit Executable Runtime Harnesses from Agent Failure Trajectories | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2605.09998](https://arxiv.org/abs/2605.09998v1) | Continual Harness: Online Adaptation for Self-Improving Foundation Agents | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2606.01770](https://arxiv.org/abs/2606.01770v2) | Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.24972](https://arxiv.org/abs/2609.24972v3) | RRSI: Regularized Recursive Self-Improvement of Agent Harnesses | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.20519](https://arxiv.org/abs/2609.20519v1) | SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.24974](https://arxiv.org/abs/2609.24974v1) | Harness-Zero: Harness Distillation via Agent-as-Harness | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.26760](https://arxiv.org/abs/2609.26760v2) | Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents | 方法候选，待全文研读 | 从无策略脚手架逐步积累可执行控制代码，按函数轨迹定位故障、联合修复并用留出门控回滚；持续继承对象清楚，需核查训练发现成本。 |
| [2604.25850](https://arxiv.org/abs/2604.25850v4) | Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses | 方法候选，待全文研读 | 把可编辑组件、分层轨迹证据和可检验修改预测对齐，形成自主harness编辑闭环；需全文核查跨基座迁移、门控及各组件消融。 |
| [2608.10178](https://arxiv.org/abs/2608.10178v1) | One Recipe, Many Harnesses: What Self-Evolution Encodes Across Languages and Models | 评测 / 理论候选 | 固定进化配方横跨八种语言和三基座，分解通用补偿机制与生态专属实现；可检验自演化到底迁移什么，而非只看最终均值。 |
| [2609.20804](https://arxiv.org/abs/2609.20804v1) | An Empirical Study of Harness Design for Coding Agents | 评测 / 理论候选 | 固定执行循环、匹配176组配置考察上下文、规划和动作接口，解释不同模型与预算下的机制贡献；为自演化提供必要基线但不构成自演化。 |
| [2607.12227](https://arxiv.org/abs/2607.12227v4) | Rethinking the Evaluation of Harness Evolution for Agents | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2605.30621](https://arxiv.org/abs/2605.30621v1) | Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2607.13083](https://arxiv.org/abs/2607.13083v1) | Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened | 评测 / 理论候选 | 构造真实最优行动是不改动的确定性环境，检验harness提议者虚构失败并固化无效guardrail；直接区分修复进展与修改本身。 |
| [2609.20474](https://arxiv.org/abs/2609.20474v1) | How Do Agent Harnesses Create Value? Planning Information and Release Control in Stateful LLM Agents | 评测 / 理论候选 | 用等长打乱文本对照分离规划信息，用终态验证器测错接纳和成本；本身不是自演化，但提供harness价值归因和接受损失的控制实验。 |
| [2609.18366](https://arxiv.org/abs/2609.18366v3) | Bad Genius: Counterfactual-Guided Harness Evolution Beyond Task-Specific Shortcuts | 评测 / 理论候选 | 在harness进化中加入反事实协议挑战者和有效性防火墙，检测任务留出仍存在的协议捷径；直接研究泛化证据与评测共演化边界。 |
| [2605.10663](https://arxiv.org/abs/2605.10663v1) | Evolving-RL: End-to-End Optimization of Experience-Driven Self-Evolving Capability within Agents | 方法候选，待全文研读 | 联合优化经验提取与使用能力，评价信号分别训练提取器和求解器，并测试有无推理期经验积累；可解释模型与外部经验的协同演化。 |
| [2411.00418](https://arxiv.org/abs/2411.00418v3) | Self-Evolved Reward Learning for LLMs | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2603.17621](https://arxiv.org/abs/2603.17621v2) | Complementary RL: Towards Efficient Experience-Driven Agent Learning | 方法候选，待全文研读 | 在RL内协同训练经验提取器与policy，按经验对成功的边际帮助更新提取策略；外部经验随actor变化，值得核查是否真正共同更新。 |
| [2408.02632](https://arxiv.org/abs/2408.02632v2) | SEAS: Self-Evolving Adversarial Safety Optimization for Large Language Models | 方法候选，待全文研读 | 红队与目标模型经初始化、攻击和对抗优化多轮共同训练，自生成数据构成反馈；属于模型协同进化，需核查安全评分与攻击迁移。 |
| [2510.23595](https://arxiv.org/abs/2510.23595v3) | Multi-Agent Evolve: LLM Self-Improve through Co-evolution | 方法候选，待全文研读 | 提问者、求解者和裁判由单一LLM实例化并共同RL，目标降低外部标注与验证依赖；应核查裁判信号是否可自我强化错误。 |
| [2504.00587](https://arxiv.org/abs/2504.00587v2) | AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems | 方法候选，待全文研读 | 去中心化agent图按本地经验调整连接、任务路由和检索记忆，涉及持久技能专化；摘要尚不能区分跨任务继承与单次任务动态编排。 |
| [2505.16997](https://arxiv.org/abs/2505.16997v1) | X-MAS: Towards Building Multi-Agent Systems with Heterogeneous LLMs | 使能方法 / 背景 | 大规模评估异构模型在不同领域和职能的选择，提升固定多agent组合；未展示模型或harness通过自身反馈递归更新，属配置设计参考。 |
| [2604.18292](https://arxiv.org/abs/2604.18292v1) | Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2602.04837](https://arxiv.org/abs/2602.04837v1) | Group-Evolving Agents: Open-Ended Self-Improvement via Experience Sharing | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2603.16910](https://arxiv.org/abs/2603.16910v1) | TerraLingua: Emergence and Analysis of Open-endedness in LLM Ecologies | 使能方法 / 背景 | 持久多agent生态研究资源约束下规范与文化产物的累积，可能启发群体继承机制；摘要未显示AI能力或研发改进器被优化。 |
| [2601.03192](https://arxiv.org/abs/2601.03192v2) | MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2402.17574](https://arxiv.org/abs/2402.17574v3) | Agent-Pro: Learning to Evolve via Policy-Level Reflection and Optimization | 方法候选，待全文研读 | 从交互轨迹和信念做策略层反思，再用深度优先搜索优化政策；有跨轨迹行为修订，摘要的fine-tuning措辞不足以确认存在权重训练。 |
| [2605.09315](https://arxiv.org/abs/2605.09315v1) | Do Self-Evolving Agents Forget? Capability Degradation and Preservation in Lifelong LLM Agent Adaptation | 评测 / 理论候选 | 跨工作流、技能、模型和记忆展示新任务适应会侵蚀旧能力，并提出保留约束；直接检验自改进单调性，不能因报告负结果而排除。 |
| [2607.00871](https://arxiv.org/abs/2607.00871v1) | Self-Evolving Agents with Anytime-Valid Certificates | 评测 / 理论候选 | 用anytime-valid门控与固定错误预算审核版本化harness和小适配器，并设计no-op控制；重点是可审计接受，须核查证书假设及单次运行限制。 |
| [2603.11768](https://arxiv.org/abs/2603.11768v2) | Governing Evolving Memory in LLM Agents: Risks, Mechanisms, and the Stability and Safety Governed Memory (SSGM) Framework | 使能方法 / 背景 | 提出演化记忆治理架构，合并前做一致性验证、衰减和访问控制；摘要主要是概念和形式分析，应与实测自演化收益分开。 |
| [2605.18421](https://arxiv.org/abs/2605.18421v2) | EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective | 评测 / 理论候选 | 以episode内外及知识/执行记忆双轴比较15类方法与强长上下文基线，评估记忆何时真正贡献；是自演化记忆的比较工具。 |
| [2510.16079](https://arxiv.org/abs/2510.16079v3) | EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle | 方法候选，待全文研读 | 离线将轨迹蒸馏成策略库、在线检索再积累轨迹，并称有policy强化更新；明确经验闭环，但仅凭摘要不能判定强化是否实际更新模型权重。 |
| [2605.23989](https://arxiv.org/abs/2605.23989v1) | Towards trustworthy agentic AI: a comprehensive survey of safety, robustness, privacy, and system security | 综述 / 路线图 | 综述agent安全、鲁棒性、隐私与系统验证并讨论自演化，作为风险与评测背景；覆盖普通agent问题，不应整体统计为RSI研究成果。 |
| [2606.06114](https://arxiv.org/abs/2606.06114v3) | ANCHOR: An External LLM-Driven Supervisory Module Facilitating Healthy Evolution in Self-Evolving Systems | 评测 / 理论候选 | 给两个现有自演化框架加外部LLM监督，比较不同阶段反馈和监督频率对安全与能力的作用；属于闭环稳定化证据而非新基础模型。 |
| [2606.21090](https://arxiv.org/abs/2606.21090v1) | Self-Improvement Can Self-Regress: The Rise-and-Collapse Failure Mode of LLM Self-Training | 评测 / 理论候选 | 多种子连续强化训练显示同任务先升后崩，并比较跨轮记忆、早停和GRPO；直接研究自训练稳定性，不能仅以初期峰值声称持续提升。 |
| [2605.19576](https://arxiv.org/abs/2605.19576v3) | Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries | 评测 / 理论候选 | 通过关闭注入、提前退休等消融定位技能累积造成的检索漂移，再比较退休与容量治理；研究持久技能库的失效与修复而非简单数量增长。 |
| [2503.13657](https://arxiv.org/abs/2503.13657v3) | Why Do Multi-Agent LLM Systems Fail? | 使能方法 / 背景 | 建立多agent失败轨迹数据和设计、协调、验证三类taxonomy，为自动改进定位缺陷；研究对象是一般MAS而非自身更新闭环。 |
| [2505.00212](https://arxiv.org/abs/2505.00212v3) | Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems | 使能方法 / 背景 | 将多agent失败定位到责任agent与关键步骤，提供标注和方法比较；可支撑自改进信用分配，但并未让系统使用归因结果持续演化。 |
| [2509.06822](https://arxiv.org/abs/2509.06822v3) | RAFFLES: Reasoning-based Attribution of Faults for LLM Systems | 使能方法 / 背景 | 离线多评估器与裁判反复判断故障位置及理由，提升一般LLM系统诊断；是改进信号基础工具，摘要未显示闭环系统自修改。 |
| [2505.19234](https://arxiv.org/abs/2505.19234v2) | GUARDIAN: Safeguarding LLM Multi-Agent Collaborations with Temporal Graph Modeling | 使能方法 / 背景 | 用时序交互图检测和缓解多agent幻觉传播，训练异常检测模块；监督功能可服务改进循环，但摘要没有系统持续自修改的机制。 |
| [2508.19504](https://arxiv.org/abs/2508.19504v1) | Aegis: Taxonomy and Optimizations for Overcoming Agent-Environment Failures in LLM Agents | 使能方法 / 背景 | 从失败轨迹设计环境可观测性、计算卸载与推测动作优化，不修改agent或基座；提供环境层设计参考，未展示优化器自己进化。 |
| [2601.22290](https://arxiv.org/abs/2601.22290v1) | The Six Sigma Agent: Achieving Enterprise-Grade Reliability in LLM Systems Through Consensus-Driven Decomposed Execution | 使能方法 / 背景 | 分解任务并以多模型采样、共识和动态冗余提升可靠性，未体现持久学习或改进器演化；独立错误假设也不能直接外推真实agent。 |
| [2604.08906](https://arxiv.org/abs/2604.08906v4) | Understanding Bugs in Modern Agentic Frameworks: A Study of Symptoms, Root Causes, and Triggering Conditions | 使能方法 / 背景 | 分析五种agent框架已修复bug，定位模型接入、上下文和编排问题及触发组合；有助harness测试，但不是系统自我改进实验。 |
| [2603.21522](https://arxiv.org/abs/2603.21522v1) | Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation | 使能方法 / 背景 | 学习历史推理轨迹表示以检测、诊断并缓解多agent失败；可提供改进反馈，但摘要未展示持久自修改或由改进后系统继续改进。 |
| [2608.15763](https://arxiv.org/abs/2608.15763v5) | Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Technical Report | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2607.24300](https://arxiv.org/abs/2607.24300v1) | Self-Authored Verification Is Unreliable in Heuristic Self-Improving Agents | 评测 / 理论候选 | 对照自写验证分数与封闭部署评估，并用外部接受环阻止策略和测试共同漂移；直接研究自证循环，名称SEAL不等于既有模型编辑SEAL。 |
| [2608.18066](https://arxiv.org/abs/2608.18066v2) | On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification | 评测 / 理论候选 | 对记忆自改进重复运行并打乱任务顺序，检验方差与隐含课程依赖；还测试更明确反馈能否修复退化，属于关键可靠性和泛化证据。 |
| [2607.27687](https://arxiv.org/abs/2607.27687v1) | Rehearse: Stepping Back from the Confidence Cliff in Self-Improving Autoresearch | 方法候选，待全文研读 | 研究agent用相似历史尝试结果辅助执行前候选判断，并以可复用skill改造autoresearch循环；有同训练轮数比较，须全文核查后继与记忆继承。 |
| [2606.08106](https://arxiv.org/abs/2606.08106v1) | PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents | 评测 / 理论候选 | 把重复接纳改动视为序贯检验，用paired e-process控制单候选假接纳与可选停止；需区分每次决策保证和整个无限改进链的总风险。 |
| [2608.20290](https://arxiv.org/abs/2608.20290v1) | Phantom Gains: Auditing Self-Improvement Against a Measured Null | 评测 / 理论候选 | 将LoRA自训练与完全冻结但同管线的对照比较，逐题检测虚假增益、推理批次效应和错误发现；直接约束模型自改进的证据标准。 |
| [2608.00017](https://arxiv.org/abs/2608.00017v1) | Memory Reward Inflation in Self-Improving LLM Agents | 评测 / 理论候选 | 研究自评分错误如何经记忆检索持续放大，提出误差独立条件和去膨胀方法；直接涉及冻结模型下经验继承是否改善真实表现。 |
| [2607.07436](https://arxiv.org/abs/2607.07436v2) | The Blind Curator: How a Biased Judge Silently Disables Skill Retirement in Self-Evolving Agents | 评测 / 理论候选 | 分析裁判假阳性如何阻断技能退休，用受控奖励污染区分机制故障与端到端分数；揭示自演化库即使总分稳定也可能失去更新约束。 |
| [2606.14629](https://arxiv.org/abs/2606.14629v3) | When Good Verifiers Go Bad: Silent Negative Transfer in Verifier-Guided VLM Training | 评测 / 理论候选 | 分析VLM自DPO中训练分数提高但留出退化，区分验证诱导梯度保真与跨分布迁移，并测试非对称过滤；直接揭示模型自训练负迁移。 |
| [2606.28374](https://arxiv.org/abs/2606.28374v1) | Recursive Self-Evolving Agents via Held-Out Selection | 方法候选，待全文研读 | 从轨迹改写策略、技能、playbook三层状态，以独立split的keep-better门控接纳；需审查重复使用留出集的选择偏差及单调安全主张。 |
| [2605.20086](https://arxiv.org/abs/2605.20086v1) | What Do Evolutionary Coding Agents Evolve? | 评测 / 理论候选 | 回放进化代码局部搜索状态并干预常数、组件和模型，区分新算法、调参、重组与过拟合；可校验AI4AI搜索的创新解释。 |
| [2609.09219](https://arxiv.org/abs/2609.09219v2) | Scores Alone Do Not Prove Discovery: The Discovery Certification Protocol for Auditing AI Research Agents | 评测 / 理论候选 | 为AI研究发现建立受信息和预算约束的恢复对照与反馈因果审计，区分高分、可恢复已知结论和新发现；不属于新RSI能力系统。 |
| [2608.14905](https://arxiv.org/abs/2608.14905v3) | How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks | 评测 / 理论候选 | 100项真实科研任务和800条完整轨迹用于过程失效归因，直接评价研究agent的自检与修订能力；跨harness相似失效不能单独证明模型因果。 |
| [2605.27905](https://arxiv.org/abs/2605.27905v2) | AI Research Agents Narrow Scientific Exploration | 评测 / 理论候选 | 用多框架和模型产生大量科研想法，比较其集中度、距起始文献及后续人类研究；检验研究搜索宽度，尚不能替代实际实验发现评价。 |
| [2601.22436](https://arxiv.org/abs/2601.22436v3) | Large Language Model Agents Are Not Always Faithful Self-Evolvers | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2603.23994](https://arxiv.org/abs/2603.23994v2) | Understanding the Challenges in Iterative Generative Optimization with LLMs | 评测 / 理论候选 | 研究初始产物、轨迹反馈跨度和批次如何决定生成式优化成败，并指出增大批次不必然提升泛化；可用于解释自改闭环设计条件。 |
| [2603.24647](https://arxiv.org/abs/2603.24647v5) | Can LLMs Beat Classical Hyperparameter Optimization Algorithms? A Study on autoresearch | 评测 / 理论候选 | 同预算比较autoresearch中的LLM、经典HPO及共享优化状态的混合方法，检验自主研究收益来源；小目标模型是受控环境而非排除理由。 |
| [2509.26354](https://arxiv.org/abs/2509.26354v2) | Your Agent May Misevolve: Emergent Risks in Self-evolving LLM Agents | 评测 / 理论候选 | 沿模型、记忆、工具和工作流四路径实验自演化偏离，揭示安全退化与工具漏洞继承；与能力主线正交但对完整领域图谱必要。 |
| [2602.03224](https://arxiv.org/abs/2602.03224v2) | TAME: A Trustworthy Test-Time Evolution of Agent Memory with Systematic Benchmarking | 方法候选，待全文研读 | Executor使用经验、Evaluator评估贡献并产生信任反馈，共同调整共享记忆的强化与复用；属于冻结权重下持续记忆演化方法。 |
| [2605.02900](https://arxiv.org/abs/2605.02900v2) | Safety in Embodied AI: A Survey of Risks, Attacks, and Defenses | 综述 / 路线图 | 综述具身系统感知、规划、行动与交互的安全风险，范围大于自改系统；可作跨路线安全背景，摘要未提出递归改进机制。 |
| [2601.13518](https://arxiv.org/abs/2601.13518v3) | AgenticRed: Evolving Agentic Systems for Red-Teaming | 方法候选，待全文研读 | 以进化选择和代际知识迭代生成红队系统架构，而非只优化单次攻击文本；修改对象是可复用工作流，需全文核实继承及评价隔离。 |
| [2602.12430](https://arxiv.org/abs/2602.12430v4) | Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward | 综述 / 路线图 | 系统梳理技能架构、获取、部署与生命周期治理，可帮助组织Harness技能分支；综述本身不应计为新的自我改进实证系统。 |
| [2309.15817](https://arxiv.org/abs/2309.15817v2) | Identifying the Risks of LM Agents with an LM-Emulated Sandbox | 评测 / 理论候选 | 以语言模型模拟工具及风险评价来测试agent，主要服务一般工具使用可靠性；可作为评价基础设施，摘要未展示自身持续改进。 |
| [2608.12851](https://arxiv.org/abs/2608.12851v2) | Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents | 评测 / 理论候选 | 重置会话但保留技能库，分离不安全技能写入与后续调用传播，并检验双阶段防护；直接评估经验继承的效用和风险是否共同增长。 |
| [2609.00069](https://arxiv.org/abs/2609.00069v1) | Auditing Harness Tampering in Self-Improving Agents | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.02246](https://arxiv.org/abs/2609.02246v1) | LLM-as-a-Judge Is Not an Oracle: Why Self-Improving Agents Need Deterministic Guardrails | 方法候选，待全文研读 | 给出带状态编排器和确定性验收门槛的提示优化系统，并分析评价器及指标失真；需核实生产经验、独立测试与规则持久化。 |
| [2606.23075](https://arxiv.org/abs/2606.23075v1) | Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies | 评测 / 理论候选 | 按系统模块与演化生命周期分析攻击面，并用开源系统考察跨代持续与放大；直接涉及参数、记忆、工具和架构自改的可靠性。 |
| [2608.03509](https://arxiv.org/abs/2608.03509v2) | SkillJack: Persistent Skill Backdoors in Self-Evolving Agents | 评测 / 理论候选 | 研究污染经验转成长期技能后仍可影响新任务，区分原始记忆删除与技能残留；直接关联经验到能力的持久继承风险。 |
| [2608.25776](https://arxiv.org/abs/2608.25776v1) | EVOMAL: Self-Poisoning in Self-Evolving Coding Agents | 评测 / 理论候选 | 考察技能生成时复制污染代码并再次进入库的跨代传播，明确针对可继承技能闭环；应作为自改系统失效机制候选阅读。 |
| [2608.30429](https://arxiv.org/abs/2608.30429v1) | EvoSkill Injection: Red-Teaming Autonomous Skill Generation and Evolution in Self-Evolving Agents | 评测 / 理论候选 | 构建技能形成与后续激活的连续红队评估，关注恶意能力被保存和复用；与技能进化闭环直接相关，但不是正向能力提升证据。 |
| [2609.17817](https://arxiv.org/abs/2609.17817v1) | Reflections on Trusting Trust, Revisited: Contaminating Self-Modifying AI Coding Agents with Poisoned Benchmarks | 评测 / 理论候选 | 在DGM、SICA和Hyperagents上研究评价基准污染如何写入后续版本，并检验清理基准后的残留，直接涉及跨代自修改可信度。 |
| [2609.24130](https://arxiv.org/abs/2609.24130v1) | Self-Healing Harness for Runtime Oversight of Agent Self-Modification | 方法候选，待全文研读 | 外部runtime只允许修复当前失败且不过度损害保护案例的规则跨episode持久化，包含回放、前向试验与累积规则复检。 |
| [2604.16968](https://arxiv.org/abs/2604.16968v1) | On Safety Risks in Experience-Driven Self-Evolving Agents | 评测 / 理论候选 | 直接检验经验累积如何改变后续安全行为，涵盖良性经验导致执行偏置及拒绝经验引起过度拒绝，属于持久学习的失效评估。 |
| [2604.15774](https://arxiv.org/abs/2604.15774v2) | MemEvoBench: Benchmarking Safety Risks from Memory Misevolution in LLM Agents | 评测 / 理论候选 | 专门评估持续记忆更新的误演化，包含恶意注入、噪声工具反馈和多轮漂移；属于记忆自进化的长期可靠性基准。 |
| [2602.15654](https://arxiv.org/abs/2602.15654v2) | Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections | 评测 / 理论候选 | 研究不可信外部内容经正常记忆更新跨会话持久化的风险，观察继承与后续工具行为；是自演化机制的安全评估，非能力提升工作。 |
| [2602.09877](https://arxiv.org/abs/2602.09877v2) | The Devil Behind Moltbook: Anthropic Safety is Always Vanishing in Self-Evolving AI Societies | 使能方法 / 背景 | 提出封闭自演化与安全不变性的理论冲突，并结合多agent案例；属于动力学边界线索，摘要不足以判断定理假设与普适范围。 |
| [2603.25111](https://arxiv.org/abs/2603.25111v3) | SEVerA: Verified Synthesis of Self-Evolving Agents | 方法候选，待全文研读 | 同时合成带形式契约的agent程序并以梯度方法优化其中模型调用，包含结构与参数两种更新；需读证明假设、训练规模和闭环边界。 |
| [2603.28650](https://arxiv.org/abs/2603.28650v2) | Information-Theoretic Limits of Safety Verification for Self-Improving Systems | 使能方法 / 背景 | 以累计风险与可接受改动数研究安全门控上限，并讨论形式验证例外；属于条件性理论，摘要不足以把有限GPT-2试验外推任意RSI。 |
| [2604.24618](https://arxiv.org/abs/2604.24618v1) | Evaluating whether AI models would sabotage AI safety research | 评测 / 理论候选 | 评估作为AI研究agent的模型是否破坏安全研究，属于AI4AI执行可信度而非递归改进算法；需区分主动发生与预置破坏轨迹续写。 |
| [2511.20857](https://arxiv.org/abs/2511.20857v2) | Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory | 评测 / 理论候选 | 将连续任务流中的经验检索、整合与更新纳入统一评估，并提出ReMem行动—思考—记忆修订方法，兼具基准和持久学习线索。 |
| [2505.11942](https://arxiv.org/abs/2505.11942v3) | LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners | 评测 / 理论候选 | 以有技能依赖的跨任务序列检验知识累积与迁移，提供自动核验环境及经验复用对照；属于持续agent学习基准。 |
| [2502.14499](https://arxiv.org/abs/2502.14499v1) | MLGym: A New Framework and Benchmark for Advancing AI Research Agents | 评测 / 理论候选 | 为提出假设、训练模型和迭代实验的AI研究agent提供Gym环境与十三类任务，可支撑AI4AI训练评估，非自身递归演化实证。 |
| [2601.22964](https://arxiv.org/abs/2601.22964v1) | EvoClinician: A Self-Evolving Agent for Multi-Turn Medical Diagnosis via Test-Time Evolutionary Learning | 方法候选，待全文研读 | 诊断—评分—演化循环以过程贡献和资源效率反馈更新Actor提示及记忆，具有跨轮策略继承；应用领域不影响其机制相关性。 |
| [2608.20318](https://arxiv.org/abs/2608.20318v1) | AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2607.25886](https://arxiv.org/abs/2607.25886v1) | RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement | 评测 / 理论候选 | 固定训练与服务设施，让研究agent依据失败和checkpoint反馈修订数据策略，并记录后续退化；直接评估数据中心AI4AI研究。 |
| [2608.04003](https://arxiv.org/abs/2608.04003v1) | PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents | 评测 / 理论候选 | 以新会话序列和保留经验开关检验保存—检索—更新是否真正导致收益，并提供Hermes+干预；是长期产品学习机制的重要检验线索。 |
| [2606.04455](https://arxiv.org/abs/2606.04455v1) | The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development? | 评测 / 理论候选 | 让元agent在隔离环境里迭代开发agent程序，以独立测试集和防指标作弊措施评价；直接衡量AI改进AI系统的工程研究能力。 |
| [2608.31100](https://arxiv.org/abs/2608.31100v1) | S3Gym: Can LLMs Turn Self-Testing and Self-Judging into Self-Improvement? | 评测 / 理论候选 | 统一比较历史上下文、摘要记忆与参数训练三种经验吸收路径，并用独立任务评估负迁移；直接支撑两条RSI路线的机制对照。 |
| [2608.31111](https://arxiv.org/abs/2608.31111v1) | Aspire: Can Models Self-Evolve from Vague Goals? | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.04280](https://arxiv.org/abs/2609.04280v3) | EvoHarnessBench: Can Your Agents Keep Pace with an Evolving Harness? | 评测 / 理论候选 | 把工具、技能和专家agent的外部扩展作为环境非平稳性，检验既有能力保留与经验适应；须区别Harness被外部改变和自主修改。 |
| [2608.09096](https://arxiv.org/abs/2608.09096v2) | Evo-Bench: Can Language Models Improve Agent Harness? | 评测 / 理论候选 | 专门隔离底层模型强弱与Harness开发能力，设计敏感任务划分及跨套件泛化，评估长期工作流改进及跨policy迁移。 |
| [2605.17373](https://arxiv.org/abs/2605.17373v2) | FML-bench: A Controlled Study of AI Research Agent Strategies from the Perspective of Search Dynamics | 评测 / 理论候选 | 分离搜索策略与执行设施，比较十八项ML研究任务的过程指标，并测试停滞后扩大探索；可解释何时复杂自改搜索有优势。 |
| [2609.24663](https://arxiv.org/abs/2609.24663v1) | Beyond Endpoint Performance: Process-Level Evaluation of Self-Evolving Agents | 评测 / 理论候选 | 冻结底层模型工具，逐检查点评估记忆或技能的迁移、保留和规则适应，直接检验持续自改过程而非仅终点成绩。 |
| [2604.12290](https://arxiv.org/abs/2604.12290v2) | Frontier-Eng: Benchmarking Self-Evolving Agents on Real-World Engineering Tasks with Generative Optimization | 使能方法 / 背景 | 提供工业模拟器下的候选—执行—评分工程优化任务，可借鉴搜索过程与预算评估；摘要未证明改进agent自身或AI训练系统。 |
| [2604.02369](https://arxiv.org/abs/2604.02369v3) | Beyond Message Passing: A Semantic View of Agent Communication Protocols | 综述 / 路线图 | 比较十八种agent通信协议的传输、语法和语义层，提供互操作基础设施脉络；未提出自动改写协议或持续能力演化闭环。 |
| [2601.02371](https://arxiv.org/abs/2601.02371v2) | Permission Manifests for Web Agents | 当前图谱范围外 | 网站通过声明式manifest规定agent交互权限，解决一般网页自动化协调；没有经验学习、自改选择或AI研究训练闭环。 |
| [2507.21035](https://arxiv.org/abs/2507.21035v3) | GenoMAS: A Multi-Agent Framework for Scientific Discovery via Code-Driven Gene Expression Analysis | 当前图谱范围外 | 六个固定专长agent围绕基因表达任务规划、回退与修正分析代码；摘要未出现跨任务继承或研究器自修改，属于领域科学自动化。 |
| [2603.08127](https://arxiv.org/abs/2603.08127v2) | EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery | 方法候选，待全文研读 | Evolution Manager把研究与代码实验历史提炼为持续的选题及实验记忆，供后续研究者与工程agent复用；有明确研究策略继承。 |
| [2603.28986](https://arxiv.org/abs/2603.28986v1) | Mimosa Framework: Toward Evolving Multi-Agent Systems for Scientific Research | 方法候选，待全文研读 | 元编排器生成多agent拓扑、动态发现MCP工具，并依据实验与judge反馈修订工作流；直接关联科学研究Harness的结构搜索。 |
| [2504.09855](https://arxiv.org/abs/2504.09855v1) | PestMA: LLM-based Multi-Agent System for Informed Pest Management | 当前图谱范围外 | 编辑、检索、校验三个固定角色在当前农业任务中协作修正答案；摘要未出现可继承策略、参数或工作流更新，属于一般应用agent。 |
| [2505.23885](https://arxiv.org/abs/2505.23885v2) | OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation | 方法候选，待全文研读 | 对分层多agent系统中的通用规划器做真实反馈RL，并报告32B训练；工作流模块化是外部设计，摘要尚不支持其拓扑也自主进化。 |
| [2602.04411](https://arxiv.org/abs/2602.04411v1) | Self-evolving Embodied AI | 综述 / 路线图 | 提出记忆、任务、环境预测、具身适应和模型演化的统一概念并回顾组件工作；属具身自演化综述，不应当成单个闭环实证。 |
| [2604.07767](https://arxiv.org/abs/2604.07767v1) | Administrative Decentralization in Edge-Cloud Multi-Agent for Mobile Automation | 当前图谱范围外 | 边云划分高层设计与设备执行，并在当前任务内做战术规划和纠错；没有持久经验或跨任务自修改，属于执行架构优化。 |
| [2212.10560](https://arxiv.org/abs/2212.10560v2) | Self-Instruct: Aligning Language Models with Self-Generated Instructions | 使能方法 / 背景 | 自身生成指令与回答、过滤后微调原模型，是自合成数据自举的基础方法；摘要未说明反复更新生成器的多代循环，宜作为机制先例。 |
| [2210.11610](https://arxiv.org/abs/2210.11610v2) | Large Language Models Can Self-Improve | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2306.02707](https://arxiv.org/abs/2306.02707v1) | Orca: Progressive Learning from Complex Explanation Traces of GPT-4 | 使能方法 / 背景 | 用更强教师的解释轨迹训练学生，相关于AI生成训练信号，但没有学生持续改进自身训练过程的闭环；作为蒸馏背景而非直接RSI。 |
| [2310.00533](https://arxiv.org/abs/2310.00533v4) | SELF: Self-Evolution with Language Feedback | 方法候选，待全文研读 | 先学习自反馈与修订元技能，再用自身生成和改进的回答反复微调自己，具备数据—权重—新数据闭环；规模及外部监督待全文核实。 |
| [2407.12874](https://arxiv.org/abs/2407.12874v2) | SELF-GUIDE: Better Task-Specific Instruction Following via Self-Synthetic Finetuning | 方法候选，待全文研读 | 学生合成任务输入输出后用于微调自身，省去更强外部教师，明确涉及自生成监督驱动参数改善；循环轮次与泛化边界需正文确认。 |
| [2505.03059](https://arxiv.org/abs/2505.03059v1) | Improving Model Alignment Through Collective Intelligence of Open-Source LLMS | 方法候选，待全文研读 | 多模型协同生成对齐与偏好数据并用于自身微调，摘要明确报告不依赖更强教师的自提升；需全文确认代际更新及集体知识来源。 |
| [2503.02103](https://arxiv.org/abs/2503.02103v2) | Superficial Self-Improved Reasoners Benefit from Model Merging | 方法候选，待全文研读 | 针对自生成数据训练的分布外退化，迭代合并原始与自改模型参数以保留泛化；直接研究模型自改的稳定性而非单次指标提升。 |
| [2503.12303](https://arxiv.org/abs/2503.12303v6) | Will Pre-Training Ever End? A First Step Toward Next-Generation Foundation MLLMs via Self-Improving Systematic Cognition | 方法候选，待全文研读 | 最小外部监督启动多模态感知推理，再生成与筛选描述和推理数据用于预训练，形成自数据—训练循环；需核实规模与轮次。 |
| [2506.10055](https://arxiv.org/abs/2506.10055v2) | TaskCraft: Automated Generation of Agentic Tasks | 使能方法 / 背景 | 自动合成难度可扩展且可验证的多工具任务，用于提示优化和agent微调；提供训练与评估数据，不等于研究器自身循环改进。 |
| [2504.21561](https://arxiv.org/abs/2504.21561v5) | Iterative Tool Usage Exploration for Multimodal Agents via Step-wise Preference Tuning | 方法候选，待全文研读 | 任务合成、工具探索、步骤验证与偏好训练反复耦合，更新多模态控制器参数；工具本身是否演化及规模需要全文确认。 |
| [2505.22660](https://arxiv.org/abs/2505.22660v4) | Maximizing Confidence Alone Improves Reasoning | 方法候选，待全文研读 | 以模型自身答案置信度构造内在奖励，通过强化学习更新推理参数而不依赖标准答案；需全文检查奖励可靠性、迭代与跨题泛化。 |
| [2501.00747](https://arxiv.org/abs/2501.00747v1) | DIVE: Diversified Iterative Self-Improvement | 方法候选，待全文研读 | 在迭代自生成数据训练中扩展采样池并兼顾多样性与质量选择偏好对，针对自改后的探索塌缩，属模型路线稳定化方法。 |
| [2506.10943](https://arxiv.org/abs/2506.10943v2) | Self-Adapting Language Models | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2505.22453](https://arxiv.org/abs/2505.22453v2) | First SFT, Second RL, Third UPT: Continual Improving Multi-Modal LLM Reasoning via Unsupervised Post-Training | 方法候选，待全文研读 | 用多次采样多数答案作为GRPO自奖励，并进一步让模型合成新训练样本，具有数据与policy更新闭环；需检验奖励偏差和长期稳定性。 |
| [2503.00735](https://arxiv.org/abs/2503.00735v3) | LADDER: Self-Improving LLMs Through Recursive Problem Decomposition | 方法候选，待全文研读 | 递归生成更容易的问题变体作自主练习，并对测试题变体做推理期RL；涉及课程与参数自适应，需隔离测试适应和任务外泛化。 |
| [2411.04109](https://arxiv.org/abs/2411.04109v3) | Self-Consistency Preference Optimization | 方法候选，待全文研读 | 把自一致答案作为偏好目标并迭代训练，无须人工新标注，直接涉及自身输出产生训练信号；参数规模和泛化稳定性待正文。 |
| [2411.00412](https://arxiv.org/abs/2411.00412v4) | Adapting While Learning: Grounding LLMs for Scientific Problems with Intelligent Tool Usage Adaptation | 使能方法 / 背景 | 以工具解题数据训练知识，再按模型正确率分配直接推理或工具调用；是能力和工具选择的训练方法，未展示研究器自主升级。 |
| [2505.21493](https://arxiv.org/abs/2505.21493v1) | Reinforcing General Reasoning without Verifiers | 使能方法 / 背景 | 不用单独验证器而最大化参考答案概率，仍依赖外部参考答案；提供policy与隐式验证训练机制，不能误称无监督递归自奖励。 |
| [2603.15255](https://arxiv.org/abs/2603.15255v2) | SAGE: Multi-Agent Self-Evolution for LLM Reasoning | 方法候选，待全文研读 | 共享模型承担出题、规划、求解和批评角色，借助外部验证及课程质量筛选共同自训练；需核实各角色参数更新与外部反馈边界。 |
| [2606.01279](https://arxiv.org/abs/2606.01279v1) | ANDES: Agent Native Data Evolving Synthesis Tool for Autonomous Instruction Alignment | 方法候选，待全文研读 | 以自演化路由树和诊断报告让训练agent闭环控制数据合成，并用于后训练；需区分数据技能状态变化与被训练目标模型的参数变化。 |
| [2605.13803](https://arxiv.org/abs/2605.13803v1) | EvoGround: Self-Evolving Video Agents for Video Temporal Grounding | 方法候选，待全文研读 | 出题者从原始视频生成查询与区间，求解者反馈又训练出题者，二者通过RL反复共同进步；属于多角色模型参数协同而非必然Hybrid。 |
| [2212.08073](https://arxiv.org/abs/2212.08073v1) | Constitutional AI: Harmlessness from AI Feedback | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2312.10003](https://arxiv.org/abs/2312.10003v1) | ReST meets ReAct: Self-Improvement for Multi-Step Reasoning LLM Agent | 方法候选，待全文研读 | 将ReAct工具轨迹与ReST式增长批次训练结合，按AI反馈反复更新agent并自蒸馏；有明确多轮数据—参数改进闭环。 |
| [2502.11959](https://arxiv.org/abs/2502.11959v2) | STRIVE: Structured Reasoning for Self-Improvement in Claim Verification | 方法候选，待全文研读 | 通过结构化推理与证据核验筛选自身生成训练链，避免二元答案偶然正确造成错误自训练；具有可验证的自反馈数据闭环线索。 |
| [2504.02902](https://arxiv.org/abs/2504.02902v1) | Beyond Accuracy: The Role of Calibration in Self-Improving Large Language Models | 评测 / 理论候选 | 比较提示、推理提示和微调式自改中的过度自信，并测试逐轮校准；用于检验自评分反馈是否随迭代失真，而非只看准确率。 |
| [2506.02918](https://arxiv.org/abs/2506.02918v2) | World Modelling Improves Language Model Agents | 使能方法 / 背景 | 后训练中学习动作后状态预测，并在推理时自验证选样，属于规划与评价使能机制；摘要没有自身数据—权重的持续自改闭环。 |
| [2505.08827](https://arxiv.org/abs/2505.08827v2) | RLSR: Reinforcement Learning from Self Reward | 方法候选，待全文研读 | 结合自主出题、解题、自判断和RL形成无参考答案训练循环，直接相关自奖励模型路线；需验证judge可靠性和持续迭代上限。 |
| [2504.05812](https://arxiv.org/abs/2504.05812v3) | Right Question is Already Half the Answer: Fully Unsupervised LLM Reasoning Incentivization | 方法候选，待全文研读 | 以潜在语义空间中的预测熵作为无监督优化信号，持续更新推理policy，属于内生反馈自训练候选；需检查置信度与正确性的偏差。 |
| [2505.21444](https://arxiv.org/abs/2505.21444v2) | Can Large Reasoning Models Self-Train? | 方法候选，待全文研读 | 直接研究多数投票自反馈的多轮RL，报告推理和反馈质量互相改善，也出现长期伪奖励利用与性能崩溃，是自训练边界的重要线索。 |
| [2505.24726](https://arxiv.org/abs/2505.24726v1) | Reflect, Retry, Reward: Self-Improving LLMs via Reinforcement Learning | 方法候选，待全文研读 | 把重试成功反馈归因于此前自反思token并训练反思能力，改进的不仅是答案还包括修复策略；需核实跨任务训练与独立评估。 |
| [2502.02534](https://arxiv.org/abs/2502.02534v2) | Adaptive Self-improvement LLM Agentic System for ML Library Development | 方法候选，待全文研读 | 面向ML库和硬件专用语言构造自适应agent优化系统，符合AI4AI产物方向；摘要未交代持久改进对象与反馈继承，需全文定性。 |
| [2601.07180](https://arxiv.org/abs/2601.07180v1) | Structured Reasoning for Large Language Models | 使能方法 / 背景 | 将生成、验证与修订分解为可训练模块，按人工设定两阶段RL优化效率；支持自验证能力，却未显示自主改变学习流程的递归闭环。 |
| [2601.03193](https://arxiv.org/abs/2601.03193v2) | UniCorn: Towards Self-Improving Unified Multimodal Models through Self-Generated Supervision | 方法候选，待全文研读 | 单一统一多模态模型分担出题、生成和评分，靠自博弈监督改进生成并保持理解；需全文确认参数更新对象与循环一致性评价。 |
| [2606.14302](https://arxiv.org/abs/2606.14302v2) | Retrospective Progress-Aware Self-Refinement for LLM Agent Training | 方法候选，待全文研读 | 初始外部示范后由自身回顾完整轨迹形成进度奖励，结合环境反馈更新policy，无需持续教师标注；直接涉及自评估训练信号。 |
| [2605.22905](https://arxiv.org/abs/2605.22905v1) | EVE-Agent: Evidence-Verifiable Self-Evolving Agents | 方法候选，待全文研读 | 在出题—求解自训练中增加可审查原文证据，并按证据带来的边际正确率奖励课程；需核实实际训练对象，不能把架构不变理解为权重冻结。 |
| [2306.11706](https://arxiv.org/abs/2306.11706v2) | RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation | 使能方法 / 背景 | 机器人policy自采数据供后续训练并改善新任务适应，是自数据闭环的重要先例；对象为视觉动作模型，非当前LLM-Harness主线。 |
| [2505.16410](https://arxiv.org/abs/2505.16410v1) | Tool-Star: Empowering LLM-Brained Multi-Tool Reasoner via Reinforcement Learning | 方法候选，待全文研读 | 合成多工具轨迹后以self-critic与分层奖励做RL，更新工具使用推理模型；工具集合固定，是否反复自生数据需正文进一步区分。 |
| [2503.23145](https://arxiv.org/abs/2503.23145v2) | CodeARC: Benchmarking Reasoning Capabilities of LLM Agents for Inductive Program Synthesis | 使能方法 / 背景 | 通过隐藏函数查询与差分测试评价交互程序归纳，提供反馈和训练轨迹；主要优化外部程序，未展示agent自身跨任务演化。 |
| [2504.16078](https://arxiv.org/abs/2504.16078v1) | LLMs are Greedy Agents: Effects of RL Fine-tuning on Decision-Making Abilities | 使能方法 / 背景 | 通过自生成推理轨迹上的RL缓解贪心探索与知行差距，为改进研究策略提供训练机制；摘要未显示研究器或学习规则自主升级。 |
| [2506.11425](https://arxiv.org/abs/2506.11425v2) | Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards | 方法候选，待全文研读 | 在软件任务中先探索、接收验证与AI引导、再以引导轨迹做RLVR，报告72B参数更新；须进一步区分教师辅助学习与真正递归自改。 |
| [2411.02337](https://arxiv.org/abs/2411.02337v3) | WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2507.14172](https://arxiv.org/abs/2507.14172v2) | Self-Improving Language Models for Evolutionary Program Synthesis: A Case Study on ARC-AGI | 方法候选，待全文研读 | 程序进化搜索产生的尝试被转成训练对，再微调生成与修订模型以增强后续搜索，直接构成搜索—学习循环；外部搜索规则是否变动待核实。 |
| [2504.03160](https://arxiv.org/abs/2504.03160v4) | DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments | 使能方法 / 背景 | 在真实开放网页中端到端RL训练研究代理，强调多代理浏览与反思行为；普通环境反馈学习本身不足以证明改进机制或harness递归演化。 |
| [2505.01441](https://arxiv.org/abs/2505.01441v1) | Agentic Reasoning and Tool Integration for LLMs via Reinforcement Learning | 使能方法 / 背景 | 以终局奖励训练何时及怎样调用工具，增强多轮推理与环境交互；摘要未给出自动改进训练器、评价器或持久harness的机制，保留代理RL背景。 |
| [2505.21496](https://arxiv.org/abs/2505.21496v1) | UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents | 方法候选，待全文研读 | 摘要明确GUI代理和奖励模型经奖励引导探索与结果验证共同改善，并报告三代数据—模型迭代；属于直接参数共进化候选，应优先核查。 |
| [2504.20073](https://arxiv.org/abs/2504.20073v2) | RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning | 使能方法 / 背景 | 研究多轮代理RL的Echo Trap、轨迹过滤及梯度稳定，提供可复用训练系统；其self-evolution主要指固定RL下策略学习，应与递归训练器改进区分。 |
| [2508.04700](https://arxiv.org/abs/2508.04700v2) | SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience | 方法候选，待全文研读 | 通过世界状态评价、自动课程和失败模仿/成功GRPO更新电脑代理，再把专长合并成通用模型；具备明确经验反馈与参数继承，需核查具体循环。 |
| [2601.02439](https://arxiv.org/abs/2601.02439v6) | WebGym: Scaling Training Environments for Visual Web Agents with Realistic Tasks | 使能方法 / 背景 | 构建近三十万真实网页训练任务并加速异步采样，利用交互奖励训练视觉代理；属于环境与代理RL使能，未声称训练器或反馈体系自行进化。 |
| [2606.07412](https://arxiv.org/abs/2606.07412v1) | Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2606.07367](https://arxiv.org/abs/2606.07367v1) | Self-evolving LLM agents with in-distribution Optimization | 方法候选，待全文研读 | 每轮从专家与自采样数据学习分布内critic，再把优势变成过程奖励并更新策略；评价与策略共同演化且明确迭代，需全文核查稳定性与外部锚点。 |
| [2607.22529](https://arxiv.org/abs/2607.22529v1) | Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.04094](https://arxiv.org/abs/2609.04094v1) | DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training | 方法候选，待全文研读 | 训练时动态生成适应策略能力的rubrics，并把轨迹评价分配到相关步骤；可改变反馈机制，需确认rubrics是否跨轮继承及如何校准无真值判断。 |
| [2608.19880](https://arxiv.org/abs/2608.19880v1) | EnvHarness: Awakening Static Worlds for Agent Learning | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.39306](https://arxiv.org/abs/2609.39306v1) | ReSAIL: Mitigating Collapse in Iterative Agent Self-Distillation | 方法候选，待全文研读 | 直接研究部署后多轮自蒸馏坍塌，选择特权信息敏感步骤并保持下一轮教师能力，报告三个循环；与递归参数改善的稳定性高度相关。 |
| [2610.11384](https://arxiv.org/abs/2610.11384v1) | Environmental Feedback Modeling Matters: Rethinking Feedback Treatment in Agentic Hindsight Self-Distillation | 方法候选，待全文研读 | 环境响应预测与事后自蒸馏共同训练，摘要明确两种能力相互增强；需全文确认检查点刷新、循环次数及教师角色，不能只按小模型规模排除。 |
| [2305.10626](https://arxiv.org/abs/2305.10626v3) | Language Models Meet World Models: Embodied Experiences Enhance Language Models | 使能方法 / 背景 | 在固定物理模拟器收集规划与随机探索经验，以EWC和LoRA微调语言模型；说明具身经验如何内化，摘要没有反复改善自身改进机制。 |
| [2405.14205](https://arxiv.org/abs/2405.14205v4) | Agent Planning with World Knowledge Model | 使能方法 / 背景 | 从专家及自身轨迹合成知识，训练世界知识模型辅助规划；涉及经验提炼，但摘要没有明确多轮更新世界模型与策略的闭环。 |
| [2410.13232](https://arxiv.org/abs/2410.13232v2) | Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation | 使能方法 / 背景 | 训练网页状态差异预测器，在推理时模拟动作后果以改善固定代理规划；摘要强调无需训练策略，未展示跨任务继承的自改进循环。 |
| [2411.14499](https://arxiv.org/abs/2411.14499v4) | Understanding World or Predicting Future? A Comprehensive Survey of World Models | 综述 / 路线图 | 综述理解当前世界与预测未来两类世界模型及多个应用领域；可补环境建模背景，但不应把综述覆盖的所有世界模型方法计作RSI工作。 |
| [2506.01622](https://arxiv.org/abs/2506.01622v5) | General agents contain world models | 使能方法 / 背景 | 形式化分析多步目标泛化所必需的预测世界模型，并讨论从策略提取模型；可用于理解代理表征与能力边界，但不是RSI实施或递归增益实证。 |
| [2504.21024](https://arxiv.org/abs/2504.21024v2) | WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2507.04370](https://arxiv.org/abs/2507.04370v1) | WebSynthesis: World-Model-Guided MCTS for Efficient WebUI-Trajectory Synthesis | 方法候选，待全文研读 | 学习网页世界模型，利用可回退MCTS合成轨迹后训练网页策略；与经验再生成相关，需核实是否多轮刷新双方模型，还是一次模型辅助数据合成。 |
| [2501.10116](https://arxiv.org/abs/2501.10116v1) | GAWM: Global-Aware World Model for Multi-Agent Reinforcement Learning | 当前图谱范围外 | 以集中世界模型改善一般多agent强化学习的状态表示与仿真数据，实验为SMAC；未涉及LLM、AI研究器或改进自身算法的闭环。 |
| [2511.09515](https://arxiv.org/abs/2511.09515v1) | WMPO: World Model-based Policy Optimization for Vision-Language-Action Models | 使能方法 / 背景 | 在像素世界模型内对VLA执行在线GRPO，研究样本效率与持续学习；与参数自训练机制相邻，摘要未显示学习器自身改进或世界模型共同进化。 |
| [2510.15047](https://arxiv.org/abs/2510.15047v2) | Why Do LLM Agents Fail in Exploring New Environments? A World-Modeling Perspective | 使能方法 / 背景 | 诊断新环境RL探索坍塌，以自身交互的状态和转移预测SFT再启动RL；解释自训练失败条件，但摘要方法是固定两阶段配方而非多代RSI。 |
| [2601.00930](https://arxiv.org/abs/2601.00930v1) | AlignUSER: Human-Aligned LLM Agents via World Models for Recommender System Evaluation | 使能方法 / 背景 | 以人类交互学习世界模型，再从反事实轨迹提取经验以拟合用户行为；是推荐系统评价的用户模拟器，摘要未显示改进器持续自我更新。 |
| [2606.30639](https://arxiv.org/abs/2606.30639v2) | Self-Evolving World Models for LLM Agent Planning | 方法候选，待全文研读 | 冻结代理及全部权重，依据真实转移与预测误差持续更新情景记忆和规则，并过滤不可靠前瞻；是明确的部署期世界模型上下文自改进。 |
| [2506.23468](https://arxiv.org/abs/2506.23468v2) | NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments | 方法候选，待全文研读 | 以环境动力学模型和Contextual Evolution Memory支持导航中在线适应，可能涉及外部状态或参数学习；两者边界须正文确认。 |
| [2510.01183](https://arxiv.org/abs/2510.01183v1) | EvoWorld: Evolving Panoramic World Generation with Explicit 3D Memory | 当前图谱范围外 | 通过显式三维记忆保证全景视频长期生成的一致性，演化的是场景重建；摘要没有代理改进策略、模型训练闭环或可复用harness自优化机制。 |
| [2602.11075](https://arxiv.org/abs/2602.11075v2) | RISE: Self-Improving Robot Policy with Compositional World Model | 使能方法 / 背景 | 以组合世界模型生成想象轨迹并连续更新机器人策略；提供模型化经验训练机制，但摘要未显示世界模型随策略共同更新，亦非LLM自身改进证据。 |
| [2407.00247](https://arxiv.org/abs/2407.00247v1) | Prompt Refinement with Image Pivot for Text-to-Image Generation | 当前图谱范围外 | 借图像潜表示把用户描述翻译成文生图系统偏好的关键词提示；属于提示转换模型，未展示反馈驱动的提示搜索或对自身系统的持续改进。 |
| [2409.15199](https://arxiv.org/abs/2409.15199v1) | Learning from Contrastive Prompts: Automated Optimization and Adaptation | 方法候选，待全文研读 | 分析好坏提示的对比模式来生成并迁移提示，覆盖模型版本和语言变化；属于提示层自动适配，需全文核查反馈如何进入迭代与历史继承。 |
| [2402.08702](https://arxiv.org/abs/2402.08702v4) | PRompt Optimization in Multi-Step Tasks (PROMST): Integrating Human Feedback and Heuristic-based Sampling | 方法候选，待全文研读 | 围绕多步代理任务以人定反馈规则修改提示，并学习候选表现预测器提高搜索效率；提示与启发式评价的反馈关系值得核查，尚不等于无监督RSI。 |
| [2501.01329](https://arxiv.org/abs/2501.01329v1) | The Prompt Alchemist: Automated LLM-Tailored Prompt Optimization for Test Case Generation | 使能方法 / 背景 | 目标是面向测试生成自动寻找模型专属提示，但该摘要只展开现有方法缺陷，未交代自身更新算法；应阅读全文核实闭环，不能据标题认定RSI。 |
| [2510.15260](https://arxiv.org/abs/2510.15260v1) | DRO-InstructZero: Distributionally Robust Prompt Optimization for Large Language Models | 使能方法 / 背景 | 以分布鲁棒贝叶斯优化选择在分布偏移下稳定的提示；是自动提示优化的稳健性方法，摘要没有优化器本身演化或长期代理经验继承。 |
| [2606.04465](https://arxiv.org/abs/2606.04465v1) | SePO: Self-Evolving Prompt Agent for System Prompt Optimization | 方法候选，待全文研读 | 同一提示代理同时修改任务提示和自身提示，保留候选档案并进行多任务元训练与目标适配；明确针对优化器自身，是高相关自指harness候选。 |
| [2606.18902](https://arxiv.org/abs/2606.18902v2) | SAGE: Stochastic Prompt Optimization via Agent-Guided Exploration | 方法候选，待全文研读 | 将提示优化视为随机黑箱搜索，结合多代理诊断与代码执行，并报告线上八轮A/B反馈优化；有明确部署循环，需审查指标与迁移范围。 |
| [2302.02676](https://arxiv.org/abs/2302.02676v8) | Chain of Hindsight Aligns Language Models with Feedback | 使能方法 / 背景 | 将多个生成结果及正负反馈串成训练上下文，通过微调学习纠错；为经验内化提供方法，但摘要未表明反复生成新监督或改进自身训练机制。 |
| [2405.03845](https://arxiv.org/abs/2405.03845v1) | Self-Improving Customer Review Response Generation Based on LLMs | 方法候选，待全文研读 | RAG客服系统利用LLM评判与自优化提示改善回复，并给出人工复核；可归应用型harness优化，需核查跨任务继承和持续循环而非单次改写。 |
| [2405.17346](https://arxiv.org/abs/2405.17346v1) | Prompt Optimization with Human Feedback | 使能方法 / 背景 | 以人类成对偏好而非数值分数进行dueling-bandit提示优化，可支持反馈稀缺的harness调整；学习信号来自用户，摘要未展示自身改进器更新。 |
| [2406.11695](https://arxiv.org/abs/2406.11695v2) | Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs | 方法候选，待全文研读 | MIPRO联合优化多阶段LM程序的指令与示例，并随优化过程调整提案生成方式；既涉及系统组件又涉及元提案，需全文分清实际采用与消融方案。 |
| [2410.02748](https://arxiv.org/abs/2410.02748v3) | CriSPO: Multi-Aspect Critique-Suggestion-guided Automatic Prompt Optimization for Text Generation | 方法候选，待全文研读 | 自动发现评价维度并以多方面批评建议迭代修改生成任务提示，另做多指标后缀优化；属于外部提示反馈搜索，需核查评价器是否随循环变化。 |
| [2412.19684](https://arxiv.org/abs/2412.19684v2) | Boosting Private Domain Understanding of Efficient MLLMs: A Tuning-free, Adaptive, Universal Prompt Optimization Framework | 方法候选，待全文研读 | 先通过强化搜索建立提示策略树，再以反思搜索适配私有领域，冻结模型参数；包含策略先验与提示更新，需核查是否为可持续元优化循环。 |
| [2605.16233](https://arxiv.org/abs/2605.16233v1) | FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast | 方法候选，待全文研读 | 冻结权重，把失败轨迹提炼为规则或例子，并跨代理种群传播最佳记忆；明确存在持久记忆继承和反馈选择，且报告广播机制的消融。 |
| [2309.08532](https://arxiv.org/abs/2309.08532v3) | EvoPrompt: Connecting LLMs with Evolutionary Algorithms Yields Powerful Prompt Optimizers | 方法候选，待全文研读 | 以LLM实现离散提示的进化变异，按开发集表现迭代筛选提示种群，冻结模型参数；可归harness提示进化，需区分固定搜索器与自指优化。 |
| [2304.12244](https://arxiv.org/abs/2304.12244v3) | WizardLM: Empowering large pre-trained language models to follow complex instructions | 使能方法 / 背景 | Evol-Instruct逐步复杂化指令后混合数据微调模型，提供AI合成训练数据的基础方法；演化对象首先是数据，摘要未表明目标模型反馈驱动多代循环。 |
| [2506.00178](https://arxiv.org/abs/2506.00178v2) | Tournament of Prompts: Evolving LLM Instructions Through Structured Debates and Elo Ratings | 方法候选，待全文研读 | 用辩论评价与Elo选择驱动提示种群交叉、变异，保留搜索多样性；无需真值不等于反馈可靠，应核查评判者固定角色和持久提示收益。 |
| [2510.18257](https://arxiv.org/abs/2510.18257v1) | DelvePO: Direction-Guided Self-Evolving Framework for Flexible Prompt Optimization | 方法候选，待全文研读 | 拆分提示组件并利用工作记忆总结历史搜索，指导下一代提示生成；属于提示与搜索经验积累，需核实记忆更新及跨任务迁移，而非仅看self-evolving名称。 |
| [2510.21148](https://arxiv.org/abs/2510.21148v1) | How to Auto-optimize Prompts for Domain Tasks? Adaptive Prompting and Reasoning through Evolutionary Domain Knowledge Adaptation | 方法候选，待全文研读 | 从专家初始语义因果图出发，以真值文本反馈共同修订图与推理机制；属于知识及提示层的反馈优化，摘要不足以确认模型权重也在更新。 |
| [2305.03495](https://arxiv.org/abs/2305.03495v2) | Automatic Prompt Optimization with "Gradient Descent" and Beam Search | 使能方法 / 背景 | 用小批量错误生成文本批评，再结合束搜索与bandit改写提示，是文本梯度优化的早期方法；可解释后续harness路线，但未展示优化器自身演化。 |
| [2412.03624](https://arxiv.org/abs/2412.03624v1) | How to Correctly do Semantic Backpropagation on Language-based Agentic Systems | 使能方法 / 背景 | 形式化语义梯度及多节点反馈分配，为代理计算图自动优化提供方法；可以解释harness改进的信用分配，但摘要未说明优化器自身递归更新。 |
| [2406.16218](https://arxiv.org/abs/2406.16218v2) | Trace is the Next AutoDiff: Generative Optimization with Rich Feedback, Execution Traces, and LLMs | 方法候选，待全文研读 | 把执行轨迹与丰富反馈组成优化oracle，以LLM迭代更新提示、代码及一般工作流；直接关联harness自动优化，需区分改进外部程序与自身优化器。 |
| [2505.18524](https://arxiv.org/abs/2505.18524v2) | metaTextGrad: Automatically optimizing language model optimizers | 方法候选，待全文研读 | 明确优化现有LLM优化器本身，联合元提示和元结构优化以适配任务；比只优化被调用模型提示更接近递归改进，应核查元层反馈与泛化。 |
| [2506.00400](https://arxiv.org/abs/2506.00400v4) | Scaling Textual Gradients via Sampling-Based Momentum | 使能方法 / 背景 | 通过历史高质量提示的动量采样提高文本梯度优化稳定性，能接入TextGrad等框架；提供harness搜索使能算法，摘要未证明优化器自行演化。 |
| [2605.23904](https://arxiv.org/abs/2605.23904v2) | SkillOpt: Executive Strategy for Self-Evolving Agent Skills | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2606.05395](https://arxiv.org/abs/2606.05395v1) | VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents | 方法候选，待全文研读 | 冻结基础模型，把形式验证反例转成文本梯度更新可复用机器人技能契约；改进对象是持续使用的技能接口，区别于只验证单次计划。 |
| [2604.20714](https://arxiv.org/abs/2604.20714v1) | Learning to Evolve: A Self-Improving Framework for Multi-Agent Systems via Textual Parameter Graph Optimization | 方法候选，待全文研读 | 把多代理系统表示为可编辑文本参数图，再从历史优化成功与失败学习改进提案；直接涉及优化器能力积累，是否更新权重须由全文确认。 |
| [2604.00830](https://arxiv.org/abs/2604.00830v4) | Meta-TTL: Meta-Learning Self-Improvement Policies for Language Agents | 方法候选，待全文研读 | 以双层优化学习测试时自改进策略：内层代理跨回合纠错，外层按下游提升元训练；明确优化改进机制而非只优化答案，值得优先补读。 |
| [2305.00833](https://arxiv.org/abs/2305.00833v2) | Learning to Reason and Memorize with Self-Notes | 使能方法 / 背景 | 让模型在读取输入时插入自己的笔记以辅助后续推理和记忆；主要是单次上下文内计算，摘要未给跨任务技能继承或反馈驱动系统修改。 |
| [2402.09727](https://arxiv.org/abs/2402.09727v3) | A Human-Inspired Reading Agent with Gist Memory of Very Long Contexts | 使能方法 / 背景 | 通过分段摘要、gist记忆及回看原文扩大有效上下文，是固定阅读流程；记忆主要表征当前文档，摘要未给跨任务经验学习或自改进算法。 |
| [2401.07339](https://arxiv.org/abs/2401.07339v2) | CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges | 使能方法 / 背景 | 构建仓库级代码生成基准并用固定工具与四种代理策略改善生成；可作编码代理基础设施参照，但摘要没有跨任务保留改进或系统自行演化。 |
| [2402.04624](https://arxiv.org/abs/2402.04624v2) | MEMORYLLM: Towards Self-Updatable Large Language Models | 使能方法 / 背景 | 在Transformer潜空间设置可持续更新的定长记忆，验证大量知识注入后的保留；需区别可变记忆状态与模型权重训练，未见优化改进规则的循环。 |
| [2409.07429](https://arxiv.org/abs/2409.07429v1) | Agent Workflow Memory | 方法候选，待全文研读 | 从以往任务轨迹诱导可复用工作流，并在线为之后任务提供策略；明确跨任务经验继承和新网站迁移，是技能及流程记忆路线的重要候选。 |
| [2509.25140](https://arxiv.org/abs/2509.25140v2) | ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2508.09736](https://arxiv.org/abs/2508.09736v4) | Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory | 使能方法 / 背景 | 通过视频音频构建情景及语义记忆，并以RL训练多轮检索推理；是多模态记忆与策略训练，摘要未展示二者持续共同改善自身学习机制。 |
| [2509.22315](https://arxiv.org/abs/2509.22315v3) | PRIME: Planning and Retrieval-Integrated Memory for Enhanced Reasoning | 使能方法 / 背景 | 按不确定性切换快速回答与多代理规划、检索流程；摘要描述固定推理架构，没有通过跨任务反馈更新记忆策略或修改系统，属代理架构背景。 |
| [2509.24704](https://arxiv.org/abs/2509.24704v2) | MemGen: Weaving Generative Latent Memory for Self-Evolving Agents | 方法候选，待全文研读 | 记忆触发器监控推理状态，weaver生成潜在记忆token参与后续推理；与内生记忆学习相关，但摘要未明确参数更新及跨任务持久继承的完整循环。 |
| [2502.00592](https://arxiv.org/abs/2502.00592v2) | M+: Extending MemoryLLM with Scalable Long-Term Memory | 使能方法 / 背景 | 扩展潜空间记忆并共同训练检索器，改善长期知识保留；训练检索器与维护记忆不等于递归改善系统，摘要未给部署反馈或多代循环。 |
| [2604.12231](https://arxiv.org/abs/2604.12231v1) | Thought-Retriever: Don't Just Retrieve Raw Data, Retrieve Thoughts for Memory-Augmented Agentic Systems | 方法候选，待全文研读 | 把解决过去查询的中间思考筛选、去冗余并组织为长期记忆，后续检索复用，报告查询增加后的提升；属于上下文经验进化候选。 |
| [2606.02215](https://arxiv.org/abs/2606.02215v2) | Better with Experience: Self-Evolving LLM Agents for Evidence-Grounded Health Community Notes | 方法候选，待全文研读 | 把健康纠错轨迹反馈分配到分析、取证和写作动作，形成持续演化的经验记忆；跨案例学习明确，需核查评判校准、泄漏与独立效果评价。 |
| [2606.24177](https://arxiv.org/abs/2606.24177v1) | Agon: An Autonomous Large-Scale Omnidisciplinary Research System Built on Prompt Economy | 使能方法 / 背景 | 部署研究编排器运行444轮Prompt Economy并分析失败；摘要未说明循环更新的是科研产物还是自身研究系统，应保留AI科研使能并补读边界。 |
| [2207.07115](https://arxiv.org/abs/2207.07115v2) | XMem: Long-Term Video Object Segmentation with an Atkinson-Shiffrin Memory Model | 当前图谱范围外 | 为长视频物体分割设计感官、工作及长期特征记忆与巩固规则；虽可借鉴记忆架构，但研究不涉及LLM代理或AI系统自我改进闭环。 |
| [2307.16449](https://arxiv.org/abs/2307.16449v4) | MovieChat: From Dense Token to Sparse Memory for Long Video Understanding | 当前图谱范围外 | 利用稀疏记忆处理长视频及时间关联，是视频理解架构和基准；摘要没有训练反馈闭环、代理经验演化或修改自身AI系统的机制。 |
| [2312.03003](https://arxiv.org/abs/2312.03003v3) | Explore, Select, Derive, and Recall: Augmenting LLM with Human-like Memory for Mobile Task Automation | 方法候选，待全文研读 | 将手机任务分解为可重用、重排及适配的子任务，形成app记忆以改善后续执行；具备经验持久化，需核查失败反馈与技能修订而非仅缓存。 |
| [2304.13343](https://arxiv.org/abs/2304.13343v4) | SCM: Enhancing Large Language Model with Self-Controlled Memory Framework | 使能方法 / 背景 | 由记忆控制器更新和检索长期文本记忆以处理长会话、书籍及会议；当前摘要侧重上下文保持，没有反馈驱动能力或改进器进化实验。 |
| [2507.22925](https://arxiv.org/abs/2507.22925v1) | Hierarchical Memory for High-Efficiency Long-Term Reasoning in LLM Agents | 使能方法 / 背景 | 按语义抽象层级组织和更新记忆，用位置索引逐层检索降低开销；摘要主要验证长期会话问答，没有明确能力反馈驱动的自改进规则。 |
| [2505.09081](https://arxiv.org/abs/2505.09081v2) | SALM: A Multi-Agent Framework for Language Model-Driven Social Network Simulation | 当前图谱范围外 | 以分层提示与注意力记忆稳定多代理社会网络模拟，评价人格和行为保真度；没有根据任务反馈改进模型或代理harness的机制，属于其他应用。 |
| [2504.19413](https://arxiv.org/abs/2504.19413v1) | Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | 使能方法 / 背景 | 持续抽取、合并并检索会话事实，提供图结构长期记忆与成本评测；知识累积不自动等于策略自改进，摘要未展示成功失败驱动记忆优化。 |
| [2506.07398](https://arxiv.org/abs/2506.07398v2) | G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems | 方法候选，待全文研读 | 以洞察、查询和交互三层图保留多代理协作经验，任务后持续吸收新轨迹并为后续任务定制检索；是明确的跨任务harness记忆演化。 |
| [2501.13956](https://arxiv.org/abs/2501.13956v1) | Zep: A Temporal Knowledge Graph Architecture for Agent Memory | 使能方法 / 背景 | 以时序知识图融合会话与业务数据并保留历史关系，改善长期检索与问答；是企业代理记忆基础设施，摘要未描述成败反馈驱动自身机制优化。 |
| [2509.21212](https://arxiv.org/abs/2509.21212v1) | SGMem: Sentence Graph Memory for Long-Term Conversational Agents | 使能方法 / 背景 | 把会话表示为多粒度句子图，结合原对话及摘要事实检索，提高长期问答；是记忆组织方法，未说明根据任务成败持续修订行为策略。 |
| [2503.19878](https://arxiv.org/abs/2503.19878v3) | CausalRAG: Integrating Causal Graphs into Retrieval-Augmented Generation | 使能方法 / 背景 | 以因果图组织检索并保持上下文连续，属于知识组织与RAG设计；摘要没有依据执行反馈修订图或持久改进代理，宜作为知识库路线背景。 |
| [2504.06135](https://arxiv.org/abs/2504.06135v1) | Decentralizing AI Memory: SHIMI, a Semantic Hierarchical Memory Index for Scalable Agent Reasoning | 使能方法 / 背景 | 用分层语义索引和去中心化同步支持代理记忆共享，核心是检索与一致性基础设施；动态知识结构本身尚不能证明系统具备反馈学习闭环。 |
| [2505.23422](https://arxiv.org/abs/2505.23422v1) | From Knowledge to Noise: CTIM-Rover and the Pitfalls of Episodic Memory in Software Engineering Agents | 评测 / 理论候选 | 将通用及仓库级跨任务记忆加入编码代理，所有配置均未超越基线，分析检索噪声导致退化；这是经验累积失效的有用证据，负结果不等于低质量。 |
| [2503.08026](https://arxiv.org/abs/2503.08026v2) | In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents | 方法候选，待全文研读 | 同时做多粒度经验摘要及基于引用证据的在线RL检索改进，反馈会改变检索行为；需全文确认更新的是选择统计、提示还是参数，再确定路线。 |
| [2605.13941](https://arxiv.org/abs/2605.13941v1) | EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents | 方法候选，待全文研读 | 让LLM诊断失败日志并修改自身记忆检索配置，带退化回滚及停滞探索，且可发现新配置维度；是直接架构自优化候选，应优先阅读全文核实。 |
| [2605.12061](https://arxiv.org/abs/2605.12061v2) | SAGE: A Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory | 方法候选，待全文研读 | 记忆读者将检索反馈交回写者，经过两轮改进图记忆；需全文核实图基础模型是否也更新，以及反馈如何影响跨任务持久结构。 |
| [2604.19795](https://arxiv.org/abs/2604.19795v1) | Prism: An Evolutionary Memory Substrate for Multi-Agent Open-Ended Discovery | 方法候选，待全文研读 | 提出分层记忆、因果图、信息价值检索与停滞控制，并声称自演化策略选择；机制和理论较多，需全文核实实际更新对象、证明假设及匹配消融。 |
| [2605.22721](https://arxiv.org/abs/2605.22721v1) | Self-Evolving Multi-Agent Systems via Decentralized Memory | 方法候选，待全文研读 | 每个代理维护经验利用池与候选探索池，按阶段性评判在线调权；存在去中心化记忆反馈与继承，理论遗憾保证的假设须全文审查。 |
| [2605.17721](https://arxiv.org/abs/2605.17721v1) | EXG: Self-Evolving Agents with Experience Graphs | 方法候选，待全文研读 | 将成功与失败组织为可在线增长的经验图，支持即时跨任务复用和离线迁移；明确修改持久经验结构，需核查图更新、筛选与独立终测。 |
| [2603.15421](https://arxiv.org/abs/2603.15421v2) | CLAG: Adaptive Memory Organization via Agent-Driven Clustering for Small Language Model Agents | 方法候选，待全文研读 | 代理主动聚类记忆并生成簇画像，在局部邻域演化知识以减少干扰；有持久组织更新，但摘要未清楚交代效果反馈，需核查是否仅是索引维护。 |
| [2509.09498](https://arxiv.org/abs/2509.09498v4) | SEDM: Selective Self-Evolving Distributed Memory for Agents | 方法候选，待全文研读 | 发送者以配对执行选择共享经验，接收者学习有无记忆的收益差并按成本门控；外部记忆信用与共享形成改进，模型训练边界待核。 |
| [2503.21760](https://arxiv.org/abs/2503.21760v2) | MemInsight: Autonomous Memory Augmentation for LLM Agents | 使能方法 / 背景 | 对历史交互做自主语义增强以改善记忆检索，能支持代理经验积累；摘要没有基于后续成败重新优化增强机制的闭环证据。 |
| [2502.12110](https://arxiv.org/abs/2502.12110v11) | A-MEM: Agentic Memory for LLM Agents | 方法候选，待全文研读 | 新经验能修改旧记忆表示与连接，形成持续维护的知识网络；应核查这种记忆演化是否改变后续策略及是否有任务效果驱动反馈。 |
| [2501.09136](https://arxiv.org/abs/2501.09136v4) | Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG | 综述 / 路线图 | 综述Agentic RAG的控制结构、记忆与检索编排，可用于相关术语和系统边界；并非RSI直接成果，也不证明所述RAG系统持续自改进。 |
| [2506.06326](https://arxiv.org/abs/2506.06326v1) | Memory OS of AI Agent | 使能方法 / 背景 | 分层存储和固定FIFO、分页规则支持长期记忆管理，是harness基础；内容动态更新不等于记忆规则自我优化，摘要未给闭环证据。 |
| [2507.20215](https://arxiv.org/abs/2507.20215v1) | MLC-Agent: Cognitive Model based on Memory-Learning Collaboration in LLM Empowered Agent Simulation Environment | 当前图谱范围外 | 目标是人工社会仿真中的个体建模，记忆共享改善模拟决策；不是研究LLM代理如何优化自身能力、训练过程或运行系统。 |
| [2601.21557](https://arxiv.org/abs/2601.21557v2) | Meta Context Engineering via Agentic Skill Evolution | 方法候选，待全文研读 | 元层通过技能执行历史与评价做交叉搜索，底层按技能改上下文文件和代码；同时演化改进方法与产物，是需优先补读的直接候选。 |
| [2607.28048](https://arxiv.org/abs/2607.28048v4) | SKILL-KD: Contrastive Skill Distillation for LLM Agents | 方法候选，待全文研读 | 比较学生失败与教师轨迹生成技能补丁，重跑固定学生验证并持续合并防漂移；明确是外部技能改善，不能把蒸馏名称当成权重训练。 |
| [2605.08374](https://arxiv.org/abs/2605.08374v4) | MemQ: Integrating Q-Learning into Self-Evolving Memory Agents over Provenance DAGs | 方法候选，待全文研读 | 通过记忆来源DAG反向传播任务信用，学习记忆价值并影响后续检索和新记忆；属于外部经验资产的持续改进，须核实价值近似假设。 |
| [2606.09483](https://arxiv.org/abs/2606.09483v1) | Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents | 方法候选，待全文研读 | 同步记录信念修订，异步从长期记忆归纳意图与跨域schema；存在持久知识结构演化，尚需核查其是否依据下游失败调整记忆加工机制。 |
| [2604.21725](https://arxiv.org/abs/2604.21725v2) | AEL: Evolving Agent Harness in Open-Ended Environments | 方法候选，待全文研读 | 快层bandit选择检索策略，慢层LLM诊断退化并新增策略，优化对象是使用经验的规则而非只增记忆；应核查跨流任务和无害性条件。 |
| [2606.24151](https://arxiv.org/abs/2606.24151v1) | Metis: Bridging Text and Code Memory for Self-Evolving Agents | 方法候选，待全文研读 | 固定经验集合比较文本与代码记忆，再将重复计划固化为验证过的工具；持久经验选择及能力扩展直接相关，需读成本和迁移控制。 |
| [2604.10923](https://arxiv.org/abs/2604.10923v1) | Mem$^2$Evolve: Towards Self-Evolving Agents via Co-Evolutionary Capability Expansion and Experience Distillation | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.15457](https://arxiv.org/abs/2609.15457v1) | AnchorGUI: Asymmetric Memory for Dual-Scale Learning in GUI Navigation | 方法候选，待全文研读 | 预测误差定位GUI失败并跨尝试蒸馏经验，超出单轮纠错；摘要未交代蒸馏更新外部记忆还是模型权重，路线需据方法核实。 |
| [2403.00839](https://arxiv.org/abs/2403.00839v1) | ToolNet: Connecting Large Language Models with Massive Tools via Tool Graph | 当前图谱范围外 | 用有向工具图约束调用顺序以扩展可用工具规模；摘要没有在线重写工具图、跨任务经验学习或模型自我训练机制。 |
| [2506.12508](https://arxiv.org/abs/2506.12508v6) | AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool-Environment-Agent(TEA) Protocol | 方法候选，待全文研读 | TEA将工具、环境和代理作为可版本化资源，并声称持续演化提示及组件代码；需读全文确认哪些修改由系统提出、验证并跨任务保留。 |
| [2508.00271](https://arxiv.org/abs/2508.00271v2) | MetaAgent: Toward Self-Evolving Agent via Tool Meta-Learning | 方法候选，待全文研读 | 固定权重下从工具使用经验反思验证，积累自建工具和持久知识库，并影响后续任务；直接对应外部能力和经验的自改进路线。 |
| [2510.24663](https://arxiv.org/abs/2510.24663v1) | OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs | 使能方法 / 背景 | 以DAG生成可控复杂度工具轨迹并构造图奖励，支持后训练和评测；摘要没有生成器随学习者反馈演化或系统自修改的证据。 |
| [2507.21836](https://arxiv.org/abs/2507.21836v1) | AutoTIR: Autonomous Tools Integrated Reasoning via Reinforcement Learning | 当前图谱范围外 | 使用人工定义的正确性和工具惩罚奖励训练调用策略，属于一般工具增强RL；摘要不含自生成课程、训练器演化或系统继任机制。 |
| [2510.24284](https://arxiv.org/abs/2510.24284v3) | MCP-Flow: Facilitating LLM Agents to Master Real-World, Diverse and Scaling MCP Tools | 使能方法 / 背景 | web代理自动发现MCP服务、合成调用数据并训练模型，是AI4AI数据管线；摘要没有新模型反馈再改变发现与合成策略的循环。 |
| [2510.05592](https://arxiv.org/abs/2510.05592v2) | In-the-Flow Agentic System Optimization for Effective Planning and Tool Use | 使能方法 / 背景 | 在实时多轮环境中用终局奖励训练planner，解决长程信用分配；摘要未表明编排结构或训练方法自我修改，演化记忆是否持久须核查。 |
| [2507.00487](https://arxiv.org/abs/2507.00487v2) | MassTool: A Multi-Task Search-Based Tool Retrieval Framework for Large Language Models | 当前图谱范围外 | 联合训练工具检测与检索网络，主要改进查询和工具匹配；摘要没有AI依据自身执行经验改进系统或生成下一轮训练过程的机制。 |
| [2506.01056](https://arxiv.org/abs/2506.01056v4) | MCP-Zero: Active Tool Discovery for Autonomous LLM Agents | 使能方法 / 背景 | 模型按能力缺口主动发现并组合工具，是动态harness扩展的相关基础；摘要未证明工具链跨任务继承或系统从反馈持续改进。 |
| [2503.01940](https://arxiv.org/abs/2503.01940v2) | AskToAct: Enhancing LLMs Tool Use via Self-Correcting Clarification | 使能方法 / 背景 | 自动构造缺失参数查询与纠错样本训练工具澄清能力，可作数据合成基础；摘要中的自纠错是交互行为，未建立持续自训闭环。 |
| [2507.21428](https://arxiv.org/abs/2507.21428v1) | MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Calling in LLM Agent Multi-Turn Conversations | 使能方法 / 背景 | 研究连续对话中工具上下文的加入移除，提供运行时记忆管理比较；主要是短期容量控制，未证明持久能力增长或管理策略自改进。 |
| [2406.03807](https://arxiv.org/abs/2406.03807v4) | Tool-Planner: Task Planning with Clusters across Multiple Tools | 当前图谱范围外 | 按功能聚类工具并在调用失败时重新规划，属于单任务工具编排与错误恢复；摘要没有经验持久化、自主修改系统或递归训练证据。 |
| [2511.01854](https://arxiv.org/abs/2511.01854v2) | Tool-to-Agent Retrieval: Bridging Tools and Agents for Scalable LLM Multi-Agent Systems | 当前图谱范围外 | 利用工具与父代理的元数据关系改善检索，属于路由表示方法；摘要不涉及自身经验驱动的能力更新、训练迭代或harness演化。 |
| [2410.03439](https://arxiv.org/abs/2410.03439v3) | ToolGen: Unified Tool Retrieval and Calling via Generation | 当前图谱范围外 | 以专用token将工具知识写入模型参数，统一调用与检索；属于工具学习表征，摘要未描述自生成反馈驱动的多轮改进或研发循环。 |
| [2504.01400](https://arxiv.org/abs/2504.01400v3) | ToolACE-R: Model-aware Iterative Training and Adaptive Refinement for Tool Learning | 方法候选，待全文研读 | 训练样本随模型能力迭代调整，并训练工具调用自修正；模型感知课程与后续参数更新相关，测试时自修正则须同持久学习分开。 |
| [2510.21618](https://arxiv.org/abs/2510.21618v3) | DeepAgent: A General Reasoning Agent with Scalable Toolsets | 使能方法 / 背景 | ToolPO训练通用工具策略，记忆折叠维持长任务上下文；需区分普通agent后训练与自我改进，摘要尚未给出跨轮系统继承机制。 |
| [2511.05271](https://arxiv.org/abs/2511.05271v4) | DeepEyesV2: Toward Agentic Multimodal Model | 当前图谱范围外 | 采用人工设计的冷启动和RL两阶段训练多模态工具使用，报告自适应调用；摘要未说明课程、反馈器或训练过程随模型自主进化。 |
| [2604.17091](https://arxiv.org/abs/2604.17091v1) | GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0) | 方法候选，待全文研读 | 将已验证历史轨迹沉淀为SOP和可执行代码，结合分层记忆供后续任务使用；明确涉及跨episode经验保存及外部能力增长。 |
| [2507.02004](https://arxiv.org/abs/2507.02004v1) | STELLA: Self-Evolving LLM Agent for Biomedical Research | 方法候选，待全文研读 | 通过经验演化推理模板库，并自主发现整合生物工具，报告随试验积累改进；应补读持久策略、工具更新和数据隔离以核实闭环。 |
| [2504.07079](https://arxiv.org/abs/2504.07079v1) | SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2507.07998](https://arxiv.org/abs/2507.07998v3) | PyVision: Agentic Vision with Dynamic Tooling | 使能方法 / 背景 | 视觉代理可按任务生成、执行并修复Python工具，支持动态能力构造；摘要未说明这些工具跨任务保留或持续改进生成工具的机制。 |
| [2410.08197](https://arxiv.org/abs/2410.08197v2) | From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions | 方法候选，待全文研读 | 通过探索工具、分析调用反馈、重写说明书三阶段迭代改进外部接口知识，并声称跨模型迁移；是文档型harness自改进的重要早期候选。 |
| [2412.14841](https://arxiv.org/abs/2412.14841v2) | Helping LLMs Improve Code Generation Using Feedback from Testing and Static Analysis | 当前图谱范围外 | 测试与静态分析反馈用于修复当前生成的C代码，改进的是任务产物；摘要没有保存代理策略、更新模型或改写自身系统的机制。 |
| [2605.27366](https://arxiv.org/abs/2605.27366v2) | MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation | 方法候选，待全文研读 | 技能跨任务存储、检索，按单技能经验评价与修订，并测试迁移到另一代理；这是持久技能生命周期演化，需核查覆盖子集报告口径。 |
| [2605.25430](https://arxiv.org/abs/2605.25430v2) | CODESKILL: Learning Self-Evolving Skills for Coding Agents | 方法候选，待全文研读 | 用冻结下游代理的执行成败训练LLM技能管理策略，并演化持久技能库；涉及改进器权重与外部知识，须区分管理模型和任务模型角色。 |
| [2604.10846](https://arxiv.org/abs/2604.10846v1) | PFAgent: A Tractable and Self-Evolving Power-Flow Agent for Interactive Grid Analysis | 方法候选，待全文研读 | 电网分析代理结合验证反馈和人工反馈声称自演化，但摘要也可能只描述当前任务调试；需核查是否真正保留组件变化而非仅修代码。 |
| [2305.17126](https://arxiv.org/abs/2305.17126v2) | Large Language Models as Tool Makers | 方法候选，待全文研读 | 工具制造者生成可复用功能，工具使用者在后续请求中调用缓存，构成持久外部能力扩展；需区分初次工具构造与递归改进制造者。 |
| [2402.07456](https://arxiv.org/abs/2402.07456v2) | OS-Copilot: Towards Generalist Computer Agents with Self-Improvement | 方法候选，待全文研读 | FRIDAY通过前任务积累技能、少量监督学习操作新软件，具有持久能力增长线索；需全文核实自训练是否只发生在外部工具与技能。 |
| [2505.20286](https://arxiv.org/abs/2505.20286v1) | Alita: Generalist Agent Enabling Scalable Agentic Reasoning with Minimal Predefinition and Maximal Self-Evolution | 方法候选，待全文研读 | 从开源资源自主构造、修订和复用任务MCP能力，明确以外部工具扩展代理；需全文验证能力库继承、评测隔离及搜索成本。 |
| [2510.23601](https://arxiv.org/abs/2510.23601v1) | Alita-G: Self-Evolving Generative Agent for Agent Generation | 方法候选，待全文研读 | 从目标领域成功轨迹生成、抽象并整理可复用MCP原语，部署检索调用；是持久能力迁移候选，需核实是否持续更新而非一次编译。 |
| [2502.11705](https://arxiv.org/abs/2502.11705v2) | LLM Agents Making Agent Tools | 使能方法 / 背景 | 从论文代码构造可调用工具并闭环调试，支持代理能力扩展；摘要主要验证单次工具实现正确性，尚未建立跨任务自进化流程。 |
| [2503.10071](https://arxiv.org/abs/2503.10071v1) | Advanced Tool Learning and Selection System (ATLASS): A Closed-Loop Framework Using LLM | 方法候选，待全文研读 | 按需求生成并调试工具，存入工具库供后续请求复用，另含环境配置与文档获取；存在持久能力增长，须核查验证与人工参与范围。 |
| [2509.05941](https://arxiv.org/abs/2509.05941v4) | Code2MCP: Transforming Code Repositories into MCP Services | 使能方法 / 背景 | 自动分析仓库、安装依赖并生成MCP服务，闭环调试保证可用性；为能力扩展提供工具生成基础，未显示自身管理流程被递归优化。 |
| [2312.17294](https://arxiv.org/abs/2312.17294v3) | Enhancing Open-Domain Task-Solving Capability of LLMs via Autonomous Tool Integration from GitHub | 方法候选，待全文研读 | 自主从GitHub整合专用工具，并从人类及自身经验学习处理工具缺陷；有能力扩展与经验反馈线索，需核实长期保留及优化对象。 |
| [2606.03841](https://arxiv.org/abs/2606.03841v1) | EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2604.15082](https://arxiv.org/abs/2604.15082v1) | Autonomous Evolution of EDA Tools: Multi-Agent Self-Evolved ABC | 使能方法 / 背景 | LLM团队在编译、正确性与QoR反馈下演化ABC综合工具，能参考程序进化机制；优化对象是EDA软件，非代理自身或AI训练系统。 |
| [2604.01687](https://arxiv.org/abs/2604.01687v3) | CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification | 方法候选，待全文研读 | 技能生成器与代理验证器共同迭代，面向复杂多文件技能包且不见真值测试；应优先核查验证器更新对象及二者共偏差控制。 |
| [2406.18532](https://arxiv.org/abs/2406.18532v1) | Symbolic Learning Enables Self-Evolving Agents | 方法候选，待全文研读 | 将提示、工具及组合结构视作符号参数，以语言形式反馈优化整个代理网络；属于自动harness设计，需核查部署后保留更新的实证。 |
| [2601.04620](https://arxiv.org/abs/2601.04620v1) | AgentDevel: Reframing Self-Evolving LLM Agents as Release Engineering | 方法候选，待全文研读 | 将代理版本作为发布产物，轨迹批评驱动诊断和候选修改，按修复与回退门控晋升；直接研究可审计的持续harness改进。 |
| [2601.07477](https://arxiv.org/abs/2601.07477v2) | JudgeFlow: Agentic Workflow Optimization via Block Judge | 方法候选，待全文研读 | 执行轨迹按逻辑块分配故障责任，再由LLM优化器改最有问题的工作流块；有明确评价—修改—更新循环，应补读局部信用分配机制。 |
| [2601.01126](https://arxiv.org/abs/2601.01126v2) | RoboPhD: Self-Improving Text-to-SQL Through Autonomous Agent Evolution | 方法候选，待全文研读 | 独立演化代理依据SQL效果改分析脚本与指令，经ELO选择和交叉继承18轮；直接对应代理代码与提示的外部自改进。 |
| [2605.22794](https://arxiv.org/abs/2605.22794v2) | MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems | 方法候选，待全文研读 | 生产失败驱动源码修改，试验容器回放验证后经用户同意晋升或回滚；直接harness演化，摘要中自主运行和发布审批需分别核实。 |
| [2608.05144](https://arxiv.org/abs/2608.05144v2) | Argus: A General-Purpose Agentic Reasoning Runtime for Long-Horizon Tasks | 方法候选，待全文研读 | 固定模型下让审核通过的记忆、技能、验证器及路由成为持久运行状态，支持多轮任务改进；需区分启动波与成熟波任务难度和成本。 |
| [2606.15874](https://arxiv.org/abs/2606.15874v2) | LLM-as-Code: Agentic Programming for Agent Harness | 使能方法 / 背景 | 提出程序掌管控制流、LLM作为受控调用组件的架构，可作为harness设计对照；摘要未描述代理自动改写该程序或跨轮改进过程。 |
| [2608.08311](https://arxiv.org/abs/2608.08311v3) | Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution | 方法候选，待全文研读 | 经审查的核心代码提交成为后续runtime，既可自调度演化也从普通任务吸收改动；需分开冻结benchmark快照与长期运行谱系。 |
| [2607.13285](https://arxiv.org/abs/2607.13285v1) | Harness Handbook: Making Evolving Agent Harnesses Readable,Navigable, and Editable | 使能方法 / 背景 | 自动建立harness行为到源码的映射，并引导修改位置定位；直接支撑自主harness修改，但自身不是持续改进循环，应作为工程基础。 |
| [2608.23552](https://arxiv.org/abs/2608.23552v1) | Prime Agent: A Self-Improving RLM Harness | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.01437](https://arxiv.org/abs/2609.01437v1) | HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness? | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2609.05903](https://arxiv.org/abs/2609.05903v2) | EvoSafeHarness: Evolving Model- and Domain-Specific Harnesses for Securing Agents | 方法候选，待全文研读 | 固定模型下根据行为反馈共同演化自然语言规则与可执行安全逻辑，另用新上下文对抗审查防基准依赖；直接安全harness演化。 |
| [2609.37968](https://arxiv.org/abs/2609.37968v2) | SelfSearch: Reward-Free Search for Self-Improving Agents | 方法候选，待全文研读 | 利用先前自修改过程记录继续改自身指令、工具与执行程序，搜索阶段不依赖下游奖励；直接研究改进经验继承，应优先查验证隔离。 |
| [2609.35530](https://arxiv.org/abs/2609.35530v1) | AutoRef: Harness Optimization for Agentic Multi-Reference Image Generation | 方法候选，待全文研读 | 冻结生成与推理模型，由编码agent迭代重写图像生成harness；分开提案反馈与候选选择，另报告跨模型和任务迁移，直接相关。 |
| [2601.11100](https://arxiv.org/abs/2601.11100v3) | ReCreate: Reasoning and Creating Domain Agents Driven by Experience | 方法候选，待全文研读 | 优化器代理检索执行证据，将成功失败原因变成提示、工具、流程和记忆修改，并归纳领域级版本；是明确的harness演化候选。 |
| [2605.29790](https://arxiv.org/abs/2605.29790v2) | Evolve as a Team: Collaborative Self-Evolution for LLM-based Multi-Agent Systems | 方法候选，待全文研读 | 利用各agent执行轨迹和事后通信，将分布式失败证据变成可复用行为、协调与组织改进；需全文确认持久产物和独立测试。 |
| [2306.06070](https://arxiv.org/abs/2306.06070v3) | Mind2Web: Towards a Generalist Agent for the Web | 当前图谱范围外 | 真实网站任务数据集及HTML过滤基线，评测一般网页操作与域外迁移；摘要没有自生成反馈、持续系统更新或递归改进研究。 |
| [2410.06992](https://arxiv.org/abs/2410.06992v2) | SWE-Bench+: Enhanced Coding Benchmark for LLMs | 评测 / 理论候选 | 审查代码基准中的答案泄漏和弱测试，并展示成功率重估；直接影响基于同类基准声称自改进的可信度，但不是RSI机制本身。 |
| [2406.04151](https://arxiv.org/abs/2406.04151v1) | AgentGym: Evolving Large Language Model-based Agents across Diverse Environments | 方法候选，待全文研读 | 提供多环境探索和轨迹基础，AgentEvol研究超出已有任务数据的代理自演化并发布checkpoint；需核查具体自生成数据与参数更新回路。 |
| [2508.18993](https://arxiv.org/abs/2508.18993v2) | GitTaskBench: A Benchmark for Code Agents Solving Real-World Tasks Through Code Repository Leveraging | 使能方法 / 背景 | 评测代理整合真实仓库、部署依赖和完成任务的能力，并测成本；可支撑工具生成与研发代理工程能力衡量，本身不测递归自改进。 |
| [2412.13178](https://arxiv.org/abs/2412.13178v5) | SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents | 当前图谱范围外 | 提供具身任务危险性与安全规划基准，评测执行及拒绝行为；不涉及自演化系统或更新后的失效，属于一般代理安全评测范围。 |
| [2503.23804](https://arxiv.org/abs/2503.23804v3) | DrunkAgent: Stealthy Memory Corruption in LLM-Powered Recommender Agents | 评测 / 理论候选 | 攻击推荐agent的动态记忆写入，暴露经验继承的污染面；与harness记忆更新可靠性有关，不是正向自改进方法。 |
| [2601.08613](https://arxiv.org/abs/2601.08613v1) | Magnetization reversal mechanism of double-helix nanowires probed by dark-field magneto-optical Kerr effect | 当前图谱范围外 | 研究双螺旋纳米线磁化反转的实验与微磁模拟；主题与AI代理、训练或自身改进无关，是检索范围误入，不能据此评价研究质量。 |
| [2410.10934](https://arxiv.org/abs/2410.10934v2) | Agent-as-a-Judge: Evaluate Agents with Agents | 评测 / 理论候选 | 代理评审可检查代码和中间过程，提供自动AI开发任务的细粒度评价；直接支撑自改进反馈，仍需核实评审可靠性而非等同改进成果。 |
| [2311.18760](https://arxiv.org/abs/2311.18760v4) | TaskBench: Benchmarking Large Language Models for Task Automation | 使能方法 / 背景 | 评测任务分解、工具选择和参数预测，并自动生成测试指令；可作为代理组件测量基础，但不直接测量跨轮自改进能力。 |
| [2310.03128](https://arxiv.org/abs/2310.03128v6) | MetaTool Benchmark for Large Language Models: Deciding Whether to Use Tools and Which to Use | 当前图谱范围外 | 评测是否使用工具及选择何种工具，未测量系统更新、经验继承或改进能力；属于一般代理能力基准，不宜当作RSI研究成果。 |
| [2412.02883](https://arxiv.org/abs/2412.02883v1) | TDD-Bench Verified: Can LLMs Generate Tests for Issues Before They Get Resolved? | 使能方法 / 背景 | 研究修复前自动生成可区分失败与修复状态的测试，支撑代码演化的独立验证；本身主要评测测试生成，不是代理自身递归改进。 |
| [2511.13998](https://arxiv.org/abs/2511.13998v1) | LoCoBench-Agent: An Interactive Benchmark for LLM Agents in Long-Context Software Engineering | 当前图谱范围外 | 评测长上下文软件工程多轮交互、效率及恢复，主要比较固定代理能力；未测量迭代改进器或跨任务继承，不应计作RSI方法。 |
| [2406.12373](https://arxiv.org/abs/2406.12373v3) | WebCanvas: Benchmarking Web Agents in Online Environments | 当前图谱范围外 | 研究动态网页中的在线任务评价与数据维护，环境变化不等于代理自进化；摘要没有可保留的模型或harness更新回路。 |
| [2405.20859](https://arxiv.org/abs/2405.20859v1) | clembench-2024: A Challenging, Dynamic, Complementary, Multilingual Benchmark and Underlying Flexible Framework for LLMs as Multi-Action Agents | 使能方法 / 背景 | 通过可自动评分的对话自博弈评价推理和指令遵循，可提供训练反馈环境；闭环开发只作为展望，摘要没有实际模型或系统演化。 |
| [2406.06613](https://arxiv.org/abs/2406.06613v2) | GameBench: Evaluating Strategic Reasoning Abilities of LLM Agents | 评测 / 理论候选 | 九种游戏检验策略推理，并比较固定模型的CoT与规划支架；适合作外部能力评测，摘要没有跨任务自修改或训练继承。 |
| [2402.12348](https://arxiv.org/abs/2402.12348v2) | GTBench: Uncovering the Strategic Reasoning Limitations of LLMs via Game-Theoretic Evaluations | 当前图谱范围外 | 以十类博弈比较固定LLM的策略推理，自博弈用作评测而非学习；没有从博弈经验更新模型或自身系统的实证。 |
| [2504.01848](https://arxiv.org/abs/2504.01848v3) | PaperBench: Evaluating AI's Ability to Replicate AI Research | 评测 / 理论候选 | 要求代理复现20篇真实AI论文并执行实验，以作者协作rubric和评审器评价；直接测量自动AI研发能力，是RSI支撑评测候选。 |
| [2605.08678](https://arxiv.org/abs/2605.08678v3) | MLS-Bench: A Holistic and Rigorous Assessment of AI Systems on Building Better AI | 评测 / 理论候选 | 140项任务要求AI改进ML组件且证明跨设置与尺度泛化，直接针对AI4AI方法发现；是需优先补读的研究评测，不能仅凭摘要断言有效。 |
| [2610.10388](https://arxiv.org/abs/2610.10388v1) | RoboQuest: Generalist Physical Agents that Search, Inspect and Test | 当前图谱范围外 | 评测物理操作中探索隐藏信息、检查和试工具的能力，主要是单episode主动感知；没有自身模型、训练过程或持久运行系统改进。 |
| [2404.07972](https://arxiv.org/abs/2404.07972v2) | OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments | 评测 / 理论候选 | 提供真实操作系统、多应用任务与可执行评分，可测自进化后继的计算机能力；基准自身不是改进模型或harness的闭环。 |
| [2605.08083](https://arxiv.org/abs/2605.08083v2) | LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling | 方法候选，待全文研读 | 代理在预采样推理环境中搜索分支、探测、剪枝与停止控制程序，用细粒度轨迹反馈优化推理计算分配；直接属于自动harness算法设计。 |
| [2403.12014](https://arxiv.org/abs/2403.12014v2) | EnvGen: Generating and Adapting Environments via LLMs for Training Embodied Agents | 使能方法 / 背景 | 固定LLM按学习者表现持续改造训练环境并训练小RL策略，体现环境—策略课程反馈；需作为外部策略机制参考，不冒充LLM自身RSI。 |
| [2602.06366](https://arxiv.org/abs/2602.06366v1) | Towards Adaptive Environment Generation for Training Embodied Agents | 使能方法 / 背景 | 按照当前具身学习者的细粒度表现修改环境难度，存在课程反馈回路；摘要未明确LLM角色及参数更新对象，应先作机制参考。 |
| [2203.01302](https://arxiv.org/abs/2203.01302v3) | Evolving Curricula with Regret-Based Environment Design | 使能方法 / 背景 | 基于regret编辑环境，使课程跟随学习者能力边界；属于前LLM时代自动课程与协同学习背景，不能冒充当代LLM自改进结果。 |
| [2402.03479](https://arxiv.org/abs/2402.03479v4) | DRED: Zero-Shot Transfer in Reinforcement Learning via Data-Regularised Environment Design | 使能方法 / 背景 | 分析课程分布偏移并用生成模型正则化环境设计，提高RL零样本泛化；是自动课程背景，摘要没有LLM或自改写系统。 |
| [2605.09423](https://arxiv.org/abs/2605.09423v2) | SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning | 方法候选，待全文研读 | SimCoder按验证反馈积累可复用工具/skills，并依学习者表现生成3D课程；环境构造器与具身策略联合进步，需核验独立迁移。 |
| [2511.03773](https://arxiv.org/abs/2511.03773v2) | Scaling Agent Learning via Experience Synthesis | 方法候选，待全文研读 | 合成环境转移与奖励支持在线RL，并按当前策略自适应生成课程；模型改进明确，环境模型是否跨代更新及协同因果需全文确认。 |
| [2505.20347](https://arxiv.org/abs/2505.20347v2) | SeRL: Self-Play Reinforcement Learning for Large Language Models with Limited Data | 方法候选，待全文研读 | 每步自行生成过滤新指令，以多数投票估计反馈后做RL，迭代扩大训练数据；直接相关，但共识错误与奖励锚定需查全文。 |
| [2509.21543](https://arxiv.org/abs/2509.21543v4) | Self-CriTeach: LLM Self-Teaching and Self-Critiquing for Improving Robotic Planning via Automated Domain Generation | 方法候选，待全文研读 | LLM生成规划域，既产训练轨迹又作结构化奖励，再训练规划模型；应查域是否随模型反复修订，避免把一次生成误作协同递归。 |
| [2401.01335](https://arxiv.org/abs/2401.01335v3) | Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2407.10627](https://arxiv.org/abs/2407.10627v1) | Arena Learning: Build Data Flywheel for LLMs Post-training via Simulated Chatbot Arena | 方法候选，待全文研读 | 模拟模型竞技场产生比较反馈，按目标模型弱点持续改进训练数据并做SFT/RL，构成生成数据与模型迭代的闭环候选。 |
| [2502.05605](https://arxiv.org/abs/2502.05605v6) | Evolving LLMs' Self-Refinement Capability via Synergistic Training-Inference Optimization | 方法候选，待全文研读 | 训练模型的自修订能力，再用推理期修订产物供下一轮训练，形成训练—推理数据闭环；改进生成策略是否持久自修改需全文区分。 |
| [2502.05400](https://arxiv.org/abs/2502.05400v4) | Dynamic Noise Preference Optimization: Self-Improvement of Large Language Models with Self-Synthetic Data | 方法候选，待全文研读 | 用模型自生成数据迭代偏好优化，动态标签及可训练噪声缓解停滞；与模型自训练直接相关，规模本身不能裁定贡献质量。 |
| [2511.00091](https://arxiv.org/abs/2511.00091v1) | Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | 方法候选，待全文研读 | 残差RL寻找VLA失败区域，采集贴近部署的恢复轨迹再蒸馏回通用模型；明确AI生成监督，但是否多轮递归仍需正文证据。 |
| [2512.05145](https://arxiv.org/abs/2512.05145v1) | Self-Improving VLM Judges Without Human Annotations | 方法候选，待全文研读 | VLM裁判自行合成不同质量回答、推理和判断，筛选后迭代训练自身；直接涉及评价能力自训练，仍需查质量锚点和独立验证。 |
| [2508.09586](https://arxiv.org/abs/2508.09586v3) | EvoCurr: Self-evolving Curriculum with Behavior Code Generation for Complex Decision-making | 方法候选，待全文研读 | 冻结LLM，Designer按已验收进度和失败生成课程，Solver产生可执行策略，门控保留已掌握行为；需分清策略训练与LLM权重。 |
| [2604.17739](https://arxiv.org/abs/2604.17739v2) | Democratizing Tool Learning with Environments Fully Simulated by a Free 8B Language Model | 方法候选，待全文研读 | 用语言模型模拟任务、用户、工具和评价，按学生能力调整课程训练工具agent；需全文区分固定模拟器与持续可继承环境改进。 |
| [2602.20532](https://arxiv.org/abs/2602.20532v1) | Actor-Curator: Co-adaptive Curriculum Learning via Policy-Improvement Bandits for RL Post-Training | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2511.19900](https://arxiv.org/abs/2511.19900v2) | Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning | 方法候选，待全文研读 | 同一视觉语言模型兼任求解与验证，工具证据形成自反馈，再经RL联合改善两种角色；属于模型内多角色共学习候选。 |
| [2605.16299](https://arxiv.org/abs/2605.16299v2) | ACE: Self-Evolving LLM Coding Framework via Adversarial Unit Test Generation and Preference Optimization | 方法候选，待全文研读 | 同一模型轮流写代码与对抗测试，执行结果驱动代码SFT和测试KTO；属于求解—造错能力共学习，须区分运行鲁棒性和语义正确性。 |
| [2602.11524](https://arxiv.org/abs/2602.11524v1) | Adaptive Milestone Reward for GUI Agents | 方法候选，待全文研读 | 从成功探索中动态提炼可验证milestones，反过来为GUI策略RL提供分步奖励；评价结构随学习更新，须核验长期继承与独立效应。 |
| [2510.14253](https://arxiv.org/abs/2510.14253v2) | Towards Agentic Self-Learning LLMs in Search Environment | 方法候选，待全文研读 | 任务生成、执行策略与生成式奖励模型同环境闭环共训练，并报告冻结奖励模型导致停滞；直接涉及自学习反馈源随策略演化。 |
| [2606.29871](https://arxiv.org/abs/2606.29871v3) | AI Training Manager: Bounded Closed-Loop Control of Adaptive Training Recipes | 方法候选，待全文研读 | LLM管理器读取训练遥测并通过受限动作修改正在运行的训练配方；模型与训练控制耦合，管理器自身是否进化须与目标模型改进分开。 |
| [2606.03239](https://arxiv.org/abs/2606.03239v1) | ARBOR: Online Process Rewards via a Reusable Rubric Buffer for Search Agents | 方法候选，待全文研读 | 从对比轨迹生成并维护跨query奖励rubric缓冲，随策略变化合并退休规则，同时训练搜索模型；直接涉及评价harness和模型耦合。 |
| [2606.21262](https://arxiv.org/abs/2606.21262v2) | ARCO: Adaptive Rubrics with Co-Evolution for Multi-Step LLM-Based Agents | 方法候选，待全文研读 | 持续用on-policy轨迹训练逐步rubric生成和评分模型，使评价能力跟随执行agent；明确模型共学习，外部规则库持久修改尚未披露。 |
| [2602.02709](https://arxiv.org/abs/2602.02709v3) | ATLAS: A Multi-LLM Training Framework for EvoDPO with Adaptive Reference Evolution | 方法候选，待全文研读 | 元agent协作训练active agent，按训练遥测及proxy-KL门控更新DPO参考策略；需核清被训练模型、控制器与可继承配方的关系。 |
| [2601.21464](https://arxiv.org/abs/2601.21464v2) | Conversation for Non-verifiable Learning: Self-Evolving LLMs through Meta-Evaluation | 方法候选，待全文研读 | 共享策略的多个角色生成、批评、修订，以批评能否帮助改进获得诊断奖励，共同训练生成和判断能力；无外部真值时锚定需复核。 |
| [2604.26687](https://arxiv.org/abs/2604.26687v1) | COPUS: Co-adaptive Parallelism and Batch Size Selection in Large Language Model Training | 使能方法 / 背景 | 以Goodput联合调batch和并行配置，优化LLM预训练收敛时间；是自适应基础设施，不因“co-adaptive”名称即构成RSI。 |
| [2603.17775](https://arxiv.org/abs/2603.17775v2) | CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2511.19399](https://arxiv.org/abs/2511.19399v3) | DR Tulu: Reinforcement Learning with Evolving Rubrics for Deep Research | 方法候选，待全文研读 | 训练中把新搜索信息与对比回答写入持续演化rubrics，为策略提供更新反馈；模型与外部评价规则共同变化，值得查明门控和迁移。 |
| [2510.08522](https://arxiv.org/abs/2510.08522v1) | DYNAMIX: RL-based Adaptive Batch Size Optimization in Distributed Machine Learning Systems | 使能方法 / 背景 | PPO按资源、网络与统计效率动态选batch size，属于训练系统控制优化；摘要没有显示控制器改进自己的算法或研究能力。 |
| [2510.05943](https://arxiv.org/abs/2510.05943v1) | EARL: Efficient Agentic Reinforcement Learning Systems for Large Language Models | 使能方法 / 背景 | 动态选择训练并行方式并分发长上下文中间数据，解决agentic RL吞吐和显存问题；是训练基础设施，摘要未显示自治改进器。 |
| [2601.06794](https://arxiv.org/abs/2601.06794v2) | No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning | 方法候选，待全文研读 | 策略与critic用双路GRPO同步训练，critic以诱发后续改进的能力获奖；属于多模型反馈共演化，并不必然包含外部harness修改。 |
| [2605.03871](https://arxiv.org/abs/2605.03871v1) | EvoLM: Self-Evolving Language Models through Co-Evolved Discriminative Rubrics | 方法候选，待全文研读 | 同一模型交替训练rubric生成和策略，用早晚checkpoint输出构造偏好并由冻结小裁判评分；明确反馈共学习，时间偏好假设待复核。 |
| [2604.14010](https://arxiv.org/abs/2604.14010v1) | Parameter Importance is Not Static: Evolving Parameter Isolation for Supervised Fine-Tuning | 使能方法 / 背景 | 根据梯度动态更新参数隔离mask以减少多任务遗忘，属于训练算法；摘要没有自生成监督、研究器修改或可继承agent经验闭环。 |
| [2605.29847](https://arxiv.org/abs/2605.29847v2) | EvoRubric: Self-Evolving Rubric-Driven RL for Open-Ended Generation | 方法候选，待全文研读 | 共享模型训练回答与rubric生成，结合历史rubric持久池及冻结Meta-Verifier/Grader；权重和外部评价记忆共同变化，需核验闭环。 |
| [2606.23038](https://arxiv.org/abs/2606.23038v1) | EvoRubrics: Dynamic Rubrics as Rewards via Adversarial Co-Evolution for LLM Reinforcement Learning | 方法候选，待全文研读 | 策略模型与Rubric Generator逐步对抗共训练，让评价随能力提升保持区分力；相关性明确，完全自监督变体的真值锚定需复核。 |
| [2605.15224](https://arxiv.org/abs/2605.15224v1) | ICRL: Learning to Internalize Self-Critique with Reinforcement Learning | 方法候选，待全文研读 | 共享骨干solver/critic联合训练，将批评后的成功转成无批评时能力，critic按后续增益获奖；直接研究反馈能力与求解能力共同进化。 |
| [2511.23002](https://arxiv.org/abs/2511.23002v2) | JarvisEvo: Towards a Self-Evolving Photo Editing Agent with Synergistic Editor-Evaluator Optimization | 方法候选，待全文研读 | 图像编辑器与评价器通过SEPO协同优化，结合工具执行和多模态反思；权重共学习明确，固定Lightroom工具不应自动算harness进化。 |
| [2601.13060](https://arxiv.org/abs/2601.13060v1) | MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux | 方法候选，待全文研读 | 多agent奖励系统评估GUI轨迹、纠错并自动回流训练数据以增强agent；机制相关，摘要对权重更新、代数与奖励系统自身学习披露不足。 |
| [2506.06292](https://arxiv.org/abs/2506.06292v2) | Mutual-Taught for Co-adapting Policy and Reward Models | 方法候选，待全文研读 | 交替用当前奖励模型更新策略，再用更新前后输出训练奖励模型，形成类EM共适应循环；需核验时间对比标签是否持续可靠。 |
| [2108.03645](https://arxiv.org/abs/2108.03645v1) | Online Evolutionary Batch Size Orchestration for Scheduling Deep Learning Workloads in GPU Clusters | 使能方法 / 背景 | 进化搜索在线安排训练作业batch与GPU资源，优化集群完成时间；是训练系统调度背景，没有模型或调度器自身递归改进证据。 |
| [2605.04431](https://arxiv.org/abs/2605.04431v1) | Towards Robust LLM Post-Training: Automatic Failure Management for Reinforcement Fine-Tuning | 评测 / 理论候选 | 提供RFT训练故障基准及检测—诊断—修复闭环，可评价自动训练控制可靠性；摘要未说明管理器自身进化，宜作评测及基础方法。 |
| [2511.01758](https://arxiv.org/abs/2511.01758v1) | RLAC: Reinforcement Learning with Adversarial Critic for Free-Form Generation Tasks | 方法候选，待全文研读 | critic动态找最可能失败项，经外部validator核验后联合优化生成器和critic；是评价能力与生成能力共同训练，需查验证预算对照。 |
| [2602.02488](https://arxiv.org/abs/2602.02488v1) | RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2603.00724](https://arxiv.org/abs/2603.00724v1) | RLAR: An Agentic Reward System for Multi-task Reinforcement Learning on Large Language Models | 方法候选，待全文研读 | 训练中agent检索奖励模型并合成验证代码，按数据分布动态编排反馈给策略；需检查验证工具是否跨轮继承而非仅每query临时选择。 |
| [2602.10885](https://arxiv.org/abs/2602.10885v1) | Reinforcing Chain-of-Thought Reasoning with Self-Evolving Rubrics | 方法候选，待全文研读 | 自主提出并演化rubrics为CoT提供RL监督，且可在推理时作为提示；需查外部规则继承、演化频率及无结果奖励时的可靠锚定。 |
| [2505.15034](https://arxiv.org/abs/2505.15034v2) | RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2501.04519](https://arxiv.org/abs/2501.04519v1) | rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2408.08586](https://arxiv.org/abs/2408.08586v1) | Rubick: Exploiting Job Reconfigurability for Deep Learning Cluster Scheduling | 使能方法 / 背景 | 按性能模型共同重配训练执行计划和多资源分配，提高GPU集群利用；是可重配置训练基础设施，不因协同优化即属于RSI成果。 |
| [2605.10899](https://arxiv.org/abs/2605.10899v2) | RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards | 方法候选，待全文研读 | 深研策略做分阶段RL，共享骨干的反思元策略把轨迹变成复用指导，分别通过权重和文本记忆继承；混合改进机制直接相关。 |
| [2605.30888](https://arxiv.org/abs/2605.30888v1) | The Flip Side of RLHF: On-Policy Feedback for Reward Model Self-Supervised Improvement | 方法候选，待全文研读 | 用价值头作prompt级锚点，从on-policy回答构建奖励模型对比训练信号；针对静态奖励失配，是否形成多轮稳定共同改进仍需正文。 |
| [2606.04507](https://arxiv.org/abs/2606.04507v1) | Self-Evolving Deep Research via Joint Generation and Evaluation | 方法候选，待全文研读 | 共享参数的研究solver/evaluator共同训练，meta-harness按solver表现调评价环境；是混合路线候选，需查环境可变范围及独立质量锚定。 |
| [2604.10674](https://arxiv.org/abs/2604.10674v1) | Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents | 方法候选，待全文研读 | 把自身轨迹压成仅训练期使用的技能，作为teacher上下文再蒸馏给plain-prompt学生；动态教师同步，但不等于部署技能库持续进化。 |
| [2604.07837](https://arxiv.org/abs/2604.07837v1) | SPARD: Self-Paced Curriculum for RL Alignment via Integrating Reward Dynamics and Data Utility | 使能方法 / 背景 | 按学习进度调整多目标奖励权重与数据重要性，属于自动课程和训练控制；仅自适应加权不足以证明自改进研究器。 |
| [2509.22558](https://arxiv.org/abs/2509.22558v2) | StepORLM: A Self-Evolving Framework With Generative Process Supervision For Operations Research Language Models | 方法候选，待全文研读 | 运筹策略与生成式过程奖励模型交替改进，结合外部求解器结果和过程反馈做W-DPO；有明确外部锚定的模型共演化候选。 |
| [2605.18851](https://arxiv.org/abs/2605.18851v1) | STRIDE: Learnable Stepwise Language Feedback for LLM Reasoning | 方法候选，待全文研读 | 仅用结果奖励共训练生成器与语言verifier，在推理中途按批评重定向轨迹；模型反馈共学习相关，宣称无害改进的条件需全文证明。 |
| [2504.20157](https://arxiv.org/abs/2504.20157v2) | Toward Evaluative Thinking: Meta Policy Optimization with Evolving Reward Models | 方法候选，待全文研读 | meta-reward模型随训练上下文持续改写reward模型提示，同时优化策略权重；具体外部提示与模型共同更新，符合混合路线候选。 |
| [2606.29502](https://arxiv.org/abs/2606.29502v2) | UCOB: Learning to Utilize and Evolve Agentic Skills via Credit-Aware On-Policy Bidirectional Self-Distillation | 方法候选，待全文研读 | 同模型有技能/无技能两种上下文按局部回报互教，同时更新技能记忆、检索与反思训练；直接把harness利用和模型内化共同优化。 |
| [2507.17515](https://arxiv.org/abs/2507.17515v1) | URPO: A Unified Reward & Policy Optimization Framework for Large Language Models | 方法候选，待全文研读 | 单模型同时扮演player与referee，在统一GRPO中利用标注偏好、可验证逻辑与自给奖励联合学习；属于生成—评价能力共同训练。 |
| [2604.07864](https://arxiv.org/abs/2604.07864v2) | ZeroCoder: Can LLMs Improve Code Generation Without Ground-Truth Supervision? | 方法候选，待全文研读 | Coder与Tester用代码—测试执行矩阵联合训练，并识别选择器漂移；完全无标签版本须与用10个标注校准的DyB4分开评价。 |
| [2502.13138](https://arxiv.org/abs/2502.13138v1) | AIDE: AI-Driven Exploration in the Space of Code | 使能方法 / 背景 | LLM在机器学习代码空间树搜索，继承高分解法并优化外部模型任务；是AI4AI工程研究器，但摘要未显示它修改自己的研究机制。 |
| [2605.05724](https://arxiv.org/abs/2605.05724v1) | Auto Research with Specialist Agents Develops Effective and Non-Trivial Training Recipes | 方法候选，待全文研读 | 专职agent据外部实验反馈连续修改训练配方代码并继承lineage；AI4AI闭环明确，但需核验配方改进是否反馈研究器自身而非仅外部任务。 |
| [2606.31551](https://arxiv.org/abs/2606.31551v1) | AutoTrainess: Teaching Language Models to Improve Language Models Autonomously | 使能方法 / 背景 | 将人类训练经验预先编码为接口、规则和工作流，帮助agent自动后训练模型；摘要验证设计好的harness，未证明harness自演化。 |
| [2410.14660](https://arxiv.org/abs/2410.14660v1) | A Large Language Model-Driven Reward Design Framework via Dynamic Feedback for Reinforcement Learning | 使能方法 / 背景 | 编码与评价agent迭代改奖励，轨迹偏好检查减少昂贵RL重训；面向非LLM控制策略，可作反馈设计和预算控制背景。 |
| [2604.01210](https://arxiv.org/abs/2604.01210v1) | CliffSearch: Structured Agentic Co-Evolution over Theory and Code for Scientific Algorithm Discovery | 使能方法 / 背景 | 对理论加代码的科学产物做agent化选择、变异和审稿门控，实例含优化器发现；摘要未显示发现器本身迭代改写，属AI4AI背景。 |
| [2406.08414](https://arxiv.org/abs/2406.08414v3) | Discovering Preference Optimization Algorithms with and for Large Language Models | 方法候选，待全文研读 | LLM据前轮训练评测生成并实现新偏好损失，发现DiscoPOP并测迁移；是LLM训练算法发现，需区分改进目标模型与修改发现器。 |
| [2606.03073](https://arxiv.org/abs/2606.03073v1) | Efficient Hyperparameter Optimization for LLM Reinforcement Learning | 使能方法 / 背景 | 联合使用小代理模型、训练预算、早停与checkpoint复用来加速LLM RL超参搜索；是效率方法，摘要无研究器或学习机制递归更新。 |
| [2310.12931](https://arxiv.org/abs/2310.12931v2) | Eureka: Human-Level Reward Design via Coding Large Language Models | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2603.01712](https://arxiv.org/abs/2603.01712v2) | FT-Dojo: Towards Autonomous LLM Fine-Tuning with Language Agents | 评测 / 理论候选 | 标准化13个LLM自动微调任务、沙箱、反馈与held-out评价，并给FT-Agent基线；直接可评估AI4AI训练能力，不等同RSI已实现。 |
| [2406.10540](https://arxiv.org/abs/2406.10540v1) | Generating and Evolving Reward Functions for Highway Driving with Large Language Models | 使能方法 / 背景 | LLM通过RL训练反馈和反思改高速驾驶奖励代码；改进对象是模拟驾驶策略和任务奖励，适合作自动奖励设计背景。 |
| [2503.21807](https://arxiv.org/abs/2503.21807v1) | LERO: LLM-driven Evolutionary framework with Hybrid Rewards and Enhanced Observation for Multi-Agent Reinforcement Learning | 使能方法 / 背景 | LLM按MARL训练结果进化奖励和观测增强函数，包含外部反馈闭环；目标为普通多agent控制策略，宜作协同训练机制背景。 |
| [2605.29293](https://arxiv.org/abs/2605.29293v1) | LLM-ALSO: LLM-Driven Adaptive Learning-Signal Optimization for Multi-Agent Reinforcement Learning | 使能方法 / 背景 | critic诊断MARL失败，generator改奖励，经短程分叉验证后才进入主训练；是非LLM控制任务的验证门控与阶段适应机制背景。 |
| [2606.18388](https://arxiv.org/abs/2606.18388v2) | LLMZero: Discovering Adaptive Training Strategies for RL Post-Training via LLM Agents | 方法候选，待全文研读 | LLM据checkpoint诊断做树搜索，调整RL训练的多参数轨迹并比较等算力基线；训练控制和策略耦合，研究器自身继承边界待核查。 |
| [2606.06473](https://arxiv.org/abs/2606.06473v1) | MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery | 方法候选，待全文研读 | 在图搜索中共享跨分支经验，维护动态全局回顾记忆并调整编码模式；研究器经验可能改变后续探索，需验证跨任务持久继承。 |
| [2603.23951](https://arxiv.org/abs/2603.23951v1) | From AI Assistant to AI Scientist: Autonomous Discovery of LLM-RL Algorithms with LLM Agents | 方法候选，待全文研读 | 按提案、实现、评测和反思谱系迭代发现LLM策略优化算法；直接AI4AI相关，但算法是否反馈发现器自身、是否多代自治需进一步查。 |
| [2406.01309](https://arxiv.org/abs/2406.01309v4) | REvolve: Reward Evolution with Large Language Models using Human Feedback | 使能方法 / 背景 | 用人类反馈指导LLM进化机器人与驾驶奖励，将隐含偏好变成可训练函数；是人在环奖励设计，不能描述为完全自主LLM RSI。 |
| [2602.23876](https://arxiv.org/abs/2602.23876v1) | RF-Agent: Automated Reward Function Design via Language Agent Tree Search | 使能方法 / 背景 | 用语言agent树搜索和历史训练反馈设计低层控制奖励；提供可复用的搜索组织方法，摘要不含LLM自身权重或harness的进化。 |
| [2604.28056](https://arxiv.org/abs/2604.28056v1) | RHyVE: Competence-Aware Verification and Phase-Aware Deployment for LLM-Generated Reward Hypotheses | 使能方法 / 背景 | 共享策略checkpoint短程分叉验证奖励假说，研究能力阶段影响奖励排名；为共演化部署提供验证协议，不声称通用自治调度器。 |
| [2412.13492](https://arxiv.org/abs/2412.13492v1) | Efficient Language-instructed Skill Acquisition via Reward-Policy Co-Evolution | 使能方法 / 背景 | 继承已有控制策略并让奖励随其能力共同演化，避免每个候选都从头训练；是明确奖励—策略协同机制，目标为非LLM机器人。 |
| [2605.02073](https://arxiv.org/abs/2605.02073v2) | Enhanced LLM Reasoning by Optimizing Reward Functions with Search-Driven Reinforcement Learning | 方法候选，待全文研读 | 前沿LLM按前轮结果搜索奖励并实际训练LLM LoRA；摘要明确用GSM8K test排名候选，正式纳入须另查独立泛化，不能把选择集当外测。 |
| [2602.10226](https://arxiv.org/abs/2602.10226v3) | Self-Evolving Recommendation System: End-To-End Autonomous Model Optimization With LLM Agents | 方法候选，待全文研读 | Gemini agent分离离线代理指标探索与线上业务验证，自动改优化器、架构和奖励；改进对象是推荐模型，应与LLM自身RSI明确分开。 |
| [2605.15308](https://arxiv.org/abs/2605.15308v1) | SMCEvolve: Principled Scientific Discovery via Sequential Monte Carlo Evolution | 使能方法 / 背景 | 将科学程序搜索表述为SMC采样，设计重采样、接受和停止并给调用复杂度分析；是进化搜索方法，摘要未显示自身算法被递归改写。 |
| [2604.14116](https://arxiv.org/abs/2604.14116v2) | TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration | 使能方法 / 背景 | 多agent按树搜索自动完成LLM数据、配方、训练和评估，继承实验结果；是AI4AI训练自动化，摘要未验证研究器自身持续改进。 |
| [2605.28655](https://arxiv.org/abs/2605.28655v1) | AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2512.13399](https://arxiv.org/abs/2512.13399v3) | Dual-Evolving Reinforcement Learning for Automated Reward Design | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2606.03108](https://arxiv.org/abs/2606.03108v2) | EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for Autonomous Agentic Reinforcement Learning | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2605.13874](https://arxiv.org/abs/2605.13874v1) | GEAR: Genetic AutoResearch for Agentic Code Evolution | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2601.14525](https://arxiv.org/abs/2601.14525v1) | Towards Execution-Grounded Automated AI Research | 已对应目录 | 已对应阅读目录；具体机制、结果、来源章节与阅读范围见关联卡片。 |
| [2602.12063](https://arxiv.org/abs/2602.12063v2) | VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model | 方法候选，待全文研读 | 真实机器人rollout改善世界模型，再以合成rollout训练VLA并迭代；两种模型权重共同改进，须区分多模型共学习与外部harness改写。 |
