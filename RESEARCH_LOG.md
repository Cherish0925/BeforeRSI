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
