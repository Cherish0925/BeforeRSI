# Research lineage

This is a distilled record of the substantive reasoning that led to the current BeforeRSI program. It preserves changes in representation, failed framings, open alternatives, and the experiments proposed to distinguish them. It is not a raw conversation transcript.

**Historical status:** entries before the continuation audit at the end preserve earlier proposals, including claims now superseded. Current definitions are in THEORY.md; historical equations are not current results.

## 2026-08 — Strict self-improvement criteria

An early concern was that memory, prompt editing, skill libraries, and harness changes were often called self-evolution even when they produced no transferable or persistent capability.

The working criteria became:

$$
\text{experience}
\rightarrow
\text{evaluation}
\rightarrow
\text{learning signal}
\rightarrow
\text{persistent modification}
\rightarrow
\text{retention/transfer}
\rightarrow
\text{better future learning}.
$$

A useful separation emerged between four modification surfaces:

- persistent state: memory, prompts, skills, external context;
- parameters: model weights;
- architecture and executable code;
- the learning or improvement procedure itself.

This made it possible to treat harness improvement as potentially substantive without equating every state update with RSI.

## 2026-10-16 — Why BeforeRSI

The project was named **BeforeRSI** because the public field does not yet have a single stable definition, measurement protocol, or agreed mechanism for RSI.

Several observations motivated the repository:

- public work uses the same term for task-time search, memory accumulation, prompt optimization, self-training, code self-modification, harness evolution, and meta-improvement;
- small-model or bounded-task results often do not establish transfer to stronger models;
- frontier-lab practice is largely opaque, so public evidence and private possibility must be kept separate;
- benchmark gain is confounded by extra compute, repeated exposure, evaluator exploitation, and local compensation;
- model and harness gains are frequently measured jointly without attribution.

The repository therefore began as an evidence map rather than a claim that RSI had already been solved.

## 2026-10-16 — Claim depth

A five-level claim scale was introduced:

- **D0:** task-time search or adaptation;
- **D1:** persistent self-modification;
- **D2:** transferable self-improvement;
- **D3:** successor is a better improver;
- **D4:** D3 persists across changing tasks and bottlenecks without rapid saturation.

The central reason for the scale was to stop one-step improvement from being described as recursive improvement.

## 2026-10-16 — The system boundary

The minimal mutable system became

$$
S_t=(M_t,H_t,I_t,D_t),
$$

with external task environment, protected evaluator, and budget

$$
\Omega_t=(E_t,V^*,B_t).
$$

This separated:

- the model;
- the harness;
- the improver;
- persistent information;
- the environment;
- the final acceptance process;
- resource constraints.

The protected evaluator was kept outside the editable candidate state so that changing the metric could not masquerade as changing the capability.

## 2026-10-16 — Model–harness attribution

The minimum attribution experiment became the full cross

$$
(M_0,H_0),\quad
(M_1,H_0),\quad
(M_0,H_1),\quad
(M_1,H_1).
$$

The interaction

$$
\Gamma_{MH}
=
J_{11}-J_{10}-J_{01}+J_{00}
$$

distinguishes additive gain from positive synergy, conflict, and local co-adaptation.

This led to the stronger statement that the optimal harness is generally model-dependent:

$$
H^*=H^*(M,E,B).
$$

## 2026-10-16 — The experimental dependency chain

Three experiments were defined before stronger RSI claims:

1. **Harness transfer under equal total compute** — distinguish persistent improvement from extra search.
2. **Model × Harness attribution** — locate the gain and measure cross-version portability.
3. **Successor as improver** — compare parent and successor on a new improvement problem under the same budget.

Two later experiments were then identified as necessary:

4. **Repeated co-evolution** — determine whether the full cycle compounds or saturates.
5. **Evaluator phase boundary** — determine when search becomes noise selection or metric exploitation.

## 2026-10-17 — From scores to successor distributions

A scalar capability score was judged insufficient for recursion.

The central mathematical object became the improvement kernel

$$
S_{t+1}
\sim
K_{S_t}(\cdot\mid S_t,\Omega_t),
$$

which describes the distribution of successors produced by the current system under a resource budget.

The recursive statement became

