# Evidence and judgment

This document separates scientific value from the label attached to a project. A work can be useful without being RSI. A work can also contain a genuine result while making a broader claim than its evidence supports.

The current catalog separates relevance from demonstrated recursion. See [RSI_SCOPE.md](RSI_SCOPE.md): 66 direct self-evolution studies, 31 enablers, 7 evaluations, 3 theories, 14 foundations and 6 background entries. A primary abstract screen is not a full quality review.

## 1. The evidence test

For a claimed update $S_t\rightarrow S_{t+1}$, ask seven questions:

1. **What changed?** Response, prompt, memory, tool, harness code, model weights, optimizer, evaluator, or improver.
2. **What supplied the change?** The system itself, a stronger fixed model, human engineering, search, or hidden tests.
3. **What persisted?** Did a versioned successor survive beyond the current task?
4. **What transferred?** Same benchmark, held-out rows, time-forward tasks, new domains, new model families, or new environments.
5. **What was the matched baseline?** Parent with equal inference, search, training, and evaluator budget.
6. **What regressed?** Task-level failures, cost, latency, reliability, calibration, or unrelated capabilities.
7. **Did the successor improve later improvement?** Was $S_{t+1}$ compared with $S_t$ as an improver?

The last question targets this repository's stronger D3 claim. Other papers may use RSI for recursive reuse; preserve their definition and separately state what was measured.

## 2. What the historical branches establish

### Good and the intelligence-explosion argument

**Value:** identifies the possibility that machine-design ability could create positive feedback.

**Established:** a qualitative argument.

**Unestablished:** a realizable update process, a growth law, evaluator stability, and whether improvement accelerates rather than saturates.

Treating Good’s argument as a prediction confirmed by current agents is unsupported.

### EURISKO

**Value:** early evidence that heuristic rules can be represented as editable objects and that a system can generate heuristics affecting later search.

**Established:** self-modification of heuristics in bounded, hand-engineered representations.

**Unestablished:** scalable transfer, reproducibility under modern standards, model-level learning, and sustained improvement of the improver.

EURISKO is historically central. It is not evidence that modern open-ended RSI has already occurred.

### Gödel machines

**Value:** the cleanest formal statement of self-reference, utility-preserving self-rewrite, and modification of the proof searcher itself.

**Established:** conditional theoretical properties under the encoded axioms and proof requirements.

**Unestablished:** tractable discovery of useful proofs in realistic AI systems.

The work is conceptually important and operationally distant from current LLM agents.

## 3. Strong adjacent work that should not be called RSI by default

### Meta-learning and self-play

MAML, AlphaGo Zero, and related work establish that learning behavior can be shaped across tasks and that self-generated experience can produce capabilities beyond supervised imitation. Their objectives, update algorithms, and acceptance rules remain externally specified.

They answer “can a system learn to adapt?” They do not by themselves answer “can a successor improve the procedure that creates later successors?”

### AutoML and algorithm search

AutoML-Zero, FunSearch, AlphaEvolve, and similar systems automate parts of algorithm discovery. Their output can be scientifically or commercially valuable. The actor may remain fixed while improving an external artifact. AlphaEvolve additionally reports optimizing training components used by its underlying LLM, so feedback into later system versions or resource efficiency is a possible path that must be traced rather than excluded by definition.

These systems are essential baselines for automated AI research. The actor-target distinction preserves both external algorithm discovery and cases where discovered changes return to improve the producing system.

### Prompt, workflow, and agent search

ADAS, AFlow, GEPA, AgentBreeder, OPRO-like methods, and prompt optimizers can discover better agent configurations. They belong in BeforeRSI when they provide a strong comparison or expose transferable design principles.

Their default claim depth is D0 or D1. They reach D2 only after untouched transfer. They reach D3 only if the improved system becomes a better generator of later improvements.

## 4. Direct modern evidence

### STOP and Promptbreeder

These works are important because the update rule enters the editable state.

- STOP improves an improver program while leaving the underlying language model fixed.
- Promptbreeder evolves both task prompts and mutation prompts that generate future mutations.

They demonstrate bounded self-reference. Their evidence does not establish broad, multi-generation system improvement.

### Gödel Agent and SICA

These systems make executable agent code editable. The parent–successor relation is concrete, and modifications can affect future tasks.

The main limitations are benchmark concentration, dependence on a strong fixed model and evaluator, small numbers of generations, and limited cross-model transfer. They establish a route to persistent self-modification. General RSI remains unestablished.

### Darwin Gödel Machine and HGM

DGM contributes open lineage: unsuccessful or non-incumbent branches can later become useful ancestors. HGM raises parent selection to the level of future branch potential.

The scientific question is whether lineage and clade selection improve future transferable gain under matched cost. A richer archive can outperform greedy search simply by spending more evaluation. The comparison must control candidate count, evaluator exposure, and total compute.

### HyperAgents and HSI

These systems move more of the meta-level into the editable program. This is closer to D3 because task-agent and meta-agent behavior, or harness and meta-evolver behavior, can both change.

Hyperagents explicitly reports meta-level improvements that transfer across domains and accumulate across runs. That report must be retained. The remaining audit is whether the experiments isolate common-target improver effects and how independently the result can be replicated; HSI must be assessed on its own evidence.

### AIDE²

AIDE² is one of the strongest public multi-generation claims. The authors report repeated accepted rewrites of an AI research agent, fixed-budget evaluation, and transfer to held-out AI-R&D benchmarks.

