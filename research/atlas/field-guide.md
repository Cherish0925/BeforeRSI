# 三条 RSI 路线：领域主题与机制联系

这是一份可修订的问题空间与方法索引。主题可以交叉；主路线以实际更新对象确定。没有对应论文的主题仍保留，暂未收录不等于研究不存在。

## Harness

在这一主线中，主要学习与演化对象是 foundation model 参数之外、决定代理行为和改进过程的持久状态与可执行程序。基础模型通常保持冻结；若研究同时更新模型参数，则可与 Model × Harness 图建立连接。

什么被改写，怎样产生下一次改进？

一个代理在真实任务或实验环境中运行，留下行动轨迹、工具错误、结果与成本。系统据此修改提示、知识、技能或执行代码，把候选放回任务中比较；被保留的资产进入后续任务。递归研究进一步把“如何发现问题、提出并实施修改”的程序也放入可编辑范围，由更新后的系统继续推进改进。

### 指令与上下文程序 · Instructions & Context Programs

在权重不变时，怎样改变模型看到的信息和执行指令，使行为稳定改善？

可修改的对象包括 system prompt、模块提示、few-shot examples、上下文组装与压缩规则。文件只是存储载体；研究对象是这些内容对条件生成和后续工具调用的控制作用。

**研究子问题**

- 任务提示与模块提示
- 示例选择与排序
- context assembly / compression
- 可执行规范与格式约束
- 反思形成的 playbook

**主要技术**

- 基于执行轨迹的语言反思
- 候选提示变异与组合
- 按模块优化提示
- 增量编辑与去重

**机制联系**

- 长期记忆与知识组织 → 指令与上下文程序：检索后进入上下文。被检索的经验改变模型下一步看到的信息；长时记忆与单次上下文是两种不同状态。
- 候选生成、搜索与选择 → 指令与上下文程序：产生并选择提示修改。反思、变异和 Pareto 选择可以作用于提示空间。

**论文与团队（包括初筛与跨路线联系）**

