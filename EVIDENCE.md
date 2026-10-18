# Evidence and judgment

This document separates scientific value from the label attached to a project. A work can be useful without being RSI. A work can also contain a genuine result while making a broader claim than its evidence supports.

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