$$
K_{S_{t+1}}\succ K_{S_t},
$$

meaning the successor generates better descendants on new improvement problems.

This formulation can represent model updates, harness edits, code rewrites, data generation, and changes to the improver without choosing one implementation in advance.

## 2026-10-17 — Improvement efficiency

A macro-variable was introduced:

$$
\eta
=
\frac{
\mathbb E[\Delta J_{\rm transfer}-\lambda L_{\rm regression}]
}{
C_{\rm improve}
}.
$$

This separates:

$$
J_{t+1}>J_t
$$

from

$$
\eta_{t+1}>\eta_t.
$$

The first means the system became stronger. The second means the system became more efficient at manufacturing future capability.

The possibility that no stable scalar $\eta$ exists remains open; the kernel or a vector-valued frontier may be required instead.

## 2026-10-17 — Resource-normalized dynamics

Cumulative improvement resource $r$ replaced wall-clock time as the natural independent variable:

$$
\frac{ds}{dr}=F(s)+\xi(r).
$$

For capability functional $J$,

$$
\frac{dJ}{dr}=\nabla J^\top F.
$$

The acceleration decomposes as

$$
\frac{d^2J}{dr^2}
=
F^\top\nabla^2J\,F
+
\nabla J^\top(DF)F.
$$

The first term is capability-landscape curvature. The second is the candidate recursive term: the current update changes the future improvement field.

This was an important correction to the naive idea that accelerating capability alone proves RSI.

## 2026-10-17 — Co-evolution matrix

The system was projected to measurable macrovariables

$$
x=(m,h,i,d,v),
$$

for model, harness, improver, data/experience, and evaluator fidelity.

Local coupling is represented by

$$
K=DF(x).
$$

Cross-terms such as $K_{HM}$, $K_{MH}$, $K_{IM}$, and $K_{IH}$ express genuine co-evolution. Eigenmodes may identify harness-limited, verification-limited, or coupled model–harness–improver regimes.

A positive eigenvalue is not sufficient: the growing mode must project positively onto protected capability and future improvement ability.

## 2026-10-17 — Harness portfolios and evolutionary dynamics

A single best harness was judged insufficient under model and task nonstationarity.

The proposed state became a harness distribution or portfolio:

