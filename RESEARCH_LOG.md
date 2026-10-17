# Research lineage

This is a distilled record of the substantive reasoning that led to the current BeforeRSI program. It preserves changes in representation, failed framings, open alternatives, and the experiments proposed to distinguish them. It is not a raw conversation transcript.

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