The [full method](https://arxiv.org/html/2609.26457v1) keeps the main outer
proposer fixed while editing the inner research agent. Its separate ignition
test replaces the outer proposer on common starting targets; superiority over
the strong reference proposer is not decisively established. Thus improved
research behavior and improved outer-agent production remain distinct findings.

The result changes the prior belief that self-rewriting research agents can only produce isolated one-step gains. It does not yet establish open-ended RSI. The reported run is author-produced, the task family is AI R&D, the number of accepted generations is small, and independent end-to-end reproduction is still needed.

### RRSI, Meta-Harness, RHI, and related harness systems

Harness evolution has produced the clearest inspectable gains around frozen models. RRSI explicitly addresses edit size, benchmark-specific logic, evaluation noise, token cost, and pruning. Meta-Harness exposes full source code. RHI and related methods optimize task-specific harness specifications from trajectory feedback.

The strongest limitation is portability. A harness can encode task-family structure, compensate for one model’s defects, or alter resource use. Transfer across a few related benchmarks does not imply a universal harness improvement.

### Harness Updating Is Not Harness Benefit

This result is central because it splits a vague capability into two measurable ones:

- producing a useful harness update;
- exploiting the updated harness during task execution.

The reported non-monotonic relation between base-model strength and harness benefit directly contradicts the simple belief that a stronger model will always gain more from harness evolution. It motivates separate evolver and executor models, cross-model transfer matrices, and scale-dependent experiments.

## 5. Model-level self-improvement

### SPIN and iterative self-training

SPIN shows that a model can improve through iterative interaction with previous versions under an externally specified training procedure.

The main uncertainty is long-run information quality. If each generation learns mainly from the distribution already represented by earlier generations, gains can saturate and rare capabilities can disappear. External data, verifiers, or environment interaction may be necessary to keep the loop informative.

### Self-Rewarding Language Models

These systems use the model to generate reward or preference labels and update the model from them. They test whether task ability and judging ability can improve together.

The primary paper reports three iterative training rounds and improvements in both instruction following and reward provision. This is positive evidence for co-improvement under a fixed outer training rule. It does not by itself establish a universal growth law or independent replication. Correlated generation/judgment errors still require external assessment.

### SEAL and self-generated updates

SEAL makes the content of model updates an output of the model. This is closer to model-level self-improvement than ordinary self-training.

Recursive reuse is distinct from increased update-producing ability. The stronger D3 claim requires a controlled comparison of earlier and later systems as improvers; claims about sustained transfer additionally require repeated generations, new tasks, and regression measurements.

## 6. Model–harness co-evolution

HELIX, Co-Harness, OpenRSI, MASS, SIA, and related work identify the correct deployed unit: model and harness jointly determine behavior, and harness rollouts determine part of the data available for later model training.

One possible implementation is:

$

H_t \rightarrow D_t^{\text{verified}}
\rightarrow M_{t+1}
\rightarrow H_{t+1}.

$

Current public evidence is early. Common limitations include one-round demonstrations, task-specific evaluators, incomplete $M\times H$ crossing, no time-forward tasks, and no comparison of parent and successor as improvers.

The direction deserves priority because it can combine cheap external adaptation with durable parameter learning. It should not be described as solved RSI until the repeated loop is measured.

HELIX's [reported experiment](https://arxiv.org/html/2608.13951v1) measures
harness execution and training-record production, not a completed trained-model
update and rebuild. Its corpus depth label is corrected accordingly.

## 7. Evaluation results that change the research program

### Matched-compute evaluation

Rethinking the Evaluation of Harness Evolution shows why harness search must be compared with simple task-level search under the same feedback and inference budget. Without this comparison, a persistent harness may merely amortize extra search rather than create a better algorithm.

### Statistical selection limits

Repeated candidate search can create winner's curse and adaptive overfitting. The cataloged paper On the Statistical Limits of Self-Improving Agents specifically studies reachable policy-family capacity under i.i.d. PAC assumptions; it must not be cited as if it only established noisy winner selection. An unrestricted state representation gives no statistical learnability guarantee.

### Harness tampering

An editable harness can alter logging, provenance, parsing, task coverage, authorization, or evaluation behavior. Apparent gains can therefore result from changing what is measured or recorded. The final acceptance path and evidence log require protection outside the editable surface.

### Scale dependence

Public evidence indicates that harness gains can be non-monotonic with base-model strength. Weak models may fail to follow a useful harness; strong models may already implement the strategy internally or be constrained by the harness. Any claimed general method needs a model-scale curve rather than one endpoint.

## 8. Claim patterns with low RSI value

The following patterns should not occupy the center of the repository.

### Reflection without persistence

The system critiques or revises its current answer but retains no reusable change. This is task-time computation.

### Best-of-$N$ presented as learning

A system samples many candidates and keeps the best output. Unless the selected information changes later behavior, no successor was created.

### Benchmark editing

A prompt, tool, or code patch exploits repeated exposure to a fixed suite. Large in-distribution gain with weak untouched transfer is task fitting.

### Compute hidden inside the harness

More retries, longer context, extra sub-agents, or more evaluator calls are counted as “architecture improvement” without matched total cost.

### Single-generation recursion

A parent produces one better child. That observation can establish a persistent update and, with appropriate evidence, transfer. It does not alone establish that the child is a better improver. A recursively defined procedure can exist without that stronger D3 result.

### Joint update without attribution

Model and harness are updated together and only the paired endpoints are tested. The source of gain and co-adaptation cannot be determined.

### Self-approval

The same model generates, judges, and accepts an update with no independent final test. Correlated error and reward hacking remain uncontrolled.

### Tiny-model proof by extrapolation

A method works on a small model or toy environment and is presented as a route to frontier RSI without a scale-transfer experiment.

### Vocabulary in place of evidence

New names for loops, roles, memories, or agent layers do not change the scientific state unless they enable a new capability, prediction, or controlled result.

These patterns can contain valuable findings. They do not by themselves establish improved improvement ability, broad transfer, or sustained growth. The scope of the particular claim determines the missing evidence.

## 9. Current evidence boundary

As of October 2026, public work supports the following statement:

> AI systems can participate in producing persistent changes to prompts, context, memory, tools, harness code, agent programs, training data, rewards, and model weights. Some changes transfer to held-out tasks, and several systems report short multi-generation improvement.

This repository has not established the stronger claim:

> A general AI system repeatedly improves its model, harness, and improvement process; the successors become better improvers; gains transfer broadly across tasks and scales; and the process remains stable over many generations.

BeforeRSI is organized around closing the gap between these two statements.

## 10. Representation audit and source corrections (2026-10-17)

[COMPATIBILITY.md](COMPATIBILITY.md) maps every catalog entry to the operational model and records the behavior it must preserve. Coverage of mechanisms is distinct from reproduction of results and prediction across methods. The audit corrected the earlier understatement of Self-Rewarding LM's reported iterations and Hyperagents' reported meta-level transfer.

Four works already named in the prose are now cataloged explicitly: [HGM](https://arxiv.org/abs/2510.21614) studies descendant-informed parent selection; [ACE](https://arxiv.org/abs/2510.04618) incrementally adapts contextual playbooks; [AlphaEvolve](https://arxiv.org/abs/2506.13131) searches executable algorithms, including infrastructure used in model training; [OPRO](https://arxiv.org/abs/2309.03409) uses an LLM to propose candidates from optimization history. These are source-backed method descriptions, not independently reproduced outcomes.

## 11. Mechanism coverage additions (2026-10-18)

**Learned parameter updates.** [Andrychowicz et al.](https://arxiv.org/html/1606.04474v2) train LSTM optimizer weights using external Adam and truncated backpropagation. Validation selects optimizers; evaluation uses freshly sampled problems. The MNIST setup uses 100 optimizee steps and 20-step unrolls. Reported transfer includes larger networks, but the sigmoid-to-ReLU change fails. This supplies a learned-update mechanism and a transfer boundary, without establishing autonomous recursion or a comparable lifecycle-cost result.

**Evolving development environments.** [POET](https://arxiv.org/html/1901.01753v3) changes terrain configurations and policies while retaining fixed mutation, optimization, and transfer rules. It reports gains from cross-environment transfer. The curriculum comparison uses up to 25,200 iterations, 20 active environments and 512 ES samples per step, taking about ten days on 256 CPU cores per run. Development environments evolve; the study is not a hidden-domain generalization test. Terrain parameters have explicit caps. This supports bounded environment–agent co-evolution, not an unbounded growth theorem or self-rewriting generator.

Both additions remain author-reported and have not been rerun here. They expand mechanism coverage beyond the preferred model–harness schedule; they do not complete the literature or establish a universal quantitative law.

## 12. Self-training optimizers and executed BeforeRSI results

[Metz et al. (2020), Section 4.6](https://arxiv.org/html/2009.11243v1)
report a learned optimizer training new learned optimizers with curves similar
to tuned Adam. The displayed comparison uses 10,000 outer iterations; extending
the horizon worsens performance. Appendix F.4 reports that retaining external
gradient clipping is necessary for progress. This is source-reported transfer
to optimizer training, not an independently reproduced indefinite growth result.
It also prevents treating numerical optimizer self-training as a new idea here.

[Experiment 006](experiments/006-recursive-optimizer/RESULTS.md) is an empirical
BeforeRSI result in a small numerical search class. It contains executed recursive
versus pinned-actor comparisons, direct J-versus-G training and equal-call update
orders, with independent assessment cohorts and complete candidate records.
Positive feedback-task gains did not establish transferable recursive gains.
The report separates measured effects, descriptive uncertainty and scope;
it is not a reproduction of the neural optimizer paper.

## 13. Mechanism explanations and source comparisons (2026-10-18)

[MECHANISMS.md](MECHANISMS.md) connects source facts to explicit conditional
explanations and interventions. The corpus now includes
[STaR](https://arxiv.org/abs/2203.14465) and
[ReST-EM](https://arxiv.org/abs/2312.06585): correctness filtering,
answer-conditioned rationalization where used, and likelihood projection
explain a route from generated reasoning to persistent weights. These are
source mechanisms, not inventions of this project.

[RRSI Table 2](https://arxiv.org/html/2609.24972v1) reports a useful reversal:
unregularized search has the higher evolve score (92.8 versus 90.5), whereas
RRSI has the higher OOD average (43.6 versus 40.3) and lower token cost
(2.42M versus 3.80M). The calculation in research/source-comparison-results.json
shows dominance on held-out score, OOD score and execution tokens over the
three regularizer-removal arms. This is arithmetic on reported aggregate
points, not an uncertainty estimate or a rerun.

MASS's training-token comparison and OpenRSI's shared learned operators supply
different precedents for inheritance. Their original papers are now linked
in data/works.json. The mechanism map identifies what would distinguish
teacher quality, learnability, task-mixture shifts and improved search control.
A nominally complete feedback loop does not identify which effect occurred.


## Search-and-learning foundations added on 2026-10-18

These six additions supply algorithms and conditional results needed to explain
co-evolution, rather than new instances of the same label.

| Primary work | Source-supported contribution | What it changes here |
|---|---|---|
| [Expert Iteration, 2017](https://arxiv.org/pdf/1705.08439) | Search supplies learning targets; the learned policy guides subsequent search. | The external planner can stay fixed while effective improvement behavior changes. |
| [DreamCoder, 2021](https://www.neurosymbolic.org/papers/EllisWNSMHCST21.pdf) | Learns reusable program abstractions and a recognition model; the paper separates their contributions. | A co-evolving representation must be allowed to change the available search paths. |
| [Selecting Computations, 2012](https://arxiv.org/pdf/1207.5879) | Formalizes costly information gathering for a final choice and derives scoped stopping results. | Evaluating update choices consumes resources; information and candidate improvement differ. |
| [LevinTS, 2018](https://arxiv.org/pdf/1811.10928) | Relates policy-guided search effort to solution-path probability. | Gives an explicit bridge from learned behavior to later computation. |
| [PHS, 2021](https://cdn.aaai.org/ojs/17469/17469-13-20963-1-2-20210518.pdf) | Combines policy and heuristic guidance with search-loss guarantees. | Search cost and returned-solution cost need separate objectives. |
| [LTS-CM, 2023](https://www.ijcai.org/proceedings/2023/0624.pdf) | Uses context models with a convex fixed-path search-effort loss in a bootstrap loop. | Supplies a tractable learner; fixed-path convexity does not prove whole-loop convergence. |

Original empirical findings remain author-reported. Experiment 008 is our own
small implementation in a different puzzle setting and is not recorded as a
reproduction of these papers. SEARCH.md attributes the existing bounds and
objectives, then derives the retention and cost consequences used here.

## Executed learned-search result

[Experiment 008](experiments/008-learned-search/RESULTS.md) performs five rounds
of actual context-policy fitting and solution search. Four paired lineages
compare frozen versus reused collection, CE versus a regularized search-bound
objective, and local versus whole-search preservation. The model has 2,592
parameters and no optimal-distance oracle supplies its labels.

On the declared uniform-state follow-up at 256 pops, reuse-CE solves 369/512
starts and frozen-collection CE solves 25/512. To assess the data-producing
actor on common targets, the final policies collect paths for identical new
zero-initialized learners. Those students solve 344/512 versus 176/512 under
the same assessment cap. All four paired differences have the same sign.

The bound-loss route solves 404/512 in the direct comparison at that cap.
Complete-search preservation performs better than local mixing in this run,
but usually worse than the learned solver alone. Its overhead guarantee is a
different statement from empirical same-budget superiority. Common search caps
and optimization ceilings do not match physical compute: process CPU times,
fit work and build-plus-deployment totals are included. These observations
establish a bounded mechanism, not an original general RSI result.


## 2026-10-18 — Frontier mechanisms missing from the earlier corpus

The 14 additions below correct important omissions; they do not establish exhaustive coverage. See [FRONTIER_COVERAGE.md](FRONTIER_COVERAGE.md) for the resulting change in research scope. All source results are author-reported and audit-in-progress. None was independently reproduced here. Development/assessment separation and resource disclosure vary; public benchmarks are not automatically contamination-free hidden tests. Interpretations and proposed interventions appear in the mechanism map.

| Work | Changed objects / source feedback | Tasks, assessment and resources | Limit on the supported claim |
|---|---|---|---|
| [OpenAI o1: Learning to reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/) | RL trains reasoning behavior; inference compute also changes outcomes. | Public reasoning/coding evaluations; complete training compute and procedure not disclosed in this source. | Train/test compute scaling does not identify a self-improving research process. |
| [DeepSeek-R1](https://arxiv.org/html/2501.12948v1) | GRPO, verifiable feedback, generated-data retraining and distillation. | DeepSeek-V3-Base backbone; public reasoning/coding/general benchmarks and smaller distilled models; no harmonized full-budget replication here. | A fixed trainer is compatible with self-generated learning, but the paper does not establish indefinitely improving research ability. |
| [Qwen3 Technical Report](https://arxiv.org/html/2505.09388v1) | Reasoning/general RL, thinking-mode fusion and off/on-policy teacher distillation. | Flagship 235B-A22B and dense models; multilingual/reasoning/general evaluations; report has bounded GPU-hour comparisons. | Teacher-provided information and small-model efficiency do not establish teacher-free recursive discovery. |
| [AlphaProof](https://www.nature.com/articles/s41586-025-09833-y) | Automatically formalized problems and Lean-verified search feed reinforcement learning, including problem-specific training. | Millions of problems; IMO/proof evaluations; 2024 contest statements were manually formalized and solving time differed from human conditions. | Formal proof correctness is conditional on the formal statement; it does not establish fidelity of every autoformalization or broad research recursion. |
| [MuZero](https://arxiv.org/abs/1911.08265) | Learns latent dynamics, reward/value/policy quantities and plans with the learned model. | Atari and board-game settings; separate training regimes and search-budget results, not one universal agent across all worlds. | Planning within an imperfect learned model differs from search in a known exact environment. |
| [Open-Ended Learning Leads to Generally Capable Agents (XLand)](https://arxiv.org/abs/2107.12808) | Dynamic task generation, population training and distillation support repeated learning. | Five reported generations; generated held-out and hand-authored tasks; each agent uses 8 TPUv3s in the reported setup. | Broadness within a constructed environment space is not unrestricted real-world generality. |
| [SIMA 2](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/) | Gemini supplies tasks/reward estimates; self-play experience trains later agents, including exploration in Genie worlds. | Held-out games and generated environments; full compute not specified in the checked page; linked technical report inaccessible this pass. | The official self-improvement report does not show that Genie itself recursively improves or that physical-world transfer is established. |
| [Constitutional AI](https://arxiv.org/abs/2212.08073) | Constitution-conditioned critique/revision and AI preferences support supervised and reinforcement learning. | Helpfulness/harmlessness evaluations under authored principles; compute not extracted in this pass. | The normative target remains externally specified; AI feedback is not automatically accurate or independent. |
| [Self-Taught Evaluators](https://arxiv.org/html/2408.02666v1) | Constructed response pairs anchor iterative judgment generation and evaluator training. | Llama3-70B-Instruct seed, Mixtral data support, WildChat-derived instructions; RewardBench and other judge tests. | Constructed preference labels can be imperfect; the student is reset to the seed each round rather than simply continuing fine-tuning. |
| [Eureka](https://arxiv.org/abs/2310.12931) | LLM-generated reward code is revised using policy-training feedback in accelerated simulation. | GPU Isaac Gym robot/task suite; official project/repository; full aggregate cost not extracted here. | Useful reward optimization does not establish that the LLM reward designer itself becomes a stronger designer. |
| [Co-Scientist](https://arxiv.org/abs/2502.18864v2) | Gemini agents generate, critique and refine hypotheses through tournament evolution. | 2026 revision reports external biomedical validation in three application areas; no full cost comparison extracted here. | Internal hypothesis rankings are not scientific truth; validated hypotheses do not alone prove an improved research policy. |
| [GPT-Red](https://cdn.openai.com/pdf/gpt-red-automated-red-teaming-via-self-play-at-scale.pdf) | Attacker and multiple defenders undergo self-play RL; learned attacks subsequently train production models. | Large post-training scale stated officially; held-out scenarios, frozen-attacker controls and cross-checkpoint evaluations; exact GPU total not disclosed in checked source. | Task-specific robustness improvement and co-training do not establish unrestricted recursive research acceleration. |
| [Automated Alignment Researchers: mitigating alignment failures](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures) | Claude proposes methods/data, trains targets and tests alignment interventions. | Ten failure categories, withheld evaluations and larger targets; reported production-model case; human comparison has unequal iteration opportunities. | Improving target models does not show that the researcher improves itself; production data-efficiency claims are not full research-cost ratios. |
| [Seed for Seed (Seed2.1)](https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity) | Officially reported agent participation in evaluation, data synthesis, RL infrastructure and research implementation. | Industrial model-development workflow; matched no-agent and repeated-generation resources not disclosed on the source page. | A deployment report supports use in AI development, not an identified causal multiplier or autonomous closed-loop growth. |

The added sources support concrete mechanism and deployment claims, not a common quantitative growth law. Exact per-source reading boundaries are recorded in data/mechanisms.json.

<!-- scope-expansion -->
## Scope-focused expansion: 56 primary-source screens

The operation column paraphrases author reports. Scope, limits and counterfactuals are our judgments. These entries have not been independently reproduced. Ten have selected primary sections read; the other 46 remain abstract-level screens. Full GPU/API cost accounting is not inferred where it is absent from the inspected passage.
Read RSI_SCOPE.md and research/scope-catalog.md before interpreting the corpus count as a count of RSI systems.

| Work | Reported changed operation | Tasks / resource boundary | Scope / limitation |
|---|---|---|---|
| [SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness](https://arxiv.org/abs/2609.20519) | 从多环境轨迹搜索并整合执行、压缩和观察处理机制。 | EdgeBench、Terminal-Bench、IMO；报告 token/API 成本，完整搜索成本比较未建立。 | 直接支撑的 AI4AI/学习机制：论文把用新 harness 加速后继研发列为未来方向；成本下降不是已测递归复利。 |
| [ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement](https://arxiv.org/abs/2609.14857) | 当前智能体分析成功/失败对照轨迹并修改自身模块，再整合模块。 | 2000 个与评测基准分离的进化任务；TB2.0、SWE-bench Verified。 | 直接自进化研究：模块独立优化后存在交互；跨模型迁移不等于改进能力持续提升。 |
| [Prime Agent: A Self-Improving RLM Harness](https://arxiv.org/abs/2608.23552) | 长期 REPL 与持久经验支撑跨轨迹策略修订和技能使用。 | 长上下文编码、kernel、nanoGPT、Factorio；摘要未给统一研发预算。 | 直接自进化研究：递归子代理调用本身不是 RSI；摘要没有隔离后继作为改进者的贡献。 |
| [The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators](https://arxiv.org/abs/2606.26294) | 共同进化任务代理与评价器，替换评价器后重估档案。 | DeepSWE、论文写作、IMO；有搜索 token 计数与固定评价器对照。 | 直接自进化研究：IMO 人工评分等外部锚点仍必要；论文写作的代理评分不能等同真实科研质量。 |
| [Dr. Zero: Self-Evolving Search Agents without Training Data](https://arxiv.org/abs/2601.07055) | 出题者按当前求解者能力生成问题，双方交替学习。 | 多跳问答；相同底座初始化双方，HRPO 减少出题奖励估计开销。 | 直接自进化研究：零人工 QA 训练样本不等于零外部知识；仍依赖预训练和搜索引擎。 |
| [Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills](https://arxiv.org/abs/2607.22529) | 技能提供任务生成结构与验证程序，双方策略和技能库共同更新。 | 工具调用与推理；论文给出冻结组件消融，不提供无限任务空间保证。 | 直接自进化研究：可执行验证与技能覆盖仍有边界，能力前沿难度代理不等于真实长期学习增益。 |
| [RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System](https://arxiv.org/abs/2602.02488) | 策略、奖励模型和任务难度通过反馈共同调整。 | OSWorld、ALFWorld、编码；方法给出模型、rollout 数及 ID/OOD 划分。 | 直接自进化研究：环境变化并非任意世界创造；GUI 部分依赖预建扰动及其验证器。 |
| [Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning](https://arxiv.org/abs/2511.16043) | 工具增强执行者与课程代理共同生成下一轮训练任务。 | Qwen3-8B；数学与通用推理，摘要未给总训练算力。 | 直接自进化研究：工具与预训练提供外部能力；多轮共同训练不证明通用研发递归。 |
| [R-Zero: Self-Evolving Reasoning LLM from Zero Data](https://arxiv.org/abs/2508.05004) | 挑战者寻找求解者能力边缘任务，求解者训练后改变出题反馈。 | 多底座数学/通用推理；摘要报告 Qwen3-4B 示例，预算待全文核查。 | 直接自进化研究：自生成题目和标签可能共同偏误，不能由内部奖励证明正确性。 |
| [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335) | 同一模型生成训练任务并求解，代码执行提供验证反馈。 | 代码与数学、多模型尺度；摘要未提取总训练成本。 | 直接自进化研究：无需新人工数据仍依赖预训练、执行语义和初始任务表达范围。 |
| [Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data](https://arxiv.org/abs/2602.21320) | 生成器针对工具求解者的能力边界构造任务，真实工具调用反馈训练双方。 | 多个工具使用基准；零预置任务不等于无预训练先验。 | 直接自进化研究：工具接口和答案校验限定可学空间；不能把相对增幅当跨基准绝对优势。 |
| [EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for Autonomous Agentic Reinforcement Learning](https://arxiv.org/abs/2606.03108) | 训练代理修改诊断、训练信号和流程，保留技能供后续训练版本使用。 | 数学、竞赛代码、SWE；同数据/代码/评测，附录讨论搜索与推理预算。 | 直接自进化研究：基础训练代理权重固定且昂贵动作有人类把关；不支持完全无人递归。 |
| [AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation](https://arxiv.org/abs/2605.28655) | 去中心化团队共享成功和失败的实验知识，搜索目标模型训练改进。 | BioML、GPT 训练、ProteinGym；保留 GPT 训练分支及其预算对照价值。 | 直接支撑的 AI4AI/学习机制：生物研究部分不是本项目核心；目标 GPT 训练优化不证明研究代理自我升级。 |
| [Dual-Evolving Reinforcement Learning for Automated Reward Design](https://arxiv.org/abs/2512.13399) | 奖励设计者根据内层策略训练后的验证表现学习更好的奖励提案。 | ALFWorld、ScienceWorld、GSM8K、MATH；8:2 内层/验证划分和独立测试。 | 直接自进化研究：奖励原语由人指定；最终策略重新训练，不能描述成同一策略连续自改。 |
| [GEAR: Genetic AutoResearch for Agentic Code Evolution](https://arxiv.org/abs/2605.13874) | 维护研究状态种群并交叉重组；其中一个变体允许搜索控制器演化。 | 同环境和算力的 AutoResearch 对照；摘要未给完整预算数值。 | 直接自进化研究：固定控制器的另外两个变体不是改进器自修改，不能合并宣称递归。 |
| [Towards Execution-Grounded Automated AI Research](https://arxiv.org/abs/2601.14525) | 执行预训练/后训练研究方案，用结果做演化搜索或训练构思模型。 | LLM 预训练与后训练；报告十轮搜索和 RL 负面结果。 | 直接支撑的 AI4AI/学习机制：RL 平均奖励上升同时出现模式坍缩，上限改善未建立；并未训练自身后继。 |
| [Meta$^n$: Recursive Self-Improvement through Emergent Depth](https://arxiv.org/abs/2608.24735) | 固定元操作反复读取已有代码与轨迹，生成后续策略层及工具。 | 两个底座、八类基准；摘要未给完整成本及独立复现。 | 直接自进化研究：固定元操作不自动保证整体稳定；层数与真实改进效率不可混同。 |
| [Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498) | 代理从自身失败中挖掘弱点、提出最小修改并经回归测试保留。 | 三模型×TB2.0/SWE-bench Verified/AppWorld，含 held-in/held-out。 | 直接自进化研究：自己提出修改不自动证明后继更会修改；同基准划分与跨领域迁移不同。 |
| [Harness-Zero: Harness Distillation via Agent-as-Harness](https://arxiv.org/abs/2609.24974) | harnessing agent 把复杂 harness 指导转换为目标动作空间的训练示范。 | 知识工作、工具使用、科学任务；摘要未给全部数据生成与训练成本。 | 直接支撑的 AI4AI/学习机制：展示内化与部署收益，未据摘要证明多代改进器闭环。 |
| [Harness-R1: Learning to Edit Executable Runtime Harnesses from Agent Failure Trajectories](https://arxiv.org/abs/2608.02276) | 用目标代理重跑后的任务成功训练专门的 harness 编辑模型。 | 9B 编辑者；WebShop、ALFWorld、DBBench，另测目标微调后增益。 | 直接支撑的 AI4AI/学习机制：主训练只更新编辑者、目标冻结；论文指向共同进化，未证明持续双向循环。 |
| [SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning](https://arxiv.org/abs/2602.08234) | 从经验提炼分层技能，并让技能库与 RL 策略共同更新。 | ALFWorld、WebShop、七个搜索增强任务；摘要未给总训练成本。 | 直接自进化研究：技能压缩可能丢失适用条件，特定基准增益不证明通用递归能力。 |
| [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/abs/2605.23904) | 外部优化模型把评分轨迹变成受限文本编辑，验证后保留技能。 | 六基准、七目标模型、三 harness；52 个评测组合和迁移报告。 | 直接支撑的 AI4AI/学习机制：外部技能优化与优化器自改不同；重复验证选择仍需最终未触碰测试。 |
| [Mem$^2$Evolve: Towards Self-Evolving Agents via Co-Evolutionary Capability Expansion and Experience Distillation](https://arxiv.org/abs/2604.10923) | 经验指导创建工具/专家资产，新资产反过来产生后续经验。 | 六类任务、八基准；摘要给隔离经验与资产的对照。 | 直接自进化研究：资产增加不保证改进速度上升，组合依赖和维护成本尚须控制。 |
| [MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents](https://arxiv.org/abs/2602.02474) | 控制器学习选择记忆技能，设计者根据难例周期性修订技能集。 | LoCoMo、LongMemEval、HotpotQA、ALFWorld；预算未从摘要提取。 | 直接自进化研究：设计者本身是否改进未确定；技能选择和技能生成的贡献需分离。 |
| [MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory](https://arxiv.org/abs/2601.03192) | 固定推理模型通过环境反馈更新经验检索效用。 | HLE、BigCodeBench、ALFWorld、Lifelong Agent Bench；无权重更新。 | 直接支撑的 AI4AI/学习机制：持久记忆学习成立不等于记忆更新规则或改进能力已自进化。 |
| [EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management](https://arxiv.org/abs/2606.03841) | 学习生成可复用执行技能，并把上下文压缩作为训练控制策略。 | 四类数据科学基准、两阶段多代理训练；完整算力待核。 | 直接自进化研究：数据科学成绩与生成后继研究者能力不同；摘要定理不能代替逐项假设核查。 |
| [Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails](https://arxiv.org/abs/2609.09134) | 先适配 harness，再在学生自身轨迹的失败位置提供专家局部纠正。 | 七企业任务，Qwen/Gemma LoRA，H100/H200，三次测试均值。 | 直接自进化研究：整轨迹模仿在已进化 harness 上退化；局部纠正平均增益有限，不是普遍最优。 |
| [Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Technical Report](https://arxiv.org/abs/2608.15763) | 用多种 harness 状态增强训练，使紧凑模型适应独立变化的运行框架。 | 淘宝直播部署；四评测集、单 H20 延迟和线上 A/B 报告。 | 直接支撑的 AI4AI/学习机制：兼容变化中的 harness 不等于 AI 自己设计或进化该 harness。 |
| [RewardHarness: Self-Evolving Agentic Post-Training](https://arxiv.org/abs/2605.08703) | 奖励代理依据偏好误差修订工具/技能库，再提供模型后训练奖励。 | 图像编辑偏好，100 示范，后接 FlowGRPO；非纯 LLM 输出领域。 | 直接自进化研究：初始人类偏好是锚点；奖励器自改与被训练模型回馈奖励器须区分。 |
| [WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model](https://arxiv.org/abs/2504.21024) | 网页世界模型生成训练交互并帮助规划，与网页代理共同进化。 | Mind2Web-Live、WebVoyager、GAIA-web；不使用更强闭源模型蒸馏。 | 直接自进化研究：模型想象会积累偏差，真实网页验证不能由世界模型自身评分替代。 |
| [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://arxiv.org/abs/2411.02337) | 用失败生成新课程，配合结果奖励与策略漂移控制进行在线训练。 | Llama/GLM，WebArena-Lite；摘要未提取全部训练开销。 | 直接自进化研究：课程反馈闭环不同于训练算法自改；目标领域仍限定在网页任务。 |
| [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://arxiv.org/abs/2501.04519) | 搜索轨迹训练策略和过程偏好模型，两者四轮共同更新。 | 747k 数学题、百万合成解、四轮；Qwen/Phi 两底座。 | 直接自进化研究：外部题库与执行验证仍支撑学习；数学域共同进化不是开放科研闭环。 |
| [Self-Evolved Reward Learning for LLMs](https://arxiv.org/abs/2411.00418) | 奖励模型生成训练反馈，迭代训练自己的评价能力。 | HH-RLHF、UltraFeedback，Mistral/Llama；总预算待全文核查。 | 直接自进化研究：有限人工标注和预训练仍是信息锚点；自反馈可能积累偏差。 |
| [Self-Evolving Curriculum for LLM Reasoning](https://arxiv.org/abs/2505.14970) | 以估计学习收益更新非平稳 bandit 课程策略，配合模型 RL。 | 规划、归纳、数学；题目类别作为 bandit 臂。 | 直接支撑的 AI4AI/学习机制：固定课程更新律是自适应训练，不自动构成改进器递归重写。 |
| [SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills](https://arxiv.org/abs/2504.07079) | 网页代理探索、练习并封装 API，复用新技能继续积累能力。 | WebArena 与真实网站，另报告向弱模型迁移。 | 直接自进化研究：技能积累和任务迁移不等于技能发现过程效率持续上升。 |
| [Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?](https://arxiv.org/abs/2511.13646) | 代理在解决软件任务时修改自身运行 scaffold。 | SWE-bench Verified、SWE-bench Pro；摘要未给持续代际对照。 | 直接自进化研究：同任务内自改与跨任务继承是不同证据，不能从 solve rate 推出代际增长。 |
| [Group-Evolving Agents: Open-Ended Self-Improvement via Experience Sharing](https://arxiv.org/abs/2602.04837) | 智能体群共享不同进化分支的经验来指导后续结构修改。 | SWE-bench Verified、Polyglot，报告跨模型迁移与错误修复。 | 直接自进化研究：同进化个体数不保证同算力；探索多样性的价值需与开销分开。 |
| [Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams](https://arxiv.org/abs/2606.01770) | 任务流驱动持续构建不同 harness，并按任务路由及保留演化经验。 | 预测市场、安全竞赛、事件预测任务流；摘要未给统一完整成本。 | 直接自进化研究：部分信号来自人类引导；路由收益不等于改进器变强。 |
| [Continual Harness: Online Adaptation for Self-Improving Foundation Agents](https://arxiv.org/abs/2605.09998) | 代理在持续交互中交替行动并修订持久技能、提示和记忆。 | 具身长期任务/游戏；摘要报告 reset-free 流程，完整预算待核。 | 直接自进化研究：早期 GPP 人类参与与后续自动循环必须分开，游戏进度不直接代表通用研发能力。 |
| [EnvHarness: Awakening Static Worlds for Agent Learning](https://arxiv.org/abs/2608.19880) | 根据代理失败生成环境包装组件，保留原验证器并训练策略。 | 四领域五基准；报告独立实例泛化与执行步数。 | 直接自进化研究：环境包装保留验证器是特定设计，不保证所有新任务忠实有效。 |
| [Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design](https://arxiv.org/abs/2605.15871) | 研究代理设计计算原语和架构，并将候选扩展到较大模型训练。 | 24 小时搜索，候选扩展至350M/1B/3B；有1B预训练结果。 | 直接支撑的 AI4AI/学习机制：发现目标模型架构不等于将目标用作下一代设计者。 |
| [AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement](https://arxiv.org/abs/2608.20318) | 隔离训练算法修改，用隐藏评估器重训提交代码。 | 10 冻结仓库；1 B300 搜索4小时，重训至12小时。 | 评测与反例：它测研发能力而非运行多代 RSI，归一化分数仍依赖所选任务和参照。 |
| [Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement](https://arxiv.org/abs/2609.13406) | 统一描述策略、评价、修改机制及评价基准是否属于可修改系统。 | 形式框架，非大规模训练实验；已选读定义和边界。 | RSI 理论：属于可重写组件不等于实际发生有效重写；表示统一不是经验泛化定律。 |
| [Aspire: Can Models Self-Evolve from Vague Goals?](https://arxiv.org/abs/2608.31111) | 让代理从模糊目标自行选数据和更新方式，再用隐藏专家任务评价。 | 六目标、520隐藏条目，支持权重与harness修改；预算待全文核查。 | 评测与反例：完成训练或编辑流程不等于提高能力；报告中增益稀疏且不稳定。 |
| [Large Language Model Agents Are Not Always Faithful Self-Evolvers](https://arxiv.org/abs/2601.22436) | 干预原始和压缩经验，检查代理决策是否真正依赖积累经验。 | 四框架、13底座、九环境；原始摘要与实验范围已核。 | 评测与反例：对经验不敏感可来自已有知识或压缩丢失，不能一概判为无学习。 |
| [ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution](https://arxiv.org/abs/2509.19349) | 通过多样性、父代选择与模型组合提高程序演化样本效率。 | 包含 agent harness 与 MoE 损失发现，也有一般算法任务。 | 直接支撑的 AI4AI/学习机制：只有目标涉及 AI 训练/harness 时属直接 AI4AI；普通圆堆积不算自身进化。 |
| [CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution](https://arxiv.org/abs/2603.17775) | 同一模型交替学习生成与验证，以验证反馈过滤自一致错误。 | Qwen/Llama 数学推理；标签自由训练中的共识陷阱。 | 直接自进化研究：多数投票仍提供噪声标签，摆脱部分共识错误不保证无锚点真理发现。 |
| [Actor-Curator: Co-adaptive Curriculum Learning via Policy-Improvement Bandits for RL Post-Training](https://arxiv.org/abs/2602.20532) | 神经课程选择器直接学习预计策略提升，适配非平稳题库采样。 | 推理后训练；bandit 目标与遗憾界，假设未完整审阅。 | 直接支撑的 AI4AI/学习机制：课程控制器的学习不同于其自身更新算法被改进。 |
| [Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence](https://arxiv.org/abs/2604.18292) | 探索真实工具生态并生成可验证任务，按能力缺口持续训练。 | 23个 agent 基准、8B/14B；预印本标注进行中。 | 直接自进化研究：MCP 环境主题多不等于未见世界泛化，生成器和验证器来源需全文核查。 |
| [SkillOS: Learning Skill Curation for Self-Evolving Agents](https://arxiv.org/abs/2605.06614) | 用较晚关联任务的表现训练技能整理者，执行者保持冻结。 | 任务流中的延迟反馈，多轮 agent 与单轮推理；成本待核。 | 直接支撑的 AI4AI/学习机制：改善技能整理者是有价值的 AI4AI，但其更新流程未被自身改写。 |
| [Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills](https://arxiv.org/abs/2606.07412) | 从解题轨迹提取技能生成下一轮修复任务，执行验证后更新求解者。 | 四个 SWE/Terminal 基准；摘要报告三轮和相同算力对照。 | 直接自进化研究：梯度对齐作为学习价值代理需检验；软件领域闭环未推出通用科研提升。 |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | 在 Minecraft 中创建并复用可组合代码技能继续探索。 | Minecraft 新世界迁移；黑盒模型，无参数微调。 | 直接自进化研究：固定 GPT-4 与课程程序；技能复用不是已证元算法自改。 |
| [AgentEvolver: Towards Efficient Self-Evolving Agent System](https://arxiv.org/abs/2511.10395) | 自提问、自导航与贡献归因让环境经验进入后续 agent 训练。 | 多环境自主学习；原摘要为初步实验描述，完整算力待核。 | 直接自进化研究：训练闭环的元过程仍有固定部分；高效率需全流程成本而非仅样本数。 |
| [Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning](https://arxiv.org/abs/2607.21971) | 用执行反馈训练多轮反思与修订能力，部署时进行演化搜索。 | 七编码基准及域外算法优化；初筛未提取总训练成本。 | 直接支撑的 AI4AI/学习机制：改进目标代码不等于目标本身是改进器；需实际闭环继承证据。 |
| [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.14777) | 当前策略同时收集轨迹和提炼事后技能，技能诱导信号训练同一策略。 | 文本与视觉 agent 任务；联合结果 RL 和 token 级自蒸馏。 | 直接自进化研究：训练期事后信息在部署不可见；内化效果与信息泄漏边界需明确。 |
| [RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning](https://arxiv.org/abs/2505.15034) | 生成者与过程验证者交替用 RL 训练，外部结果正确性监督验证者。 | 7B/8B，五数学及四域外任务，另测 ProcessBench。 | 直接自进化研究：不是完全无标签自证；固定结果验证构成外部锚点。 |

## 2026-10-18 — Three-route structure and trained-target scale audit

This pass changes the atlas information architecture, not the claimed depth of every catalog entry. The new [classification note](research/atlas/classification.md) separates changed objects, functional roles, learning mechanisms, temporal regime, return paths and evidence. [Layer records](data/layer-review.json) hold the source locators and per-experiment models.

The main view now contains **12 works: 8 Harness, 2 Model, 2 mixed**. There are **24 reviewed claim cards**, including references outside the new main scope; 77 entries remain pending, with 16 historical and 6 background entries. Main-view counts are not field prevalence or completeness estimates. The mixed route explicitly distinguishes one-pass joint adaptation from demonstrated repeated cycles.

| Primary source and inspected location | Source fact | Atlas decision / inference |
|---|---|---|
| [Self-Rewarding LM §2–3](https://arxiv.org/html/2401.10020v1) | Llama 2 70B; seed SFT then two DPO updates; successive models generate responses and preferences. Actual prompt generation uses a fixed Llama 2-Chat 70B. | Added a claim card from the existing bibliography. Model-layer iterative preference learning, not online PPO and not autonomous prompt-generator evolution. |
| [Self-Taught Evaluators §3.5, §4.1](https://arxiv.org/html/2408.02666v1) | 70B evaluator; current judge creates supervision, but each student is initialized again from the seed. | Model layer; teacher/data return rather than uninterrupted checkpoint inheritance. |
| [MASS §3–4, Appendix C](https://arxiv.org/html/2610.12176v1) | Qwen3.6-27B; two workflow-evolution/SFT cycles, with model reuse across roles. | Mixed main view; SFT with refreshed trajectories, not an online-RL claim. |
| [On-policy correction §3.1–3.4, Table 1 and model footnote](https://arxiv.org/html/2609.09134) | Qwen3-Coder 30B total / 3B active; supplementary Gemma 26B / 4B. Local expert corrections at student states are used for LoRA SFT. | Include the 30B branch; exclude 26B from the primary scale. Observed joint adaptation is not itself a demonstration of repeated coevolution. |
| [Frontis-MA1 §8, Appendix B.2–B.3](https://arxiv.org/html/2607.28568v1) | 35B/30B SFT and RL; candidate ML solutions evolve while the evolutionary system remains largely fixed. | Scale passes but scope does not establish autonomous mixed RSI. Retain as AI4AI support. |
| [SEAL §4 and Appendix B](https://arxiv.org/html/2506.10943v1) | Knowledge branch 7B; ARC branch 1B. | Small-model mechanism reference, outside main scope. |
| [Dr. Zero §4.1, Table 3](https://arxiv.org/html/2601.07055v2) | 3B/7B trained proposer/solver configurations and multi-round results. | Small-model reference; a search role does not make these large trained models. |
| [RLAnything Appendix C.1–C.2](https://arxiv.org/html/2602.02488v1) | Policy/reward configurations inspected are 7B/8B/14B; larger models occur as evaluation supervisors. | Small-model reference. Do not use 32B/72B evaluation models to satisfy the target-training gate. |
| [EvoTrainer §3.5–3.6, Table 3](https://arxiv.org/html/2606.03108v2) | SWE targets 4B/9B; fixed Sonnet 4.6 trainer; human-gated launches/promotion. Other-domain target sizes were not verified in this pass. | No verified >=27B branch; scale-unverified reference, not an assertion that every experiment is small. |
| [Co-Harness §3–4](https://arxiv.org/html/2607.22688v1) | 8B and 32B branches; alternating harness optimization and SFT. | 32B passes scale, but the prior contribution/causal-review gate remains pending. |

Harness-role contributions retain their earlier primary-source locators. RQGM updates agent/evaluator code, whereas Self-Taught Evaluators trains evaluator weights: the word “evaluator” cannot determine the layer. The six Harness functions and eighteen research-space positions are this project's analytical organization, not author-claimed categories or proofs of worldwide research gaps.

The >=27B cutoff is a user-selected main-view scope. Total and active parameters are distinct; a LoRA-trained 30B model does not mean 30B trainable adapter parameters or 30B dense compute. Small models are not added together, and frozen teacher/evaluator/API models do not satisfy the actual-target gate. Source facts remain author-reported and were not independently reproduced.

## 2026-10-18 coverage correction: the 12-case view was not a field census

The earlier 8/2/2 view was an incomplete editorial selection. It was not the result of rejecting the rest of the field. This update adds missing primary-source claim reviews and preserves the difference between iterative task learning, self-modification of an improver, and one-pass joint adaptation. No new result is independently reproduced.

### STOP

- Source fact / locator: [首页署名与脚注；§3–4、Algorithm 1、迁移实验](https://arxiv.org/pdf/2310.02304v3). 用调用冻结 GPT-4 的改进程序修改该改进程序自身。 改进程序产生后继；后继继续生成程序改进。
- Reported evidence / distributions / resources: 作者报告后继改进程序在受限算法任务上优于种子，包含跨任务检验。 GPT-4 冻结；改进器代码可变；算法任务与规定调用预算。
- BeforeRSI judgment: 机制和回流已核对，纳入重点案例；不等于所有递归主张均已证明。 任务规模有限；作者也未称为全部组件均可改的完整 RSI。

### Promptbreeder

- Source fact / locator: [首页；§3、§4、Table 1；ICML 2024 正式版另列](https://arxiv.org/pdf/2309.16797v1). 共同演化任务提示与生成变异的提示，基础模型冻结。 任务提示与对应变异提示共同进入后继种群。
- Reported evidence / distributions / resources: 在算术、常识和分类任务上报告提示搜索收益，并分析自指成分。 PaLM 2-L 冻结；多代种群；训练样本作适应度、测试集报告结果。
- BeforeRSI judgment: 机制和回流已核对，纳入重点案例；不等于所有递归主张均已证明。 提示演化不等于模型训练，也不证明开放任务上的持续加速。

### SICA

- Source fact / locator: [首页；§3、Algorithm 1；§4 与 Appendix D](https://arxiv.org/html/2504.15228v1). 从历史档案选当前最佳 agent，让它修改自己的代码库。 被选中的后继 agent 承担下一轮自修改。
- Reported evidence / distributions / resources: 作者在 SWE-bench Verified 随机子集报告 17%→53%，并报告其他编码/推理任务结果。 冻结 LLM；SWE 子集、LiveCodeBench 与合成任务；选择效用含时间和费用。
- BeforeRSI judgment: 机制和回流已核对，纳入重点案例；不等于所有递归主张均已证明。 不能把子集分数说成完整 SWE-bench 成绩；未证明后继改进效率持续增长。

### ACE

- Source fact / locator: [首页；§3–4，尤其 §3.1–3.2、§4.5–4.6](https://arxiv.org/html/2510.04618v1). 从轨迹提炼经验，以局部增量更新持久 playbook。 新任务使用已维护的经验，再把成败反馈写回经验库。
- Reported evidence / distributions / resources: AppWorld 与金融任务报告收益；有反思、维护组件消融和成本分析。 冻结基座；离线上下文优化和在线记忆适应；不训练模型权重。
- BeforeRSI judgment: 机制和回流已核对，纳入重点案例；不等于所有递归主张均已证明。 证据是经验积累与任务适应；反思/维护算法本身没有自动进化。

### Iterative RPO

- Source fact / locator: [首页；§2、§3.1–3.3、Appendix A](https://arxiv.org/html/2404.19733v2). 用当前模型生成推理候选，按答案正确性组成偏好对，再用 DPO+NLL 更新。 新权重生成下一轮偏好对，并作为下一轮参数与参考模型。
- Reported evidence / distributions / resources: 70B 多轮训练改善三个推理任务，包含 DPO/NLL 消融；收益最终饱和。 Llama-2-70B-Chat；GSM8K、MATH、ARC-Challenge；固定训练问题和答案。
- BeforeRSI judgment: 机制和回流已核对，纳入重点案例；不等于所有递归主张均已证明。 依赖外部正确答案；没有学习训练算法或证明通用自主科研能力。

### DeepSeekMath-V2

- Source fact / locator: [§2.1–2.3、§3.1–3.3；官方 Math-V2 config.json 与 V3.2-Exp 部署配置](https://arxiv.org/html/2511.22570v1). 迭代训练证明验证器与生成器，并用元验证筛选自动标注。 生成器产生更难证明→验证/元验证标注→更新验证器→再训练生成器。
- Reported evidence / distributions / resources: 最后两轮由自动标注取代人工标注；报告数学证明表现及专家评估。 DeepSeek-V3.2-Exp-Base 的 671B 级模型；公开配置仅路由专家矩阵已超过 653.9B。
- BeforeRSI judgment: 机制和回流已核对，纳入重点案例；不等于所有递归主张均已证明。 非形式化验证仍可能犯错；高计算搜索成绩不是单次生成分数，亦未证明全域递归加速。

### Kimi K2 · 自评价 RL

- Source fact / locator: [§1、§3.2.2–3.2.3、§4 与 Appendix F](https://arxiv.org/html/2507.20534v1). K2 actor 生成回答，K2 critic 按 rubric 提供偏好，critic 又从可验证的 on-policy 轨迹更新。 当前策略轨迹更新 critic；critic 的反馈继续训练策略。
- Reported evidence / distributions / resources: 技术报告明确描述策略—critic 闭环；最终模型有广域评测。 约 1.04T 总参数、32B 激活；本卡只纳入后训练自评价机制。
- BeforeRSI judgment: 机制和回流已核对，纳入重点案例；不等于所有递归主张均已证明。 报告未充分隔离该闭环对最终总成绩的因果贡献；人工 rubric 仍是锚点。

### ReST-EM

- Source fact / locator: [首页；§3 Algorithm 1、§5–6、Figure 4/7](https://arxiv.org/pdf/2312.06585v4). 生成自训练样本、用外部二元反馈筛选，再监督学习；反复交替。 每轮从原基座重训，但样本由上轮改进模型产生。
- Reported evidence / distributions / resources: PaLM 2 的数学/编码训练与任务外迁移；重置基座的对照。 PaLM 2-S / 2-L；本论文未公开精确参数，不能将图中的 62B/540B 对照当作训练对象。
- BeforeRSI judgment: 机制有直接证据，实际训练总参数未核准；不是低价值排除。 外部验证规则与更新程序固定；规模未知不表示低于 27B。

### SIMA 2

- Source fact / locator: [首页；§3.3、§4.5，Figures 15–17](https://arxiv.org/html/2512.04797v1). Gemini 出题并评价游戏轨迹；agent 从自生成经验继续训练。 更新 agent 再产生经验，任务选择可聚焦弱项；外部 Gemini 组件未证参数共演。
- Reported evidence / distributions / resources: ASKA 技能/进度改善；Genie 3 城市场景训练后在自然场景测迁移。 Gemini 基础模型；训练目标参数未公开核准。
- BeforeRSI judgment: 机制有直接证据，实际训练总参数未核准；不是低价值排除。 未证明 task setter、reward model 或世界模型也随 agent 共同训练。

### AlphaProof

- Source fact / locator: [Agent / Training / Methods: Proof network；test-time RL](https://www.nature.com/articles/s41586-025-09833-y). 证明搜索和 Lean 校验产生经验训练策略/价值网络，难题再做测试时 RL。 搜索成功轨迹与变体反馈进入证明网络训练。
- Reported evidence / distributions / resources: 报告正式竞赛级证明与主训练、测试时学习机制。 主证明网络 3B；Gemini 自动形式化模型的规模不能替代它。
- BeforeRSI judgment: 实际训练目标低于27B，保留机制参考；不是质量否定。 不满足本项目 ≥27B 主图门槛，但不能因此判为低质量；外部训练程序仍固定。

### Constitutional AI

- Source fact / locator: [§1.2、§3、§4；Figure 2 的 52B RL runs](https://arxiv.org/html/2212.08073v1). 自批评/修订样本用于 SFT；AI 偏好训练奖励模型，再用于 RL。 AI 输出和偏好进入后续权重训练；未证持续重复整个系统共演。
- Reported evidence / distributions / resources: 52B 实验有人类对比评价；帮助性仍使用人类反馈。 含 52B 策略；不是无人工目标、无人工数据。
- BeforeRSI judgment: 关键前身/比较基线，保留贡献但不计入直接演化重点数。 关键 AI4AI 前身；论文没有证实改进器不断自改的多代闭环。

### ADAS

- Source fact / locator: [首页；§3、§4.3、Appendix G](https://arxiv.org/html/2408.08435v1). 固定 meta-agent 依据档案编写、评测目标 agent 的 forward 实现。 设计结果写回档案；改进器从档案学习上下文，但其实现固定。
- Reported evidence / distributions / resources: 报告 ARC、推理任务和跨域/跨模型迁移；有成本附录。 冻结基础模型；meta-agent 与目标 agent 分离。
- BeforeRSI judgment: 关键前身/比较基线，保留贡献但不计入直接演化重点数。 自动设计前身；生成的目标 agent 没有替换固定 meta-agent。

### GEPA

- Source fact / locator: [首页；§2–4、Algorithm 1、实验与成本设置](https://arxiv.org/pdf/2507.19457v2). 反思执行轨迹、修改提示，并从 Pareto 前沿组合互补候选。 候选提示及轨迹反馈进入后续搜索；外层优化算法固定。
- Reported evidence / distributions / resources: 六任务报告与 GRPO、MIPROv2 的比较；需要同时看反思模型成本。 提示优化基座冻结；GRPO 是对照，不应把其训练算成 GEPA 的参数更新。
- BeforeRSI judgment: 关键前身/比较基线，保留贡献但不计入直接演化重点数。 优化器本身未证自改；较少 rollout 不等于同比总 FLOPs 或费用。

### LLMs Can Self-Improve

- Source fact / locator: [首页；§2–3、消融；2022 预印本 / EMNLP 2023](https://aclanthology.org/2023.emnlp-main.67.pdf). 用 self-consistency 筛选自生成推理样本，再微调同一模型。 自身生成样本回到参数更新；未证多代循环。
- Reported evidence / distributions / resources: PaLM 540B 在多项推理任务报告改善及多样性消融。 PaLM 540B；2022 预印本、2023 正式发表。
- BeforeRSI judgment: 关键前身/比较基线，保留贡献但不计入直接演化重点数。 一轮自训练前身；不把它计成已证持续递归系统。

## 2026-10-19 — Public-literature graph reconstruction

**Source facts added:** the bibliography now includes the primary versions used for paper affiliations, checked full paper titles, and the extra method readings below. `data/literature-affiliation-sources.json` records the new title-page checks. An affiliation check establishes authorship metadata only; it does not promote the paper to a full method or quality review. Institutions are not inferred from funding or the model provider. The Co-Harness v1 title page identifies Meituan, Ai2 and an independent affiliation.

**Editorial representation:** the current reader has 97 route positions (38 Harness, 34 Model, 25 mixed), eight cross-route references and 22 historical/background entries. Forty-one cards contain selected-method readings; 64 are abstract/source screens. The old 38 claim reviews/19-case shortlist remains distinct. Thirteen source-explicit paper relations and 30 method comparisons are encoded separately, with original URLs and locations on every edge. These numbers are coverage progress, not worldwide quality judgments. Principal-route labels are relative to the selected learning object; cross-route method links retain multi-component structure.

### Voyager — skill-library mechanism reading

[Primary source, §2–3](https://arxiv.org/html/2305.16291v2): a frozen GPT-4 agent proposes executable skills, revises them using environment/error/self-verification feedback, and saves successful code for later retrieval and composition. The curriculum and model-call program are fixed. The paper reports Minecraft exploration and transfer to new worlds. This adds a Harness method card; no matched-compute reproduction or exhaustive cost extraction is claimed. Persisted code-skill reuse is not evidence that the curriculum generator or improvement algorithm rewrites itself.

### MemRL — nonparametric memory utility

[Primary source, §3–4, especially Eq. (8)](https://arxiv.org/html/2601.03192v1): similarity retrieval is followed by utility-based memory selection. The implemented episodic utility update is Q←Q+α(r−Q); it should not be silently replaced by the general TD equation discussed elsewhere in the paper. The inference LLM stays frozen. Retained memories and utility values affect later tasks. The card describes the memory mechanism; full benchmark-cost accounting and independent replication remain absent.

### SkillRL — skill bank and policy learning; 7B scope correction

[Primary source, §2–3, §4.1 and Tables 1–2](https://arxiv.org/html/2602.08234v1): hierarchical skills augment the policy context and are revised from trajectories while the policy is trained. Qwen2.5-7B-Instruct is the actual trained policy; o3 supplies skill/SFT data, and GRPO updates the policy. ALFWorld, WebShop and search QA are reported. This is a mixed-route mechanism card but belongs to the sub-27B supplement. Neither the larger teacher nor comparison to large models establishes a ≥27B trained target. The Table 1 MemRL baseline is a source-explicit comparison edge, not an inheritance claim. The full implementation and all appendices were not reviewed.

### Harness-R1 — learned engineer; 9B scope correction

[Primary source, abstract, §4 settings, Appendix B.1–B.2](https://arxiv.org/html/2608.02276v1): the engineer is a separate 9B model initialized by SFT and trained with online GRPO from patched-target rerun rewards. Main-loop target weights are frozen. The paper also tests a separately fine-tuned target and larger transfer targets. These are not evidence of sustained bidirectional coevolution. It is placed with learned improvers in Model, with a cross-route workflow link, and excluded from the default graph by the size scope. This is a bounded setting check; its overall reading status remains a source screen.

### EURISKO — historical explanation rewritten

[Lenat primary paper, abstract and representation/control discussion](https://www.cs.northwestern.edu/~mek802/papers/not-mine/Lenat_EURISKO.pdf): concepts and heuristics have manipulable representations; retained rules influence later discovery. The card now explains the research problem, representation, feedback and domain limitations in Chinese. It remains historical background, outside the three contemporary LLM route views.
