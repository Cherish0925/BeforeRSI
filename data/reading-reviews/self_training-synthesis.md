# 模型自训练、自博弈、任务与课程生成：87项原文比较综合

本文件对应 `self_training.jsonl` 的全部87项。61项完成主文、实验、限制与相关附录的本轮全文阅读；26项已有完整原文阅读记录，本轮复核关键方法、结果与边界。每项卡片保留来源URL、原始哈希和章节/表号。没有以抓取全文代替阅读，也没有按预设比例保留。

最终取舍为16项core、11项support、52项mechanism_supplement、4项redundant、4项insufficient；无来源阻塞。route为74项model、9项crosscut、4项background。core约18.4%是逐篇判断的结果，不是20%配额。52项小模型机制补充仍完整可查，不等于低质量；support与core也不由模型大小直接决定。

## 先辨认真正被改进的对象

本组最容易混淆的是“系统里有工具、检索、经验池”与“工具/训练框架本身在演化”。TTT-Discover更新gpt-oss-120B的LoRA，固定PUCT搜索和候选档案帮助找到好程序；档案里是目标解，不是被优化的harness。它因此属于Model核心，可连接程序搜索路线。NeoHorse-1的router供应轨迹和分层信息，本作不训练router，且只验证初次evaluation–selection–update；已由hybrid改为model。Harness-R1学习产生框架编辑的策略，但编辑产物不跨训练任务持续继承，主轴仍是编辑能力写入模型。

EvoHarness-RL另有跨batch的可编辑经验资产，和持续策略训练有实质互作，可在Model主线外保留Hybrid关系。AgentEvolver却不能因同有经验模块就获得相同结论：其§4.1明确从初始策略轨迹离线建库，在线指检索；重要贡献是用经验引导rollout、优化时删除经验提示，再调整裁剪以内化轨迹。它没有充分证明经验库和出题器随学生多代共同更新。AgentEvolver的Qwen-Plus、235B任务judge、Qwen-Max归因器均固定，学生是7B/14B。

## 三类数据来源不可混为“自己生数据”

第一类是固定强教师的数据制造。Orca、WizardLM和AskToAct主要说明如何蒸馏、改写、补齐工具调用情境；多次生成或多轮改写不代表学生反馈进入生成器。WizardLM确实训练到65B/70B，但这一事实不能把静态Evol-Instruct自动升级为强闭环。AskToAct保留全卡，详细主叙事移出至redundant。

第二类是学生改变下一轮选什么，但强教师不变。Arena Learning最有代表性：当前学生在哪些题落败，决定下一轮强对手响应、偏好和奖励训练数据。其最大学生为141B总参数/39B激活，7B实验另列。每轮SFT重启原始base，再走DPO/PPO；继承的是数据和用于对战的上轮模型，而非始终接着上轮权重训练。通用知识四项平均未超过官方同基座后训练版本，不能把竞技偏好进步写成全面知识超越。Arena据此升为core enabler，固定教师与重启事实同时保留。

第三类是生成与评价能力都更新。GPT-Red的攻击者和多个防御者共同RL，受控冻结攻击者对照支持非平稳对手的价值；产品GPT-5.1到5.6又混入其他训练，应与受控实验分开。DeepSeekMath-V2将新证明变成下一轮验证器难例，用meta-verification约束虚构批评，最后两轮标签完全自动。Kimi K2把可验证任务rollout用于持续校准critic，再用于开放偏好；这是工业规模的明确设计，但缺独立critic更新消融。三者均不证明训练算法自行重写。

## 继承权重与重启基座，是两种不同学习机制

STaR、ReST-EM、STRIVE、SOAR、AgentGym、Arena和Self-Taught Evaluators均需明确各轮何处重启。ReST-EM直接比较每轮base重启与接续训练，重启在某些迁移任务更好；它是反复改进采样分布后重新拟合，而非积累无限参数记忆。SOAR每轮从base训练，但程序合成器与修复器会因历史数据变化而改进，并在新ARC任务上再适配；其123B结果、6k候选搜索与52%多模型集合成绩分开。

SPIN持续替换自产负例与参考模型，R-Zero类持续训练出题/解题角色，SRT每个RL步刷新多数标签，反馈误差因而可能更快积累。是否持续继承不是优劣判据，却决定漂移机制、成本和比较基线。RoboCat、PLD、UniCorn、UI-Genie、WebEvolver还应标清实验轮次：RoboCat主要展示一次自采集回流；PLD是一轮探针探索—残差学习—蒸馏；UniCorn只有一个完整生成/训练周期；UI-Genie的72B是最后一次SFT，实际迭代闭环主要7B；WebEvolver先做两轮policy/world-model训练，再固定world-model扩充策略数据，不能画成无限交替共演化。

## 验证锚点决定闭环能相信什么

执行反馈最强也有边界。AZR用程序执行构造任务与标签，AlphaProof用Lean内核检查最终形式证明；它们比单纯多数票更接近独立正确性约束。SQL-Zero的SQL可执行不保证与自然语言意图一致；SVG渲染不保证MM-Zero问题的语义正确；单元测试通过不保证测试本身完备。ZeroCoder把代码和测试交叉执行，用一致性和mutation构造训练信号，但其最强DyB4仍依赖10个带标签样本持续校准，并非零监督；mutation与执行是主要时间成本，校准占2%不等于全部额外成本2%。

检索环境提供外部信息，却通常不直接给最终正确答案。Dr. Zero和EVE-Agent与纯自包含投票相邻而不等同；ReST meets ReAct使用搜索信息、固定强模型排序及实际PaLM2-L权重迭代。其Bamboogle用于验证，另造BamTwoogle留出测试，须分别展示；未知参数量不能当成小模型排除。