- [Promptbreeder](https://arxiv.org/pdf/2309.16797) · Google DeepMind。任务提示；变异提示。变异提示也参与演化；不是权重训练。
- [GEPA](https://arxiv.org/pdf/2507.19457v2) · UC Berkeley / Stanford / Notre Dame / MIT / Databricks / Bespoke Labs。LLM 模块提示。更新提示；优化算法不自修改。
- [Recursive Harness SI](https://arxiv.org/html/2607.15524v1) · Sakana AI / UC Berkeley。任务专用文本工作流跨轮修订；基础模型、评价者及优化器固定。
- [Meta-Harness](https://arxiv.org/html/2603.28052v1) · Stanford / KRAFTON / MIT。应用源码；记忆组织与上下文。源码可编辑范围广不等于每种资产均已有有效自改实证。
- [ACE](https://arxiv.org/html/2510.04618v1) · Stanford / SambaNova / UC Berkeley。持久 playbook。内容与条目演化；生成—反思—整理流程固定。
- [OPRO](https://arxiv.org/abs/2309.03409) · Google DeepMind。候选提示或数值解。优化提示是相关机制；未因迭代次数多成为改进器自修改。
- [Continual Harness](https://arxiv.org/abs/2605.09998) · Princeton / Google DeepMind / ARISE Foundation。技能；提示；记忆。跨交互持久改进；早期人类参与和后续自动循环分开。
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) · Nous Research。从任务经验创建和修改技能文档，保留记忆与会话检索，使后续执行使用已有经验。

### 长期记忆与知识组织 · Persistent Memory & Knowledge

哪些经历应跨任务保留，怎样抽象、检索、修订并消除相互矛盾的经验？

外部记忆保留模型参数之外的可更新状态：episodic traces、经验规则、检索索引、知识库和效用估计。存入更多记录不自动等于学得更多；关键在后续决策是否有效使用这些记录。

**研究子问题**

- episodic / semantic memory
- 经验提炼与抽象
- 检索、排序与记忆效用
- 冲突、过时知识与遗忘
- 跨任务知识整合
- 知识库、数据库与可检索状态

**主要技术**

- 轨迹总结与增量合并
- 相似度检索与效用排序
- 回报更新检索价值
- 基于使用反馈的记忆修订

**机制联系**

- 长期记忆与知识组织 → 指令与上下文程序：检索后进入上下文。被检索的经验改变模型下一步看到的信息；长时记忆与单次上下文是两种不同状态。
- 任务、探索与经验分布 → 长期记忆与知识组织：轨迹形成经验。任务交互产生可总结、可修订的持久记录。
- 长期记忆与知识组织 → 候选生成、搜索与选择：提供既往搜索经验。历史失败、候选和执行结果可以改善后续提案，不一定改变搜索算法本身。
- 长期记忆与知识组织 → 继承、组合与跨域迁移：知识跨任务保留。持久知识要经后续使用才能转化为能力，而非只增加存储量。

**论文与团队（包括初筛与跨路线联系）**

- [HyperAgents](https://arxiv.org/html/2603.19461v1) · Meta / UBC / Vector / Edinburgh / NYU。task agent 代码；meta-agent 代码。meta-agent 修改逻辑可改；主实验 parent selection 固定。
- [HELIX](https://github.com/HKUDS/HELIX) · HKU · In3 Lab。harness 变体；成功及失败轨迹。产出训练记录不等于已实现 model 与 harness 共同演化。
- [Meta-Harness](https://arxiv.org/html/2603.28052v1) · Stanford / KRAFTON / MIT。应用源码；记忆组织与上下文。源码可编辑范围广不等于每种资产均已有有效自改实证。
- [ACE](https://arxiv.org/html/2510.04618v1) · Stanford / SambaNova / UC Berkeley。持久 playbook。内容与条目演化；生成—反思—整理流程固定。
- [Prime Agent](https://arxiv.org/abs/2608.23552) · Princeton / Prime Intellect / MIT。长期 REPL 状态；持久经验与技能。持久执行和经验修订可确认；改进器自修改范围待方法确认。
- [GEAR](https://arxiv.org/abs/2605.13874) · Toronto / Vector / Samsung AI Center–Toronto / York。研究状态种群；部分变体中的搜索控制器。仅部分变体让控制器演化，不能概括为所有 GEAR 设置均递归。
- [Mem²Evolve](https://arxiv.org/abs/2604.10923) · Beihang / Beijing Institute of Technology / Independent / MCML / Edinburgh。经验记忆；工具与专家资产。经验与能力资产双向影响；不据此认定更新算法也进化。
- [MemRL](https://arxiv.org/html/2601.03192v1) · SJTU / Xidian / NUS / Shanghai Innovation Institute / MemTensor / USTC。情景记忆；记忆效用值。LLM 参数冻结；记忆排序价值学习，更新规则本身固定。
- [Group-Evolving Agents](https://arxiv.org/abs/2602.04837) · UC Santa Barbara。代理分支；跨分支经验。初筛支持经验共享引导结构修改；具体递归边界待方法核实。
- [Continual Harness](https://arxiv.org/abs/2605.09998) · Princeton / Google DeepMind / ARISE Foundation。技能；提示；记忆。跨交互持久改进；早期人类参与和后续自动循环分开。
- [Voyager](https://arxiv.org/html/2305.16291v2) · NVIDIA / Caltech / Stanford / UT Austin / UW–Madison。可组合代码技能库。固定 GPT-4 和课程程序；持久技能积累成立，元算法自改未示范。
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) · Nous Research。从任务经验创建和修改技能文档，保留记忆与会话检索，使后续执行使用已有经验。

### 工具、技能与行动接口 · Tools, Skills & Action Interfaces

代理如何从重复操作中创造可调用能力，并把已有能力组合成更长的任务？

可修改对象是可执行工具代码、技能程序、工具说明、输入输出契约及发现与调用方式。Skills、plugins、MCP 是能力暴露和复用的不同载体；安装或调用现成工具本身不构成自改进。

**研究子问题**

- tool synthesis / API construction
- 代码技能与语言技能
- 插件、skills、MCP / API 与调用协议
- 技能组合与依赖
- 技能测试、修复与淘汰

**主要技术**

- 探索后封装可执行程序
- 执行错误驱动修复
- 检索已有技能并组合
- 评测反馈驱动技能编辑

**机制联系**

- 任务、探索与经验分布 → 工具、技能与行动接口：探索产生新技能。完成课程或探索网页后，把有效操作封装为可调用技能。
- 工具、技能与行动接口 → 推理与协作控制结构：扩展可调用动作。新工具扩大动作空间，控制逻辑决定何时调用与组合。
- 候选生成、搜索与选择 → 工具、技能与行动接口：选择工具与技能版本。技能候选通过执行或任务反馈被保留和修复。
- 工具、技能与行动接口 → 继承、组合与跨域迁移：技能可以复用与组合。可执行技能是跨任务继承的一种具体载体。

**论文与团队（包括初筛与跨路线联系）**

- [DGM](https://arxiv.org/html/2505.22954v3) · Sakana AI / UBC / Vector Institute。编码代理代码；工具及上下文实现。被选后继负责修改；archive maintenance 与 parent selection 固定。
- [Prime Agent](https://arxiv.org/abs/2608.23552) · Princeton / Prime Intellect / MIT。长期 REPL 状态；持久经验与技能。持久执行和经验修订可确认；改进器自修改范围待方法确认。
- [Metaⁿ](https://arxiv.org/abs/2608.24735) · University of Minnesota / Seoul National University。策略层与工具。已有初筛表明元操作固定；层数增加不等于元操作本身进化。
- [SkillOpt](https://arxiv.org/abs/2605.23904) · Microsoft / SJTU / Tongji / Fudan。技能文本。外部优化模型修改技能；不是优化模型权重自改。
- [Mem²Evolve](https://arxiv.org/abs/2604.10923) · Beihang / Beijing Institute of Technology / Independent / MCML / Edinburgh。经验记忆；工具与专家资产。经验与能力资产双向影响；不据此认定更新算法也进化。
- [SkillWeaver](https://arxiv.org/abs/2504.07079) · Ohio State / Virginia / Purdue / Carnegie Mellon / Cisco Research。网页 API 技能。技能库增长并用于后续任务；生成过程是否自改另论。
- [Live-SWE-agent](https://arxiv.org/html/2511.13646v1) · UIUC / Google。任务运行时创建的自定义工具脚本。主实验不改变 agentic loop；论文重点是同任务在线工具创造，不能说已证明跨任务递归演化。
- [Continual Harness](https://arxiv.org/abs/2605.09998) · Princeton / Google DeepMind / ARISE Foundation。技能；提示；记忆。跨交互持久改进；早期人类参与和后续自动循环分开。
- [Voyager](https://arxiv.org/html/2305.16291v2) · NVIDIA / Caltech / Stanford / UT Austin / UW–Madison。可组合代码技能库。固定 GPT-4 和课程程序；持久技能积累成立，元算法自改未示范。
- [RewardHarness](https://arxiv.org/html/2605.08703v1) · UBC / Vector / Kuaishou Kolors / Etude AI / Waterloo / Carnegie Mellon / Tsinghua / Georgia Tech。冻结视觉语言模型，通过偏好误差改进 reward agent 的技能和工具；该评价系统随后用于外部图像编辑模型的 GRPO 训练。
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) · Nous Research。从任务经验创建和修改技能文档，保留记忆与会话检索，使后续执行使用已有经验。

### 推理与协作控制结构 · Control Flow & Agent Architecture

何时规划、行动、反思、调用工具或委派，以及多个代理之间怎样交换信息？

结构包括控制流、信息流、角色分工、模型调用路由、停止条件和重试策略。工作流图是其中一种表示；代码还可以表达循环、条件、动态工具和运行时生成的子任务。

**研究子问题**

- 规划与反思调度
- 条件、循环与终止
- multi-agent roles / communication
- 模型与专家路由
- 并行搜索和结果聚合

**主要技术**

- 代码空间中的架构搜索
- 图结构搜索与进化
- MCTS 分配工作流探索
- 执行反馈修订控制逻辑

**机制联系**

- 工具、技能与行动接口 → 推理与协作控制结构：扩展可调用动作。新工具扩大动作空间，控制逻辑决定何时调用与组合。
- 推理与协作控制结构 → 执行系统与资源配置：在执行系统中实现。同一工作流需要具体的调用、状态与错误处理实现，运行成本也随之改变。
- 候选生成、搜索与选择 → 推理与协作控制结构：搜索控制程序。搜索算法也可以修改循环、角色与 LLM 调用次序。

**论文与团队（包括初筛与跨路线联系）**

- [Gödel Agent](https://github.com/Arvid-pku/Godel_Agent) · Peking University / UC Santa Barbara / University of Arizona。代理控制代码。自修改的具体范围与跨任务继承仍需方法全文确认。
- [ADAS](https://arxiv.org/html/2408.08435v1) · UBC / Vector Institute。目标 agent 的 forward 代码。meta-agent 实现固定；目标设计与档案更新。
- [AFlow](https://arxiv.org/html/2410.10762v4) · DeepWisdom / HKUST / HKUST(GZ) / RUC / Nanjing / Fudan / KAUST / Montréal / Mila。工作流代码；模块提示。搜索器固定；搜索的是工作流。
- [DGM](https://arxiv.org/html/2505.22954v3) · Sakana AI / UBC / Vector Institute。编码代理代码；工具及上下文实现。被选后继负责修改；archive maintenance 与 parent selection 固定。
- [AgentBreeder](https://arxiv.org/abs/2502.00757) · University of Oxford。多代理角色与结构。目标多代理系统演化；外层算法自修改未确认。
- [HyperAgents](https://arxiv.org/html/2603.19461v1) · Meta / UBC / Vector / Edinburgh / NYU。task agent 代码；meta-agent 代码。meta-agent 修改逻辑可改；主实验 parent selection 固定。
- [Recursive Harness SI](https://arxiv.org/html/2607.15524v1) · Sakana AI / UC Berkeley。任务专用文本工作流跨轮修订；基础模型、评价者及优化器固定。
- [HarnessDev](https://arxiv.org/abs/2609.01437) · ByteDance Seed / SUTD / Georgia Tech / M-A-P / TokenWave.AI。可执行 scaffold。创造者与执行者可以不同；不把目标优化等同创造者自改。
- [Meta-Harness](https://arxiv.org/html/2603.28052v1) · Stanford / KRAFTON / MIT。应用源码；记忆组织与上下文。源码可编辑范围广不等于每种资产均已有有效自改实证。
- [SoL-Pi](https://arxiv.org/html/2609.20519v1) · NVIDIA / NTU / MIT。运行机制与代理 harness。以执行机制迁移及效率为重点，具体元循环边界见论文。
- [ModularRSI](https://arxiv.org/html/2609.14857v2) · IQuest Research / Langboat / Beihang / Manchester / Hohai / M-A-P。harness 模块。模块局部改进必须经组合后的整体验证。
- [Metaⁿ](https://arxiv.org/abs/2608.24735) · University of Minnesota / Seoul National University。策略层与工具。已有初筛表明元操作固定；层数增加不等于元操作本身进化。
- [Adaptive Auto-Harness](https://arxiv.org/abs/2606.01770) · Emory / Amazon / Penn State / UIUC / Northeastern。harness 集合；任务路由及经验。持续适应含人类引导信号；路由与改进器更新分别判断。
- [Dream-RSI](https://arxiv.org/html/2609.14858v2) · Google / Google DeepMind / Maryland / Virginia。LLM 改写可执行的研究探索策略代码，用已有研究树进行回放、比较和选择；基础 agent 与评价器保持不变。
- [Autoscience · Carl / Mira](https://www.autoscience.ai/blog/autoscience-autonomous-ai-lab) · Autoscience。自动科学家提出和检验算法假设，自动工程师将被验证的模型改进转成可部署实现。

### 执行系统与资源配置 · Runtime, Environment & Infrastructure

怎样让同一模型用更少的时间、调用与资源完成更可靠的任务，并使系统改动可以运行？

包括 REPL、文件与进程状态、执行环境、依赖、调度、缓存、上下文预算、错误恢复与部署配置。须区分代理自己的运行环境，与被研究的外部任务环境；也须区分优化外部基础设施和改造自身 harness。

**研究子问题**

- persistent execution / REPL
- 工具沙箱与依赖环境
- 并行、缓存与调用预算
- 错误恢复及状态恢复
- 软硬件与推理服务优化

**主要技术**

- 执行剖析和瓶颈定位
- 可运行代码补丁
- 性能—费用联合选择
- 在多个环境复用执行机制

**机制联系**

- 推理与协作控制结构 → 执行系统与资源配置：在执行系统中实现。同一工作流需要具体的调用、状态与错误处理实现，运行成本也随之改变。
- 执行系统与资源配置 → 任务、探索与经验分布：产生轨迹与故障。执行日志、异常和运行代价决定系统可以学习哪些失败。

**论文与团队（包括初筛与跨路线联系）**

- [SICA](https://arxiv.org/html/2504.15228v1) · iGent AI / University of Bristol。编码代理代码。历史最佳后继承担下一轮修改；非全部外层程序可改。
- [HELIX](https://github.com/HKUDS/HELIX) · HKU · In3 Lab。harness 变体；成功及失败轨迹。产出训练记录不等于已实现 model 与 harness 共同演化。
- [HSI](https://github.com/TailinZhou/hsi) · HKUST。harness 代码；元演化过程。仓库初筛显示元演化可改；完整作用边界待确认。
- [HarnessDev](https://arxiv.org/abs/2609.01437) · ByteDance Seed / SUTD / Georgia Tech / M-A-P / TokenWave.AI。可执行 scaffold。创造者与执行者可以不同；不把目标优化等同创造者自改。
- [RRSI](https://arxiv.org/html/2609.24972v1) · Google Cloud AI Research / Stanford / Washington University / UNC。harness 修改提案及接受规则。约束的是自修改过程；泛化和成本约束需要分别观察。
- [Meta-Harness](https://arxiv.org/html/2603.28052v1) · Stanford / KRAFTON / MIT。应用源码；记忆组织与上下文。源码可编辑范围广不等于每种资产均已有有效自改实证。
- [AlphaEvolve](https://arxiv.org/abs/2506.13131) · Google DeepMind。目标程序；部分计算基础设施算法。通用程序发现；只有涉及 AI 基础设施的应用属于 AI4AI，不能全部称自身 RSI。
- [SoL-Pi](https://arxiv.org/html/2609.20519v1) · NVIDIA / NTU / MIT。运行机制与代理 harness。以执行机制迁移及效率为重点，具体元循环边界见论文。
- [ModularRSI](https://arxiv.org/html/2609.14857v2) · IQuest Research / Langboat / Beihang / Manchester / Hohai / M-A-P。harness 模块。模块局部改进必须经组合后的整体验证。
- [Prime Agent](https://arxiv.org/abs/2608.23552) · Princeton / Prime Intellect / MIT。长期 REPL 状态；持久经验与技能。持久执行和经验修订可确认；改进器自修改范围待方法确认。
- [Self-Harness](https://arxiv.org/abs/2606.09498) · Shanghai AI Laboratory。自身 harness 代码。需要区分补丁产生与后继继续承担改进的完整循环。
- [Live-SWE-agent](https://arxiv.org/html/2511.13646v1) · UIUC / Google。任务运行时创建的自定义工具脚本。主实验不改变 agentic loop；论文重点是同任务在线工具创造，不能说已证明跨任务递归演化。
- [Adaptive Auto-Harness](https://arxiv.org/abs/2606.01770) · Emory / Amazon / Penn State / UIUC / Northeastern。harness 集合；任务路由及经验。持续适应含人类引导信号；路由与改进器更新分别判断。
- [ShinkaEvolve](https://arxiv.org/abs/2509.19349) · Sakana AI。候选程序；包括部分 agent harness。算法演化框架；普通程序任务属于相关搜索机制，不直接证明自身 RSI。
- [ComfyResearch](https://meta-circle.com/blog/comfyresearch-see-how-learning-happens) · MetaCircle。把训练协议、观测与分析组织成可执行依赖图，供人或 agent 构造、运行和比较实验。
- [Apex-Tune](https://www.apexin.ai/assets/papers/what-happens-when-ai-starts-improving-ai.pdf) · Apex Intelligence。自动提出并验证 scaling law、训练实现和 GPU kernel 的改进，以实验结果继续搜索。
- [Recursive · First Steps](https://www.recursive.com/articles/first-steps-toward-automated-ai-research) · Recursive Superintelligence。长时程并行研究线程积累实验上下文、组合候选分支，并对改进进行方差与 reward-hack 检查。

### 任务、探索与经验分布 · Task Streams, Exploration & Curriculum

系统下一步做什么，才能同时获得有用成果和改善自身所需的信息？

任务选择决定可以观察到的失败和成功。研究包括开放任务流、自动课程、主动探索、失败挖掘与迁移任务选择；课程和环境生成器在部分研究中固定，在另一些研究中也可能成为更新对象。

**研究子问题**

- 自动课程与能力边界
- 任务流及分布变化
- 失败发现与诊断
- 探索和 exploitation
- 同任务适应与跨任务积累

**主要技术**

- 根据进度生成下一任务
- 从失败轨迹选择改进问题
- 任务路由与专家选择
- 跨环境复用已有技能

**机制联系**

- 任务、探索与经验分布 → 长期记忆与知识组织：轨迹形成经验。任务交互产生可总结、可修订的持久记录。
- 任务、探索与经验分布 → 工具、技能与行动接口：探索产生新技能。完成课程或探索网页后，把有效操作封装为可调用技能。
- 执行系统与资源配置 → 任务、探索与经验分布：产生轨迹与故障。执行日志、异常和运行代价决定系统可以学习哪些失败。
- 继承、组合与跨域迁移 → 任务、探索与经验分布：已有能力改变后续探索。继承的技能使更复杂任务可达，进而改变将来收集到的经验。

**论文与团队（包括初筛与跨路线联系）**

- [Self-Harness](https://arxiv.org/abs/2606.09498) · Shanghai AI Laboratory。自身 harness 代码。需要区分补丁产生与后继继续承担改进的完整循环。
- [Mem²Evolve](https://arxiv.org/abs/2604.10923) · Beihang / Beijing Institute of Technology / Independent / MCML / Edinburgh。经验记忆；工具与专家资产。经验与能力资产双向影响；不据此认定更新算法也进化。
- [SkillWeaver](https://arxiv.org/abs/2504.07079) · Ohio State / Virginia / Purdue / Carnegie Mellon / Cisco Research。网页 API 技能。技能库增长并用于后续任务；生成过程是否自改另论。
- [Live-SWE-agent](https://arxiv.org/html/2511.13646v1) · UIUC / Google。任务运行时创建的自定义工具脚本。主实验不改变 agentic loop；论文重点是同任务在线工具创造，不能说已证明跨任务递归演化。
- [Adaptive Auto-Harness](https://arxiv.org/abs/2606.01770) · Emory / Amazon / Penn State / UIUC / Northeastern。harness 集合；任务路由及经验。持续适应含人类引导信号；路由与改进器更新分别判断。
- [Continual Harness](https://arxiv.org/abs/2605.09998) · Princeton / Google DeepMind / ARISE Foundation。技能；提示；记忆。跨交互持久改进；早期人类参与和后续自动循环分开。
- [Voyager](https://arxiv.org/html/2305.16291v2) · NVIDIA / Caltech / Stanford / UT Austin / UW–Madison。可组合代码技能库。固定 GPT-4 和课程程序；持久技能积累成立，元算法自改未示范。
- [Dream-RSI](https://arxiv.org/html/2609.14858v2) · Google / Google DeepMind / Maryland / Virginia。LLM 改写可执行的研究探索策略代码，用已有研究树进行回放、比较和选择；基础 agent 与评价器保持不变。
- [OPHIS](https://meta-circle.com/blog/ophis-a-new-paradigm-for-autoresearch) · MetaCircle。以训练内部观测提出假设和干预，再用重复训练结果决定下一步研究。
- [ComfyResearch](https://meta-circle.com/blog/comfyresearch-see-how-learning-happens) · MetaCircle。把训练协议、观测与分析组织成可执行依赖图，供人或 agent 构造、运行和比较实验。
- [nanoGPT Observable Library](https://meta-circle.com/blog/observe-learning-in-full) · MetaCircle。把权重、梯度、激活和注意力统计与模型模块对应，比较不同深度与训练条件。
- [Recursive · First Steps](https://www.recursive.com/articles/first-steps-toward-automated-ai-research) · Recursive Superintelligence。长时程并行研究线程积累实验上下文、组合候选分支，并对改进进行方差与 reward-hack 检查。
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) · Nous Research。从任务经验创建和修改技能文档，保留记忆与会话检索，使后续执行使用已有经验。
- [Locus](https://intology.ai/blog/previewing-locus) · Intology。公开定位为长时程 AI 研发系统；公司报告多日研究与 RE-Bench 结果。

### 评测、验证器与反馈信号 · Evaluation, Verifiers & Feedback

什么变化算真实进步？反馈不足或评价器自己变化时，怎样继续可靠比较系统版本？

反馈可来自可执行测试、环境回报、人工评价或模型评审；它既指导更新，也决定版本选择。评价器代码和提示可以被优化，但其改进需要独立的任务结果或可信锚点支撑。

**研究子问题**

- verifiable tests / environment reward
- 语言反馈与错误归因
- 模型评审及校准
- 代价、延迟和回归
- 评价器更新与历史结果可比性

**主要技术**

- 阶段性评估和多保真选择
- 外部测试验证候选
- 评审器与任务代理共同演化
- 更新评价器后重评或校准记录

**机制联系**

- 评测、验证器与反馈信号 → 候选生成、搜索与选择：提供比较与选择信号。评价结果影响候选保留、父代采样及下一步探索预算。
- 评测、验证器与反馈信号 → 改进程序的自修改：评价后代改进能力。任务分数之外，需观察改进器在给定预算内产生更强后代的能力。
- 改进程序的自修改 → 评测、验证器与反馈信号：可更新评审组件。改进程序可以产生新评价器；采用新评价器改变了后续搜索的信号。

**论文与团队（包括初筛与跨路线联系）**

- [STOP](https://arxiv.org/pdf/2310.02304) · Microsoft Research / Stanford / OpenAI（研究在微软期间完成）。改进程序源码。后继改进程序继续改写自身；模型冻结。
- [AFlow](https://arxiv.org/html/2410.10762v4) · DeepWisdom / HKUST / HKUST(GZ) / RUC / Nanjing / Fudan / KAUST / Montréal / Mila。工作流代码；模块提示。搜索器固定；搜索的是工作流。
- [SICA](https://arxiv.org/html/2504.15228v1) · iGent AI / University of Bristol。编码代理代码。历史最佳后继承担下一轮修改；非全部外层程序可改。
- [GEPA](https://arxiv.org/pdf/2507.19457v2) · UC Berkeley / Stanford / Notre Dame / MIT / Databricks / Bespoke Labs。LLM 模块提示。更新提示；优化算法不自修改。
- [Recursive Harness SI](https://arxiv.org/html/2607.15524v1) · Sakana AI / UC Berkeley。任务专用文本工作流跨轮修订；基础模型、评价者及优化器固定。
- [RRSI](https://arxiv.org/html/2609.24972v1) · Google Cloud AI Research / Stanford / Washington University / UNC。harness 修改提案及接受规则。约束的是自修改过程；泛化和成本约束需要分别观察。
- [AIDE²](https://arxiv.org/html/2609.26457v1) · Weco AI。内层研究代理。主实验外层研究者固定；另有后继接管外层的实验。
- [Huxley–Gödel Machine](https://arxiv.org/html/2510.21614v1) · KAUST。代理分支；分支研发价值估计。选择机制由研究者设计；它指导自修改分支探索。
- [Red Queen Gödel Machine](https://arxiv.org/html/2606.26294v3) · Cambridge / NVIDIA / Flower Labs / MBZUAI / Inria。任务代理；评价器。评价器可改；独立 ground-truth anchors 不随评审器替换而抹去。
- [Self-Harness](https://arxiv.org/abs/2606.09498) · Shanghai AI Laboratory。自身 harness 代码。需要区分补丁产生与后继继续承担改进的完整循环。
- [SkillOpt](https://arxiv.org/abs/2605.23904) · Microsoft / SJTU / Tongji / Fudan。技能文本。外部优化模型修改技能；不是优化模型权重自改。
- [MemRL](https://arxiv.org/html/2601.03192v1) · SJTU / Xidian / NUS / Shanghai Innovation Institute / MemTensor / USTC。情景记忆；记忆效用值。LLM 参数冻结；记忆排序价值学习，更新规则本身固定。
- [RewardHarness](https://arxiv.org/html/2605.08703v1) · UBC / Vector / Kuaishou Kolors / Etude AI / Waterloo / Carnegie Mellon / Tsinghua / Georgia Tech。冻结视觉语言模型，通过偏好误差改进 reward agent 的技能和工具；该评价系统随后用于外部图像编辑模型的 GRPO 训练。
- [OPHIS](https://meta-circle.com/blog/ophis-a-new-paradigm-for-autoresearch) · MetaCircle。以训练内部观测提出假设和干预，再用重复训练结果决定下一步研究。
- [ComfyResearch](https://meta-circle.com/blog/comfyresearch-see-how-learning-happens) · MetaCircle。把训练协议、观测与分析组织成可执行依赖图，供人或 agent 构造、运行和比较实验。
- [nanoGPT Observable Library](https://meta-circle.com/blog/observe-learning-in-full) · MetaCircle。把权重、梯度、激活和注意力统计与模型模块对应，比较不同深度与训练条件。
- [Apex-Tune](https://www.apexin.ai/assets/papers/what-happens-when-ai-starts-improving-ai.pdf) · Apex Intelligence。自动提出并验证 scaling law、训练实现和 GPU kernel 的改进，以实验结果继续搜索。
- [Apex Research report](https://github.com/apexin-ai/apex-research-report) · Apex Intelligence。公司报告自主研究系统产生科研项目与论文，并用真实外部同行评审检验产出。
- [ASI-Bench](https://arxiv.org/abs/2608.17271) · Tsinghua / University of Michigan / MIT / Harvard / Carnegie Mellon / UIUC / Boston University / University of Queensland / USTC / Flatiron Institute / Microsoft Research / AG2 AI / Independent Researchers。在相同科研任务上逐步撤去方法指导，区分按步骤执行和自主选择科研方法的能力。
- [Recursive · First Steps](https://www.recursive.com/articles/first-steps-toward-automated-ai-research) · Recursive Superintelligence。长时程并行研究线程积累实验上下文、组合候选分支，并对改进进行方差与 reward-hack 检查。
- [Autoscience · Carl / Mira](https://www.autoscience.ai/blog/autoscience-autonomous-ai-lab) · Autoscience。自动科学家提出和检验算法假设，自动工程师将被验证的模型改进转成可部署实现。

### 候选生成、搜索与选择 · Search, Selection & Evolution

如何在昂贵、噪声大而组合复杂的程序空间中找到有积累价值的修改？

这是作用于不同资产的更新机制，而不是一种独立资产。反思给出修改方向，搜索决定探索分配，选择决定继承哪些候选；档案和种群可以保留暂时非最优但有用的中间方案。

**研究子问题**

- reflection-guided proposals
- evolution / crossover
- MCTS / bandit allocation
- Pareto selection
- archives / stepping stones

**主要技术**

- 基于反馈的程序变异
- 多分支搜索与重组
- 分层评估分配计算
- 根据后代收益选择父代

**机制联系**

- 评测、验证器与反馈信号 → 候选生成、搜索与选择：提供比较与选择信号。评价结果影响候选保留、父代采样及下一步探索预算。
- 候选生成、搜索与选择 → 指令与上下文程序：产生并选择提示修改。反思、变异和 Pareto 选择可以作用于提示空间。
- 候选生成、搜索与选择 → 推理与协作控制结构：搜索控制程序。搜索算法也可以修改循环、角色与 LLM 调用次序。
- 候选生成、搜索与选择 → 工具、技能与行动接口：选择工具与技能版本。技能候选通过执行或任务反馈被保留和修复。
- 长期记忆与知识组织 → 候选生成、搜索与选择：提供既往搜索经验。历史失败、候选和执行结果可以改善后续提案，不一定改变搜索算法本身。
- 改进程序的自修改 → 候选生成、搜索与选择：改写改进策略。当改进器可编辑时，后继系统可以改变诊断和提案方法；外层选择机制是否可改需逐项说明。
- 候选生成、搜索与选择 → 改进程序的自修改：把改进器作为候选对象。被搜索的程序可以恰好就是产生下一轮修改的程序，形成自指更新。
- 候选生成、搜索与选择 → 继承、组合与跨域迁移：保留分支与中间方案。谱系档案允许当前非最优候选成为未来改进的起点。

**论文与团队（包括初筛与跨路线联系）**

- [STOP](https://arxiv.org/pdf/2310.02304) · Microsoft Research / Stanford / OpenAI（研究在微软期间完成）。改进程序源码。后继改进程序继续改写自身；模型冻结。
- [Promptbreeder](https://arxiv.org/pdf/2309.16797) · Google DeepMind。任务提示；变异提示。变异提示也参与演化；不是权重训练。
- [ADAS](https://arxiv.org/html/2408.08435v1) · UBC / Vector Institute。目标 agent 的 forward 代码。meta-agent 实现固定；目标设计与档案更新。
- [AFlow](https://arxiv.org/html/2410.10762v4) · DeepWisdom / HKUST / HKUST(GZ) / RUC / Nanjing / Fudan / KAUST / Montréal / Mila。工作流代码；模块提示。搜索器固定；搜索的是工作流。
- [SICA](https://arxiv.org/html/2504.15228v1) · iGent AI / University of Bristol。编码代理代码。历史最佳后继承担下一轮修改；非全部外层程序可改。
- [DGM](https://arxiv.org/html/2505.22954v3) · Sakana AI / UBC / Vector Institute。编码代理代码；工具及上下文实现。被选后继负责修改；archive maintenance 与 parent selection 固定。
- [GEPA](https://arxiv.org/pdf/2507.19457v2) · UC Berkeley / Stanford / Notre Dame / MIT / Databricks / Bespoke Labs。LLM 模块提示。更新提示；优化算法不自修改。
- [AgentBreeder](https://arxiv.org/abs/2502.00757) · University of Oxford。多代理角色与结构。目标多代理系统演化；外层算法自修改未确认。
- [HELIX](https://github.com/HKUDS/HELIX) · HKU · In3 Lab。harness 变体；成功及失败轨迹。产出训练记录不等于已实现 model 与 harness 共同演化。
- [HSI](https://github.com/TailinZhou/hsi) · HKUST。harness 代码；元演化过程。仓库初筛显示元演化可改；完整作用边界待确认。
- [HarnessDev](https://arxiv.org/abs/2609.01437) · ByteDance Seed / SUTD / Georgia Tech / M-A-P / TokenWave.AI。可执行 scaffold。创造者与执行者可以不同；不把目标优化等同创造者自改。
- [Meta-Harness](https://arxiv.org/html/2603.28052v1) · Stanford / KRAFTON / MIT。应用源码；记忆组织与上下文。源码可编辑范围广不等于每种资产均已有有效自改实证。
- [AIDE²](https://arxiv.org/html/2609.26457v1) · Weco AI。内层研究代理。主实验外层研究者固定；另有后继接管外层的实验。
- [Huxley–Gödel Machine](https://arxiv.org/html/2510.21614v1) · KAUST。代理分支；分支研发价值估计。选择机制由研究者设计；它指导自修改分支探索。
- [AlphaEvolve](https://arxiv.org/abs/2506.13131) · Google DeepMind。目标程序；部分计算基础设施算法。通用程序发现；只有涉及 AI 基础设施的应用属于 AI4AI，不能全部称自身 RSI。
- [OPRO](https://arxiv.org/abs/2309.03409) · Google DeepMind。候选提示或数值解。优化提示是相关机制；未因迭代次数多成为改进器自修改。
- [SoL-Pi](https://arxiv.org/html/2609.20519v1) · NVIDIA / NTU / MIT。运行机制与代理 harness。以执行机制迁移及效率为重点，具体元循环边界见论文。
- [Red Queen Gödel Machine](https://arxiv.org/html/2606.26294v3) · Cambridge / NVIDIA / Flower Labs / MBZUAI / Inria。任务代理；评价器。评价器可改；独立 ground-truth anchors 不随评审器替换而抹去。
- [GEAR](https://arxiv.org/abs/2605.13874) · Toronto / Vector / Samsung AI Center–Toronto / York。研究状态种群；部分变体中的搜索控制器。仅部分变体让控制器演化，不能概括为所有 GEAR 设置均递归。
- [Group-Evolving Agents](https://arxiv.org/abs/2602.04837) · UC Santa Barbara。代理分支；跨分支经验。初筛支持经验共享引导结构修改；具体递归边界待方法核实。
- [Adaptive Auto-Harness](https://arxiv.org/abs/2606.01770) · Emory / Amazon / Penn State / UIUC / Northeastern。harness 集合；任务路由及经验。持续适应含人类引导信号；路由与改进器更新分别判断。
- [ShinkaEvolve](https://arxiv.org/abs/2509.19349) · Sakana AI。候选程序；包括部分 agent harness。算法演化框架；普通程序任务属于相关搜索机制，不直接证明自身 RSI。
- [Dream-RSI](https://arxiv.org/html/2609.14858v2) · Google / Google DeepMind / Maryland / Virginia。LLM 改写可执行的研究探索策略代码，用已有研究树进行回放、比较和选择；基础 agent 与评价器保持不变。
- [RewardHarness](https://arxiv.org/html/2605.08703v1) · UBC / Vector / Kuaishou Kolors / Etude AI / Waterloo / Carnegie Mellon / Tsinghua / Georgia Tech。冻结视觉语言模型，通过偏好误差改进 reward agent 的技能和工具；该评价系统随后用于外部图像编辑模型的 GRPO 训练。
- [OPHIS](https://meta-circle.com/blog/ophis-a-new-paradigm-for-autoresearch) · MetaCircle。以训练内部观测提出假设和干预，再用重复训练结果决定下一步研究。
- [Apex-Tune](https://www.apexin.ai/assets/papers/what-happens-when-ai-starts-improving-ai.pdf) · Apex Intelligence。自动提出并验证 scaling law、训练实现和 GPU kernel 的改进，以实验结果继续搜索。
- [Apex Research report](https://github.com/apexin-ai/apex-research-report) · Apex Intelligence。公司报告自主研究系统产生科研项目与论文，并用真实外部同行评审检验产出。
- [Recursive · First Steps](https://www.recursive.com/articles/first-steps-toward-automated-ai-research) · Recursive Superintelligence。长时程并行研究线程积累实验上下文、组合候选分支，并对改进进行方差与 reward-hack 检查。
- [Locus](https://intology.ai/blog/previewing-locus) · Intology。公开定位为长时程 AI 研发系统；公司报告多日研究与 RE-Bench 结果。
- [Autoscience · Carl / Mira](https://www.autoscience.ai/blog/autoscience-autonomous-ai-lab) · Autoscience。自动科学家提出和检验算法假设，自动工程师将被验证的模型改进转成可部署实现。

### 改进程序的自修改 · Self-Modification of the Improver

更新后的系统能否参与下一轮更新，并改变提出、实施或组织改进的方法？

把 task agent 与改进器区分开：自动优化目标系统，不必然修改优化器。真正需要定位的是哪些改进程序可编辑、修改后是否被下一代执行，以及父代选择、评价、预算等外层机制仍有哪些固定部分。

**研究子问题**

- self-editing task agent
- 可演化的 mutation prompt
- editable meta-agent
- 元层诊断和实验策略
- 固定外层控制的边界

**主要技术**

- 改进器以自身代码为输入
- 更新任务逻辑与元代理逻辑
- 后继改进器继续提出修改
- 测试改进策略的跨任务迁移

**机制联系**

- 改进程序的自修改 → 候选生成、搜索与选择：改写改进策略。当改进器可编辑时，后继系统可以改变诊断和提案方法；外层选择机制是否可改需逐项说明。
- 候选生成、搜索与选择 → 改进程序的自修改：把改进器作为候选对象。被搜索的程序可以恰好就是产生下一轮修改的程序，形成自指更新。
- 评测、验证器与反馈信号 → 改进程序的自修改：评价后代改进能力。任务分数之外，需观察改进器在给定预算内产生更强后代的能力。
- 改进程序的自修改 → 评测、验证器与反馈信号：可更新评审组件。改进程序可以产生新评价器；采用新评价器改变了后续搜索的信号。
- 继承、组合与跨域迁移 → 改进程序的自修改：改进经验可跨域使用。迁移的不仅可以是解题程序，也可以是产生改进的策略；须由对应的迁移实验确认。

**论文与团队（包括初筛与跨路线联系）**

- [STOP](https://arxiv.org/pdf/2310.02304) · Microsoft Research / Stanford / OpenAI（研究在微软期间完成）。改进程序源码。后继改进程序继续改写自身；模型冻结。
- [Promptbreeder](https://arxiv.org/pdf/2309.16797) · Google DeepMind。任务提示；变异提示。变异提示也参与演化；不是权重训练。
- [Gödel Agent](https://github.com/Arvid-pku/Godel_Agent) · Peking University / UC Santa Barbara / University of Arizona。代理控制代码。自修改的具体范围与跨任务继承仍需方法全文确认。
- [SICA](https://arxiv.org/html/2504.15228v1) · iGent AI / University of Bristol。编码代理代码。历史最佳后继承担下一轮修改；非全部外层程序可改。
- [DGM](https://arxiv.org/html/2505.22954v3) · Sakana AI / UBC / Vector Institute。编码代理代码；工具及上下文实现。被选后继负责修改；archive maintenance 与 parent selection 固定。
- [HyperAgents](https://arxiv.org/html/2603.19461v1) · Meta / UBC / Vector / Edinburgh / NYU。task agent 代码；meta-agent 代码。meta-agent 修改逻辑可改；主实验 parent selection 固定。
- [HSI](https://github.com/TailinZhou/hsi) · HKUST。harness 代码；元演化过程。仓库初筛显示元演化可改；完整作用边界待确认。
- [RRSI](https://arxiv.org/html/2609.24972v1) · Google Cloud AI Research / Stanford / Washington University / UNC。harness 修改提案及接受规则。约束的是自修改过程；泛化和成本约束需要分别观察。
- [AIDE²](https://arxiv.org/html/2609.26457v1) · Weco AI。内层研究代理。主实验外层研究者固定；另有后继接管外层的实验。
- [Huxley–Gödel Machine](https://arxiv.org/html/2510.21614v1) · KAUST。代理分支；分支研发价值估计。选择机制由研究者设计；它指导自修改分支探索。
- [ModularRSI](https://arxiv.org/html/2609.14857v2) · IQuest Research / Langboat / Beihang / Manchester / Hohai / M-A-P。harness 模块。模块局部改进必须经组合后的整体验证。
- [Red Queen Gödel Machine](https://arxiv.org/html/2606.26294v3) · Cambridge / NVIDIA / Flower Labs / MBZUAI / Inria。任务代理；评价器。评价器可改；独立 ground-truth anchors 不随评审器替换而抹去。
- [GEAR](https://arxiv.org/abs/2605.13874) · Toronto / Vector / Samsung AI Center–Toronto / York。研究状态种群；部分变体中的搜索控制器。仅部分变体让控制器演化，不能概括为所有 GEAR 设置均递归。
- [Metaⁿ](https://arxiv.org/abs/2608.24735) · University of Minnesota / Seoul National University。策略层与工具。已有初筛表明元操作固定；层数增加不等于元操作本身进化。
- [Self-Harness](https://arxiv.org/abs/2606.09498) · Shanghai AI Laboratory。自身 harness 代码。需要区分补丁产生与后继继续承担改进的完整循环。
- [Group-Evolving Agents](https://arxiv.org/abs/2602.04837) · UC Santa Barbara。代理分支；跨分支经验。初筛支持经验共享引导结构修改；具体递归边界待方法核实。

### 继承、组合与跨域迁移 · Inheritance, Composition & Transfer

一次修改如何成为后续仍可调用的能力，而非只对当前任务有效的临时技巧？

继承对象可以是提示、记忆、技能、程序版本或搜索经验。需要分别观察同任务复用、跨任务迁移、跨模型迁移以及改进策略迁移；这些能力不同，不能用一个总分代替。

**研究子问题**

- 跨 episode 继承
- 模块与技能的组合
- 跨模型迁移
- 跨任务与环境迁移
- 改进策略的迁移

**主要技术**

- 版本与谱系档案
- 技能检索和依赖复用
- 模块整合及回归测试
- 固定预算下比较迁移后改进

**机制联系**

- 候选生成、搜索与选择 → 继承、组合与跨域迁移：保留分支与中间方案。谱系档案允许当前非最优候选成为未来改进的起点。
- 工具、技能与行动接口 → 继承、组合与跨域迁移：技能可以复用与组合。可执行技能是跨任务继承的一种具体载体。
- 长期记忆与知识组织 → 继承、组合与跨域迁移：知识跨任务保留。持久知识要经后续使用才能转化为能力，而非只增加存储量。
- 继承、组合与跨域迁移 → 任务、探索与经验分布：已有能力改变后续探索。继承的技能使更复杂任务可达，进而改变将来收集到的经验。
- 继承、组合与跨域迁移 → 改进程序的自修改：改进经验可跨域使用。迁移的不仅可以是解题程序，也可以是产生改进的策略；须由对应的迁移实验确认。

**论文与团队（包括初筛与跨路线联系）**

- [ADAS](https://arxiv.org/html/2408.08435v1) · UBC / Vector Institute。目标 agent 的 forward 代码。meta-agent 实现固定；目标设计与档案更新。
- [DGM](https://arxiv.org/html/2505.22954v3) · Sakana AI / UBC / Vector Institute。编码代理代码；工具及上下文实现。被选后继负责修改；archive maintenance 与 parent selection 固定。
- [HyperAgents](https://arxiv.org/html/2603.19461v1) · Meta / UBC / Vector / Edinburgh / NYU。task agent 代码；meta-agent 代码。meta-agent 修改逻辑可改；主实验 parent selection 固定。
- [HarnessDev](https://arxiv.org/abs/2609.01437) · ByteDance Seed / SUTD / Georgia Tech / M-A-P / TokenWave.AI。可执行 scaffold。创造者与执行者可以不同；不把目标优化等同创造者自改。
- [AIDE²](https://arxiv.org/html/2609.26457v1) · Weco AI。内层研究代理。主实验外层研究者固定；另有后继接管外层的实验。
- [ACE](https://arxiv.org/html/2510.04618v1) · Stanford / SambaNova / UC Berkeley。持久 playbook。内容与条目演化；生成—反思—整理流程固定。
- [SoL-Pi](https://arxiv.org/html/2609.20519v1) · NVIDIA / NTU / MIT。运行机制与代理 harness。以执行机制迁移及效率为重点，具体元循环边界见论文。
- [ModularRSI](https://arxiv.org/html/2609.14857v2) · IQuest Research / Langboat / Beihang / Manchester / Hohai / M-A-P。harness 模块。模块局部改进必须经组合后的整体验证。
- [SkillOpt](https://arxiv.org/abs/2605.23904) · Microsoft / SJTU / Tongji / Fudan。技能文本。外部优化模型修改技能；不是优化模型权重自改。
- [Mem²Evolve](https://arxiv.org/abs/2604.10923) · Beihang / Beijing Institute of Technology / Independent / MCML / Edinburgh。经验记忆；工具与专家资产。经验与能力资产双向影响；不据此认定更新算法也进化。
- [MemRL](https://arxiv.org/html/2601.03192v1) · SJTU / Xidian / NUS / Shanghai Innovation Institute / MemTensor / USTC。情景记忆；记忆效用值。LLM 参数冻结；记忆排序价值学习，更新规则本身固定。
- [SkillWeaver](https://arxiv.org/abs/2504.07079) · Ohio State / Virginia / Purdue / Carnegie Mellon / Cisco Research。网页 API 技能。技能库增长并用于后续任务；生成过程是否自改另论。
- [Group-Evolving Agents](https://arxiv.org/abs/2602.04837) · UC Santa Barbara。代理分支；跨分支经验。初筛支持经验共享引导结构修改；具体递归边界待方法核实。
- [Voyager](https://arxiv.org/html/2305.16291v2) · NVIDIA / Caltech / Stanford / UT Austin / UW–Madison。可组合代码技能库。固定 GPT-4 和课程程序；持久技能积累成立，元算法自改未示范。
- [Dream-RSI](https://arxiv.org/html/2609.14858v2) · Google / Google DeepMind / Maryland / Virginia。LLM 改写可执行的研究探索策略代码，用已有研究树进行回放、比较和选择；基础 agent 与评价器保持不变。

### 持续研究的问题

- **什么样的经验能够成为跨任务、跨模型仍然有效的程序改进？** 从当前任务中得到的提示、技能和代码补丁，哪些依赖原模型与环境，哪些能组合为可迁移能力？如何避免长期积累后相互干扰、过时或上下文膨胀？ 现有工作已经展示局部迁移和长期记忆机制，但不能由单一分布、有限任务上的迁移推出开放任务流中的持续泛化。
- **什么改进会同时提升解题能力和产生下一轮改进的能力？** 更高 solve rate 是否提高给定预算内发现有效修改的概率？若解题与改进技能不对齐，哪些元层表示、反馈和可编辑边界有帮助？ DGM 和 HyperAgents 已研究自指更新与元层迁移；有限轮次收益还不能建立跨领域、跨预算持续提高改进效率的一般规律。
- **评价器与任务分布都变化时，系统怎样保持进步的方向？** 学习中的 evaluator 如何与任务真值、实际效用和旧版本保持联系？怎样区分真实能力提升、评价器偏好变化与重复选择造成的过拟合？ 共同演化与评价锚点已有方法；开放任务中真值稀少、目标变化和长期比较仍不是已解决的一般问题。

## Model

收录参数被学习更新的自训练、自反馈与 AI4AI 机制。ordinary RL、一次性 distillation 和使用 AI 处理数据是相关机制，不自动称为多代 RSI。若迭代对象仅为代码 / prompt，则归 Harness。

学习信号从哪里来，下一代怎样变强？

一代模型产生任务、答案或行动经验；反馈决定训练信号和数据分布；参数更新产生下一代。更深的闭环会继续训练评价者、出题者、数据选择者或改进器，使下一代不只更会解题，也改变下一轮学习条件。

### 自生成数据与自训练 · Self-training & bootstrapping

模型的哪些输出值得成为下一轮训练数据？

模型生成解答、推理链或示范，经筛选后回流参数学习。关键变量是样本质量、覆盖、多样性，以及新一代是否重新产生训练数据。

**研究子问题**

- Rationale bootstrapping：推理链自举
- Rejection fine-tuning：正确轨迹筛选
- Self-consistency filtering：自一致筛选
- Self-distillation：自身经验蒸馏
- Replay / mixture：新旧数据混合

**主要技术**

- 采样候选 → 选取高质量轨迹 → SFT / 蒸馏 → 再采样
- 筛选信号可来自答案、执行器或 learned evaluator

**机制联系**

- 可验证反馈与策略改进 → 自生成数据与自训练：筛选正确轨迹。外部答案或执行结果可以提供自训练的样本接受条件。
- 评价器学习与生成—验证共演 → 自生成数据与自训练：筛选 / 标注自生数据。学到的评价器可决定哪些生成样本进入下一轮训练。
- 自生成数据与自训练 → 评价器学习与生成—验证共演：提供新判断样本。自生成候选及其选择结果构造新的 evaluator 训练材料。
- 环境交互与长程经验学习 → 自生成数据与自训练：回放 / 蒸馏有效经验。经反馈选择的交互经验可变为后续监督训练材料；与在线 RL 可组合。
- 学习如何改进学习者 → 自生成数据与自训练：优化训练材料。外层按内层学习收益训练数据 / 自编辑生成策略。
- 预训练中的 AI4AI → 自生成数据与自训练：扩展训练材料。AI 合成 / 改写语料可以进入预训练；这条使用关系不证明训练反馈反向改进生成器。

**论文与团队（包括初筛与跨路线联系）**

- [SPIN](https://github.com/uclaml/SPIN) · UCLA · Quanquan Gu 团队。以当前输出与原始示范分布比较，迭代改进模型；self-play 一词不等于动态出题。
- [SEAL](https://arxiv.org/html/2506.10943v1) · MIT · Improbable AI Lab / CSAIL。学习自编辑数据 / 更新指令，并用内层适应效果训练编辑策略。
- [STaR](https://arxiv.org/abs/2203.14465) · Stanford / Google Research。正确答案筛选自生推理链，答案辅助 rationalization 后再微调。
- [ReST-EM](https://arxiv.org/html/2312.06585v4) · Google DeepMind / Mila。自生样本按外部二元反馈筛选，E/M 轮交替。
- [AlphaProof](https://www.nature.com/articles/s41586-025-09833-y) · Google DeepMind。Lean 验证搜索经验，训练证明网络并做 test-time RL。
- [Constitutional AI](https://arxiv.org/html/2212.08073v1) · Anthropic。原则引导 self-critique / revision，再以 AI 偏好训练奖励与策略；非多代奖励者共演证据。
- [Self-Taught Evaluators](https://arxiv.org/html/2408.02666v1) · Meta FAIR。合成判断与偏好训练 evaluator，再以新评价生成下一轮训练数据。
- [rStar-Math](https://arxiv.org/abs/2501.04519) · Microsoft Research Asia / Peking University / Tsinghua。搜索轨迹训练 policy 与 process preference model，结果验证约束反馈。
- [Self-Evolved Reward](https://arxiv.org/abs/2411.00418) · Fudan / Peking University / Microsoft。奖励模型用自生训练反馈迭代学习评价能力。
- [DeepSeekMath-V2](https://arxiv.org/html/2511.22570v1) · DeepSeek-AI。验证器、元验证与生成器迭代；轮间 rejection fine-tuning 融合能力。
- [LLMs Can Self-Improve](https://aclanthology.org/2023.emnlp-main.67.pdf) · Google / UIUC。self-consistency 筛选自生推理，回流 SFT；保留一轮自训练范围。
- [SEED Distillation](https://arxiv.org/html/2607.14777v1) · Tsinghua / Zhejiang University / CUHK / NTU / Tongji。同一策略承担 actor 与训练期 analyzer；从自身轨迹提炼 hindsight skills，形成 on-policy distillation 与 RL 信号。部署时移除 analyzer，保留更新后的策略模型。
- [WebEvolver](https://arxiv.org/html/2504.21024v2) · Tencent AI Lab。策略 LLM 与 world-model LLM 从交互轨迹中共同训练；世界模型提供合成经验与前瞻规划。可变对象是两类模型的参数。

### 自批评与 AI 偏好反馈 · Self-critique & AI feedback

没有唯一正确答案时，怎样把批评或偏好变成训练信号？

由模型根据原则、rubric 或比较任务生成批评、修订与偏好，再训练回答策略。评价者可以冻结，也可以参与下一轮学习；这两种闭环强度不同。

**研究子问题**

- Critique–revise：批评与修订
- RLAIF：AI 反馈强化学习
- Iterative DPO / preference optimization
- Constitution / rubric：原则与评价准则
- Shared generator–judge：生成与评价共享参数

**主要技术**

- 自批评 → 修订示范 → SFT
- 成对评价 → 偏好对 → DPO 或 reward-model RL

**机制联系**

- 评价器学习与生成—验证共演 → 自批评与 AI 偏好反馈：形成 AI 偏好。评价模型把开放式回答比较转为偏好训练信号。
- 自批评与 AI 偏好反馈 → 评价器学习与生成—验证共演：共同更新评价能力。生成与判断共享参数时，偏好训练可能同时改变二者；需实测判断能力。

**论文与团队（包括初筛与跨路线联系）**

- [SPIN](https://github.com/uclaml/SPIN) · UCLA · Quanquan Gu 团队。以当前输出与原始示范分布比较，迭代改进模型；self-play 一词不等于动态出题。
- [Self-Rewarding LM](https://arxiv.org/html/2401.10020v1) · Meta / NYU。回答与 judge 共享模型；自生偏好用于逐轮 DPO。
- [Constitutional AI](https://arxiv.org/html/2212.08073v1) · Anthropic。原则引导 self-critique / revision，再以 AI 偏好训练奖励与策略；非多代奖励者共演证据。
- [Iterative RPO](https://arxiv.org/html/2404.19733v2) · Meta FAIR / NYU。答案正确性形成正负推理对，以 DPO+NLL 迭代训练；AI 生成数据不等于 AI 决定偏好真值。
- [Kimi K2](https://arxiv.org/html/2507.20534v1) · Moonshot AI（月之暗面）。RLVR 信号校准 K2 critic，rubric 评价开放任务；另有预训练 rephrasing，二者不是一个已证递归环。

### 可验证反馈与策略改进 · Verifiable feedback & policy improvement

哪些任务能把执行结果变成可靠、可扩展的学习信号？

答案检查、程序运行、环境状态或形式化证明核验提供外部反馈。可以用这些反馈筛选示范，也可以直接进行 RLVR；可验证反馈不是某一种优化算法。

**研究子问题**

- Outcome verification：结果核验
- Execution feedback：程序与工具执行
- Formal verification：Lean 等证明核验
- Search-to-train：搜索结果回流训练
- Process credit：中间步骤与轨迹归因

**主要技术**

- 当前策略采样 / 搜索 → 执行核验 → reward 或正负样本 → 参数更新

**机制联系**

- 可验证反馈与策略改进 → 自生成数据与自训练：筛选正确轨迹。外部答案或执行结果可以提供自训练的样本接受条件。
- 可验证反馈与策略改进 → 评价器学习与生成—验证共演：校准评价器。结果可靠的任务为 learned critic / verifier 提供训练信号。
- 可验证反馈与策略改进 → 任务生成与自博弈：验证任务与解答。可执行环境同时检查自生任务是否合法、解答是否正确。
- 环境交互与长程经验学习 → 可验证反馈与策略改进：产生执行结果。环境动作和程序执行产生可检验的状态变化与反馈。
- 可验证反馈与策略改进 → 持续学习与测试时适应：支持测试时参数学习。测试时的可验证尝试可回流参数，而不只增加搜索量。

**论文与团队（包括初筛与跨路线联系）**

- [STaR](https://arxiv.org/abs/2203.14465) · Stanford / Google Research。正确答案筛选自生推理链，答案辅助 rationalization 后再微调。
- [ReST-EM](https://arxiv.org/html/2312.06585v4) · Google DeepMind / Mila。自生样本按外部二元反馈筛选，E/M 轮交替。
- [AlphaProof](https://www.nature.com/articles/s41586-025-09833-y) · Google DeepMind。Lean 验证搜索经验，训练证明网络并做 test-time RL。
- [Absolute Zero](https://arxiv.org/abs/2505.03335) · Tsinghua / BIGAI / Penn State。同一模型兼任 proposer / solver，执行器给 correctness，求解成功率给 learnability。
- [Tool-R0](https://arxiv.org/abs/2602.21320) · UIUC / ETH Zürich。工具任务生成与工具求解互相反馈；运行结果支持训练信号。
- [rStar-Math](https://arxiv.org/abs/2501.04519) · Microsoft Research Asia / Peking University / Tsinghua。搜索轨迹训练 policy 与 process preference model，结果验证约束反馈。
- [Teaching LLMs to Self-Evolve](https://arxiv.org/abs/2607.21971) · UIUC。用执行反馈训练多轮程序修订；meta-skills 不等于学习优化器。
- [RL Tango](https://arxiv.org/abs/2505.15034) · MIT / MIT–IBM Watson AI Lab。生成者与过程验证者交替训练，结果正确性提供外部评价锚点。
- [Iterative RPO](https://arxiv.org/html/2404.19733v2) · Meta FAIR / NYU。答案正确性形成正负推理对，以 DPO+NLL 迭代训练；AI 生成数据不等于 AI 决定偏好真值。
- [Kimi K2](https://arxiv.org/html/2507.20534v1) · Moonshot AI（月之暗面）。RLVR 信号校准 K2 critic，rubric 评价开放任务；另有预训练 rephrasing，二者不是一个已证递归环。
- [INTELLECT-3 / PRIME-RL](https://www.primeintellect.ai/blog/intellect-3) · Prime Intellect。以合成数据、可验证环境和异步 RL 训练 106B MoE，公开训练框架、环境与模型。

### 评价器学习与生成—验证共演 · Evaluator learning & generator–verifier co-training

生成器变强之后，评价器如何继续识别新错误？

把 judge、reward model 或 verifier 也作为学习对象。生成器不断提供新的判断难例，评价器更新后再影响生成器或数据选择。共享权重和独立模型都能实现这条关系。

**研究子问题**

- Generative reward model：生成式奖励模型
- Process / outcome verifier：过程与结果验证
- Meta-verification：检查评价理由
- Actor–critic co-training：执行与评价共训
- Calibration：以可验证任务校准开放式评价

**主要技术**

- 生成器产生新样本 → 训练评价器 → 反馈训练生成器
- 外部可验证信号 → 评价器校准 → 开放任务反馈

**机制联系**

- 评价器学习与生成—验证共演 → 自生成数据与自训练：筛选 / 标注自生数据。学到的评价器可决定哪些生成样本进入下一轮训练。
- 评价器学习与生成—验证共演 → 自批评与 AI 偏好反馈：形成 AI 偏好。评价模型把开放式回答比较转为偏好训练信号。
- 自批评与 AI 偏好反馈 → 评价器学习与生成—验证共演：共同更新评价能力。生成与判断共享参数时，偏好训练可能同时改变二者；需实测判断能力。
- 可验证反馈与策略改进 → 评价器学习与生成—验证共演：校准评价器。结果可靠的任务为 learned critic / verifier 提供训练信号。
- 自生成数据与自训练 → 评价器学习与生成—验证共演：提供新判断样本。自生成候选及其选择结果构造新的 evaluator 训练材料。

**论文与团队（包括初筛与跨路线联系）**

- [Self-Rewarding LM](https://arxiv.org/html/2401.10020v1) · Meta / NYU。回答与 judge 共享模型；自生偏好用于逐轮 DPO。
- [Self-Taught Evaluators](https://arxiv.org/html/2408.02666v1) · Meta FAIR。合成判断与偏好训练 evaluator，再以新评价生成下一轮训练数据。
- [rStar-Math](https://arxiv.org/abs/2501.04519) · Microsoft Research Asia / Peking University / Tsinghua。搜索轨迹训练 policy 与 process preference model，结果验证约束反馈。
- [Self-Evolved Reward](https://arxiv.org/abs/2411.00418) · Fudan / Peking University / Microsoft。奖励模型用自生训练反馈迭代学习评价能力。
- [CoVerRL](https://arxiv.org/abs/2603.17775) · Zhejiang University / Baidu。同一模型交替生成与验证，通过验证缓解 self-consistency 错误。
- [RL Tango](https://arxiv.org/abs/2505.15034) · MIT / MIT–IBM Watson AI Lab。生成者与过程验证者交替训练，结果正确性提供外部评价锚点。
- [DeepSeekMath-V2](https://arxiv.org/html/2511.22570v1) · DeepSeek-AI。验证器、元验证与生成器迭代；轮间 rejection fine-tuning 融合能力。
- [Kimi K2](https://arxiv.org/html/2507.20534v1) · Moonshot AI（月之暗面）。RLVR 信号校准 K2 critic，rubric 评价开放任务；另有预训练 rephrasing，二者不是一个已证递归环。

### 任务生成与自博弈 · Task generation & self-play

模型如何持续遇到自己还不会、又可能学会的问题？

proposer、challenger 或 opponent 根据当前 solver 的表现改变任务或对手。这里区分生成新任务和从既有题库选任务，也区分共享模型与独立角色。

**研究子问题**

- Proposer–solver：出题者与求解者
- Adversarial self-play：攻防自博弈
- Environment-grounded task generation
- Learnability reward：可学习性反馈
- Diversity / novelty：覆盖与新颖性

**主要技术**

- 求解表现 → 出题 / 对手策略 → 新任务 → 求解学习 → 新表现

**机制联系**

- 任务生成与自博弈 → 课程与数据价值学习：生成能力边缘任务。出题策略改变训练候选池；课程策略再分配采样。
- 课程与数据价值学习 → 任务生成与自博弈：反馈难度与可学习性。求解者当前表现反馈给任务生成者，塑造下轮任务。
- 可验证反馈与策略改进 → 任务生成与自博弈：验证任务与解答。可执行环境同时检查自生任务是否合法、解答是否正确。
- 任务生成与自博弈 → 环境交互与长程经验学习：驱动新交互。AI 生成任务使执行者获得新的环境轨迹。

**论文与团队（包括初筛与跨路线联系）**

- [SIMA 2](https://arxiv.org/html/2512.04797v1) · Google DeepMind。AI 提供游戏任务与轨迹反馈，执行代理从交互经验学习；此映射不声称出题者同步训练。
- [GPT-Red](https://cdn.openai.com/pdf/gpt-red-automated-red-teaming-via-self-play-at-scale.pdf) · OpenAI。攻防模型相互提供训练压力；角色关系是 adversarial self-play。
- [Dr. Zero](https://arxiv.org/html/2601.07055v2) · Meta Superintelligence Labs / UIUC。搜索增强的 proposer / solver 共训，求解表现决定训练任务。
- [Agent0](https://arxiv.org/abs/2511.16043) · UNC / Google / Stanford / Recursive Superintelligence。课程代理与工具执行代理形成任务生成和求解反馈。
- [R-Zero](https://arxiv.org/abs/2508.05004) · Tencent AI Seattle / WashU / Maryland / UT Dallas。challenger 围绕 solver 能力边缘生成下一批任务。
- [Absolute Zero](https://arxiv.org/abs/2505.03335) · Tsinghua / BIGAI / Penn State。同一模型兼任 proposer / solver，执行器给 correctness，求解成功率给 learnability。
- [Tool-R0](https://arxiv.org/abs/2602.21320) · UIUC / ETH Zürich。工具任务生成与工具求解互相反馈；运行结果支持训练信号。
- [Agent-World](https://arxiv.org/abs/2604.18292) · RUC / ByteDance Seed。真实工具生态中构造可验证任务，按能力缺口产生后续训练经验。
- [AgentEvolver](https://arxiv.org/abs/2511.10395) · Alibaba Tongyi Lab。自提问生成任务，自导航重用经验，自归因分配训练反馈。

### 课程与数据价值学习 · Adaptive curriculum & data selection

有限训练预算应投入哪些任务、难度和能力缺口？

课程控制器根据学习者反馈调整采样分布；反馈可以是当前难度、预期学习增益或训练后的真实提升。困难、罕见、正确率低与有学习价值并不等价。

**研究子问题**

- Competence frontier：能力边界
- Learning-progress curriculum：学习进展课程
- Bandit curator：数据选择 bandit
- Difficulty / domain balancing
- Data valuation：样本的下游训练价值

**主要技术**

- 学习者表现 / advantage → 任务采样权重 → 新训练批次 → 更新学习者

**机制联系**

- 任务生成与自博弈 → 课程与数据价值学习：生成能力边缘任务。出题策略改变训练候选池；课程策略再分配采样。
- 课程与数据价值学习 → 任务生成与自博弈：反馈难度与可学习性。求解者当前表现反馈给任务生成者，塑造下轮任务。
- 环境交互与长程经验学习 → 课程与数据价值学习：从失败调整课程。失败与能力缺口改变下一批任务。
- 课程与数据价值学习 → 预训练中的 AI4AI：连接数据混合优化。按学习反馈选数据的思想也用于预训练数据配比；DoReMi 是机制参考，不列为当前大模型 RSI 主案例。

**论文与团队（包括初筛与跨路线联系）**

- [Dr. Zero](https://arxiv.org/html/2601.07055v2) · Meta Superintelligence Labs / UIUC。搜索增强的 proposer / solver 共训，求解表现决定训练任务。
- [Agent0](https://arxiv.org/abs/2511.16043) · UNC / Google / Stanford / Recursive Superintelligence。课程代理与工具执行代理形成任务生成和求解反馈。
- [R-Zero](https://arxiv.org/abs/2508.05004) · Tencent AI Seattle / WashU / Maryland / UT Dallas。challenger 围绕 solver 能力边缘生成下一批任务。
- [Absolute Zero](https://arxiv.org/abs/2505.03335) · Tsinghua / BIGAI / Penn State。同一模型兼任 proposer / solver，执行器给 correctness，求解成功率给 learnability。
- [WebRL](https://arxiv.org/abs/2411.02337) · Tsinghua / Zhipu AI。失败轨迹产生新课程，outcome reward 与在线 RL 更新网页行动策略。
- [Self-Evolving Curriculum](https://arxiv.org/abs/2505.14970) · Mila / Montréal / KAIST / Microsoft Research / HEC Montréal / ServiceNow AI。以 advantage-derived learning gain 更新非平稳 bandit 课程。
- [Actor-Curator](https://arxiv.org/abs/2602.20532) · UIC / Caltech / RPI / MBZUAI / UChicago / NEC Labs America。学习 neural curator，以预计策略提升而非单纯难度选题。
- [Agent-World](https://arxiv.org/abs/2604.18292) · RUC / ByteDance Seed。真实工具生态中构造可验证任务，按能力缺口产生后续训练经验。

### 环境交互与长程经验学习 · Interactive learning & experience reuse

多步工具行动的成功与失败，如何成为可迁移的策略能力？

在工具、网页、游戏或代码环境中生成轨迹，通过结果奖励、过程归因、示范筛选与回放训练行动策略。外部 memory 被写入并不等于模型参数学习，需分别标明。

**研究子问题**

- Agentic RL：工具与多步决策训练
- Trajectory credit assignment
- Experience replay / relabeling
- Simulated and real environments
- Harness coordination：学会使用外部状态
- Policy–world-model co-learning

**主要技术**

- 行动轨迹 → 环境结果 / 过程反馈 → 轨迹选择与归因 → 行动策略更新

**机制联系**

- 任务生成与自博弈 → 环境交互与长程经验学习：驱动新交互。AI 生成任务使执行者获得新的环境轨迹。
- 环境交互与长程经验学习 → 课程与数据价值学习：从失败调整课程。失败与能力缺口改变下一批任务。
- 环境交互与长程经验学习 → 可验证反馈与策略改进：产生执行结果。环境动作和程序执行产生可检验的状态变化与反馈。
- 环境交互与长程经验学习 → 自生成数据与自训练：回放 / 蒸馏有效经验。经反馈选择的交互经验可变为后续监督训练材料；与在线 RL 可组合。
- 学习如何改进学习者 → 环境交互与长程经验学习：训练经验整理策略。改进器把经历改写为 skills 或 harness，后续执行效果训练改进器。

**论文与团队（包括初筛与跨路线联系）**

- [EvoHarness-RL](https://arxiv.org/abs/2608.05446) · UIUC / Meta AI / Rutgers / Carnegie Mellon。SFT 与 cost-aware GRPO 训练外部 BPE 状态访问策略；不因名称含 harness 就当成学习更新器。
- [SIMA 2](https://arxiv.org/html/2512.04797v1) · Google DeepMind。AI 提供游戏任务与轨迹反馈，执行代理从交互经验学习；此映射不声称出题者同步训练。
- [Dr. Zero](https://arxiv.org/html/2601.07055v2) · Meta Superintelligence Labs / UIUC。搜索增强的 proposer / solver 共训，求解表现决定训练任务。
- [Agent0](https://arxiv.org/abs/2511.16043) · UNC / Google / Stanford / Recursive Superintelligence。课程代理与工具执行代理形成任务生成和求解反馈。
- [Tool-R0](https://arxiv.org/abs/2602.21320) · UIUC / ETH Zürich。工具任务生成与工具求解互相反馈；运行结果支持训练信号。
- [WebRL](https://arxiv.org/abs/2411.02337) · Tsinghua / Zhipu AI。失败轨迹产生新课程，outcome reward 与在线 RL 更新网页行动策略。
- [Agent-World](https://arxiv.org/abs/2604.18292) · RUC / ByteDance Seed。真实工具生态中构造可验证任务，按能力缺口产生后续训练经验。
- [SkillOS](https://arxiv.org/abs/2605.06614) · UIUC / Google Cloud AI Research / MIT。冻结执行者，训练 skill curator；较晚关联任务评价早先 SkillRepo 更新。
- [AgentEvolver](https://arxiv.org/abs/2511.10395) · Alibaba Tongyi Lab。自提问生成任务，自导航重用经验，自归因分配训练反馈。
- [Teaching LLMs to Self-Evolve](https://arxiv.org/abs/2607.21971) · UIUC。用执行反馈训练多轮程序修订；meta-skills 不等于学习优化器。
- [SEED Distillation](https://arxiv.org/html/2607.14777v1) · Tsinghua / Zhejiang University / CUHK / NTU / Tongji。同一策略承担 actor 与训练期 analyzer；从自身轨迹提炼 hindsight skills，形成 on-policy distillation 与 RL 信号。部署时移除 analyzer，保留更新后的策略模型。
- [WebEvolver](https://arxiv.org/html/2504.21024v2) · Tencent AI Lab。策略 LLM 与 world-model LLM 从交互轨迹中共同训练；世界模型提供合成经验与前瞻规划。可变对象是两类模型的参数。
- [INTELLECT-3 / PRIME-RL](https://www.primeintellect.ai/blog/intellect-3) · Prime Intellect。以合成数据、可验证环境和异步 RL 训练 106B MoE，公开训练框架、环境与模型。

### 学习如何改进学习者 · Learning to adapt & learned improvement policies

如何训练一个真正提高后续学习或执行效果的改进器？

内层执行数据学习、奖励学习、技能整理或 harness 修改，外层用内层之后的表现训练改进策略。下游提升是反馈对象；一般的反思提示或多轮代码修订并不自动属于 meta-learning。

**研究子问题**

- Bilevel optimization：内外层学习
- Synthetic-data generator training
- Learned self-edit：学习数据 / 更新指令
- Reward designer training
- Skill / harness curator training

**主要技术**

- 改进器提出更新 → 内层学习或执行 → 下游效果 → 外层改进器训练

**机制联系**

- 学习如何改进学习者 → 自生成数据与自训练：优化训练材料。外层按内层学习收益训练数据 / 自编辑生成策略。
- 学习如何改进学习者 → 环境交互与长程经验学习：训练经验整理策略。改进器把经历改写为 skills 或 harness，后续执行效果训练改进器。
- 持续学习与测试时适应 → 学习如何改进学习者：把更新策略用于新任务。学习如何 self-edit 可用于部署时知识吸收；长期保留仍需单独解决。
- 学习如何改进学习者 → 预训练中的 AI4AI：研究预训练改进器。把训练收益用作数据生成器或更新规则的外层目标是研究方向；此处没有据此声称现有目录已经实现前沿预训练 RSI。

**论文与团队（包括初筛与跨路线联系）**

- [SEAL](https://arxiv.org/html/2506.10943v1) · MIT · Improbable AI Lab / CSAIL。学习自编辑数据 / 更新指令，并用内层适应效果训练编辑策略。
- [DERL](https://arxiv.org/html/2512.13399v3) · Waterloo / HKU / CUHK-Shenzhen / Duke。奖励程序设计者通过内层策略训练后的验证效果更新。
- [Harness-R1](https://arxiv.org/abs/2608.02276) · SJTU / Xiaohongshu / Southeast University。训练 harness 编辑模型，用目标 agent 重跑后的成功评价编辑效果；与 Hybrid 关联。
- [SkillOS](https://arxiv.org/abs/2605.06614) · UIUC / Google Cloud AI Research / MIT。冻结执行者，训练 skill curator；较晚关联任务评价早先 SkillRepo 更新。

### 持续学习与测试时适应 · Continual learning & test-time adaptation

模型如何在新任务上学习，同时保留旧能力？

把上述学习机制放到任务流和部署阶段：何时写入参数、哪些参数可变、何时重置，以及新知识如何长期保留。它是跨机制研究主题，不与 SFT、RL 或 self-play 构成互斥分类。

**研究子问题**

- Test-time training / RL
- Streaming adaptation：任务流适应
- Retention / interference：保留与干扰
- Parameter-efficient adaptation：LoRA 等
- Reset / consolidation：重置与长期保留

**主要技术**

- 新任务 → 局部适应 → 新任务效果与旧任务保留 → 下一次适应

**机制联系**

- 持续学习与测试时适应 → 学习如何改进学习者：把更新策略用于新任务。学习如何 self-edit 可用于部署时知识吸收；长期保留仍需单独解决。
- 可验证反馈与策略改进 → 持续学习与测试时适应：支持测试时参数学习。测试时的可验证尝试可回流参数，而不只增加搜索量。

**论文与团队（包括初筛与跨路线联系）**

- [SEAL](https://arxiv.org/html/2506.10943v1) · MIT · Improbable AI Lab / CSAIL。学习自编辑数据 / 更新指令，并用内层适应效果训练编辑策略。
- [AlphaProof](https://www.nature.com/articles/s41586-025-09833-y) · Google DeepMind。Lean 验证搜索经验，训练证明网络并做 test-time RL。

### 预训练中的 AI4AI · AI-assisted pretraining

AI 能否改善基础模型的数据、训练规则与训练效率？

AI 改写语料、选择数据混合、设计损失 / 优化器或改进训练代码，均可能帮助预训练；只有训练结果进一步改进这些 AI 组件并形成继承关系，才出现相应的自改进闭环。

**研究子问题**

- Synthetic / rephrased corpora
- Data mixture optimization
- Curriculum for pretraining
- Learned optimizer / objective search
- Training systems co-design

**主要技术**

- AI 处理数据 / 训练方案 → 基础模型训练 → 训练收益反馈；是否回流 AI 改进器需单独核实

**机制联系**

- 预训练中的 AI4AI → 自生成数据与自训练：扩展训练材料。AI 合成 / 改写语料可以进入预训练；这条使用关系不证明训练反馈反向改进生成器。
- 课程与数据价值学习 → 预训练中的 AI4AI：连接数据混合优化。按学习反馈选数据的思想也用于预训练数据配比；DoReMi 是机制参考，不列为当前大模型 RSI 主案例。
- 学习如何改进学习者 → 预训练中的 AI4AI：研究预训练改进器。把训练收益用作数据生成器或更新规则的外层目标是研究方向；此处没有据此声称现有目录已经实现前沿预训练 RSI。

**论文与团队（包括初筛与跨路线联系）**

- [Kimi K2](https://arxiv.org/html/2507.20534v1) · Moonshot AI（月之暗面）。RLVR 信号校准 K2 critic，rubric 评价开放任务；另有预训练 rephrasing，二者不是一个已证递归环。
- [OPHIS](https://meta-circle.com/blog/ophis-a-new-paradigm-for-autoresearch) · MetaCircle。以训练内部观测提出假设和干预，再用重复训练结果决定下一步研究。
- [Apex-Tune](https://www.apexin.ai/assets/papers/what-happens-when-ai-starts-improving-ai.pdf) · Apex Intelligence。自动提出并验证 scaling law、训练实现和 GPU kernel 的改进，以实验结果继续搜索。

### 持续研究的问题

- **谁能可靠地评价新的能力？** 当生成器超出现有评审能力时，如何获得仍然相关、可扩展、不会与生成器共同偏移的训练信号？ 更强的自生数据只有在反馈能辨别质量时才改变学习上限。
- **什么样的自生任务真正增加能力覆盖？** 怎样同时优化 learnability、diversity 与跨分布迁移，使课程走向新能力而非在窄题型中重复提高分数？ 当前成功率与即时 advantage 只是训练价值代理；出题、选题与学习者相互适应可能产生局部循环。
- **一次适应如何成为持续保留的能力？** 如何在长期任务流中选择更新时机和参数范围，让新能力可迁移、旧能力被保留，并使更新收益覆盖训练代价？ SEAL 的逐次自编辑实验仍出现遗忘；单任务 test-time 提升不能直接说明长期积累。

## Model × Harness

Model指系统内所有被学习的参数，包括策略、reward model、world model与controller。Harness指参数之外可保留、可执行或可配置的组织结构与状态，包括工作流、tools、skills、记忆、环境包装和训练程序。Hybrid要求同时说明参数与外部系统的实际更新对象；强一些的协同进化还要说明两类更新怎样相互影响并跨轮复用。

模型参数和外部系统同时变化时，经验如何进入参数，更新后的模型又如何改变下一轮学习与执行的组织方式？

模型在 harness 中执行，形成轨迹与任务反馈。反馈可以同时用于参数学习和外部系统修改；更新后的模型是否继续参与系统设计，需要逐篇追踪。循环结构是阅读索引。每篇论文只高亮它实际实现的边；其余边保持空白。

### 工作流与策略共同适配 · Workflow–Policy Co-adaptation

模型行为改变以后，原来有效的规划、工具调用和错误恢复流程还有效吗？

将模型参数与外部工作流作为相互依赖的更新对象：先改变工作流会改变轨迹分布；随后训练模型又会改变该工作流的适用条件。研究对象是这种双向适配。

**研究子问题**

- 规划与执行分工
- 工具调用与错误恢复
- 模型—工作流分布匹配
- 交替更新与联合目标

**主要技术**

- harness evolution
- failure attribution
- alternating optimization
- on-policy expert correction

**机制联系**

- 工作流与策略共同适配 → 外部经验进入参数：生成学习轨迹。工作流改变模型经历的状态和行动，将新的执行经验提供给参数学习。
- 外部经验进入参数 → 工作流与策略共同适配：改变适配条件。训练可改变规划风格与能力，原harness不一定继续匹配新模型。
- 模型能力用于系统改写 → 工作流与策略共同适配：改写执行流程。模型提出并筛选新的角色、指令、工具流程和修复策略。
- 组织结构与角色能力共同学习 → 工作流与策略共同适配：规定分工与路由。角色分工和通信拓扑成为工作流可优化的内容。
- 部署变化与再适配 → 工作流与策略共同适配：暴露兼容性变化。接口、工具或模型版本变化会使既有工作流失配，从而要求重新适配。

**论文与团队（包括初筛与跨路线联系）**

- [SIA](https://github.com/hexo-ai/sia) · Hexo Labs / University of Oxford。反馈代理同时修改目标agent scaffold并训练其LoRA；主实验更新目标agent，未说明反馈代理自身权重随代更新。
- [Co-Harness](https://arxiv.org/abs/2607.22688) · Meituan / Ai2 / Independent。HarnessCritic修订外部系统后，用成功轨迹SFT；原文报告两轮。两轮结果不代表无限持续改善。
- [MASS](https://arxiv.org/html/2610.12176v1) · Sakana AI / UC Berkeley。优化的是文本形式的多agent工作流；底层coding harness、工具和记忆固定。共享模型经SFT后再次承担执行、优化和评价角色；报告两轮。
- [Harness-Zero](https://arxiv.org/abs/2609.24974) · Peking University / Google / HKUST。先演化harness，再由harnessing agent在学生动作空间生成干预轨迹并SFT；支持H→M内化，未直接展示更新学生继续演化H的反复闭环。
- [On-policy Co-evolution](https://arxiv.org/html/2609.09134v1) · Salesforce AI。对进化后harness做学生访问状态上的局部纠错与LoRA-SFT；主要实证是一次顺序适配，循环接续是提出的方向。on-policy描述采样状态，不代表训练算法为RL。
- [TaoLive HAT](https://arxiv.org/abs/2608.15763) · TaoLive AIGC LLM Team。harness-state augmentation使模型适应skills/tool schemas/prompts/hooks变体；这是训练鲁棒性与部署适配，不证明AI自动演化harness。

### 外部经验进入参数 · Harness-to-Model Internalization

外部流程带来的行为能力，怎样转化为模型在简化或不同harness下仍能使用的能力？

从外部工具、工作流、技能或教师干预获得训练轨迹与学习信号，通过SFT、RL或蒸馏更新模型。仅有这条单向传递，还不等于反复的双向共演。

**研究子问题**

- 成功轨迹筛选与SFT
- 局部纠错与on-policy监督
- 技能条件自蒸馏
- 复杂harness向目标动作空间编译
- 外部支持移除后的能力保持

**主要技术**

- trajectory distillation
- behavioral internalization
- on-policy distillation
- agent-as-harness

**机制联系**

- 工作流与策略共同适配 → 外部经验进入参数：生成学习轨迹。工作流改变模型经历的状态和行动，将新的执行经验提供给参数学习。
- 外部经验进入参数 → 工作流与策略共同适配：改变适配条件。训练可改变规划风格与能力，原harness不一定继续匹配新模型。
- 外部经验进入参数 → 模型能力用于系统改写：更新后重新设计。更新模型再次承担改进器角色，检验任务学习是否迁移为系统设计能力。
- 技能、记忆与策略共演 → 外部经验进入参数：技能引导学习。可检索技能影响rollout与监督，使经验转化为策略学习信号。
- 外部经验进入参数 → 技能、记忆与策略共演：产生新的能力缺口。更新后的策略产生新成败轨迹，暴露技能库或记忆操作尚未覆盖的情况。
- 任务、环境与学习共同变化 → 外部经验进入参数：决定训练分布。环境与课程的改变决定模型采样到哪些状态、动作和反馈。
- 奖励、评价与策略互相影响 → 外部经验进入参数：筛选、赋分与纠错。评价结果决定保留哪些轨迹、怎样构造奖励或训练目标。
- 外部经验进入参数 → 奖励、评价与策略互相影响：改变评价器所见轨迹。策略更新改变评价器的训练样本；评价器需要适应新的错误与成功分布。
- 训练器与学习系统共同优化 → 外部经验进入参数：实施参数更新。训练系统决定如何把经验变为梯度更新，以及哪些模型版本继续保留。
- 组织结构与角色能力共同学习 → 外部经验进入参数：提供多角色监督。局部执行轨迹与编排轨迹训练同一模型或不同角色策略。
- 外部经验进入参数 → 部署变化与再适配：改变所需外部支持。被内化的行为可能降低复杂harness依赖，但必须在目标部署接口下检验。
- 部署变化与再适配 → 外部经验进入参数：提供适配训练分布。训练覆盖不同harness状态或当前学生实际访问状态，以学习稳健行为。

**论文与团队（包括初筛与跨路线联系）**

- [Co-Harness](https://arxiv.org/abs/2607.22688) · Meituan / Ai2 / Independent。HarnessCritic修订外部系统后，用成功轨迹SFT；原文报告两轮。两轮结果不代表无限持续改善。
- [Frontis-MA1 / OpenMLE](https://arxiv.org/html/2607.28568v1) · Horizon Research / Frontis.AI / 清华大学。研发操作经过SFT/RL，部署执行长程ML搜索；主要改外部ML解法，系统本身固定。不能按“训练模型+有harness”认定协同RSI。
- [MASS](https://arxiv.org/html/2610.12176v1) · Sakana AI / UC Berkeley。优化的是文本形式的多agent工作流；底层coding harness、工具和记忆固定。共享模型经SFT后再次承担执行、优化和评价角色；报告两轮。
- [RLAnything](https://arxiv.org/html/2602.02488v1) · Yinjie Wang · Tianbao Xie · Ke Shen · Mengdi Wang · Ling Yang（作者；机构待核）。同时训练策略和奖励模型，依据错误模式改写外部任务；Hybrid归属来自任务侧变化，并非来自“有两个模型”。
- [Harness-Zero](https://arxiv.org/abs/2609.24974) · Peking University / Google / HKUST。先演化harness，再由harnessing agent在学生动作空间生成干预轨迹并SFT；支持H→M内化，未直接展示更新学生继续演化H的反复闭环。
- [SkillRL](https://arxiv.org/html/2602.08234v1) · UNC / UChicago / UCSD / NEC Labs / Berkeley / UCSC。外部SkillBank与策略GRPO共同更新，teacher负责技能提炼且非被训练主体。训练主体7B，属于机制补充。
- [MemSkill](https://arxiv.org/html/2602.02474v1) · NTU / UIUC / UIC / Tsinghua。训练对象是轻量MLP技能选择controller（PPO，精确参数量未报告）；Qwen3-Embedding-0.6B作shared encoder，LLaMA70B与Qwen80B通过API使用，executor/designer固定。不得将70B/80B当作被训练模型。
- [EvoDS](https://arxiv.org/abs/2606.03841) · HKUST。共享骨干的多角色策略经过SFT和online RL，产生并复用可执行技能；组织架构本身固定，不应把多角色训练说成拓扑演化。
- [On-policy Co-evolution](https://arxiv.org/html/2609.09134v1) · Salesforce AI。对进化后harness做学生访问状态上的局部纠错与LoRA-SFT；主要实证是一次顺序适配，循环接续是提出的方向。on-policy描述采样状态，不代表训练算法为RL。
- [TaoLive HAT](https://arxiv.org/abs/2608.15763) · TaoLive AIGC LLM Team。harness-state augmentation使模型适应skills/tool schemas/prompts/hooks变体；这是训练鲁棒性与部署适配，不证明AI自动演化harness。
- [WebEvolver](https://arxiv.org/html/2504.21024v2) · Tencent AI Lab。跨路线机制联系。同时改多个模型仍是参数侧共学；已读方法没有非参数工作流/工具/环境包装被优化。 策略 LLM 与 world-model LLM 从交互轨迹中共同训练；世界模型提供合成经验与前瞻规划。可变对象是两类模型的参数。
- [EnvHarness](https://arxiv.org/abs/2608.19880) · WashU / Google Cloud AI Research / Google Cloud / UNC。EnvRigger根据失败生成环境wrapper，原环境底层和verifier冻结；再用重塑环境训练policy。是否跨多代反复重建wrapper应依据训练流程逐项说明。
- [Socratic-SWE](https://arxiv.org/abs/2606.07412) · Alibaba AI Data / SJTU。从软件求解轨迹提炼技能并生成新任务训练求解者；是否有跨轮持久可调用技能库及其明确更新边界，需方法全文确认。
- [SEED Distillation](https://arxiv.org/html/2607.14777v1) · Tsinghua / Zhejiang University / CUHK / NTU / Tongji。跨路线机制联系。明确更新模型参数；未显示持久非参数harness共同演化。 同一策略承担 actor 与训练期 analyzer；从自身轨迹提炼 hindsight skills，形成 on-policy distillation 与 RL 信号。部署时移除 analyzer，保留更新后的策略模型。

### 模型能力用于系统改写 · Model-to-Harness Design

更新后的模型能否提出更有用的工具、技能、工作流和训练干预？

模型以设计者或改进器身份生成外部系统的修改；反馈筛选后的修改影响后续执行或学习。模型行为变强本身，不自动证明其系统设计能力也变强。

**研究子问题**

- 工作流与通信结构生成
- 工具与技能程序合成
- 环境包装与任务设计
- 训练程序与诊断工具修订
- 改进器在下一轮复用

**主要技术**

- program synthesis
- workflow search
- feedback-conditioned editing
- improver reuse

**机制联系**

- 外部经验进入参数 → 模型能力用于系统改写：更新后重新设计。更新模型再次承担改进器角色，检验任务学习是否迁移为系统设计能力。
- 模型能力用于系统改写 → 工作流与策略共同适配：改写执行流程。模型提出并筛选新的角色、指令、工具流程和修复策略。
- 模型能力用于系统改写 → 任务、环境与学习共同变化：生成任务和包装。设计者根据失败轨迹生成课程或环境包装，改变可获得的训练经验。
- 模型能力用于系统改写 → 训练器与学习系统共同优化：设计训练干预。研究模型产生可执行训练程序、诊断工具和配方修改。

**论文与团队（包括初筛与跨路线联系）**

- [SIA](https://github.com/hexo-ai/sia) · Hexo Labs / University of Oxford。反馈代理同时修改目标agent scaffold并训练其LoRA；主实验更新目标agent，未说明反馈代理自身权重随代更新。
- [Co-Harness](https://arxiv.org/abs/2607.22688) · Meituan / Ai2 / Independent。HarnessCritic修订外部系统后，用成功轨迹SFT；原文报告两轮。两轮结果不代表无限持续改善。
- [MASS](https://arxiv.org/html/2610.12176v1) · Sakana AI / UC Berkeley。优化的是文本形式的多agent工作流；底层coding harness、工具和记忆固定。共享模型经SFT后再次承担执行、优化和评价角色；报告两轮。
- [Eureka](https://arxiv.org/abs/2310.12931) · NVIDIA / UPenn / Caltech / UT Austin。奖励程序与机器人策略更新；奖励设计LLM冻结。它是AI设计学习信号的参考，不能当LLM研究者自身参数递归升级。
- [Automated Alignment Researchers](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures) · Anthropic。研究代理提出干预并训练外部目标模型；目标改善没有直接证明研究代理自身学习或自改。
- [Seed for Seed](https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity) · ByteDance Seed。官方描述AI参与数据、算法和工程开发；尚无统一公开的自我递归协议可从介绍推定。
- [Skill Self-Play](https://arxiv.org/html/2607.22529v1) · Alibaba Qwen / CUHK / RUC / SYSU / PKU / ETH / UZH / Buffalo。技能保存任务生成与验证结构，出题/求解策略与技能内容共同变化；实际训练规模单列，不以教师规模替代。
- [EvoTrainer](https://arxiv.org/html/2606.03108v2) · Alibaba Tongyi Lab / SIAT-CAS / SUAT。训练侧诊断工具/流程与目标策略版本共同改进；训练者LLM为固定Sonnet，昂贵执行有人类把关。不能描述成训练者权重自进化。
- [Execution-Grounded Research](https://arxiv.org/abs/2601.14525) · Stanford。执行候选AI研究方案并反馈构思者；训练构思模型与改进目标模型须分开计，不把外部训练目标当成其自身后继。
- [SkillRL](https://arxiv.org/html/2602.08234v1) · UNC / UChicago / UCSD / NEC Labs / Berkeley / UCSC。外部SkillBank与策略GRPO共同更新，teacher负责技能提炼且非被训练主体。训练主体7B，属于机制补充。
- [MemSkill](https://arxiv.org/html/2602.02474v1) · NTU / UIUC / UIC / Tsinghua。训练对象是轻量MLP技能选择controller（PPO，精确参数量未报告）；Qwen3-Embedding-0.6B作shared encoder，LLaMA70B与Qwen80B通过API使用，executor/designer固定。不得将70B/80B当作被训练模型。
- [EvoDS](https://arxiv.org/abs/2606.03841) · HKUST。共享骨干的多角色策略经过SFT和online RL，产生并复用可执行技能；组织架构本身固定，不应把多角色训练说成拓扑演化。
- [RewardHarness](https://arxiv.org/html/2605.08703v1) · UBC / Vector / Kuaishou Kolors / Etude AI / Waterloo / Carnegie Mellon / Tsinghua / Georgia Tech。跨路线机制联系。主贡献是评价Harness演化；下游训练提供跨路线联系，未建立更新目标反向改进奖励系统的闭环。 冻结视觉语言模型，通过偏好误差改进 reward agent 的技能和工具；该评价系统随后用于外部图像编辑模型的 GRPO 训练。
- [EnvHarness](https://arxiv.org/abs/2608.19880) · WashU / Google Cloud AI Research / Google Cloud / UNC。EnvRigger根据失败生成环境wrapper，原环境底层和verifier冻结；再用重塑环境训练policy。是否跨多代反复重建wrapper应依据训练流程逐项说明。
- [AIRA-Compose / Design](https://arxiv.org/abs/2605.15871) · Meta FAIR / Oxford。研究代理搜索架构/计算原语，候选扩展到外部目标预训练；没有据此证明目标模型回到下一代研究者角色。

### 技能、记忆与策略共演 · Skill–Memory–Policy Co-evolution

哪些经验留在外部技能/记忆库，哪些写入参数；二者如何协作？

外部技能或记忆操作持续增删、修订，同时训练使用这些资产的策略或控制器。技能内容变化与技能使用能力变化必须分别说明。

**研究子问题**

- 可执行技能与自然语言技能
- 技能检索及调用策略
- 记忆写入/更新/删除策略
- 经验抽象与适用条件
- 外部库扩展与参数学习

**主要技术**

- skill discovery
- skill-conditioned RL
- memory controller learning
- hard-case-driven skill revision

**机制联系**

- 技能、记忆与策略共演 → 外部经验进入参数：技能引导学习。可检索技能影响rollout与监督，使经验转化为策略学习信号。
- 外部经验进入参数 → 技能、记忆与策略共演：产生新的能力缺口。更新后的策略产生新成败轨迹，暴露技能库或记忆操作尚未覆盖的情况。
- 技能、记忆与策略共演 → 训练器与学习系统共同优化：复用研究经验。训练诊断和失效经验沉淀成可调用技能，影响后续训练干预。

**论文与团队（包括初筛与跨路线联系）**

- [Skill Self-Play](https://arxiv.org/html/2607.22529v1) · Alibaba Qwen / CUHK / RUC / SYSU / PKU / ETH / UZH / Buffalo。技能保存任务生成与验证结构，出题/求解策略与技能内容共同变化；实际训练规模单列，不以教师规模替代。
- [EvoTrainer](https://arxiv.org/html/2606.03108v2) · Alibaba Tongyi Lab / SIAT-CAS / SUAT。训练侧诊断工具/流程与目标策略版本共同改进；训练者LLM为固定Sonnet，昂贵执行有人类把关。不能描述成训练者权重自进化。
- [AutoScientists](https://arxiv.org/abs/2605.28655) · Harvard。研究团队共享实验知识并搜索外部目标训练方案；需要单独验证团队系统本身是否更新。
- [SkillRL](https://arxiv.org/html/2602.08234v1) · UNC / UChicago / UCSD / NEC Labs / Berkeley / UCSC。外部SkillBank与策略GRPO共同更新，teacher负责技能提炼且非被训练主体。训练主体7B，属于机制补充。
- [MemSkill](https://arxiv.org/html/2602.02474v1) · NTU / UIUC / UIC / Tsinghua。训练对象是轻量MLP技能选择controller（PPO，精确参数量未报告）；Qwen3-Embedding-0.6B作shared encoder，LLaMA70B与Qwen80B通过API使用，executor/designer固定。不得将70B/80B当作被训练模型。
- [EvoDS](https://arxiv.org/abs/2606.03841) · HKUST。共享骨干的多角色策略经过SFT和online RL，产生并复用可执行技能；组织架构本身固定，不应把多角色训练说成拓扑演化。
- [RewardHarness](https://arxiv.org/html/2605.08703v1) · UBC / Vector / Kuaishou Kolors / Etude AI / Waterloo / Carnegie Mellon / Tsinghua / Georgia Tech。跨路线机制联系。主贡献是评价Harness演化；下游训练提供跨路线联系，未建立更新目标反向改进奖励系统的闭环。 冻结视觉语言模型，通过偏好误差改进 reward agent 的技能和工具；该评价系统随后用于外部图像编辑模型的 GRPO 训练。
- [Socratic-SWE](https://arxiv.org/abs/2606.07412) · Alibaba AI Data / SJTU。从软件求解轨迹提炼技能并生成新任务训练求解者；是否有跨轮持久可调用技能库及其明确更新边界，需方法全文确认。
- [SEED Distillation](https://arxiv.org/html/2607.14777v1) · Tsinghua / Zhejiang University / CUHK / NTU / Tongji。跨路线机制联系。明确更新模型参数；未显示持久非参数harness共同演化。 同一策略承担 actor 与训练期 analyzer；从自身轨迹提炼 hindsight skills，形成 on-policy distillation 与 RL 信号。部署时移除 analyzer，保留更新后的策略模型。

### 任务、环境与学习共同变化 · Environment–Curriculum Co-adaptation

训练任务怎样随当前能力和失败类型改变，同时保留可验证的任务语义？

策略表现影响任务生成、难度或环境接口；这些改变再塑造策略可获得的经验。可学习世界模型提供模拟经验，但仅更新世界模型权重不等于修改harness。

**研究子问题**

- 自动课程与能力边界
- 任务生成及验证
- 环境Stage/Contract/Chain
- 真实交互与世界模型模拟
- 探索分布与学习价值

**主要技术**

- automatic curriculum
- task generation
- environment wrappers
- world-model rollouts

**机制联系**

- 模型能力用于系统改写 → 任务、环境与学习共同变化：生成任务和包装。设计者根据失败轨迹生成课程或环境包装，改变可获得的训练经验。
- 任务、环境与学习共同变化 → 外部经验进入参数：决定训练分布。环境与课程的改变决定模型采样到哪些状态、动作和反馈。
- 任务、环境与学习共同变化 → 奖励、评价与策略互相影响：改变反馈可学习性。任务过难或过易会改变成功/失败样本平衡，进而影响评价器训练。

**论文与团队（包括初筛与跨路线联系）**

- [RSI-Anything](https://github.com/Gen-Verse/RSI-Anything) · Gen-Verse（项目团队；机构未核准）。官方仓库给出预测—交互—反馈—保留循环。不同领域更新对象可能不同，需逐域核实是否同时改参数与非参数系统。
- [Eureka](https://arxiv.org/abs/2310.12931) · NVIDIA / UPenn / Caltech / UT Austin。奖励程序与机器人策略更新；奖励设计LLM冻结。它是AI设计学习信号的参考，不能当LLM研究者自身参数递归升级。
- [Skill Self-Play](https://arxiv.org/html/2607.22529v1) · Alibaba Qwen / CUHK / RUC / SYSU / PKU / ETH / UZH / Buffalo。技能保存任务生成与验证结构，出题/求解策略与技能内容共同变化；实际训练规模单列，不以教师规模替代。
- [RLAnything](https://arxiv.org/html/2602.02488v1) · Yinjie Wang · Tianbao Xie · Ke Shen · Mengdi Wang · Ling Yang（作者；机构待核）。同时训练策略和奖励模型，依据错误模式改写外部任务；Hybrid归属来自任务侧变化，并非来自“有两个模型”。
- [WebEvolver](https://arxiv.org/html/2504.21024v2) · Tencent AI Lab。跨路线机制联系。同时改多个模型仍是参数侧共学；已读方法没有非参数工作流/工具/环境包装被优化。 策略 LLM 与 world-model LLM 从交互轨迹中共同训练；世界模型提供合成经验与前瞻规划。可变对象是两类模型的参数。
- [EnvHarness](https://arxiv.org/abs/2608.19880) · WashU / Google Cloud AI Research / Google Cloud / UNC。EnvRigger根据失败生成环境wrapper，原环境底层和verifier冻结；再用重塑环境训练policy。是否跨多代反复重建wrapper应依据训练流程逐项说明。
- [Socratic-SWE](https://arxiv.org/abs/2606.07412) · Alibaba AI Data / SJTU。从软件求解轨迹提炼技能并生成新任务训练求解者；是否有跨轮持久可调用技能库及其明确更新边界，需方法全文确认。
- [INTELLECT-3 / PRIME-RL](https://www.primeintellect.ai/blog/intellect-3) · Prime Intellect。以合成数据、可验证环境和异步 RL 训练 106B MoE，公开训练框架、环境与模型。

### 奖励、评价与策略互相影响 · Reward–Evaluator–Policy Coupling

评价器怎样跟随策略变化而改进，同时避免把自身偏差当作进步？

策略轨迹提供评价器学习或诊断材料，评价信号又决定样本选择与参数更新。权重型reward model与外部tool/skill型评价器是两种不同载体。

**研究子问题**

- 过程奖励与结果奖励
- reward-model更新
- 可演化的评价工具和skills
- 偏好示例与环境真值
- 策略—评价器分布变化

**主要技术**

- reward-model co-training
- process supervision
- self-evolving reward harness
- external outcome feedback

**机制联系**

- 奖励、评价与策略互相影响 → 外部经验进入参数：筛选、赋分与纠错。评价结果决定保留哪些轨迹、怎样构造奖励或训练目标。
- 外部经验进入参数 → 奖励、评价与策略互相影响：改变评价器所见轨迹。策略更新改变评价器的训练样本；评价器需要适应新的错误与成功分布。
- 任务、环境与学习共同变化 → 奖励、评价与策略互相影响：改变反馈可学习性。任务过难或过易会改变成功/失败样本平衡，进而影响评价器训练。
- 奖励、评价与策略互相影响 → 训练器与学习系统共同优化：触发训练诊断。分数与实际行为的差异可以触发奖励、数据过滤或训练诊断工具修改。

**论文与团队（包括初筛与跨路线联系）**

- [MASS](https://arxiv.org/html/2610.12176v1) · Sakana AI / UC Berkeley。优化的是文本形式的多agent工作流；底层coding harness、工具和记忆固定。共享模型经SFT后再次承担执行、优化和评价角色；报告两轮。
- [RSI-Anything](https://github.com/Gen-Verse/RSI-Anything) · Gen-Verse（项目团队；机构未核准）。官方仓库给出预测—交互—反馈—保留循环。不同领域更新对象可能不同，需逐域核实是否同时改参数与非参数系统。
- [Eureka](https://arxiv.org/abs/2310.12931) · NVIDIA / UPenn / Caltech / UT Austin。奖励程序与机器人策略更新；奖励设计LLM冻结。它是AI设计学习信号的参考，不能当LLM研究者自身参数递归升级。
- [Automated Alignment Researchers](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures) · Anthropic。研究代理提出干预并训练外部目标模型；目标改善没有直接证明研究代理自身学习或自改。
- [RLAnything](https://arxiv.org/html/2602.02488v1) · Yinjie Wang · Tianbao Xie · Ke Shen · Mengdi Wang · Ling Yang（作者；机构待核）。同时训练策略和奖励模型，依据错误模式改写外部任务；Hybrid归属来自任务侧变化，并非来自“有两个模型”。
- [EvoTrainer](https://arxiv.org/html/2606.03108v2) · Alibaba Tongyi Lab / SIAT-CAS / SUAT。训练侧诊断工具/流程与目标策略版本共同改进；训练者LLM为固定Sonnet，昂贵执行有人类把关。不能描述成训练者权重自进化。
- [Execution-Grounded Research](https://arxiv.org/abs/2601.14525) · Stanford。执行候选AI研究方案并反馈构思者；训练构思模型与改进目标模型须分开计，不把外部训练目标当成其自身后继。
- [RewardHarness](https://arxiv.org/html/2605.08703v1) · UBC / Vector / Kuaishou Kolors / Etude AI / Waterloo / Carnegie Mellon / Tsinghua / Georgia Tech。跨路线机制联系。主贡献是评价Harness演化；下游训练提供跨路线联系，未建立更新目标反向改进奖励系统的闭环。 冻结视觉语言模型，通过偏好误差改进 reward agent 的技能和工具；该评价系统随后用于外部图像编辑模型的 GRPO 训练。
- [SEED Distillation](https://arxiv.org/html/2607.14777v1) · Tsinghua / Zhejiang University / CUHK / NTU / Tongji。跨路线机制联系。明确更新模型参数；未显示持久非参数harness共同演化。 同一策略承担 actor 与训练期 analyzer；从自身轨迹提炼 hindsight skills，形成 on-policy distillation 与 RL 信号。部署时移除 analyzer，保留更新后的策略模型。
- [OPHIS](https://meta-circle.com/blog/ophis-a-new-paradigm-for-autoresearch) · MetaCircle。以训练内部观测提出假设和干预，再用重复训练结果决定下一步研究。
- [ASI-Bench](https://arxiv.org/abs/2608.17271) · Tsinghua / University of Michigan / MIT / Harvard / Carnegie Mellon / UIUC / Boston University / University of Queensland / USTC / Flatiron Institute / Microsoft Research / AG2 AI / Independent Researchers。在相同科研任务上逐步撤去方法指导，区分按步骤执行和自主选择科研方法的能力。

### 训练器与学习系统共同优化 · Training-Harness Co-evolution

怎样让模型训练的改进过程本身学会更好地诊断、选择和执行下一次训练？

目标策略训练产生的结果，反过来用于改写训练程序、数据处理、奖励配方、诊断工具与研究记忆。固定研究LLM驱动目标模型训练属于AI4AI；只有说明哪部分研究系统被保留和改写，才可讨论其自身演化。

**研究子问题**

- 训练配方与优化器
- 样本过滤与rollout调度
- 奖励形状与训练目标
- 诊断工具及训练记忆
- 实验分支选择、合并与复用

**主要技术**

- training-program search
- optimizer/recipe design
- training diagnostics
- versioned interventions

**机制联系**

- 奖励、评价与策略互相影响 → 训练器与学习系统共同优化：触发训练诊断。分数与实际行为的差异可以触发奖励、数据过滤或训练诊断工具修改。
- 模型能力用于系统改写 → 训练器与学习系统共同优化：设计训练干预。研究模型产生可执行训练程序、诊断工具和配方修改。
- 训练器与学习系统共同优化 → 外部经验进入参数：实施参数更新。训练系统决定如何把经验变为梯度更新，以及哪些模型版本继续保留。
- 技能、记忆与策略共演 → 训练器与学习系统共同优化：复用研究经验。训练诊断和失效经验沉淀成可调用技能，影响后续训练干预。

**论文与团队（包括初筛与跨路线联系）**

- [SIA](https://github.com/hexo-ai/sia) · Hexo Labs / University of Oxford。反馈代理同时修改目标agent scaffold并训练其LoRA；主实验更新目标agent，未说明反馈代理自身权重随代更新。
- [Frontis-MA1 / OpenMLE](https://arxiv.org/html/2607.28568v1) · Horizon Research / Frontis.AI / 清华大学。研发操作经过SFT/RL，部署执行长程ML搜索；主要改外部ML解法，系统本身固定。不能按“训练模型+有harness”认定协同RSI。
- [RSI-Anything](https://github.com/Gen-Verse/RSI-Anything) · Gen-Verse（项目团队；机构未核准）。官方仓库给出预测—交互—反馈—保留循环。不同领域更新对象可能不同，需逐域核实是否同时改参数与非参数系统。
- [Eureka](https://arxiv.org/abs/2310.12931) · NVIDIA / UPenn / Caltech / UT Austin。奖励程序与机器人策略更新；奖励设计LLM冻结。它是AI设计学习信号的参考，不能当LLM研究者自身参数递归升级。
- [Automated Alignment Researchers](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures) · Anthropic。研究代理提出干预并训练外部目标模型；目标改善没有直接证明研究代理自身学习或自改。
- [Seed for Seed](https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity) · ByteDance Seed。官方描述AI参与数据、算法和工程开发；尚无统一公开的自我递归协议可从介绍推定。
- [EvoTrainer](https://arxiv.org/html/2606.03108v2) · Alibaba Tongyi Lab / SIAT-CAS / SUAT。训练侧诊断工具/流程与目标策略版本共同改进；训练者LLM为固定Sonnet，昂贵执行有人类把关。不能描述成训练者权重自进化。
- [AutoScientists](https://arxiv.org/abs/2605.28655) · Harvard。研究团队共享实验知识并搜索外部目标训练方案；需要单独验证团队系统本身是否更新。
- [Execution-Grounded Research](https://arxiv.org/abs/2601.14525) · Stanford。执行候选AI研究方案并反馈构思者；训练构思模型与改进目标模型须分开计，不把外部训练目标当成其自身后继。
- [RewardHarness](https://arxiv.org/html/2605.08703v1) · UBC / Vector / Kuaishou Kolors / Etude AI / Waterloo / Carnegie Mellon / Tsinghua / Georgia Tech。跨路线机制联系。主贡献是评价Harness演化；下游训练提供跨路线联系，未建立更新目标反向改进奖励系统的闭环。 冻结视觉语言模型，通过偏好误差改进 reward agent 的技能和工具；该评价系统随后用于外部图像编辑模型的 GRPO 训练。
- [AIRA-Compose / Design](https://arxiv.org/abs/2605.15871) · Meta FAIR / Oxford。研究代理搜索架构/计算原语，候选扩展到外部目标预训练；没有据此证明目标模型回到下一代研究者角色。
- [OPHIS](https://meta-circle.com/blog/ophis-a-new-paradigm-for-autoresearch) · MetaCircle。以训练内部观测提出假设和干预，再用重复训练结果决定下一步研究。
- [ComfyResearch](https://meta-circle.com/blog/comfyresearch-see-how-learning-happens) · MetaCircle。把训练协议、观测与分析组织成可执行依赖图，供人或 agent 构造、运行和比较实验。
- [Apex-Tune](https://www.apexin.ai/assets/papers/what-happens-when-ai-starts-improving-ai.pdf) · Apex Intelligence。自动提出并验证 scaling law、训练实现和 GPU kernel 的改进，以实验结果继续搜索。
- [Recursive · First Steps](https://www.recursive.com/articles/first-steps-toward-automated-ai-research) · Recursive Superintelligence。长时程并行研究线程积累实验上下文、组合候选分支，并对改进进行方差与 reward-hack 检查。
- [INTELLECT-3 / PRIME-RL](https://www.primeintellect.ai/blog/intellect-3) · Prime Intellect。以合成数据、可验证环境和异步 RL 训练 106B MoE，公开训练框架、环境与模型。

### 组织结构与角色能力共同学习 · Organization–Policy Co-learning

什么分工和信息路由能产生可学习的协作经验，而非仅增加agent数量？

组织层规定角色、通信、路由和分配；参数学习改变各角色的能力。研究两者如何共同适配。多个模型同时训练或固定多agent流程，都不足以单独证明组织结构在进化。

**研究子问题**

- 共享权重与角色特化
- 异构模型与专家路由
- 层次化委派与信息交接
- 协作轨迹与联合训练
- 预算分配与组织重构

**主要技术**

- multi-agent workflow search
- role-conditioned policies
- communication topology
- orchestrator–subagent learning

**机制联系**

- 组织结构与角色能力共同学习 → 工作流与策略共同适配：规定分工与路由。角色分工和通信拓扑成为工作流可优化的内容。
- 组织结构与角色能力共同学习 → 外部经验进入参数：提供多角色监督。局部执行轨迹与编排轨迹训练同一模型或不同角色策略。

**论文与团队（包括初筛与跨路线联系）**

- [Frontis-MA1 / OpenMLE](https://arxiv.org/html/2607.28568v1) · Horizon Research / Frontis.AI / 清华大学。研发操作经过SFT/RL，部署执行长程ML搜索；主要改外部ML解法，系统本身固定。不能按“训练模型+有harness”认定协同RSI。
- [MASS](https://arxiv.org/html/2610.12176v1) · Sakana AI / UC Berkeley。优化的是文本形式的多agent工作流；底层coding harness、工具和记忆固定。共享模型经SFT后再次承担执行、优化和评价角色；报告两轮。
- [Seed for Seed](https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity) · ByteDance Seed。官方描述AI参与数据、算法和工程开发；尚无统一公开的自我递归协议可从介绍推定。
- [AutoScientists](https://arxiv.org/abs/2605.28655) · Harvard。研究团队共享实验知识并搜索外部目标训练方案；需要单独验证团队系统本身是否更新。
- [EvoDS](https://arxiv.org/abs/2606.03841) · HKUST。共享骨干的多角色策略经过SFT和online RL，产生并复用可执行技能；组织架构本身固定，不应把多角色训练说成拓扑演化。
- [AIRA-Compose / Design](https://arxiv.org/abs/2605.15871) · Meta FAIR / Oxford。研究代理搜索架构/计算原语，候选扩展到外部目标预训练；没有据此证明目标模型回到下一代研究者角色。

### 部署变化与再适配 · Deployment-time Re-adaptation

工具、skills、hooks或模型版本变化后，如何保持原有能力并学会新的接口？

模型更新与harness更新的时间尺度常不一致；训练需要覆盖接口变化，部署反馈也可能触发后续学习或系统改写。离线鲁棒性训练、测试时适配和持续在线共演应明确区分。

**研究子问题**

- 工具schema与动作空间变化
- skills/hooks/prompt变体
- 跨模型harness迁移
- 测试时训练与局部适配
- 版本兼容及长期回退

**主要技术**

- harness-state augmentation
- test-time adaptation
- continual adaptation
- interface alignment

**机制联系**

- 部署变化与再适配 → 工作流与策略共同适配：暴露兼容性变化。接口、工具或模型版本变化会使既有工作流失配，从而要求重新适配。
- 外部经验进入参数 → 部署变化与再适配：改变所需外部支持。被内化的行为可能降低复杂harness依赖，但必须在目标部署接口下检验。
- 部署变化与再适配 → 外部经验进入参数：提供适配训练分布。训练覆盖不同harness状态或当前学生实际访问状态，以学习稳健行为。

**论文与团队（包括初筛与跨路线联系）**

- [SIA](https://github.com/hexo-ai/sia) · Hexo Labs / University of Oxford。反馈代理同时修改目标agent scaffold并训练其LoRA；主实验更新目标agent，未说明反馈代理自身权重随代更新。
- [Harness-Zero](https://arxiv.org/abs/2609.24974) · Peking University / Google / HKUST。先演化harness，再由harnessing agent在学生动作空间生成干预轨迹并SFT；支持H→M内化，未直接展示更新学生继续演化H的反复闭环。
- [On-policy Co-evolution](https://arxiv.org/html/2609.09134v1) · Salesforce AI。对进化后harness做学生访问状态上的局部纠错与LoRA-SFT；主要实证是一次顺序适配，循环接续是提出的方向。on-policy描述采样状态，不代表训练算法为RL。
- [TaoLive HAT](https://arxiv.org/abs/2608.15763) · TaoLive AIGC LLM Team。harness-state augmentation使模型适应skills/tool schemas/prompts/hooks变体；这是训练鲁棒性与部署适配，不证明AI自动演化harness。
- [WebEvolver](https://arxiv.org/html/2504.21024v2) · Tencent AI Lab。跨路线机制联系。同时改多个模型仍是参数侧共学；已读方法没有非参数工作流/工具/环境包装被优化。 策略 LLM 与 world-model LLM 从交互轨迹中共同训练；世界模型提供合成经验与前瞻规划。可变对象是两类模型的参数。

### 持续研究的问题

- **联合更新为什么有时互补，有时互相破坏？** harness改变了状态分布与规划习惯；参数更新可能增强它，也可能破坏已经形成的配合。需要解释性能变化来自哪条耦合路径，而不是只比较最终分数。
- **什么应保留在外部，什么应写入参数？** 可检索技能易更新并保留条件，参数内化减少部署依赖。两者的取舍涉及泛化、调用成本、遗忘和新任务适配。SkillRL与Harness-Zero代表不同位置，SEED展示训练期技能向参数的转移。
- **任务、奖励和改进器都变化后，怎样仍然得到可迁移进步？** 学习信号本身可能随策略变化而变好或发生偏移。评价可靠性、任务覆盖与长期版本演化是相互关联的问题；多轮短期增益尚不等于长期稳定增长。

