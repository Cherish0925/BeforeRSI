# BeforeRSI

<div align="center">

<img src="assets/beforersi-hero.svg" width="100%" alt="BeforeRSI — recursive self-improvement needs a sharper test">

<br>

[![Status](https://img.shields.io/badge/status-research%20in%20progress-111827?style=flat-square)](#status)
[![Corpus](https://img.shields.io/badge/candidate%20sources-622%20records-C58B35?style=flat-square)](research/scope-catalog.md)
[![Claim depth](https://img.shields.io/badge/claim%20depth-D0%E2%86%92D4-5C9C96?style=flat-square)](#claim-depth)
[![CI](https://img.shields.io/github/actions/workflow/status/Cherish0925/BeforeRSI/validate.yml?branch=main&style=flat-square&label=data)](https://github.com/Cherish0925/BeforeRSI/actions)
[![License](https://img.shields.io/badge/license-MIT-6B7280?style=flat-square)](LICENSE)

**[中文研究地图](RESEARCH_ATLAS.md)** · **[RSI scope](RSI_SCOPE.md)** · **[Frontier coverage](FRONTIER_COVERAGE.md)** · **[Theory](THEORY.md)** · **[Mechanisms](MECHANISMS.md)** · **[Compatibility](COMPATIBILITY.md)** · **[Map](MAP.md)** · **[Evidence](EVIDENCE.md)** · **[Program](PROGRAM.md)** · **[Evaluation](EVALUATION.md)** · **[Learned search](SEARCH.md)** · **[Hypotheses](HYPOTHESES.md)**

</div>

---

## 三张领域知识图谱：先看研究结构，再读论文

**[打开 RSI_Field_Atlas_v5_1.html](research/atlas/RSI_Field_Atlas_v5_1.html)** · **[领域结构文字版](research/atlas/field-guide.md)** · **[图谱阅读档案](research/atlas/literature-cards.md)** · **[参考文献](research/atlas/references.md)**

![首页直接呈现三张领域知识图谱](assets/atlas/landscape-overview.png)

三条路线包含 **29 个研究主题、146 个子问题、60 条机制联系**。首页直接显示三张图；进入路线后可展开全部子问题，也可点击主题查看关键问题、技术、相邻联系及论文与团队。图谱首先组织研究对象和机制，再挂接公开工作；空白研究位置不会因当前目录缺少论文而消失。

| 领域图 | 组织主线 | 研究主题 | 子问题 |
|---|---|---:|---:|
| Harness | 可修改资产 → 反馈、搜索与选择 → 改进器、继承与迁移 | 10 | 51 |
| Model | 自生成经验、偏好、验证、评价者、课程与参数学习之间的关系 | 10 | 51 |
| Model × Harness | 外部经验内化、能力用于系统改写、共同适配与双向反馈 | 9 | 44 |

[Harness 领域图](assets/atlas/harness-field-graph.svg) · [Model 领域图](assets/atlas/model-field-graph.svg) · [Model × Harness 领域图](assets/atlas/hybrid-field-graph.svg)。图中关系的解释与原文例证可点击读取；论文关系图另外区分明确引用、扩展与方法对照。

本轮对 **622 条候选来源记录**进行逐项原文阅读与比较：567 条检索记录，加 55 项未被检索池覆盖的既有资料。这个数目包含论文、技术报告、历史与相邻研究，不是 622 项独立 RSI 成果，也不是全世界研究的普查总量。当前仍在审读，动态统计见 HTML 的“全量阅读与研究取舍”及 [完整审查数据](data/corpus-review.json)。

主图默认显示比较后选出的重点研究；可扩展到方法、证据与规模补充。**完整搜索覆盖全部候选，包括移出主图的工作与具体理由。** 原文明示的继承/使用关系和综述分析的机制比较分别标记。约 20% 的保留预期不作为数量配额；范围外、重复、证据不足和相关但不入重点图均不等同“劣质”。

Model / 混合路线以实际训练主体 ≥27B 为默认范围偏好，冻结教师不计入训练规模，部分披露或源间冲突另行说明。全文阅读、承接既有阅读后的原文复核、仅有官方技术材料分别记录；读取分析不等于独立复现。HTML 只呈现公开研究及审查，不包含本项目自己的理论方案。早期 PDF 是旧快照，不代表本轮结论。

**公司与团队入口已接入三张领域图。** 共 27 个来源档案：24 个关联具体研究、Discovery Loop 仅公开方向、Reflection / MiroMind 另列邻近研究。元环智能、Apex、Nous Research、Recursive、Intology、Autoscience 等均可按公司名或项目名检索；关联 34 项去重研究。发布、共同署名和项目托管分别记录。公司数量不是已验证 RSI 系统数量，也不是全球普查结果。

[公司与研究关联表](research/atlas/industry-guide.md) · [公司数据与来源](data/industry-landscape.json)

## What must be true before RSI is real?

**Current scope and coverage:** A full-source audit is in progress over a fixed inventory of 622 candidate records. The original catalog IDs are preserved, with new selected research added through explicit curation bindings. The current source ledger, decisions and access boundaries are in [corpus-review.json](data/corpus-review.json). Earlier numbered catalogs and claim reviews remain dated historical records; none is a field census or a final quality ranking. The survey HTML is separate from this repository's theoretical research below.

**BeforeRSI** studies one question:

> When can we say that an AI system has improved its own capacity to improve?

A better answer after more sampling is not enough. A benchmark score obtained after repeated access to the benchmark is not enough. A fixed optimizer producing a better prompt or workflow is not enough. A joint model–harness gain establishes a result for the pair; separate component claims require additional interventions.

The object of study is a versioned AI system:

$$
S_t=(M_t,H_t,D_t),
$$

where **M** records learned models, **H** executable orchestration, and **D** persistent information. **Improver** is a role performed by a configured system; it can use the same model and harness as task solving. Environment, resource budgets, and assessment protocol are declared separately. Each artifact has one recorded owner.

<div align="center">
<img src="assets/rsi-mainline.svg" width="96%" alt="BeforeRSI research spine">
</div>

The central empirical target is stronger than task performance and than the
structural recursive reuse that some papers call RSI:

$$
S_t \xrightarrow{\text{self-modification}} S_{t+1}
\qquad\text{and then}\qquad
S_{t+1}\ \text{must be a better improver than}\ S_t.
$$

Test that second statement by letting parent and successor improve identical copies of common targets under matched budgets. **[THEORY.md](THEORY.md)** defines this comparison and gives counterexamples to the previous growth interpretation. It does not claim an identified law of RSI.

One-step improvement ability does not guarantee a better multi-generation
endpoint. THEORY.md Section 9 gives the exact finite-budget continuation
comparison, including a counterexample with monotone gains under both routes.
[Experiment 006](experiments/006-recursive-optimizer/RESULTS.md) now contains
executed numerical-optimizer self-reuse, training-objective and update-order
comparisons. It reports negative and inconclusive results alongside the measured
order effect; these are bounded numerical experiments, not LLM training runs.

## From representation to explanation

[MECHANISMS.md](MECHANISMS.md) derives how proposal distributions, diagnostic feedback, selection, inheritance, task transfer and continuation interact. It connects representative primary-source methods and ablations to distinct predictions, with a [127-entry mechanism map](research/mechanism-map.md). Scope labels and exact reading boundaries are separate from explanatory interpretations.

The resulting route learns reusable research operations while preserving their decision inputs. It selects training sources by downstream update value, instead of assuming the best executing harness is the best teacher. [Experiment 007](experiments/007-feedback-structure/RESULTS.md) executes a controlled information-localization construction; it is not an LLM reproduction.

## An executable bridge from learning to improvement cost

[SEARCH.md](SEARCH.md) connects existing policy-guided search bounds to an
actual learned search-and-reuse loop. It also distinguishes retaining a whole
ancestor computation from mixing ancestor actions locally; the former admits
a pointwise completion guarantee under explicit scheduling assumptions.

[Experiment 008](experiments/008-learned-search/RESULTS.md) trains 2,592-parameter
context policies from solutions found by search. Four paired lineages compare
frozen and reused collection, imitation and search-bound losses, and local
versus whole-search preservation. A common-target intervention trains identical
fresh learners from each final actor's search results. Reuse improves both
solver and data-producing actor performance in this bounded puzzle domain;
resource measurements and a declared distribution-shift follow-up are included.

## The research spine

The history of self-improving AI is easiest to understand as five streams that now meet:

| Stream | What it contributed | What remains unresolved |
|---|---|---|
| **Self-reference** | programs and agents that can modify their own executable description | whether self-reference produces transferable improvement rather than bounded self-editing |
| **Search** | evolutionary search, program synthesis, prompt/workflow optimization | whether the optimizer itself improves, rather than only its target |
| **Learning to learn** | meta-learning, self-play, self-training, self-generated rewards | whether repeated weight updates remain reliable and useful as models become stronger |
| **External cognition** | memory, tools, skills, context, agent control, harnesses | where durable capability should live and whether harness gains transfer across models |
| **Verification** | exact checks, learned judges, hidden tasks, selection under uncertainty | how to prevent benchmark fitting, evaluator exploitation, and metric drift |

The mainline is **AI improving its learning and development processes, with the result reused in subsequent improvement**. Self-editing improvers, learned training interventions, co-evolving curricula/evaluators/environments and model–harness compatibility are the main comparisons. General AI4Science and ordinary foundation-model reports remain background unless a specific feedback path justifies inclusion.

Read the full historical and causal map in **[MAP.md](MAP.md)**.

## Claim depth

BeforeRSI does not classify whole projects as “RSI” or “not RSI.” It asks what a specific experiment actually establishes.

| Level | Claim | Minimum observation |
|---|---|---|
| **D0** | task-time adaptation | better current-task output; no persistent successor required |
| **D1** | persistent self-modification | a versioned change survives into later tasks |
| **D2** | transferable self-improvement | the change improves untouched tasks, models, environments, or cost |
| **D3** | improved self-improvement ability | the successor improves common reference targets more effectively under matched budgets |
| **D4** | open-ended RSI | D3 persists as tasks and bottlenecks change, without rapid saturation |

These levels are this repository's evidence convention. They do not require improvement to accelerate at every generation. Useful D0/D1 results retain their value; D3/D4 require the corresponding observations.

## What the public record says now

The strongest public work has already established several pieces of the puzzle:

- **persistent capability can live outside weights** — prompts, context, memory, tools, workflows and executable agent code can materially change a fixed model's realized capability;
- **self-modification can be executable** — agents can inspect, edit, test and retain changes to their own software;
- **model updates can be self-generated** — self-training, self-generated rewards and AI-generated update data can improve model behavior in bounded settings;
- **model and harness can be improved together** — recent systems expose both as editable objects and begin to test component transfer;
- **selection quality is a first-class constraint** — hidden tasks, cost accounting, lineage and independent acceptance materially change what counts as an improvement.

The checked sources now include large-scale weight-level co-training and AI-assisted production-model development. Their existence must not be denied because they fail a narrower preferred definition. What this repository **has not established** is a common predictive law across these systems, sustained broad improved improvement under comparable resources, or exhaustive coverage of public and private frontier research.

The source-backed record is in **[EVIDENCE.md](EVIDENCE.md)** and the machine-readable corpus is in **[data/works.json](data/works.json)**.

## The system we actually want to test

One route under test alternates harness changes, learning from trajectories, and renewed system design:

$$
(M_t,H_t)
\rightarrow D_{t+1}^{\mathrm{development}}
\rightarrow M_{t+1}
\rightarrow H_{t+1}.
$$

1. improve a **portfolio of harnesses** around a fixed model;
2. collect matched trajectories and verify them independently;
3. update the model from evidence-bearing trajectories rather than undifferentiated logs;
4. cross old/new models with old/new harnesses to locate the gain;
5. rebuild the harness around the new model instead of assuming the old optimum remains optimal;
6. improve the improver using candidate lineage, failed hypotheses and transfer results;
7. compare parent and successor **as improvers** on a new improvement problem;
8. repeat only while held-out gain survives cost, regression and contamination controls.

The detailed design is in **[PROGRAM.md](PROGRAM.md)**. This schedule and its portfolio are hypotheses; model-only, harness-only, joint, and other schedules remain valid alternatives. No independent improver module is required.

## Experimental sequence

<table>
<tr>
<td width="33%" valign="top">

### 01 · Harness transfer

Does an evolved harness still win after the parent receives the same total compute?

[Protocol →](experiments/001-harness-transfer.md)

</td>
<td width="33%" valign="top">

### 02 · Model × Harness

Evaluate the full cross:

(M0,H0) · (M1,H0) · (M0,H1) · (M1,H1)

[Protocol →](experiments/002-model-harness-cross.md)

</td>
<td width="33%" valign="top">

### 03 · Successor as improver

Under the same improvement budget, does $S_1$ produce a better descendant than $S_0$?

[Protocol →](experiments/003-successor-as-improver.md)

</td>
</tr>
</table>

These experiments form an ordered candidate harness branch. They are not the
general research priority specified in FRONTIER_COVERAGE.md. Experiment 03
directly tests **improved improvement ability** on common targets; recursive
reuse is a separate structural claim.

4. **[Repeated co-evolution](experiments/004-repeated-coevolution.md)** — run model, harness, and improver updates for several generations against model-only, harness-only, fixed-improver, and equal-compute baselines.
5. **[Evaluator fidelity and search efficiency](experiments/005-evaluator-phase-boundary.md)** — distinguish absolute selected gain, gain per unit cost, and adaptive exploitation as search grows.

## What this repository rejects

BeforeRSI does not upgrade a result because its title contains *recursive*, *self-evolving*, *autonomous* or *self-reflective*. The following are insufficient on their own for the stronger claim that the successor is a better improver:

- extra samples, retries, agents or evaluator calls;
- a fixed outer optimizer repeatedly improving a target;
- benchmark-specific prompt or workflow patches;
- self-generated data without evidence that later improvement behavior became better;
- joint model/harness task gains without measuring subsequent improvement ability;
- one successful parent → child update without comparing improvement ability;
- gains demonstrated only on small models and extrapolated to frontier models;
- self-evaluation used as the sole acceptance test.

These methods may be valuable results, useful components, or strong baselines. Component crossing is needed for component attribution, not for establishing every joint-system gain. **[EVALUATION.md](EVALUATION.md)** specifies what stronger claims require.

Generality requires mechanism coverage and testable predictions across methods. It does not follow from mapping papers into shared notation. [COMPATIBILITY.md](COMPATIBILITY.md) records both the current coverage and the claim-based criteria for choosing substantive work; rigorous negative results and counterexamples remain part of the research.

## Repository

| File | Purpose |
|---|---|
| **[FRONTIER_COVERAGE.md](FRONTIER_COVERAGE.md)** | major-lab mechanisms, substantive omissions, source limits and the revised research scope |
| **[SEARCH.md](SEARCH.md)** | search-effort objectives, complete-computation preservation, and the executable learning loop |
| **[THEORY.md](THEORY.md)** | implementation boundaries, common-target improvement tests, coupling, and mathematical counterexamples |
| **[RSI_SCOPE.md](RSI_SCOPE.md)** | Chinese scope correction, filtering results, key evidence and research consequences |
| **[research/scope-catalog.md](research/scope-catalog.md)** | all 138 entries separated by relevance, plus deferred/excluded candidates |
| **[COMPATIBILITY.md](COMPATIBILITY.md)** | dated representation of the earlier 127 catalog entries and limits of universality claims |
| **[MECHANISMS.md](MECHANISMS.md)** | conditional explanations, derivations, interventions and learner-aware research route |
| **[research/mechanism-map.md](research/mechanism-map.md)** | causal operation, failure condition and separating intervention for the earlier 127-entry mechanism review |
| **[MAP.md](MAP.md)** | history, causal structure, knowledge tree and present frontier |
| **[EVIDENCE.md](EVIDENCE.md)** | strongest public work, claim depth, limitations and primary sources |
| **[PROGRAM.md](PROGRAM.md)** | research-production mechanisms and candidate implementation branches |
| **[EVALUATION.md](EVALUATION.md)** | hidden/time-forward tests, cost controls, attribution, regression and recursion tests |
| **[data/works.json](data/works.json)** | machine-readable public research corpus |
| **[data/knowledge-graph.json](data/knowledge-graph.json)** | curated core graph with typed relations; provenance in quality-review.json |
| **[experiments/](experiments/)** | protocols and the executed bounded optimizer experiment |
| **[Experiment 006](experiments/006-recursive-optimizer/RESULTS.md)** | executed numerical optimizer experiments, task-level records, resource counts and reproducible figures |
| **[Experiment 008](experiments/008-learned-search/RESULTS.md)** | actual context-policy learning, recursive reuse, common-target data generation and measured costs |
| **[SIMULATION.md](SIMULATION.md)** | illustrative trajectories, identification limits, and reproducible plots |
| **[HYPOTHESES.md](HYPOTHESES.md)** | working propositions, alternatives and decisive tests |
| **[RESEARCH_LOG.md](RESEARCH_LOG.md)** | distilled lineage of the project's changing representations and decisions |
| **[AGENTS.md](AGENTS.md)** | multi-agent research protocol and epistemic rules |

The repository stays small on purpose. New files are added when they contain a new source audit, a testable claim, an experiment, or a result.

## Status

**October 2026.** The historical map and experimental program are established; the corpus is still being audited claim by claim. Author-reported results remain labeled reported until they are independently rerun or replicated.

Experiment 006 did not establish a positive common-target improver advantage
or a generally superior schedule. Experiment 008 establishes a positive bounded
search-and-learning result under its declared conditions, including a common
fresh-learner comparison. These different outcomes constrain different routes;
neither is a universal claim about open-ended RSI.

---

<div align="center">
<sub>BeforeRSI asks for stronger evidence before stronger words.</sub>
</div>