自然语言judge更灵活，必须分辨“判断与标签一致”“批评理由忠实”“真的能使另一个模型学得更好”。Self-Taught Evaluators的70B反复学习符合合成偏好的评价推理，静态judge基准明显提升，但没有实际下游policy训练。Self-Improving VLM Judges把思路用于11B视觉裁判，部分任务回落，5/16高频阈值不是多数真值。EvoLM进一步测rubric指导训练，却在换模型、judge或代码任务时有回退；判别能力不能直接替代可教学性。

RL Tango和rStar-Math有最终答案锚点，过程信用仍须谨慎。Tango的过程判断不是独立逐步金标签，主数学实验缺双侧冻结全套消融；rStar每轮policy从base重启，PPM从该轮SFT起点训练，强搜索成绩不能冒充greedy。ARCO用终局结果监督rubric分解，逐步贡献并不因此可识别。CoNL以相对评分变化奖赏critic，存在多候选选优混入pass@1和因果效用难分的问题；PDF两例确有数学错误，但insufficient的依据是这些证据边界共同存在，绝不是用例错直接否定全部主表。

## 失败证据各自解释不同层面

SRT保留为crosscut core：跨模型、长程训练、课程与优化控制比单个“涨后跌”图更有解释力。它也报告未崩条件，例如部分较强模型/任务、较低学习率、课程调整以及固定教师控制，不能缩成“自训练必崩”。Self-Improvement Can Self-Regress的成功率按每步不同题估计，所谓阈值尚混有难度变化，证据不足以替代SRT。

Phantom Gains同样是crosscut core，却审计另一问题：小样本、随机生成、checkpoint选择及多重尝试，能否在不更新能力时产生相似涨幅。它提出实测null和成本记录，不能用来断言所有自训练无效。SRT关注训练分布与优化漂移，Phantom关注观测与选择噪声。Understand Self-Play、EMPO、DIVE的high-k结果又提醒，pass@1提升可能来自重分配已有能力；这不等于没有实用价值，也不等于已发现全新推理算法。

## AI4AI需要看研究对象和最终计算收益

Towards Execution-Grounded Automated AI Research进入Model/core：实际训练Qwen30B总/3B激活的ideator，候选经过固定实现器与真实预训练/后训练执行。强化学习改善提议平均质量的证据，不能混同固定前沿模型搜索得到的最优训练方法。其pretraining搜索速度提升与post-training得分提高有工程意义，但RL未明确带来同样幅度的极值进步，也没有跨任务/规模留出研究泛化。

TTT-Discover则直接在单个发现任务上训练模型，并以可核验程序/数学构造作为产物。它和AlphaEvolve的关系是搜索环境、候选复用与在线模型更新的交叉，不是已演示harness递归改写。INTELLECT-3作为support保留：实际106B后训练和开放异步RL栈使更复杂闭环可实行，但难度池更新仍是普通自适应课程，训练器由研究者设计。512H200两个月包括SFT、RL及消融；实际RL480H200、约1500秒/步，不能将全项目成本当单次净RL。

## 规模与证据的最终呈现

16个core中，9个有可核的≥27B实际Model训练对象：LMSI540B、TTT-Discover120B、SOAR123B、Arena141B、WebEvolver70B、Execution-Grounded30B、Self-Taught Evaluators70B、DeepSeekMath-V2名义671B、KimiK2 1040B。Math-V2官方权重页另显示685B文件统计，不能不加说明与基座名义参数混用。

4个闭源Model core规模未知：ReST meets ReAct、ReST-EM、SIMA2、GPT-Red。AlphaProof再单列“已知proof network3B，实际微调Gemini1.5Pro autoformalizer规模未知”：不能写只有3B，也不能据此计confirmed≥27B。其自动形式化器有STaR反馈，最终Lean保证只覆盖形式命题；自然语言到形式命题仍需检查。最高500TPUdays是平均每题评测预算，联合AlphaGeometry2的银牌成绩不应全归AlphaProof。

其余两个core是SRT与Phantom Gains这类跨路线证据节点，不冒充≥27B Model主线。UI-Genie72B和INTELLECT-3 106B仍可为support：前者大模型未参与主要迭代、后者贡献重在基础设施。较小模型的52个机制补充用于解释有价值的设计与失效，不参与强制配额。

## 关系终审与取舍留痕

共修正28条原“source_explicit extends”等过强关系：区分明确方法组件复用、实际基线比较和分析性互补。例如SOAR明确扩展CodeIt，但对STaR只是方法比较；WebEvolver引用ReST+ReAct不等于继承其实现；AgentEvolver明确使用ReMe；Self-Improving VLM Judges在方法位置明确引用自训练筛选思想，只保留组件借鉴；Tool-R0、OpenSIR、MM-Zero、G-Zero与R-Zero相邻并不自动形成直接继承链。所有关系仍在逐篇卡片给出位置。

4项redundant为Self-Guide、STRIVE、WebSynthesis、AskToAct：全卡保存，其特定任务/数据操作不作为详细主叙事的必需节点。4项insufficient为Self-Regress、SAGE、Agent0-VL、CoNL：相关思路保留，主要因关键机制/隔离证据或协议披露不足，不称无价值或劣质。

额外PDF复核来源已记入卡片：Agent0-VL提示与奖励、CoNL原始数学例、Arena首页机构，以及AlphaProof补充材料/表1。部分复核文件暂在/tmp，最终打包时应随原文证据一同持久保存。每项最终定位优先章节、表、公式，避免中央提取修订后的行号漂移。