$$
p_{t+1}(h')
=
\frac{1}{Z_t}
\int
Q_I(h'\mid h)
p_t(h)
e^{\beta\widehat g(h')}
dh.
$$

The selection-pressure parameter $\beta$ exposes a tradeoff:

- too large: premature collapse, benchmark fitting, loss of stepping stones;
- too small: excessive exploration cost.

This motivates portfolio plus lineage rather than greedy replacement.

## 2026-10-17 — Externalization and internalization

Model and harness were interpreted as two computational media with different update and execution costs.

The proposed long-run cycle became:

$$
\text{externalize}
\rightarrow
\text{explore}
\rightarrow
\text{verify}
\rightarrow
\text{internalize}
\rightarrow
\text{re-externalize}.
$$

A harness capability should be internalized when expected future savings exceed training, validation, and regression cost:

$$
N(c_H-c_M)
>
C_{\rm train}
+
C_{\rm validation}
+
C_{\rm regression}.
$$

This is a working economic criterion, not an established law.

## 2026-10-17 — Evaluator fidelity and search size

Candidate search was modeled as noisy selection:

$$
y_j=g_j+\epsilon_j+b_j.
$$

With selection fidelity

$$
\rho=\operatorname{Corr}(y,g),
$$

the expected true gain of the best observed candidate grows only roughly as

$$
\mu_g+\rho\sigma_g\sqrt{2\log n},
$$

while search cost is approximately linear in candidate count $n$.

This predicts a finite optimal search size and a verifier-limited regime in which more candidate generation makes the system less efficient.

## 2026-10-17 — Minimal nonlinear phase model

The current smallest phase model uses:

- protected transferable capability $C$;
- improvement efficiency $\eta$;
- evaluator fidelity $q$.

The model is

$$
\frac{dC}{dr}=\eta,
$$

$$
\frac{d\eta}{dr}
=
\left[
q\left(a_0+a_1\frac{C}{K+C}\right)
-
(d_0+d_1C^p)
\right]\eta
-\kappa\eta^2
+u_{\rm ext},
$$

$$
\frac{dq}{dr}
=
r_v(1-q)-s_v\eta q.
$$

The simulations currently illustrate saturation, bounded steady improvement, recursive acceleration, and verifier-limited growth. These are synthetic regimes, not empirical claims.

## 2026-10-17 — Optimal control view

Resource allocation was written as

$$
u=(u_M,u_H,u_I,u_D,u_V),
$$

with a long-run objective

$$
\max
\mathbb E
\left[
J(S_T)+\lambda\eta(S_T)-\sum_t C(u_t)
\right].
$$

This reframes the engineering question from “which component is most important?” to “which marginal intervention most improves future capability production under the current bottleneck?”

## Formulations deliberately demoted

The following ideas were considered too weak or misleading as primary descriptions:

- one benchmark score as the state of an AI system;
- “more capable” as equivalent to “better at self-improvement”;
- a fixed harness optimum across model generations;
- one greedy incumbent as the complete search state;
- static hidden benchmarks as permanently independent evidence;
- more candidate search as automatically beneficial;
- self-evaluation as sufficient final acceptance;
- one parent-to-child update as evidence of recursion;
- small-model success as evidence of frontier-scale behavior;
- exponential or singular growth assumed rather than inferred.

## What remains genuinely open

The current representation may still be wrong. Important alternatives include:

- improvement capability may require a vector or full kernel rather than scalar $\eta$;
- the Markov state $S_t$ may omit long-range historical dependence;
- model and harness may not admit a stable decomposition at strong coupling;
- external intelligence may be impossible to cleanly separate from endogenous recursion;
- evaluator fidelity may be task-dependent rather than a useful scalar;
- the phase dynamics may be dominated by rare discontinuous discoveries rather than smooth differential equations;
- the best formalism may be information-theoretic, evolutionary, or game-theoretic rather than control-theoretic.

These alternatives are reasons to run discriminating experiments, not reasons to avoid modeling.
## 2026-10-17 — Continuation audit: roles, common targets, and generality

**Derived corrections.** The former differential recursive term changes under a coordinate transformation of the same process. The sign of gain minus debt is not the growth condition in the retained nonlinear equation. Negative model–harness interaction can be redundant benefit; positive interaction can coexist with poor cross-pair performance. Exact witnesses are in THEORY.md and scripts/check_model_counterexamples.py.

**Representation change.** Model, executable harness, and stored information are implementation objects. Improver is a role that can use the same objects. The kernel now distinguishes acting improver A from target T. Experiment 003 compares actor versions on identical target copies; Experiment 004 pins all ancestor actor dependencies. This prevents target headroom and target difficulty from being silently attributed to actor improvement. The program also rebuilds the new harness before evaluating its cross-pairs.

**General mathematical scope.** THEORY.md gives a finite-history encoding argument for digital adaptive systems, a necessary-and-sufficient condition for exact controlled Markov summaries, a conditional multi-step approximation bound, and the pointwise condition for improvement under every task distribution. These use standard mathematical constructions. They establish representation and limits of reduction, not a universal growth law or a new physical principle.

**Source corrections.** Self-Rewarding LM reports three training rounds and improved reward provision. Hyperagents reports cross-domain meta-level transfer. AlphaEvolve includes improvements to infrastructure used in underlying model training. Fixed outer code or frozen weights do not alone exclude system-level feedback.

**Coverage.** COMPATIBILITY.md maps the 38 existing catalog entries plus HGM, ACE, AlphaEvolve, and OPRO, which were named in prose but absent from the machine-readable catalog. The 42 rows document representation and evidence obligations, not independent replication. The Good DOI remained inaccessible in this source pass.

**Retained hypotheses.** Alternating model/harness updates, portfolios, adaptive allocation, and reduced dynamics remain candidates. The sign-only H7 is superseded. Toy simulations are relabeled as path-slope examples; every reference scenario has nonzero external forcing. They cannot establish autonomous recursive acceleration.

**Next discriminating result.** Estimate a common-target actor effect and test whether proposed summary variables predict intervention responses. Cross-method prediction requires a shared measurement protocol and withheld methods/generations. No real-model run or universal empirical law is claimed by this audit.

## 2026-10-18 — Generality requires distinguishable predictions

**Derived constraint.** A general representation and sufficient state do not identify an intervention effect. THEORY.md now states the observational-equivalence criterion and its half-range absolute-error bound. An exact controlled-state witness has identical ancestor-run observations but opposite successor-reuse effects. This is standard identification reasoning, not a new RSI theorem.

**Scope corrections.** Known objectives and formal specifications need not be secret; withholding empirical final-test observations is a distinct requirement. Recursive reuse is separated from D3 throughout the corrected summaries. Editable curriculum/simulator state is explicit, and representation preserves recorded original resources without asserting equal simulation overhead.

**Evidence added.** Two primary full-paper checks expand the corpus from 42 to 44: a learned optimizer and POET. The latter covers evolving environment descriptions, not self-modification of the environment-generator algorithm. Primary findings and resource details are recorded in EVIDENCE.md.

**Research standard.** Compatibility preserves valid conditional mechanisms and results, including counterexamples. Work is prioritized by checkable scientific contribution rather than prestige, prose style, suspected AI assistance, or agreement with the preferred route.

**Remaining decision.** Competing shared-mechanism models must predict different outcomes for a feasible intervention before fitting a universal growth curve. Learned summaries, causal identification, cross-method transfer, and physical resource laws remain separate empirical obligations. No real-system run was conducted in this update.

## 2026-10-18 — Finite-budget reuse and executed optimizer comparisons

**Derived result.** The finite-horizon performance-difference identity expresses
the value of successor reuse as accumulated continuation advantages on reached
states. A five-state exact witness has pointwise one-step improver dominance
and monotone current utility under both policies, yet the dominant one-step
policy loses after two steps. The witness and 240 stochastic-kernel/horizon
cases were checked with rational arithmetic. This is an application of standard
policy-improvement mathematics, not a new universal growth law.

**Co-evolution.** Model and harness update kernels give two directional
continuation effects and an exact update-order difference. These are distinct
from crossing already-trained components during execution. The formalism admits
discrete edits, varying architectures and resource state without a five-score
closure assumption.

**Executed experiments.** A numerical optimizer with three learned controller
coefficients and three binary harness choices generated successor versions.
The pilot's continuous encoding failed to propose useful harness edits; its
source and results were retained. A typed follow-up used 32 new lineages.
Additional equal-call studies compared J/G training on 16 lineages and update
order on 32. Across all runs, 16,791,552 primitive objective calls were executed.
Source hashes, seeds, snapshots, candidate records and task-level outcomes are
preserved in experiments/006-recursive-optimizer/.

**Findings.** The typed recursive route did not establish improvement over the
pinned ancestor; final task scores declined on new instances despite positive
development feedback gains. Direct G-training did not establish better G than
matched-call J-training. M-then-H exceeded H-then-M on new instances, with no
established superiority over joint search or on new families. These findings
remove automatic promotion of a schedule, feedback winner or one-step G gain
from the proposed research route. They do not establish a general impossibility.

**Prior work.** Metz et al. (2020) is added as a primary reference for learned
optimizers training optimizers, with the authors' horizon and clipping limits.
The corpus now contains 45 entries. The present numerical experiment is a
separate implementation, not a neural-optimizer replication.

## 2026-10-18 — From universal encoding to explanatory mechanisms

The full-state kernel and continuation identity remained insufficient to
explain why existing methods work. The research now distinguishes changes
to accessible computations, actionable feedback, selection, inheritance,
task transfer and future branch value. MECHANISMS.md derives the corresponding
conditional laws and links them to source interventions. Standard tools are
attributed; selection/projection, downstream teaching value and descendant
value already have explicit precedents in ReST-EM, SEAL and HGM.

Primary methods/results were read for 14 selected entries. A per-work map
now supplies an explicit mechanism, condition and separating intervention
for all 47 entries, while marking the remaining source-review boundaries.
STaR and ReST-EM fill a missing verified-self-training branch. AIDE2's fixed
main outer proposer is recorded, and HELIX is no longer labelled a completed
model-update/rebuild demonstration.

Experiment 007 executed 4,635,614 primitive checks over 8,000 finite hidden
specifications. Correct localization follows the exact linear query law;
scalar pass/fail follows the equality-oracle law. This is a controlled
computational construction, not an LLM reproduction. Published aggregate
RRSI/MASS comparisons were calculated separately without pseudo-replication.

The route changes from presumed alternating model/harness cycles to reusable
research operations with preserved decision inputs, explicit source-task
weights, and data selection by post-update learner value. No frontier-model
training, universal speedup or new physical growth law has been established.

The teacher-selection distinction is also witnessed exactly in a finite learner
class: a perfect teacher projects to a 50%-accuracy student, while a weaker
compatible teacher projects to a 74.275%-expected-accuracy student (75% under
greedy decisions). Tasks, observations and exact likelihood optimization are
held fixed. This isolates loss/class mismatch; it is not a neural experiment
or a claim to have discovered teacher-capacity mismatch. Cho and Hariharan
(2019) are cited for the established distillation phenomenon.


## 2026-10-18 — Search effort, complete-computation retention, and learned reuse

The mechanism model lacked an executable quantitative bridge between learning
and the cost of later improvements. Added six foundations, including Expert
Iteration and DreamCoder, and connected the policy-guided search bound to a
trainable context policy. This changes the route from awaiting a general
metacontroller to implementing an operation with a defensible cost objective.
The bound, context-model convexity and value-of-computation framework are
established prior work, explicitly attributed in SEARCH.md.

A further structural distinction matters for preservation: mixing whole path
distributions protects an old path with a constant probability factor, whereas
mixing actions independently can pay that factor at every step. Fairly
interleaving complete search processes supplies a pointwise completion bound
without knowing which process will win. It compares the ancestor at its budget
share, not at the entire budget; process state, acceptance and overhead matter.
The exact witnesses are executable in scripts/check_search_preservation.py.

Experiment 008 is an actual five-round learned search loop with a 2,592-parameter
context model. It preserves its pilot and four paired runs. Reuse improves
held-out solver performance and the value of generated data for identical
fresh learners. Original random-walk tests approach a ceiling, so a documented
follow-up freezes the system and draws new uniform solvable states. At 256
pops, the common-target descendants solve 344/512 with data from the reused CE
actor, versus 176/512 from the frozen-collection actor. This is conditional on
the learner, task distribution and pop-budget convention; quantities of data
and arithmetic differ and are reported.

The harder follow-up exposes a benefit of the bound objective at small budgets
that the near-ceiling test obscures. Complete-process retention beats local
mixing here but costs performance relative to the best new search alone.
Training also costs more than frozen collection; deployment savings depend on
the task cohort and search cap. No broad adaptive-allocation victory or
open-ended recursion is inferred. Code, parameters, task identities, solved
paths, per-task outcomes, costs and hashed manifests are preserved losslessly.


## 2026-10-18 — Correcting frontier coverage and the main research boundary

The user asked whether the model explains substantive work from major labs,
not whether another bounded search experiment succeeds. Inspection found that
the earlier 53-entry catalog underrepresented large-scale reasoning RL, learned
evaluation, generated environments, adversarial co-training and industrial AI
research. Added 14 primary-source references, with changed objects, feedback,
assessment/resource boundaries and claim limits in EVIDENCE.md and exact reading
scopes in the mechanism data. No independent reproduction is claimed.

GPT-Red's co-training controls, Anthropic's automated post-training research,
SIMA 2's self-generated experience and Seed for Seed's reported development
usage make a model–harness-only mainline too narrow. AlphaEvolve also requires
following adopted computational savings into later work. The main question is
now the production of later capabilities and reuse of changes to that process.
M/H/D remains artifact bookkeeping; existing actor–target comparisons remain
useful. Neither a new label nor a larger catalog supplies a universal theory.

FRONTIER_COVERAGE.md distinguishes representation, mechanism explanation and
cross-system prediction. Important unresolved mechanisms are recorded openly.
THEORY.md adds an exact task/judge/system score decomposition and a conditional
standard Amdahl derivation, with observables and falsification implications.
They constrain interpretation rather than constituting a physical growth law.
H13 asks whether production-process variables improve withheld predictions.
No simulated dynamics were changed and no further toy experiment was run.


## 2026-10-18 — Refocus on LLM/agent self-evolution and expand the primary-source screen

**Source facts:** Four bibliography README snapshots provide 567 unique arXiv leads, not 567 verified papers. The expansion checked 61 related primary abstracts and submission histories, retained 56 entries (41 first submitted in 2026), and deferred five. A mistaken 2605/2505 query was excluded; three further source-retrieval gaps remain recorded. Ten retained entries have selected methods, definitions or result passages read; no independent reproduction was executed.

**Scope correction:** The 123-entry catalog separates 63 direct self-evolution studies, 30 enabling studies, 7 evaluations, 3 theories, 14 foundations and 6 background works. Ordinary training reports and general scientific discovery are not counted as core RSI. Direct-topic classification is not certification of structural recursion, improved improvement ability or sustained growth.

**Material evidence:** EvoTrainer makes training diagnostics and reusable trainer skills editable, with a fixed backbone and human-gated costly actions. DERL trains reward proposers from downstream training outcomes. Skill-SP supplies frozen-component comparisons of proposer, solver and skill feedback. The on-policy model–harness study reports full-trajectory expert-imitation regression after harness evolution. SoL-Pi explicitly places cheaper recursive successor research in future work, despite its title and engineering gains. GAI supplies prior formal work on modifier membership and external evaluation grounding; component naming is not our novelty.

**Research decision:** Prioritize learned training interventions, coupled curricula/evaluators/environments/model–harness behavior, and actual reuse in successor production. Keep AI4AI targets distinct from self-improving actors. Further breadth and full-method review remain unfinished; no exhaustive coverage, quality-certified set of 100 RSI papers, or universal physical growth law is claimed.


## 2026-10-18 — Replace the unfiltered paper map with a curated research atlas

**Research decision:** A topical catalog is not a knowledge map of valuable
results. Introduced explicit claim-level admission with 23 core contributions,
78 pending reviews, 16 historical/mechanistic references and 6 background
entries. No named low-value verdict is manufactured from missing evidence.
The canonical graph now contains only admitted work nodes, with separate types
for mechanism membership, source-explicit relations and analytical comparisons.

**Source corrections and judgments:** Further method/control reading exposes
Co-Harness's limited component attribution, so it remains outside the core map.
The positive game results in Rethinking Harness Evaluation are task-specific
adaptation, not held-out task transfer. SEAL is retained for the update-value
mechanism while its very small curated ARC setting remains explicit. The
OpenRSI catalog alias is reconciled with the checked Frontis-MA1 / OpenMLE source.

**Deliverables:** Chinese entry point, seven-branch illustrated knowledge tree,
feedback/return-path diagram, 23 substantive claim cards, 123-entry source index,
per-item decisions, offline search/filter/detail views and a 26-page PDF. All
views are generated from versioned sources and decisions. README and MAP now
lead to this material; theory and prior experiment artifacts are unchanged.

**Validation boundary:** Corpus/admission/graph consistency and exact embedded
HTML-data agreement are checked. PDF pages are rendered and visually reviewed.
Local browser rendering was unavailable because no browser binary was installed
and the browser download returned invalid archives; JavaScript rendering and
filter logic are checked in Node, not claimed as a real-browser interaction run.
No new toy experiment or independent literature reproduction was performed.

## 2026-10-18 — Replace the seven-family navigation with three object routes

**Reason:** The seven mechanism families mixed update location, functional role and evaluation method at one level. The user requested clearer Harness / Model / Model × Harness navigation and a >=27B actual-training scope for Model/mixed, then clarified that the substructure must derive from functions and feedback rather than merely repeat their examples.

**Change:** Added a manually sourced layer/scale/return-path registry; retained claim quality as an independent axis. The atlas now presents 12 main-view works (8/2/2), 24 claim cards and 123 bibliography records. Self-Rewarding LM was promoted after reading the actual 70B SFT/DPO procedure and fixed question-generator detail. No other unresolved work was promoted by title, institution or parameter count. The canonical graph v3 contains three route nodes and main-view works only; previous comparisons remain in the claim-review source.

**Research correction:** Frontis-MA1 qualifies by trained-model size but its own limitations identify a largely fixed evolutionary system. The on-policy coevolution paper primarily tests one joint adaptation, and uses LoRA SFT rather than RL; its 26B auxiliary branch does not meet the cutoff. EvoTrainer's fixed trainer is not its trained target. Evaluation code, learned evaluation weights and independent audit criteria are now explicitly separated.

**Scope:** Six Harness functions, orthogonal Model descriptors and eighteen functional/feedback research positions expose both populated and unconfirmed locations. These are analytical coordinates, not proof of universal predictive coverage or worldwide novelty. A–F tags select 1–3 contribution foci; no per-paper personality or exhaustive-dimension scoring.

**Artifacts:** Rebuilt offline HTML, PNG/SVG diagrams, PDF, main Markdown, cards, complete index and review queue from the same data. New validation enforces actual-target size, separate claim/main membership, graph filtering and exact embedded JSON consistency. Browser-engine layout verification remains unavailable in this environment; functional JavaScript and PDF/diagram rendering are checked separately.

## 2026-10-18 — Correct the 12-case coverage impression and add missing model research

The 8/2/2 display was an unfinished selection, not a final rejection of all other research. Primary-source checks exposed missing Kimi K2, DeepSeekMath-V2, Iterative RPO, and the 540B self-training precursor. Four new catalog records and fourteen selected-section claim reviews bring the catalog to 127 and reviewed claims to 38; seven additional cases enter the main view (12/5/2). Sixty-seven candidates still await review. No field-wide final count or paper-quality rejection count is inferred.

Institutional provenance is sourced from paper affiliations and joint work is counted once. Current main-view counts: industry-only 6, academic/nonprofit-only 1, joint 12. These are selection composition, not estimates of sector activity. Industrial goals and research directions are editorial syntheses of the cited objectives.

ReST-EM and SIMA 2 remain visible as size-unverified mechanism evidence. AlphaProof's actual 3B proof network fails the user-selected size scope without becoming a low-quality judgment. The DeepSeekMath-V2 gate uses a conservative >653.9B lower bound from its released expert dimensions; full checkpoint size is not invented. Co-Harness's 32B branch does not automatically pass causal evidence review.

The HTML front page now leads with counts, teams and goals; A–F labels and long classification essays leave the main reading path. The PDF is a concise nine-page guide, with full references and claim cards retained in HTML/Markdown. Validation checks provenance totals, the parameter lower-bound justification, membership, filters, dialogs and exact embedded data. PDF pages are rendered for visual inspection; no real-browser layout test or independent paper replication is claimed.

The secondary scope/mechanism renderers now consume the canonical reviewed JSON records instead of hard-coded historical inventories. Rebuilding them preserves manual evidence and compatibility notes. Updated the 14 reviewed records in both indexes; no old review depth is silently promoted.

## 2026-10-19 — Make three literature knowledge graphs the reading interface

The user rejected category roots with a narrow case shortlist as an adequate landscape. The replacement reader is organized around Harness, Model and Model × Harness graphs, with paper, method and institution metadata. Papers can attach to multiple methods; explicit paper relations and editorial method comparisons are distinguished and sourced. Every relationship inspector names both endpoint teams. The HTML contains public literature only; repository theory, predictions and proposed experiments remain outside it.

All 127 bibliographic IDs are preserved. Ninety-seven records receive principal route positions, eight are cross-route evaluation/theory, and 22 are historical/background. Selected-method readings now total 41 (38 route cards plus three cross-route cards); 64 remain abstract/source screens. This is a different reading representation from the earlier claim-quality shortlist, not a retrospective claim that the other works were worthless or fully reviewed. Eight known sub-27B Model/mixed records are hidden by default, including the newly checked 7B SkillRL policy and 9B Harness-R1 engineer. Unknown scale remains explicit.

New primary-source title-page checks fill institutional provenance; Voyager, MemRL and SkillRL receive bounded method cards. EURISKO's archival explanation is rewritten around its actual research mechanism. Forty-three paper relations include thirteen source-explicit edges and thirty stated method comparisons. No edge is invented merely because titles or teams resemble one another; missing connections remain an acknowledged coverage gap.

The single-file HTML retains full-text/institution search, opens each paper's supported A–F material, and provides relation/source inspection and graph localization. Browser checks passed in Chromium at desktop and mobile sizes. Graph/data/source integrity, all 127 dialogs, scale filters and the exact embedded dataset were checked. Static SVG graph views and a current overview preview are exported from the rendered reader. The earlier PDF remains dated 2026-10-18; it is not described as this version's graph export. No new theory, independent paper replication or field-wide completeness claim is made.

## 2026-10-19 — v5: field structure before paper placement

The previous interface still made the paper catalog determine the landscape. In response to the user's correction, six parallel, bounded reading/structure tasks produced three field proposals and revised paper explanations. Their source facts were integrated into one canonical field structure; no delegation plan is used as the deliverable.

The reader now opens with three actual field graphs. There are 29 themes, 146 subquestions and 60 explained conceptual links. Themes, subquestions, method relations, paper positions and institutions have different graph types. All subquestions can expand inside the graph; papers and teams attach afterward. Model training stage/objective/online collection/roles remain orthogonal dimensions. The mixed route distinguishes internalization, externalization, one-shot adaptation and sustained bidirectional updating. This is survey organization, not a proof of a complete universal theory.

Twenty-seven A–F cards were rewritten from primary method/results passages. AFlow, Meta-Harness, Live-SWE-agent and WebEvolver are promoted from source screens to bounded method readings. Actual mutable objects move Dream-RSI and RewardHarness to Harness, and SEED Distillation and WebEvolver to Model. The route counts become 40/35/22. WebEvolver's policy and world model are both 70B; WebRL's trained targets are 8B/9B and enter the size supplement. MemSkill's trained MLP controller cannot borrow the scale of its frozen 70B/80B API models. These corrections update the bibliography and evidence log while preserving the older claim-quality review as a dated layer.

The corpus remains 127 records: 45 selected-method readings, 60 source screens and 22 historical/background entries. Forty-five paper relations separate 15 source-explicit links from 30 editorial comparisons; field relations use another type. These are coverage and reading counts, not final quality rankings. Current HTML is public literature only; project theories, forecasts and proposals are absent.

The new file is named RSI_Field_Atlas_v5.html to distinguish it from the screenshot of the older 2026-10-18 reader. Offline data checks and real Chromium desktop/mobile interaction checks pass, including three visible first-screen maps, expanded subquestions, topic/edge inspection, paper-to-field return and search. Current PNG/SVG previews are exported from the reader; the PDF remains a dated snapshot. No independent research replication is claimed.


## 2026-10-19 — v5.1: companies, public releases and provenance within the three routes

The user identified a real coverage gap: Discovery Loop, MetaCircle and Apex were absent even though company research need not appear first as an academic paper. This update adds 11 primary-source work records and 27 company/industry-team profiles. It exposes existing startup affiliations and distinguishes company-issued work, joint authorship, repository hosting and strategic direction. Two adjacent companies remain outside the RSI study maps until a relevant update loop is established.

Current corpus: 138 records (49 Harness / 36 Model / 22 mixed / 9 cross-route / 22 historical-background); 53 selected-method/mechanism readings and 63 source screens. Eleven new releases include three source screens with explicit access limits. There are 48 paper/release relations, including three newly sourced relationships. The field structure remains 29 topics, 146 subquestions and 60 conceptual relations. Company, topic and study navigation is bidirectional and the original three maps remain visible on entry.

The former 127-item quality/layer review remains unchanged and is now explicitly enumerated and hash-checked as a dated snapshot. Full current-catalog consistency is enforced in the current reader and graph checks. This avoids silently extending old claim audits to new releases. The current scope catalog covers all 138 records.

The update does not infer that every autonomous research company has demonstrated RSI, that corporate scale proves research quality, or that a company with both models and a harness has demonstrated their recursive coevolution. Discovery Loop is a declared direction; MetaCircle and Apex have concrete technical artifacts with bounded claims. No global company census, independent reproduction or new project theory is claimed.
