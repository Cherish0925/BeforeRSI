# RSI 与 AI4AI 分层研究目录

共 123 条。56 条为本轮新增原始来源初筛，其中 10 条选读关键方法、定义或结果段落；不是 123 篇全文审查或独立复现。
旧条目保留原有阅读深度；范围重新分类不提升证据等级。直接自进化研究是主题标签，不等于已证实更强的递归改进能力。
完整阅读边界见 data/scope-review.json；新增工作的任务、资源和干预见 data/expansion-reviews.json。

| 分层 | 数量 |
|---|---:|
| 直接自进化研究 | 63 |
| 直接支撑的 AI4AI/学习机制 | 30 |
| 评测与反例 | 7 |
| RSI 理论 | 3 |
| 历史/机制基础 | 14 |
| 移出核心的背景 | 6 |

## 直接自进化研究

| 工作（首次公开年份） | 改了什么、如何反馈 | 尚不能推出什么 |
|---|---|---|
| [STOP](https://github.com/microsoft/stop)（2023） | An improver edits an executable improver, potentially retaining better candidate-generation operations. | Underlying language model is fixed and evidence is bounded to the supplied task setting. |
| [Promptbreeder](https://proceedings.mlr.press/v235/fernando24a.html)（2023） | Mutation prompts alter the proposal distribution used to evolve task prompts. | Self-reference is prompt-level; broad transfer and successor-as-improver performance are not established. |
| [Self-Rewarding Language Models](https://proceedings.mlr.press/v235/yuan24d.html)（2024） | Self-generated preferences reweight the training target; learning changes both answer and judgment behavior. | 实际新题由固定 Llama 2-Chat 70B 生成；有人类种子、外部评审和早停。不证明无外部信息或无限递归增长。 规模核对：Llama 2 70B；两轮偏好集分别 3,964 / 6,942 对；256 题成对比较与 805 题 AlpacaEval 2。 |
| [Gödel Agent](https://github.com/Arvid-pku/Godel_Agent)（2024） | Self-edited control logic changes accessible actions and the way feedback is used. | Transfer across unrelated tasks, models, and improvement problems remains limited. |
| [SICA](https://github.com/MaximeRobeyns/self_improving_coding_agent)（2025） | Code and tool changes can reduce execution failures and improve useful work per budget. | Coding-benchmark evidence does not establish scale transfer or improved successor generation. |
| [Darwin Gödel Machine](https://github.com/jennyzzt/dgm)（2025） | Reusable coding operations and retained alternative parents change subsequent proposal opportunities. | Open lineage must be separated from extra candidate and evaluation budget; broad transfer and rising improvement ability remain open. |
| [SEAL](https://github.com/Continual-Intelligence/SEAL)（2025） | Self-edit generation is trained on utility after the learner consumes that edit. | 小规模且筛选的 ARC 结果不能外推一般智能；旧编辑奖励对新学习者可能失效。 规模核对：知识吸收为 Qwen2.5-7B；ARC 为 Llama-3.2-1B，筛选后 11 个训练 / 8 个评测任务。 |
| [HyperAgents](https://github.com/facebookresearch/HyperAgents)（2026） | Editable meta code changes diagnosis, proposal and reuse, with task and meta roles sharing a program. | Cross-domain meta-level transfer is author-reported; common-target attribution and independent matched-budget reproduction remain to be audited. |
| [SIA](https://github.com/hexo-ai/sia)（2026） | Feedback directs updates to code or weights, changing execution and later learning data. | Update-object selection, component attribution, and repeated full-loop transfer remain open. |
| [Recursive Harness Self-Improvement](https://arxiv.org/abs/2607.15524)（2026） | Workflow specifications condition information flow and are revised from outcome comparisons. | Task-specific synthetic settings and few update iterations do not establish broad or open-ended recursion. |
| [Co-Evolving Harnesses and Model Weights for LLM Agents](https://arxiv.org/abs/2607.22688)（2026） | Diagnosed runtime failures guide harness repairs that change subsequent model-training experience. | Repeated co-evolution, structural harness redesign, and broad cross-model transfer remain open. |
| [HELIX](https://github.com/HKUDS/HELIX)（2026） | Harness variants yield both task outcomes and contrasting records potentially useful for learning. | The paper reports harness execution and training-record production; a completed model update and rebuild is not measured in the reported experiment. |
| [HSI](https://github.com/TailinZhou/hsi)（2026） | Meta-evolver changes can alter the distribution and allocation of future harness edits. | Meta-level changes need transfer to a distinct improvement problem and independent matched-budget evaluation. |
| [HarnessDev](https://arxiv.org/abs/2609.01437)（2026） | Creator search changes executable scaffolds consumed by a potentially different executor. | Creator–executor transfer, equal-compute baselines, and later successor quality require broader testing. |
| [RRSI](https://github.com/google-research/rrsi)（2026） | Proposal and acceptance constraints favor transferable, affordable edits over source-score fitting. | Frozen-model, finite-evolve-set results need independent reruns, time-forward tasks, and stronger scale transfer. |
| [Meta-Harness](https://github.com/stanford-iris-lab/meta-harness)（2026） | Search changes which information is stored, retrieved and exposed to a fixed model. | Open source-level search needs matched restricted-search baselines and broad transfer tests. |
| [AIDE²](https://arxiv.org/abs/2609.26457)（2026） | Search and memory rewrites improve the inner research agent under a fixed main outer proposer. | Main outer proposer is fixed while the inner research agent evolves; the separate common-target ignition test does not decisively establish superiority over the strong outer baseline. |
| [Frontis-MA1 / OpenMLE (catalog alias: OpenRSI)](https://github.com/FrontisAI/OpenRSI)（2026） | Execution-grounded training improves shared program-editing operators used by long-horizon search. | §8 明确：主要改外部 ML 解法，演化系统本身基本固定；训练模型加工程化 harness 不等于自治协同 RSI。 规模核对：35B 主模型；MLE-Bench Lite 每题 12 小时、单 RTX 4090 沙箱限 12 GB；不含远程模型服务总算力。 |
| [MASS](https://github.com/SakanaAI/mass)（2026） | Workflow-conditioned trajectories train shared weights used in solving, proposing and judging. | Reported cross-domain regressions show that joint updating can redistribute capability; repeated broad transfer remains open. |
| [RSI-Anything](https://github.com/Gen-Verse/RSI-Anything)（2026） | Interaction and world-model predictions guide updates in an environment. | Cross-environment transfer and resistance to simulator or evaluator exploitation need independent replication. |
| [Dream-RSI](https://github.com/zhengkid/Dream-RSI)（2026） | Replayed discovery trees train exploration choices before expensive online research. | The relation between simulated rehearsal and real improvement, and successor-as-improver gain, remains open. |
| [Huxley–Gödel Machine (HGM)](https://arxiv.org/abs/2510.21614)（2025） | Descendant-informed allocation estimates future branch value instead of current score alone. | Reported descendant-informed search and transfer need controlled actor-target comparisons and independent reproduction. |
| [SIMA 2](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)（2025） | Tasks, estimated rewards and visited states jointly determine the training distribution. | The official self-improvement report does not show that Genie itself recursively improves or that physical-world transfer is established. |
| [Self-Taught Evaluators](https://arxiv.org/html/2408.02666v1)（2024） | Better judgment generation changes the usable training pool for later evaluator versions. | Constructed preference labels can be imperfect; the student is reset to the seed each round rather than simply continuing fine-tuning. |
| [GPT-Red](https://cdn.openai.com/pdf/gpt-red-automated-red-teaming-via-self-play-at-scale.pdf)（2026） | Changing opponents generate a moving learning frontier; population diversity can prevent narrow adaptation. | Task-specific robustness improvement and co-training do not establish unrestricted recursive research acceleration. |
| [ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement](https://arxiv.org/abs/2609.14857)（2026） | 当前智能体分析成功/失败对照轨迹并修改自身模块，再整合模块。 | 模块独立优化后存在交互；跨模型迁移不等于改进能力持续提升。 |
| [Prime Agent: A Self-Improving RLM Harness](https://arxiv.org/abs/2608.23552)（2026） | 长期 REPL 与持久经验支撑跨轨迹策略修订和技能使用。 | 递归子代理调用本身不是 RSI；摘要没有隔离后继作为改进者的贡献。 |
| [The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators](https://arxiv.org/abs/2606.26294)（2026） | 共同进化任务代理与评价器，替换评价器后重估档案。 | IMO 人工评分等外部锚点仍必要；论文写作的代理评分不能等同真实科研质量。 |
| [Dr. Zero: Self-Evolving Search Agents without Training Data](https://arxiv.org/abs/2601.07055)（2026） | 出题者按当前求解者能力生成问题，双方交替学习。 | 无人工训练数据不等于无外部信息；题目真实性、难度和多样性仍是限制。 规模核对：Qwen2.5-3B / 7B Instruct；出题者与求解者迭代训练，检索提供外部信息。 |
| [Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills](https://arxiv.org/abs/2607.22529)（2026） | 技能提供任务生成结构与验证程序，双方策略和技能库共同更新。 | 可执行验证与技能覆盖仍有边界，能力前沿难度代理不等于真实长期学习增益。 |
| [RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System](https://arxiv.org/abs/2602.02488)（2026） | 策略、奖励模型和任务难度通过反馈共同调整。 | 环境变化受预建任务与验证器约束；不能据此宣称任意世界可自我生成真值。 规模核对：已读策略为 7B / 8B，奖励模型为 8B / 14B，任务改写器为 4B；32B / 72B 出现在评价角色，不能作为训练规模。 |
| [Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning](https://arxiv.org/abs/2511.16043)（2025） | 工具增强执行者与课程代理共同生成下一轮训练任务。 | 工具与预训练提供外部能力；多轮共同训练不证明通用研发递归。 |
| [R-Zero: Self-Evolving Reasoning LLM from Zero Data](https://arxiv.org/abs/2508.05004)（2025） | 挑战者寻找求解者能力边缘任务，求解者训练后改变出题反馈。 | 自生成题目和标签可能共同偏误，不能由内部奖励证明正确性。 |
| [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335)（2025） | 同一模型生成训练任务并求解，代码执行提供验证反馈。 | 无需新人工数据仍依赖预训练、执行语义和初始任务表达范围。 |
| [Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data](https://arxiv.org/abs/2602.21320)（2026） | 生成器针对工具求解者的能力边界构造任务，真实工具调用反馈训练双方。 | 工具接口和答案校验限定可学空间；不能把相对增幅当跨基准绝对优势。 |
| [EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for Autonomous Agentic Reinforcement Learning](https://arxiv.org/abs/2606.03108)（2026） | 训练代理修改诊断、训练信号和流程，保留技能供后续训练版本使用。 | 自主流程不等于完全无人参与，也不证明训练代理权重或研发能力递归增长。 规模核对：SWE 训练对象明确为 4B / 9B；Math/Coding 的参数量本轮未核准。训练代理为冻结 Sonnet 4.6，不能当作被训练模型。 |
| [Dual-Evolving Reinforcement Learning for Automated Reward Design](https://arxiv.org/abs/2512.13399)（2025） | 奖励设计者根据内层策略训练后的验证表现学习更好的奖励提案。 | 奖励原语由人指定；最终策略重新训练，不能描述成同一策略连续自改。 |
| [GEAR: Genetic AutoResearch for Agentic Code Evolution](https://arxiv.org/abs/2605.13874)（2026） | 维护研究状态种群并交叉重组；其中一个变体允许搜索控制器演化。 | 固定控制器的另外两个变体不是改进器自修改，不能合并宣称递归。 |
| [Meta$^n$: Recursive Self-Improvement through Emergent Depth](https://arxiv.org/abs/2608.24735)（2026） | 固定元操作反复读取已有代码与轨迹，生成后续策略层及工具。 | 固定元操作不自动保证整体稳定；层数与真实改进效率不可混同。 |
| [Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498)（2026） | 代理从自身失败中挖掘弱点、提出最小修改并经回归测试保留。 | 自己提出修改不自动证明后继更会修改；同基准划分与跨领域迁移不同。 |
| [SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning](https://arxiv.org/abs/2602.08234)（2026） | 从经验提炼分层技能，并让技能库与 RL 策略共同更新。 | 技能压缩可能丢失适用条件，特定基准增益不证明通用递归能力。 |
| [Mem$^2$Evolve: Towards Self-Evolving Agents via Co-Evolutionary Capability Expansion and Experience Distillation](https://arxiv.org/abs/2604.10923)（2026） | 经验指导创建工具/专家资产，新资产反过来产生后续经验。 | 资产增加不保证改进速度上升，组合依赖和维护成本尚须控制。 |
| [MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents](https://arxiv.org/abs/2602.02474)（2026） | 控制器学习选择记忆技能，设计者根据难例周期性修订技能集。 | 设计者本身是否改进未确定；技能选择和技能生成的贡献需分离。 |
| [EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management](https://arxiv.org/abs/2606.03841)（2026） | 学习生成可复用执行技能，并把上下文压缩作为训练控制策略。 | 数据科学成绩与生成后继研究者能力不同；摘要定理不能代替逐项假设核查。 |
| [Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails](https://arxiv.org/abs/2609.09134)（2026） | 先适配 harness，再在学生自身轨迹的失败位置提供专家局部纠正。 | 主要结果支持一次 harness 演化后的权重适配；多轮闭环是可接续方案，已读结果未展示长期反复迭代。完整轨迹模仿有明显退化。 规模核对：主实验 Qwen3-Coder-30B-A3B（总 30B / 激活 3B），LoRA SFT；Gemma-4-26B-A4B 为 <27B 补充实验，7 个企业任务。 |
| [RewardHarness: Self-Evolving Agentic Post-Training](https://arxiv.org/abs/2605.08703)（2026） | 奖励代理依据偏好误差修订工具/技能库，再提供模型后训练奖励。 | 初始人类偏好是锚点；奖励器自改与被训练模型回馈奖励器须区分。 |
| [WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model](https://arxiv.org/abs/2504.21024)（2025） | 网页世界模型生成训练交互并帮助规划，与网页代理共同进化。 | 模型想象会积累偏差，真实网页验证不能由世界模型自身评分替代。 |
| [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://arxiv.org/abs/2411.02337)（2024） | 用失败生成新课程，配合结果奖励与策略漂移控制进行在线训练。 | 课程反馈闭环不同于训练算法自改；目标领域仍限定在网页任务。 |
| [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://arxiv.org/abs/2501.04519)（2025） | 搜索轨迹训练策略和过程偏好模型，两者四轮共同更新。 | 外部题库与执行验证仍支撑学习；数学域共同进化不是开放科研闭环。 |
| [Self-Evolved Reward Learning for LLMs](https://arxiv.org/abs/2411.00418)（2024） | 奖励模型生成训练反馈，迭代训练自己的评价能力。 | 有限人工标注和预训练仍是信息锚点；自反馈可能积累偏差。 |
| [SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills](https://arxiv.org/abs/2504.07079)（2025） | 网页代理探索、练习并封装 API，复用新技能继续积累能力。 | 技能积累和任务迁移不等于技能发现过程效率持续上升。 |
| [Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?](https://arxiv.org/abs/2511.13646)（2025） | 代理在解决软件任务时修改自身运行 scaffold。 | 同任务内自改与跨任务继承是不同证据，不能从 solve rate 推出代际增长。 |
| [Group-Evolving Agents: Open-Ended Self-Improvement via Experience Sharing](https://arxiv.org/abs/2602.04837)（2026） | 智能体群共享不同进化分支的经验来指导后续结构修改。 | 同进化个体数不保证同算力；探索多样性的价值需与开销分开。 |
| [Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams](https://arxiv.org/abs/2606.01770)（2026） | 任务流驱动持续构建不同 harness，并按任务路由及保留演化经验。 | 部分信号来自人类引导；路由收益不等于改进器变强。 |
| [Continual Harness: Online Adaptation for Self-Improving Foundation Agents](https://arxiv.org/abs/2605.09998)（2026） | 代理在持续交互中交替行动并修订持久技能、提示和记忆。 | 早期 GPP 人类参与与后续自动循环必须分开，游戏进度不直接代表通用研发能力。 |
| [EnvHarness: Awakening Static Worlds for Agent Learning](https://arxiv.org/abs/2608.19880)（2026） | 根据代理失败生成环境包装组件，保留原验证器并训练策略。 | 环境包装保留验证器是特定设计，不保证所有新任务忠实有效。 |
| [CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution](https://arxiv.org/abs/2603.17775)（2026） | 同一模型交替学习生成与验证，以验证反馈过滤自一致错误。 | 多数投票仍提供噪声标签，摆脱部分共识错误不保证无锚点真理发现。 |
| [Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence](https://arxiv.org/abs/2604.18292)（2026） | 探索真实工具生态并生成可验证任务，按能力缺口持续训练。 | MCP 环境主题多不等于未见世界泛化，生成器和验证器来源需全文核查。 |
| [Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills](https://arxiv.org/abs/2606.07412)（2026） | 从解题轨迹提取技能生成下一轮修复任务，执行验证后更新求解者。 | 梯度对齐作为学习价值代理需检验；软件领域闭环未推出通用科研提升。 |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291)（2023） | 在 Minecraft 中创建并复用可组合代码技能继续探索。 | 固定 GPT-4 与课程程序；技能复用不是已证元算法自改。 |
| [AgentEvolver: Towards Efficient Self-Evolving Agent System](https://arxiv.org/abs/2511.10395)（2025） | 自提问、自导航与贡献归因让环境经验进入后续 agent 训练。 | 训练闭环的元过程仍有固定部分；高效率需全流程成本而非仅样本数。 |
| [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.14777)（2026） | 当前策略同时收集轨迹和提炼事后技能，技能诱导信号训练同一策略。 | 训练期事后信息在部署不可见；内化效果与信息泄漏边界需明确。 |
| [RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning](https://arxiv.org/abs/2505.15034)（2025） | 生成者与过程验证者交替用 RL 训练，外部结果正确性监督验证者。 | 不是完全无标签自证；固定结果验证构成外部锚点。 |

## 直接支撑的 AI4AI/学习机制

| 工作（首次公开年份） | 改了什么、如何反馈 | 尚不能推出什么 |
|---|---|---|
| [SPIN](https://github.com/uclaml/SPIN)（2024） | Training contrasts generated responses with a reference data distribution and changes later response probabilities. | The iterative training rule is externally fixed; long-run diversity, retention, and recursive update quality remain open. |
| [ADAS](https://github.com/ShengranHu/ADAS)（2024） | A fixed designer conditions architecture proposals on an archive of previous designs and outcomes. | The outer designer remains fixed; persistent target improvement is not evidence that the improver improved. |
| [AFlow](https://github.com/FoundationAgents/AFlow)（2024） | Tree search allocates trials among workflow designs and composes available operators. | Workflow gains require held-out transfer and comparison with recursive improvement of the generator. |
| [GEPA](https://github.com/gepa-ai/gepa)（2025） | Trace-conditioned reflection localizes repairs; instance-specialist parents preserve alternative solutions. | A strong fixed optimizer and baseline for RSI; the optimizer itself is not shown to improve. |
| [AgentBreeder](https://arxiv.org/abs/2502.00757)（2025） | Evolution changes coordination and communication among component agents. | Evolution of a target scaffold does not establish recursive improvement of the evolutionary process. |
| [EvoHarness-RL](https://arxiv.org/abs/2608.05446)（2026） | Learned coordination changes when external state is written, retrieved and used. | Transfer beyond the reported long-horizon environments and recursive update quality are not established. |
| [Agentic Context Engineering (ACE)](https://arxiv.org/abs/2510.04618)（2025） | Persistent contextual lessons alter later decisions without changing weights. | Persistent context gains do not alone establish improved common-target improver performance or indefinite growth. |
| [AlphaEvolve](https://arxiv.org/abs/2506.13131)（2025） | Executable search can improve algorithms or infrastructure reused by later model development. | Reported improvements to underlying model-training infrastructure provide a possible feedback path; repeated actor improvements require explicit lineage and budget accounting. |
| [Optimization by PROmpting (OPRO)](https://arxiv.org/abs/2309.03409)（2023） | The optimizer conditions proposals on a history of candidate-value pairs. | History-conditioned optimization of a target does not by itself establish a persistent improvement of the producing system. |
| [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465)（2022） | Correctness-filtered rationales and answer-conditioned rationalization alter the learning target. | Filtering and answer-conditioned rationalization change the learning target; repeated general improvement of the improver is not established. |
| [Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models](https://arxiv.org/abs/2312.06585)（2023） | Reward-weighted sampling and likelihood projection alternate as an approximate EM procedure. | Its EM interpretation depends on the reward and learning approximation; finite filtered data can change task coverage and transfer. |
| [AlphaProof](https://www.nature.com/articles/s41586-025-09833-y)（2024） | Verification supports reusable proof learning while generated variations alter the curriculum. | Formal proof correctness is conditional on the formal statement; it does not establish fidelity of every autoformalization or broad research recursion. |
| [Constitutional AI](https://arxiv.org/abs/2212.08073)（2022） | Feedback production can be delegated to AI while the objective and calibration remain external. | The normative target remains externally specified; AI feedback is not automatically accurate or independent. |
| [Eureka](https://arxiv.org/abs/2310.12931)（2023） | A proposed artifact is valued by the learning process it induces, not only by immediate execution. | Useful reward optimization does not establish that the LLM reward designer itself becomes a stronger designer. |
| [Automated Alignment Researchers: mitigating alignment failures](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures)（2026） | A research policy chooses interventions whose value is measured after target-model training. | Improving target models does not show that the researcher improves itself; production data-efficiency claims are not full research-cost ratios. |
| [Seed for Seed (Seed2.1)](https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity)（2026） | Useful model-development outputs can feed later model development through several operational paths. | A deployment report supports use in AI development, not an identified causal multiplier or autonomous closed-loop growth. |
| [SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness](https://arxiv.org/abs/2609.20519)（2026） | 从多环境轨迹搜索并整合执行、压缩和观察处理机制。 | 论文把用新 harness 加速后继研发列为未来方向；成本下降不是已测递归复利。 |
| [AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation](https://arxiv.org/abs/2605.28655)（2026） | 去中心化团队共享成功和失败的实验知识，搜索目标模型训练改进。 | 生物研究部分不是本项目核心；目标 GPT 训练优化不证明研究代理自我升级。 |
| [Towards Execution-Grounded Automated AI Research](https://arxiv.org/abs/2601.14525)（2026） | 执行预训练/后训练研究方案，用结果做演化搜索或训练构思模型。 | RL 平均奖励上升同时出现模式坍缩，上限改善未建立；并未训练自身后继。 |
| [Harness-Zero: Harness Distillation via Agent-as-Harness](https://arxiv.org/abs/2609.24974)（2026） | harnessing agent 把复杂 harness 指导转换为目标动作空间的训练示范。 | 展示内化与部署收益，未据摘要证明多代改进器闭环。 |
| [Harness-R1: Learning to Edit Executable Runtime Harnesses from Agent Failure Trajectories](https://arxiv.org/abs/2608.02276)（2026） | 用目标代理重跑后的任务成功训练专门的 harness 编辑模型。 | 主训练只更新编辑者、目标冻结；论文指向共同进化，未证明持续双向循环。 |
| [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/abs/2605.23904)（2026） | 外部优化模型把评分轨迹变成受限文本编辑，验证后保留技能。 | 外部技能优化与优化器自改不同；重复验证选择仍需最终未触碰测试。 |
| [MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory](https://arxiv.org/abs/2601.03192)（2026） | 固定推理模型通过环境反馈更新经验检索效用。 | 持久记忆学习成立不等于记忆更新规则或改进能力已自进化。 |
| [Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Technical Report](https://arxiv.org/abs/2608.15763)（2026） | 用多种 harness 状态增强训练，使紧凑模型适应独立变化的运行框架。 | 兼容变化中的 harness 不等于 AI 自己设计或进化该 harness。 |
| [Self-Evolving Curriculum for LLM Reasoning](https://arxiv.org/abs/2505.14970)（2025） | 以估计学习收益更新非平稳 bandit 课程策略，配合模型 RL。 | 固定课程更新律是自适应训练，不自动构成改进器递归重写。 |
| [Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design](https://arxiv.org/abs/2605.15871)（2026） | 研究代理设计计算原语和架构，并将候选扩展到较大模型训练。 | 发现目标模型架构不等于将目标用作下一代设计者。 |
| [ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution](https://arxiv.org/abs/2509.19349)（2025） | 通过多样性、父代选择与模型组合提高程序演化样本效率。 | 只有目标涉及 AI 训练/harness 时属直接 AI4AI；普通圆堆积不算自身进化。 |
| [Actor-Curator: Co-adaptive Curriculum Learning via Policy-Improvement Bandits for RL Post-Training](https://arxiv.org/abs/2602.20532)（2026） | 神经课程选择器直接学习预计策略提升，适配非平稳题库采样。 | 课程控制器的学习不同于其自身更新算法被改进。 |
| [SkillOS: Learning Skill Curation for Self-Evolving Agents](https://arxiv.org/abs/2605.06614)（2026） | 用较晚关联任务的表现训练技能整理者，执行者保持冻结。 | 改善技能整理者是有价值的 AI4AI，但其更新流程未被自身改写。 |
| [Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning](https://arxiv.org/abs/2607.21971)（2026） | 用执行反馈训练多轮反思与修订能力，部署时进行演化搜索。 | 改进目标代码不等于目标本身是改进器；需实际闭环继承证据。 |

## 评测与反例

| 工作（首次公开年份） | 改了什么、如何反馈 | 尚不能推出什么 |
|---|---|---|
| [On the Statistical Limits of Self-Improving Agents](https://arxiv.org/abs/2510.04399)（2025） | The reachable hypothesis class and feedback sample determine what generalization can be learned. | The result concerns reachable policy-family capacity under stated i.i.d. PAC assumptions; it does not guarantee unrestricted self-improvement. |
| [Harness Updating Is Not Harness Benefit](https://arxiv.org/abs/2605.30621)（2026） | Proposal competence and ability to execute the proposed computation are distinct causal factors. | Establishes an important separation and scale pattern; further models, tasks, and independent replication are needed. |
| [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227)（2026） | Task-time search and persistent harness changes compete for the same resource budget. | Defines stronger comparisons for harness evolution; results still depend on chosen tasks and feedback regimes. |
| [Auditing Harness Tampering in Self-Improving Agents](https://arxiv.org/abs/2609.00069)（2026） | Changing the measurement path can increase observed score without improving intended utility. | Audits tampering in current systems; prevention and protected acceptance remain engineering and research problems. |
| [AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement](https://arxiv.org/abs/2608.20318)（2026） | 隔离训练算法修改，用隐藏评估器重训提交代码。 | 它测研发能力而非运行多代 RSI，归一化分数仍依赖所选任务和参照。 |
| [Aspire: Can Models Self-Evolve from Vague Goals?](https://arxiv.org/abs/2608.31111)（2026） | 让代理从模糊目标自行选数据和更新方式，再用隐藏专家任务评价。 | 完成训练或编辑流程不等于提高能力；报告中增益稀疏且不稳定。 |
| [Large Language Model Agents Are Not Always Faithful Self-Evolvers](https://arxiv.org/abs/2601.22436)（2026） | 干预原始和压缩经验，检查代理决策是否真正依赖积累经验。 | 对经验不敏感可来自已有知识或压缩丢失，不能一概判为无学习。 |

## RSI 理论

| 工作（首次公开年份） | 改了什么、如何反馈 | 尚不能推出什么 |
|---|---|---|
| [Speculations Concerning the First Ultraintelligent Machine](https://doi.org/10.1016/S0065-2458(08)60418-0)（1965） | Reuse of improved design operations can increase future design yield. | Qualitative positive-feedback argument; no operational update process or empirical test. |
| [Gödel Machine](https://arxiv.org/abs/cs/0309048)（2003） | A proof can authorize a change by comparing future utility, including continued proof search. | Useful self-rewrites must be provable in the encoded axiomatic system; proof search is not shown tractable for modern AI. |
| [Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement](https://arxiv.org/abs/2609.13406)（2026） | 统一描述策略、评价、修改机制及评价基准是否属于可修改系统。 | 属于可重写组件不等于实际发生有效重写；表示统一不是经验泛化定律。 |

## 历史/机制基础

| 工作（首次公开年份） | 改了什么、如何反馈 | 尚不能推出什么 |
|---|---|---|
| [EURISKO](https://www.cs.northwestern.edu/~mek802/papers/not-mine/Lenat_EURISKO.pdf)（1983） | Retained heuristics alter which future hypotheses are generated and pursued. | Bounded hand-engineered representations, incomplete modern reproduction, and no evidence of scalable general recursion. |
| [MAML](https://proceedings.mlr.press/v70/finn17a.html)（2017） | Initialization shapes the effect of a later task-specific gradient update. | Learns fast adaptation under a fixed human-designed meta-training algorithm; does not improve the improver. |
| [AlphaGo Zero](https://www.nature.com/articles/nature24270)（2017） | Search improves behavior; self-play supplies consequences; policy/value training amortizes this computation. | Powerful self-generated experience under exact rules and reward; update algorithm and objective remain fixed. |
| [AutoML-Zero](https://proceedings.mlr.press/v119/real20a.html)（2020） | Program mutation and selection discover reusable learning procedures. | Discovers target algorithms with a fixed outer evolutionary process; no successor-improver evidence. |
| [FunSearch](https://www.nature.com/articles/s41586-023-06924-6)（2024） | A language prior proposes programs; executable scoring and an archive retain useful discoveries. | Produces valuable external programs with a fixed model-search-evaluator process; does not improve the producing system. |
| [Learning to learn by gradient descent by gradient descent](https://arxiv.org/abs/1606.04474)（2016） | A learned update rule exploits structure shared among training optimizees. | Externally trained optimizer with task-dependent transfer; autonomous recursive improvement is not established. |
| [Paired Open-Ended Trailblazer (POET): Endlessly Generating Increasingly Complex and Diverse Learning Environments and Their Solutions](https://arxiv.org/abs/1901.01753)（2019） | Environment generation and cross-environment transfer create alternative learning paths. | Finite experiments with bounded terrain parameters and fixed search rules; no demonstrated unbounded growth or self-rewriting generator. |
| [Tasks, stability, architecture, and compute: Training more effective learned optimizers, and using them to train themselves](https://arxiv.org/abs/2009.11243)（2020） | A learned optimizer can execute the updates that train another optimizer. | Self-training transfer depends on external clipping and the tested horizon; indefinite recursive improvement is not established. |
| [Thinking Fast and Slow with Deep Learning and Tree Search](https://arxiv.org/abs/1705.08439)（2017） | A planner supplies targets to a policy that guides later planning. | Search and imitation are coupled under a declared planner; bounded game results do not establish open-ended improvement across domains. |
| [DreamCoder: Bootstrapping Inductive Program Synthesis with Wake-Sleep Library Learning](https://www.neurosymbolic.org/papers/EllisWNSMHCST21.pdf)（2021） | Library abstraction changes the search language while a recognition policy guides its use. | Library abstraction and policy learning are jointly useful in tested synthesis domains; representation and search costs remain domain dependent. |
| [Selecting Computations: Theory and Applications](https://arxiv.org/abs/1207.5879)（2012） | Compute is spent where information can change the selected action. | Value-of-computation results depend on a specified uncertainty and cost model; solving the metalevel decision can itself be expensive. |
| [Single-Agent Policy Tree Search With Guarantees](https://arxiv.org/abs/1811.10928)（2018） | Depth divided by path probability controls search order and bounds effort. | The guarantee concerns deterministic verifiable search, positive solution-path mass and valid pruning, not arbitrary unknown scientific environments. |
| [Policy-Guided Heuristic Search with Guarantees](https://arxiv.org/abs/2103.11505)（2021） | A heuristic and a policy jointly prioritize paths with bounded search loss. | Search-loss guarantees and empirical learning depend on the policy, heuristic and task assumptions; an expansion is not automatically equal physical cost. |
| [Levin Tree Search with Context Models](https://www.ijcai.org/proceedings/2023/0624.pdf)（2023） | A convex context policy learns from successful paths using a search-effort loss. | Convexity holds for the specified context parameterization and fixed solution paths; it is not a global guarantee for the full bootstrapping process. |

## 移出核心的背景

| 工作（首次公开年份） | 改了什么、如何反馈 | 尚不能推出什么 |
|---|---|---|
| [OpenAI o1: Learning to reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/)（2024） | Policy learning changes the distribution of reasoning trajectories and the value of later inference. | Train/test compute scaling does not identify a self-improving research process. |
| [DeepSeek-R1](https://arxiv.org/html/2501.12948v1)（2025） | Sampling, reward-weighted policy updates and subsequent data production jointly change the learning distribution. | A fixed trainer is compatible with self-generated learning, but the paper does not establish indefinitely improving research ability. |
| [Qwen3 Technical Report](https://arxiv.org/html/2505.09388v1)（2025） | A learner-generated state distribution and teacher targets interact with capacity and reasoning budget. | Teacher-provided information and small-model efficiency do not establish teacher-free recursive discovery. |
| [MuZero](https://arxiv.org/abs/1911.08265)（2019） | Task-relevant dynamics learning changes both planning and the experience used for future updates. | Planning within an imperfect learned model differs from search in a known exact environment. |
| [Open-Ended Learning Leads to Generally Capable Agents (XLand)](https://arxiv.org/abs/2107.12808)（2021） | Task generation changes the learnable frontier and population transfer changes reachable skills. | Broadness within a constructed environment space is not unrestricted real-world generality. |
| [Co-Scientist](https://arxiv.org/abs/2502.18864v2)（2025） | Search supplies hypotheses whose true value requires delayed external experimentation. | Internal hypothesis rankings are not scientific truth; validated hypotheses do not alone prove an improved research policy. |

## 延后与排除记录

| 原始来源 | 处置 | 原因 |
|---|---|---|
| [2606.29871](https://arxiv.org/abs/2606.29871) | defer | 人工构造训练故障上的有界控制案例；暂未显示控制器本身学习，先保留为候选，非断言无价值。 |
| [2606.28374](https://arxiv.org/abs/2606.28374) | defer | 摘要中的 held-out 接受集实际参与反复选择；单调安全的外推需核全文，不据摘要认证。 |
| [2606.21090](https://arxiv.org/abs/2606.21090) | defer | 有限模型/任务上的退化案例，需核完整协议与资源；当前以 Aspire 等覆盖此问题，暂不重复扩容。 |
| [2610.11613](https://arxiv.org/abs/2610.11613) | defer | 与2025 AgentEvolver同名但不同工作；保留最新候选，独立任务迁移和总开发成本未明确。 |
| [2406.18532](https://arxiv.org/abs/2406.18532) | defer | 符号优化的早期机制候选；需进一步区分目标代理优化和改进器自身更新。 |
| [2609.33867](https://arxiv.org/abs/2609.33867) | retrieval_incomplete | 检索得到摘要线索但原始正文/摘要页面重复获取失败，本轮不升级为正式证据。 |
| [2608.20290](https://arxiv.org/abs/2608.20290) | retrieval_incomplete | 原始页面未成功获取，不用二手摘要代替原文核查。 |
| [2608.27287](https://arxiv.org/abs/2608.27287) | retrieval_incomplete | 检索到工业部署线索，原始页面未成功取得，待核。 |
| [2605.15034](https://arxiv.org/abs/2605.15034) | excluded_wrong_query | 本轮把RL Tango的2505误输入为2605，实际是社会观察语境研究；已更正为2505.15034，排除误检项。 |
