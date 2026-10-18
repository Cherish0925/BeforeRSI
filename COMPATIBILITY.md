# Compatibility with the current research corpus

**Scope:** all 123 entries in data/works.json. The latest expansion adds 56 primary-source screens to the prior 67-entry catalog and classifies every entry in [RSI_SCOPE.md](RSI_SCOPE.md). Ten new entries have selected methods, definitions or results read; 46 remain abstract-level screens. Twenty earlier entries had selected methods/results read, with separate varying scopes for the earlier frontier pass. These are not 123 proven RSI systems, full-paper reviews or independent reproductions. Representation compatibility does not establish mechanism coverage or predictive generalization. The earlier Good DOI retrieval limit remains.

**Reading the table:** the middle column is our encoding under THEORY.md, not terminology imposed by the original authors. The last column records behavior or an assumption the model must preserve. All empirical outcomes remain author-reported unless a separate reproduction record says otherwise. Representation is supported by Proposition 1; prediction requires fitted transition laws and withheld interventions. A score reduction additionally needs Proposition 2's state-sufficiency condition.

| Work / primary source | Representation | Required behavior or boundary |
|---|---|---|
| [Speculations Concerning the First Ultraintelligent Machine](https://doi.org/10.1016/S0065-2458(08)60418-0) | Conceptual proposal; no executable update specified. | Positive feedback between machine design and capability is a hypothesis to instantiate, not a measured growth law. |
| [EURISKO](https://www.cs.northwestern.edu/~mek802/papers/not-mine/Lenat_EURISKO.pdf) | Heuristics and meta-heuristics in H; search records in D; M may be absent. | Represent discovery and revision of heuristics without requiring neural training or modern harnesses. |
| [Gödel Machine](https://arxiv.org/abs/cs/0309048) | Self-editable program and proof searcher in H; axioms and proof state in D. | Proof-authorized rewrites retain their formal assumptions; empirical acceptance is not imposed as the only route. |
| [Learned optimizer](https://arxiv.org/abs/1606.04474) | Optimizer weights in M; application and meta-training code in H; recurrent state is explicit in X. | A learned update rule can transfer or fail under changed optimizees. External meta-training does not establish autonomous recursive improvement. |
| [Learned optimizers training themselves](https://arxiv.org/abs/2009.11243) | A learned optimizer A trains another optimizer T; learned parameters are in M and clipping/training support in H. | Preserve reported self-training transfer and horizon-dependent degradation; do not infer unbounded recursive improvement. |
| [MAML](https://proceedings.mlr.press/v70/finn17a.html) | Initialization in M; inner adaptation and outer training in H. | Better adaptability of the target is distinct from a better actor that redesigns common targets. |
| [AlphaGo Zero](https://www.nature.com/articles/nature24270) | Policy/value model M; search H; self-play trajectories D; game rules in E. | A fixed training/search algorithm can generate a changing policy and data distribution. |
| [POET](https://arxiv.org/abs/1901.01753) | Policy weights in M; environment descriptions and population in D; mutation, optimization, and transfer procedures in H. | Development environments co-evolve with agents. Changing environment descriptions need not change the generator algorithm; finite diversity does not prove unbounded growth. |
| [AutoML-Zero](https://proceedings.mlr.press/v119/real20a.html) | A searches over target learner programs T, with population and evaluations in D. | Discovery of a learning algorithm need not modify the searcher; actor and target must remain distinguishable. |
| [STOP](https://arxiv.org/abs/2310.02304) | Improver program is both editable H and a target T of its own calls. | Reported improvements in generated programs must be preserved; frozen LM weights do not exclude learned program-level improvement. |
| [Promptbreeder](https://proceedings.mlr.press/v235/fernando24a.html) | Task prompts and mutation prompts are addressable state used in different roles. | Represent changes to both task behavior and future mutations without inventing a separate neural improver. |
| [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) | Fixed model/search system A modifies an external program T; population in D. | Exact evaluator-guided discovery is represented without automatically assigning self-modification to A. |
| [SPIN](https://proceedings.mlr.press/v235/chen24j.html) | M produces responses in D and is updated by a declared fixed training procedure H. | Retain dependence on the reference human data distribution; fixed outer code does not imply unchanged learning behavior. |
| [Self-Rewarding Language Models](https://proceedings.mlr.press/v235/yuan24d.html) | The same M supplies answers and training rewards; role-specific prompts in H. | The paper reports three iterations and better reward provision; separate this from proof of broad repeated improvement. |
| [Gödel Agent](https://aclanthology.org/2025.acl-long.1354/) | Executable agent logic H is rewritten from feedback, with retained history D. | Represent arbitrary agent-code edits and the original evaluation conditions. |
| [ADAS](https://github.com/ShengranHu/ADAS) | A meta-agent A searches over task-agent programs T; archive in D. | Allow strong external agent design without assuming the designer itself changed. |
| [AFlow](https://arxiv.org/abs/2410.10762) | Target H is a code-represented workflow; search tree and feedback in D. | Monte Carlo tree search and workflow optimization fit a discrete, state-dependent kernel. |
| [SICA](https://arxiv.org/abs/2504.15228) | Agent source, tools, and policy H are edited by the agent; M can stay frozen. | Keep persistent source changes and benchmark gains separate from broad transfer claims. |
| [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954) | Editable agents H plus an expanding archive/lineage D. | Non-incumbent parents, branching, and stepwise self-edits do not require a smooth trajectory or scalar state. |
| [GEPA](https://arxiv.org/abs/2507.19457) | Prompt/configuration targets, reflective proposal policy, and Pareto records. | Rich textual feedback and non-gradient search must remain allowed. |
| [AgentBreeder](https://arxiv.org/abs/2502.00757) | Multi-agent scaffold H, multiple objectives, and evolutionary population D. | Represent objectives that trade off or conflict; one scalar capability is insufficient. |
| [On the Statistical Limits of Self-Improving Agents](https://arxiv.org/abs/2510.04399) | A constraint on reachable policy classes and statistical feedback. | Preserve the stated i.i.d./capacity assumptions; an expressive state representation does not imply distribution-free learnability. |
| [SEAL](https://github.com/Continual-Intelligence/SEAL) | M generates self-edit data/directives; an update program changes M; RL shapes the generator. | Represent learning how to produce updates while an outer trainer stays fixed. |
| [HyperAgents](https://arxiv.org/abs/2603.19461) | Task-agent and meta-agent code share an editable H; retained experience in D. | The source reports cross-domain meta-level transfer; preserve that report while keeping independent replication separate. |
| [Harness Updating Is Not Harness Benefit](https://arxiv.org/abs/2605.30621) | Actor A proposes harness changes; target executor M uses them. | Recover the experimentally distinct update-producing and update-benefiting roles and their non-monotone relation. |
| [SIA](https://arxiv.org/abs/2605.27276) | A feedback agent proposes target H edits and M updates. | Represent joint editable surfaces without assuming that every update direction is beneficial on every domain. |
| [Recursive Harness Self-Improvement](https://arxiv.org/abs/2607.15524) | A prompt-level agent-loop specification is revised using history and pairwise feedback. | Retain task-specific context/information-flow changes; weight updates are not required for this route. |
| [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227) | Alternative resource/feedback policies and held-out task distributions. | The theory must admit domain-dependent wins and losses against task-time search, not guarantee harness superiority. |
| [Co-Evolving Harnesses and Model Weights for LLM Agents](https://arxiv.org/abs/2607.22688) | H changes trajectory generation; selected D trains M; the schedule alternates. | An actual alternating implementation is an instance, not proof that alternation is universally optimal. |
| [HELIX](https://arxiv.org/abs/2608.13951) | Source-traceable H portfolio produces matched trajectories and training records D. | Reported harness execution and data preparation do not establish a completed model update and rebuild. |
| [HSI](https://arxiv.org/abs/2608.08466) | Task harness, evolver, and meta-evolver are code roles within H under a fixed anchor. | A fixed outer anchor is compatible with changing effective improvement behavior. |
| [EvoHarness-RL](https://arxiv.org/abs/2608.05446) | External workspace D, access interfaces H, and learned coordination policy M. | The boundary between learned policy and external support is declared; learning can reduce redundant harness use. |
| [Auditing Harness Tampering in Self-Improving Agents](https://arxiv.org/abs/2609.00069) | Editable execution/logging paths and an independently recorded assessment protocol. | Observed score can diverge from intended outcomes; changes to measurement are explicit interventions. |
| [HarnessDev](https://arxiv.org/abs/2609.01437) | Creator A builds/evolves target H; executor M is varied separately. | Represent creation, evolution, cost, and creator/executor transfer without conflating their capabilities. |
| [RRSI](https://arxiv.org/abs/2609.24972) | Frozen M; constrained H proposals; history, critic and pruning decisions in D/H. | Regularization, smaller edits, rejected candidates, and lower execution costs are part of the update process. |
| [Meta-Harness](https://github.com/stanford-iris-lab/meta-harness) | A searches full task-specific H around a frozen model; memory/search state in D. | Represent full source-level optimization and fixed-model benefits without requiring model training. |
| [AIDE²](https://arxiv.org/abs/2609.26457) | The AI research agent edits its own code H; search policy/memory changes persist. | Retain author-reported successive rewrites and held-out transfer; do not infer an exponential growth law. |
| [OpenRSI](https://github.com/FrontisAI/OpenRSI) | Search systems H, generated experience D, and trained research models M. | A bounded AI-R&D program can train the improver without claiming general RSI is solved. |
| [MASS](https://github.com/SakanaAI/mass) | Workflow search H alternates with trajectory-based M training; one model fills several roles. | Represent repeated cycles and domain-specific results; no compulsory independent I module. |
| [RSI-Anything](https://github.com/Gen-Verse/RSI-Anything) | World-model/policy parameters M, workflow H, interaction records D, external environment E. | Separate predicted consequences from external feedback and retain domain-specific observation/action spaces. |
| [Dream-RSI](https://arxiv.org/abs/2609.14858) | Discovery-tree replay in D supports exploration-policy changes in H/M. | Separate historical simulation from online feedback and allow a fixed base agent with an improving exploration policy. |
| [Huxley–Gödel Machine (HGM)](https://arxiv.org/abs/2510.21614) | Agent source H, lineage D, descendant-informed parent selection. | Preserve the distinction between current task score and future branch potential; CMP assumptions are not a universal growth theorem. |
| [Agentic Context Engineering (ACE)](https://arxiv.org/abs/2510.04618) | Contextual playbooks D and generation/reflection/curation procedures H. | Persistent context learning is represented even with unchanged weights; include information loss from destructive rewriting. |
| [AlphaEvolve](https://arxiv.org/abs/2506.13131) | Actor A searches target programs T, including infrastructure used by later model training. | Allow feedback through training efficiency and physical resources; trace actual reuse instead of excluding it as merely external optimization. |
| [Optimization by PROmpting (OPRO)](https://arxiv.org/abs/2309.03409) | Candidate/value history D conditions an LLM optimizer A; prompt or other solution is target T. | A fixed model with changing optimization context is representable; persistent actor change remains a separate empirical claim. |
| [STaR](https://arxiv.org/abs/2203.14465) | Generated rationales and answer conditioning in D/H train M. | Preserve the distinction between generated reasoning, correctness filtering, and answer-conditioned rationalization. |
| [ReST-EM](https://arxiv.org/abs/2312.06585) | Reward-filtered D supplies likelihood updates to M. | Preserve the paper's EM assumptions and approximate learning; pooled filtering may change task marginals. |
| [Expert Iteration](https://arxiv.org/abs/1705.08439) | Search-derived targets update M, which guides subsequent H search. | Preserve the distinction between planning improvement and inheritance. |
| [DreamCoder](https://www.neurosymbolic.org/papers/EllisWNSMHCST21.pdf) | Both the program library D/H and recognition model M change. | The representation can change, rather than only parameters in a fixed search language. |
| [Selecting Computations](https://arxiv.org/abs/1207.5879) | A metalevel policy chooses computations and stopping under costs. | Information value and candidate improvement are different; selector computation is not free. |
| [LevinTS](https://arxiv.org/abs/1811.10928) | H searches using a path distribution supplied by M or another policy. | Positive solution mass, verification and valid state cuts are required for its bounds. |
| [Policy-guided Heuristic Search](https://arxiv.org/abs/2103.11505) | H combines a policy and a heuristic; learned components can be updated. | Retain the difference between solution cost and search cost. |
| [LTS with context models](https://www.ijcai.org/proceedings/2023/0624.pdf) | Search-found paths D train context parameters M used in later H search. | Fixed-path convexity is narrower than a convergence result for the entire bootstrap loop. |

| [OpenAI o1: Learning to reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/) | Policy learning changes the distribution of reasoning trajectories and the value of later inference. | Train/test compute scaling does not identify a self-improving research process. |
| [DeepSeek-R1](https://arxiv.org/html/2501.12948v1) | Sampling, reward-weighted policy updates and subsequent data production jointly change the learning distribution. | A fixed trainer is compatible with self-generated learning, but the paper does not establish indefinitely improving research ability. |
| [Qwen3 Technical Report](https://arxiv.org/html/2505.09388v1) | A learner-generated state distribution and teacher targets interact with capacity and reasoning budget. | Teacher-provided information and small-model efficiency do not establish teacher-free recursive discovery. |
| [AlphaProof](https://www.nature.com/articles/s41586-025-09833-y) | Verification supports reusable proof learning while generated variations alter the curriculum. | Formal proof correctness is conditional on the formal statement; it does not establish fidelity of every autoformalization or broad research recursion. |
| [MuZero](https://arxiv.org/abs/1911.08265) | Task-relevant dynamics learning changes both planning and the experience used for future updates. | Planning within an imperfect learned model differs from search in a known exact environment. |
| [Open-Ended Learning Leads to Generally Capable Agents (XLand)](https://arxiv.org/abs/2107.12808) | Task generation changes the learnable frontier and population transfer changes reachable skills. | Broadness within a constructed environment space is not unrestricted real-world generality. |
| [SIMA 2](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/) | Tasks, estimated rewards and visited states jointly determine the training distribution. | The official self-improvement report does not show that Genie itself recursively improves or that physical-world transfer is established. |
| [Constitutional AI](https://arxiv.org/abs/2212.08073) | Feedback production can be delegated to AI while the objective and calibration remain external. | The normative target remains externally specified; AI feedback is not automatically accurate or independent. |
| [Self-Taught Evaluators](https://arxiv.org/html/2408.02666v1) | Better judgment generation changes the usable training pool for later evaluator versions. | Constructed preference labels can be imperfect; the student is reset to the seed each round rather than simply continuing fine-tuning. |
| [Eureka](https://arxiv.org/abs/2310.12931) | A proposed artifact is valued by the learning process it induces, not only by immediate execution. | Useful reward optimization does not establish that the LLM reward designer itself becomes a stronger designer. |
| [Co-Scientist](https://arxiv.org/abs/2502.18864v2) | Search supplies hypotheses whose true value requires delayed external experimentation. | Internal hypothesis rankings are not scientific truth; validated hypotheses do not alone prove an improved research policy. |
| [GPT-Red](https://cdn.openai.com/pdf/gpt-red-automated-red-teaming-via-self-play-at-scale.pdf) | Changing opponents generate a moving learning frontier; population diversity can prevent narrow adaptation. | Task-specific robustness improvement and co-training do not establish unrestricted recursive research acceleration. |
| [Automated Alignment Researchers: mitigating alignment failures](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures) | A research policy chooses interventions whose value is measured after target-model training. | Improving target models does not show that the researcher improves itself; production data-efficiency claims are not full research-cost ratios. |
| [Seed for Seed (Seed2.1)](https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity) | Useful model-development outputs can feed later model development through several operational paths. | A deployment report supports use in AI development, not an identified causal multiplier or autonomous closed-loop growth. |

See [MECHANISMS.md](MECHANISMS.md) and the [per-work mechanism map](research/mechanism-map.md) for conditional explanations and separating interventions beyond this representation table.

## What would count as cross-method prediction

Choose interventions that exist in several methods—freeze the proposer, replace the executor, alter candidate selection, vary feedback exposure, or train from a controlled trajectory source. Declare the observable, resource accounting, and task cohort before fitting. Fit on one set of methods and generations, then predict the sign and size of effects on held-out methods, tasks, and future generations. Compare with fixed-improver, independent-component, and budget-only explanations. A separate free parameter for every method/outcome is description, not demonstrated transfer.

Specify which observations distinguish competing mechanisms that fit the existing results. THEORY.md Proposition 4 gives an exact case where arbitrarily many observed runs cannot determine even the sign of a new intervention. Transfer requires a stated shared mechanism or assumption, with a result that could refute it.

The existing corpus supplies implementations and counterexamples that a model must admit. It does not yet supply a harmonized intervention dataset that proves one quantitative growth law across them. The current simulations are not such a dataset.

## Scope and scientific value

Compatibility means preserving a method's causal operations, assumptions, and valid results, including its failure conditions. It does not mean accepting every author's interpretation, requiring every method to reach D3, or prescribing one architecture for every regime. For each mechanism family, ask what changes, what supplies feedback, and how the retained change affects later behavior.

Prioritize a work when a checkable claim contributes a distinct mechanism, a valid derivation or counterexample, a discriminating experiment, or a usable research artifact. Match scrutiny to the claim: theoretical work needs explicit assumptions and a sound argument; empirical claims need the controls and observations that support their stated scope. Code, prestigious venues, citations, or positive outcomes are not universal admission requirements.

Deprioritize unsupported assertions and redundant renamings that add no mechanism, evidence, or test. Judge individual claims rather than excluding an entire work solely for weak framing. Writing style or suspected AI assistance does not establish scientific quality. Negative results, small counterexamples, and rigorous work outside the current preferred route remain relevant.

The corpus is an expandable mechanism audit, not an exhaustive ranking of the field. Representing physical interaction does not establish a physical growth law: measured resource-to-computation relations, environmental constraints, and validated predictions at that level remain outstanding.

The finite-budget continuation identity in THEORY.md Section 9 uses the same
encoded state and permits every listed update surface. That establishes the
identity's representational scope. It does not supply the individual methods'
unknown transition probabilities, continuation values or physical costs.

<!-- scope-expansion -->
## Scope-focused expansion mappings

These mappings preserve named artifacts; they neither prove recursion nor supply a predictive theory. See RSI_SCOPE.md for distinctions.

| Work | Artifacts requiring representation | Boundary |
|---|---|---|
| [SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness](https://arxiv.org/abs/2609.20519) | harness_code | 论文把用新 harness 加速后继研发列为未来方向；成本下降不是已测递归复利。 |
| [ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement](https://arxiv.org/abs/2609.14857) | harness_code, function_library | 模块独立优化后存在交互；跨模型迁移不等于改进能力持续提升。 |
| [Prime Agent: A Self-Improving RLM Harness](https://arxiv.org/abs/2608.23552) | memory, skills, prompts, subagent_specifications | 递归子代理调用本身不是 RSI；摘要没有隔离后继作为改进者的贡献。 |
| [The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators](https://arxiv.org/abs/2606.26294) | agent_code, evaluator_code, archive | IMO 人工评分等外部锚点仍必要；论文写作的代理评分不能等同真实科研质量。 |
| [Dr. Zero: Self-Evolving Search Agents without Training Data](https://arxiv.org/abs/2601.07055) | proposer_weights, solver_weights | 零人工 QA 训练样本不等于零外部知识；仍依赖预训练和搜索引擎。 |
| [Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills](https://arxiv.org/abs/2607.22529) | proposer_weights, solver_weights, skill_library | 可执行验证与技能覆盖仍有边界，能力前沿难度代理不等于真实长期学习增益。 |
| [RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System](https://arxiv.org/abs/2602.02488) | policy_weights, reward_weights, task_descriptions | 环境变化并非任意世界创造；GUI 部分依赖预建扰动及其验证器。 |
| [Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning](https://arxiv.org/abs/2511.16043) | curriculum_weights, executor_weights | 工具与预训练提供外部能力；多轮共同训练不证明通用研发递归。 |
| [R-Zero: Self-Evolving Reasoning LLM from Zero Data](https://arxiv.org/abs/2508.05004) | challenger_weights, solver_weights | 自生成题目和标签可能共同偏误，不能由内部奖励证明正确性。 |
| [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335) | model_weights, generated_tasks | 无需新人工数据仍依赖预训练、执行语义和初始任务表达范围。 |
| [Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data](https://arxiv.org/abs/2602.21320) | generator_weights, solver_weights | 工具接口和答案校验限定可学空间；不能把相对增幅当跨基准绝对优势。 |
| [EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for Autonomous Agentic Reinforcement Learning](https://arxiv.org/abs/2606.03108) | policy_weights, training_harness, diagnostic_skills | 基础训练代理权重固定且昂贵动作有人类把关；不支持完全无人递归。 |
| [AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation](https://arxiv.org/abs/2605.28655) | research_memory, team_coordination, target_training_code | 生物研究部分不是本项目核心；目标 GPT 训练优化不证明研究代理自我升级。 |
| [Dual-Evolving Reinforcement Learning for Automated Reward Design](https://arxiv.org/abs/2512.13399) | reward_proposer_weights, reward_programs, policy_weights | 奖励原语由人指定；最终策略重新训练，不能描述成同一策略连续自改。 |
| [GEAR: Genetic AutoResearch for Agentic Code Evolution](https://arxiv.org/abs/2605.13874) | research_population, search_controller | 固定控制器的另外两个变体不是改进器自修改，不能合并宣称递归。 |
| [Towards Execution-Grounded Automated AI Research](https://arxiv.org/abs/2601.14525) | ideator_weights, research_archive, target_training_code | RL 平均奖励上升同时出现模式坍缩，上限改善未建立；并未训练自身后继。 |
| [Meta$^n$: Recursive Self-Improvement through Emergent Depth](https://arxiv.org/abs/2608.24735) | helper_code, layer_stack, archive | 固定元操作不自动保证整体稳定；层数与真实改进效率不可混同。 |
| [Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498) | harness_code | 自己提出修改不自动证明后继更会修改；同基准划分与跨领域迁移不同。 |
| [Harness-Zero: Harness Distillation via Agent-as-Harness](https://arxiv.org/abs/2609.24974) | model_weights, training_demonstrations | 展示内化与部署收益，未据摘要证明多代改进器闭环。 |
| [Harness-R1: Learning to Edit Executable Runtime Harnesses from Agent Failure Trajectories](https://arxiv.org/abs/2608.02276) | engineer_weights, harness_code | 主训练只更新编辑者、目标冻结；论文指向共同进化，未证明持续双向循环。 |
| [SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning](https://arxiv.org/abs/2602.08234) | policy_weights, skill_library | 技能压缩可能丢失适用条件，特定基准增益不证明通用递归能力。 |
| [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/abs/2605.23904) | skill_document, optimizer_state | 外部技能优化与优化器自改不同；重复验证选择仍需最终未触碰测试。 |
| [Mem$^2$Evolve: Towards Self-Evolving Agents via Co-Evolutionary Capability Expansion and Experience Distillation](https://arxiv.org/abs/2604.10923) | experience_memory, asset_memory | 资产增加不保证改进速度上升，组合依赖和维护成本尚须控制。 |
| [MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents](https://arxiv.org/abs/2602.02474) | controller_weights, memory_skills | 设计者本身是否改进未确定；技能选择和技能生成的贡献需分离。 |
| [MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory](https://arxiv.org/abs/2601.03192) | episodic_memory, retrieval_values | 持久记忆学习成立不等于记忆更新规则或改进能力已自进化。 |
| [EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management](https://arxiv.org/abs/2606.03841) | policy_weights, executable_skills, context_policy | 数据科学成绩与生成后继研究者能力不同；摘要定理不能代替逐项假设核查。 |
| [Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails](https://arxiv.org/abs/2609.09134) | harness_code, model_weights | 整轨迹模仿在已进化 harness 上退化；局部纠正平均增益有限，不是普遍最优。 |
| [Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Technical Report](https://arxiv.org/abs/2608.15763) | model_weights, harness_augmentation | 兼容变化中的 harness 不等于 AI 自己设计或进化该 harness。 |
| [RewardHarness: Self-Evolving Agentic Post-Training](https://arxiv.org/abs/2605.08703) | reward_tools, reward_skills | 初始人类偏好是锚点；奖励器自改与被训练模型回馈奖励器须区分。 |
| [WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model](https://arxiv.org/abs/2504.21024) | agent_weights, world_model_weights | 模型想象会积累偏差，真实网页验证不能由世界模型自身评分替代。 |
| [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://arxiv.org/abs/2411.02337) | policy_weights, task_curriculum | 课程反馈闭环不同于训练算法自改；目标领域仍限定在网页任务。 |
| [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://arxiv.org/abs/2501.04519) | policy_weights, process_reward_weights | 外部题库与执行验证仍支撑学习；数学域共同进化不是开放科研闭环。 |
| [Self-Evolved Reward Learning for LLMs](https://arxiv.org/abs/2411.00418) | reward_weights, synthetic_preferences | 有限人工标注和预训练仍是信息锚点；自反馈可能积累偏差。 |
| [Self-Evolving Curriculum for LLM Reasoning](https://arxiv.org/abs/2505.14970) | curriculum_policy, model_weights | 固定课程更新律是自适应训练，不自动构成改进器递归重写。 |
| [SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills](https://arxiv.org/abs/2504.07079) | executable_skill_library | 技能积累和任务迁移不等于技能发现过程效率持续上升。 |
| [Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?](https://arxiv.org/abs/2511.13646) | runtime_scaffold | 同任务内自改与跨任务继承是不同证据，不能从 solve rate 推出代际增长。 |
| [Group-Evolving Agents: Open-Ended Self-Improvement via Experience Sharing](https://arxiv.org/abs/2602.04837) | agent_code, shared_experience | 同进化个体数不保证同算力；探索多样性的价值需与开销分开。 |
| [Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams](https://arxiv.org/abs/2606.01770) | harness_tree, evolver_state, routing | 部分信号来自人类引导；路由收益不等于改进器变强。 |
| [Continual Harness: Online Adaptation for Self-Improving Foundation Agents](https://arxiv.org/abs/2605.09998) | prompts, subagents, skills, memory | 早期 GPP 人类参与与后续自动循环必须分开，游戏进度不直接代表通用研发能力。 |
| [EnvHarness: Awakening Static Worlds for Agent Learning](https://arxiv.org/abs/2608.19880) | environment_wrappers, policy_weights | 环境包装保留验证器是特定设计，不保证所有新任务忠实有效。 |
| [Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design](https://arxiv.org/abs/2605.15871) | target_architecture, target_training_code | 发现目标模型架构不等于将目标用作下一代设计者。 |
| [AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement](https://arxiv.org/abs/2608.20318) | evaluation_protocol | 它测研发能力而非运行多代 RSI，归一化分数仍依赖所选任务和参照。 |
| [Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement](https://arxiv.org/abs/2609.13406) | formal_configuration | 属于可重写组件不等于实际发生有效重写；表示统一不是经验泛化定律。 |
| [Aspire: Can Models Self-Evolve from Vague Goals?](https://arxiv.org/abs/2608.31111) | model_weights, harness, training_data | 完成训练或编辑流程不等于提高能力；报告中增益稀疏且不稳定。 |
| [Large Language Model Agents Are Not Always Faithful Self-Evolvers](https://arxiv.org/abs/2601.22436) | experience_interventions | 对经验不敏感可来自已有知识或压缩丢失，不能一概判为无学习。 |
| [ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution](https://arxiv.org/abs/2509.19349) | target_programs, archive, model_selection | 只有目标涉及 AI 训练/harness 时属直接 AI4AI；普通圆堆积不算自身进化。 |
| [CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution](https://arxiv.org/abs/2603.17775) | generator_weights, verifier_weights | 多数投票仍提供噪声标签，摆脱部分共识错误不保证无锚点真理发现。 |
| [Actor-Curator: Co-adaptive Curriculum Learning via Policy-Improvement Bandits for RL Post-Training](https://arxiv.org/abs/2602.20532) | curator_weights, policy_weights | 课程控制器的学习不同于其自身更新算法被改进。 |
| [Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence](https://arxiv.org/abs/2604.18292) | policy_weights, generated_environments, task_curriculum | MCP 环境主题多不等于未见世界泛化，生成器和验证器来源需全文核查。 |
| [SkillOS: Learning Skill Curation for Self-Evolving Agents](https://arxiv.org/abs/2605.06614) | curator_weights, skill_repository | 改善技能整理者是有价值的 AI4AI，但其更新流程未被自身改写。 |
| [Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills](https://arxiv.org/abs/2606.07412) | solver_weights, trace_skills, generated_tasks | 梯度对齐作为学习价值代理需检验；软件领域闭环未推出通用科研提升。 |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | executable_skill_library, exploration_state | 固定 GPT-4 与课程程序；技能复用不是已证元算法自改。 |
| [AgentEvolver: Towards Efficient Self-Evolving Agent System](https://arxiv.org/abs/2511.10395) | policy_weights, task_curriculum, experience | 训练闭环的元过程仍有固定部分；高效率需全流程成本而非仅样本数。 |
| [Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning](https://arxiv.org/abs/2607.21971) | model_weights, evolution_training_data | 改进目标代码不等于目标本身是改进器；需实际闭环继承证据。 |
| [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.14777) | policy_weights, hindsight_skills | 训练期事后信息在部署不可见；内化效果与信息泄漏边界需明确。 |
| [RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning](https://arxiv.org/abs/2505.15034) | generator_weights, verifier_weights | 不是完全无标签自证；固定结果验证构成外部锚点。 |

## Coverage correction: four previously missing large-model studies

These four mappings extend the indexed bibliography to 127 works. Naming the artifacts establishes representational compatibility only; it does not prove a universal predictive theory or validate the reported performance.

| Work | Artifacts and return path | Boundary |
|---|---|---|
| [Iterative RPO](https://arxiv.org/html/2404.19733v2) | Updated model M generates the next preference dataset D; fixed DPO plus positive-example likelihood procedure H updates M. | Retain external answer labels, 70B target, repeated rounds and saturation; the learning algorithm does not learn to redesign itself. |
| [DeepSeekMath-V2](https://arxiv.org/html/2511.22570v1) | Role-indexed generator and verifier parameters in M; proofs and verified annotations in D; sampling, meta-verification and training orchestration in H. New proofs update the verifier, which supplies feedback for the generator. | Preserve informal-verification error, expert assessment and search budgets. This is not a proof of unrestricted recursive research acceleration. |
| [Kimi K2](https://arxiv.org/html/2507.20534v1) | Actor and critic parameters in M; on-policy traces and preferences in D; rubric, verifiable feedback and RL orchestration in H. The critic updates from verifiable policy traces and feeds policy learning. | The report describes the loop, but the contribution of that loop to every final benchmark result is not causally isolated. This row concerns the post-training mechanism, not a claim that the whole training pipeline is RSI. |
| [Large Language Models Can Self-Improve](https://aclanthology.org/2023.emnlp-main.67.pdf) | A 540B model M generates reasoning data D; self-consistency filtering and SFT in H update M. | An early large-model self-training precursor, not demonstrated indefinite or multi-generation recursive improvement. |
