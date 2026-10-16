# A dynamical theory of model–harness recursive self-improvement

This document gives a compact mathematical model of recursive self-improvement (RSI) for an AI system composed of a model, a harness, an improver, persistent experience, and an external task environment.

The central object is not task capability alone. It is the **resource-normalized operator that maps the current system into a distribution over successor systems**. RSI begins when a successor improves that operator itself.

---

## 1. The smallest useful statement

Let

$$
S_t=(M_t,H_t,I_t,D_t)
$$

be a versioned AI system:

- $M_t$: model parameters, architecture, inference policy, and trainability;
- $H_t$: context construction, memory, tools, skills, search, agent topology, control flow, and runtime;
- $I_t$: the procedure that proposes, implements, tests, and selects modifications;
- $D_t$: persistent experience, trajectories, code, failures, lineage, and training data.

The task environment, protected evaluator, and resource budget are external variables:

$$
\Omega_t=(E_t,V^*,B_t).
$$

One improvement generation is

$$
S_{t+1}\sim K_{S_t}(\cdot\mid S_t,\Omega_t),
$$

where $K_{S_t}$ is the **improvement kernel** induced by the current system. It is a probability distribution because candidate generation, execution, training, evaluation, and selection are stochastic.

Ordinary self-improvement asks whether $S_{t+1}$ is better than $S_t$. Recursive self-improvement asks whether

$$
K_{S_{t+1}} \succ K_{S_t}
$$

on new improvement problems under the same resource budget. The symbol $\succ$ means that the successor produces descendants with better held-out gain, lower cost, broader transfer, fewer regressions, or higher reliability.

Everything else in this document is a decomposition of this statement.

---

## 2. Capability is a field, not a scalar

Let $x$ denote a task and $b$ a task-time budget. The system induces a trajectory distribution

$$
\tau\sim P(\tau\mid x,S,b),
$$

and a task utility

$$
c_S(x,b)=\mathbb E[u(x,\tau)].
$$

The true capability of $S$ is the function

$$
c_S:\mathcal X\times\mathcal B\rightarrow\mathbb R^k,
$$

not one benchmark score. Its coordinates may include correctness, cost, latency, robustness, calibration, tool reliability, and domain-specific performance.

For a task distribution $Q$,

$$
J_Q(S;b)=\mathbb E_{x\sim Q}[c_S(x,b)].
$$

A successor is a transferable improvement only when the gain persists on a distribution that did not participate in candidate generation, selection, tuning, or stopping:

$$
\Delta_Q(S',S;b)=J_Q(S';b)-J_Q(S;b)>0.
$$

If the successor uses a larger task-time budget, the comparison is not identified. Capability and resource use must be measured jointly.

---

## 3. Improvement capability

An improvement problem is

$$
p=(S,\mathcal A,P,V,B),
$$

where $\mathcal A$ is the editable surface, $P$ the visible improvement tasks, $V$ the selection signal, and $B$ the total improvement budget.

The value of an improver is the expected transferable gain it produces per unit resource:

$$
\eta(S;\mu)
=
\mathbb E_{p\sim\mu}
\left[
\frac{
G_Q(S',S)-\lambda L(S',S)
}{C_{\mathrm{improve}}(p)}
\right],
$$

where

- $S'\sim K_S(\cdot\mid p)$;
- $G_Q$ is held-out capability gain;
- $L$ is protected-capability loss or regression;
- $C_{\mathrm{improve}}$ includes model calls, tokens, candidates, evaluator calls, accelerator time, wall time, external services, experiments, and human intervention;
- $\mu$ is a distribution of unseen improvement problems.

The scalar $\eta$ is a projection of a richer improvement frontier. It is useful because it separates three phenomena:

$$
J_{t+1}>J_t
$$

means the system improved;

$$
\eta_{t+1}=\eta_t
$$

means improvement continues at the same efficiency;

$$
\eta_{t+1}>\eta_t
$$

means the successor is better at producing future capability.

The last inequality is the local mathematical content of RSI.

---

## 4. Resource-normalized dynamics

Use cumulative improvement resource $r$, rather than wall-clock time, as the independent variable. This removes the trivial acceleration obtained by spending more compute.

Let $s$ be a macrostate describing the current AI system. Improvement becomes an autonomous stochastic flow on system space:

$$
\frac{ds}{dr}=F(s)+\xi(r),
$$

where $F$ is the expected modification produced per unit resource and $\xi$ is stochastic variation.

For any capability functional $J(s)$,

$$
\frac{dJ}{dr}=\nabla J(s)^\top F(s).
$$

This is ordinary improvement. The acceleration is

$$
\frac{d^2J}{dr^2}
=
F^\top \nabla^2J\,F
+
\nabla J^\top \bigl(DF\bigr)F.
$$

The two terms have different meanings:

1. $F^\top\nabla^2J F$ is curvature of the capability landscape. Capability may accelerate or decelerate even if the improvement rule stays fixed.
2. $\nabla J^\top(DF)F$ measures how improvement changes the future improvement vector field.

Define the local recursive term

$$
R_{\mathrm{rec}}(s)
=
\nabla J(s)^\top\bigl(DF(s)\bigr)F(s).
$$

A positive $R_{\mathrm{rec}}$ means the current update moves the system into a region where later resource is converted into capability more effectively. This isolates recursion from ordinary landscape curvature.

A normalized recursive gain rate is

$$
r_{\mathrm{rec}}(s)
=
\frac{R_{\mathrm{rec}}(s)}{\nabla J(s)^\top F(s)}.
$$

It can be estimated from repeated parent-versus-successor improvement experiments.

---

## 5. Multi-timescale structure

A complete AI system evolves on several timescales.

### Fast: task execution

$$
z_{k+1}=f(z_k,a_k,x;M,H,E)+\epsilon_k,
$$

where $z_k$ is research state and $a_k$ is an action selected by the model–harness policy.

### Intermediate: memory and harness adaptation

$$
D_{t+1}=\mathcal C(D_t,\tau_t,V^*),
$$

$$
H_{t+1}=\mathcal U_H(H_t,M_t,I_t,D_{t+1}).
$$

### Slow: model update

$$
M_{t+1}=\mathcal U_M(M_t,H_t,I_t,D_{t+1}).
$$

### Meta-slow: improver update

$$
I_{t+1}=\mathcal U_I(I_t,\mathcal L_t),
$$

where $\mathcal L_t$ is the full lineage of proposed, rejected, failed, accepted, and later-reevaluated modifications.

A singularly perturbed continuous model is

$$
\dot z=f(z;M,H,E),
$$

$$
\dot H=\varepsilon_H F_H,
\qquad
\dot M=\varepsilon_M F_M,
\qquad
\dot I=\varepsilon_I F_I,
$$

with

$$
1\gg \varepsilon_H\gtrsim\varepsilon_M\gg\varepsilon_I.
$$

This ordering predicts that uncontrolled simultaneous updating is usually unstable. Harness changes can happen rapidly, model training more slowly, and changes to the improver should be accepted only after evidence accumulates across several update problems.

---

## 6. The coevolution matrix

Project the full system onto measurable macrovariables

$$
x=(m,h,i,d,v),
$$

where

- $m$: intrinsic model capability under a standardized minimal harness;
- $h$: reusable harness contribution;
- $i$: improver quality;
- $d$: value and diversity of persistent experience;
- $v$: evaluator fidelity.

The local dynamics are

$$
\dot x=F(x),
$$

with Jacobian

$$
K=DF(x)
=
\begin{pmatrix}
K_{MM}&K_{MH}&K_{MI}&K_{MD}&K_{MV}\\
K_{HM}&K_{HH}&K_{HI}&K_{HD}&K_{HV}\\
K_{IM}&K_{IH}&K_{II}&K_{ID}&K_{IV}\\
K_{DM}&K_{DH}&K_{DI}&K_{DD}&K_{DV}\\
K_{VM}&K_{VH}&K_{VI}&K_{VD}&K_{VV}
\end{pmatrix}.
$$

By definition,

$$
K_{ab}=\frac{\partial F_a}{\partial x_b}.
$$

The cross-terms encode the actual coevolution:

- $K_{MH}$: how a better harness improves the rate or quality of model learning;
- $K_{HM}$: how a better model improves harness discovery;
- $K_{MI}$ and $K_{HI}$: how the improver accelerates model and harness updates;
- $K_{IM}$ and $K_{IH}$: how model and harness capability improve the improver;
- $K_{DV}$: how verification changes the value of stored experience;
- $K_{VD}$: how accumulated evidence improves evaluators.

The dominant beneficial eigenmode of $K$ predicts which combination of model, harness, improver, data, and verification will grow together. A mode dominated by $h$ is a harness-first regime. A mode dominated by $v$ is verification-limited. A mode with strong $m\leftrightarrow h\leftrightarrow i$ coupling is the regime required for system-level RSI.

A large positive eigenvalue is not automatically desirable: it may describe rapid growth of evaluator exploitation or correlated error. The mode must also have positive projection onto protected held-out capability.

---

## 7. Model–harness interaction

Let $M_0,H_0$ be the parent pair and $M_1,H_1$ the updated pair. Evaluate all four systems:

$$
J_{00}=J(M_0,H_0),
\quad
J_{10}=J(M_1,H_0),
\quad
J_{01}=J(M_0,H_1),
\quad
J_{11}=J(M_1,H_1).
$$

The model main effect is

$$
\Delta_M=J_{10}-J_{00},
$$

and the harness main effect is

$$
\Delta_H=J_{01}-J_{00}.
$$

The interaction is

$$
\Gamma_{MH}
=
J_{11}-J_{10}-J_{01}+J_{00}.
$$

Interpretation:

- $\Gamma_{MH}>0$: positive synergy;
- $\Gamma_{MH}=0$: approximately additive improvement;
- $\Gamma_{MH}<0$: conflict, compensation, or local co-adaptation.

This interaction must be estimated on hidden and time-forward tasks. A large paired score $J_{11}$ can coexist with poor portability if $H_1$ only compensates for defects in $M_1$ or if $M_1$ was trained on trajectories that reward quirks of $H_1$.

The optimal harness is therefore a function of the model:

$$
H^*=H^*(M,E,B).
$$

Likewise, the most valuable training distribution is a function of both model and harness:

$$
D^*=D^*(M,H,E,V^*).
$$

This is why one-way optimization of only $M$ or only $H$ cannot remain optimal indefinitely.

---

## 8. Harness search as statistical mechanics

A single incumbent throws away useful diversity. Maintain a distribution $p_t(h)$ over harnesses.

Let $Q_I(h'\mid h)$ be the mutation kernel produced by the improver and let $\widehat g(h')$ be the measured gain. A generic update is the replicator–mutator equation

$$
p_{t+1}(h')
=
\frac{1}{Z_t}
\int
Q_I(h'\mid h)
\,p_t(h)
\,\exp\bigl(\beta\widehat g(h')\bigr)
\,dh.
$$

The inverse temperature $\beta$ controls selection pressure:

- small $\beta$: broad exploration, slow concentration;
- large $\beta$: rapid exploitation, premature collapse, benchmark fitting, and loss of future stepping stones.

The same update solves a variational objective of the form

$$
\max_p
\left\{
\mathbb E_p[\widehat g(h)]
-
\frac{1}{\beta}
D_{\mathrm{KL}}(p\|q)
\right\},
$$

where $q$ is a prior or parent distribution. The KL term is not decorative regularization. It is the price paid to preserve alternative lineages under uncertain evaluation.

The correct state is therefore a **portfolio plus lineage**, not one current best harness.

---

## 9. Experience production and model learning

The model–harness pair generates trajectories:

$$
\tau\sim P(\tau\mid x,M,H,E).
$$

Protected verification converts raw trajectories into evidence-bearing data:

$$
z=(x,\tau,y,\text{provenance},\text{cost},\text{counterfactuals}),
$$

$$
D_{t+1}=\mathcal C(D_t,z;V^*).
$$

The marginal value of a datum is

$$
v(z)
=
\mathbb E
\left[
J_Q\bigl(\operatorname{Train}(M,D\cup\{z\})\bigr)
-
J_Q\bigl(\operatorname{Train}(M,D)\bigr)
\right].
$$

Exact evaluation requires retraining and is expensive. It can be approximated with component ablations, influence estimates, counterfactual replay, matched trajectory comparisons, or small controlled retraining runs.

This equation explains why successful trajectories cannot be copied wholesale into training. Many steps are causally irrelevant, some are harmful, and failed trajectories may contain the highest-value local decisions.

The model update is

$$
M_{t+1}=\operatorname{Train}(M_t,D_t;I_t),
$$

but the training objective should value future transfer and future improvement ability, not only imitation of successful outputs.

---

## 10. Verification is a dynamical bottleneck

Let the true transferable gain of candidate $j$ be $g_j$. The system observes

$$
y_j=g_j+\epsilon_j+b_j,
$$

where $\epsilon_j$ is ordinary evaluation noise and $b_j$ is systematic exploitability or metric bias.

Define selection fidelity

$$
\rho=\operatorname{Corr}(y,g).
$$

If candidates are approximately Gaussian and $n$ candidates are selected by maximum measured score, then

$$
\mathbb E[g_{\mathrm{selected}}]
\approx
\mu_g
+
\rho\sigma_g\sqrt{2\log n}.
$$

The resource-normalized improvement is approximately

$$
\eta(n)
\approx
\frac{
\mu_g+\rho\sigma_g\sqrt{2\log n}-R(n)
}{
C_0+n(C_{\mathrm{gen}}+C_{\mathrm{eval}})
},
$$

where $R(n)$ is regression or exploit bias that may grow with search pressure.

Consequences:

1. candidate count has a finite optimum;
2. when $\rho$ is low, additional search mostly selects evaluation noise;
3. when exploitability grows with $n$, more search can reduce true gain;
4. improving $V^*$ can have greater long-run value than improving the proposer;
5. reevaluation of selected candidates is required because winner selection biases the observed score upward.

Verification quality is therefore part of the RSI dynamics, not a final reporting detail.

---

## 11. Five dimensionless control numbers

A small set of ratios identifies the operating regime.

### Transfer number

$$
\mathcal T
=
\frac{\Delta J_{\mathrm{hidden}}}
{\Delta J_{\mathrm{visible}}+\varepsilon}.
$$

$\mathcal T\approx0$ indicates benchmark fitting. A stable positive value indicates transfer.

### Verification number

$$
\mathcal V
=
\frac{\sigma_g}{\sigma_{V}+\varepsilon}
$$

or, when paired truth estimates exist, use $\rho=\operatorname{Corr}(y,g)$. Small $\mathcal V$ means candidate differences are buried in evaluator noise.

### Coupling number

$$
\mathcal C_{MH}
=
\frac{\Gamma_{MH}}
{|\Delta_M|+|\Delta_H|+\varepsilon}.
$$

It measures whether model and harness updates are genuinely interacting rather than merely occurring in parallel.

### Amortization number

$$
\mathcal A
=
\frac{N_{\mathrm{future}}\,\Delta J_{\mathrm{per\ task}}}
{C_{\mathrm{improve}}+\varepsilon}.
$$

$\mathcal A>1$ means the persistent modification repays its creation cost over its expected lifetime.

### Recursion number

$$
\mathcal R_t
=
\frac{\eta(S_{t+1};\mu_{\mathrm{new}})}
{\eta(S_t;\mu_{\mathrm{new}})+\varepsilon}.
$$

- $\mathcal R_t<1$: improvement efficiency decays;
- $\mathcal R_t\approx1$: approximately constant-rate progress;
- $\mathcal R_t>1$: compounding improvement efficiency.

A claim of RSI should report $\mathcal R_t$, not merely $J_{t+1}-J_t$.

---

## 12. The minimal nonlinear RSI model

Compress the system to two observables:

- $C(r)$: protected transferable capability;
- $\eta(r)$: capability gain produced per unit improvement resource.

Then

$$
\frac{dC}{dr}=\eta.
$$

The evolution of improvement efficiency can be modeled as

$$
\frac{d\eta}{dr}
=
\bigl[g(C,V,\mathcal T,\Pi)-d(C)\bigr]\eta
-\kappa\eta^2
+u_{\mathrm{ext}}.
$$

Here

- $g$ is recursive design gain: how current capability improves proposal, experimentation, learning, and integration;
- $d(C)$ is complexity debt: verification burden, system coupling, regression risk, software debt, training cost, and diminishing returns;
- $\kappa\eta^2$ is saturation from finite task, data, and search capacity;
- $u_{\mathrm{ext}}$ is external intelligence supplied by humans, stronger teacher models, new benchmarks, or manually designed algorithms.

The threshold is

$$
g(C,V,\mathcal T,\Pi)>d(C).
$$

Below the threshold, improvement efficiency decays or remains externally sustained. Above it, the system enters an autocatalytic regime in which current organization improves the production of future organization.

This equation exposes the true contest behind an intelligence explosion:

$$
\text{recursive design gain}
\quad\text{versus}\quad
\text{complexity and verification debt}.
$$

High capability alone is insufficient. The sign of $g-d$ determines the regime.

A long-run recursive Lyapunov exponent is

$$
\lambda_R
=
\liminf_{R\to\infty}
\frac{1}{R}
\log
\frac{\eta(R)}{\eta(0)}.
$$

Sustained $\lambda_R>0$ on changing task distributions, with protected evaluation and controlled external input, would constitute strong evidence for open-ended recursive improvement.

---

## 13. Optimal allocation of improvement resources

Let the control vector be

$$
u=(u_M,u_H,u_I,u_D,u_V),
$$

with

$$
\sum_j u_j\le B.
$$

The correct objective is not immediate capability alone. It is future capability plus future improvement capacity:

$$
\max_{u_{0:T}}
\mathbb E
\left[
J_Q(S_T)
+\lambda\eta(S_T)
-\sum_{t=0}^{T}C(u_t)
\right]
$$

subject to

$$
S_{t+1}=F(S_t,u_t),
$$

protected regression limits, evaluator separation, and resource constraints.

This is a model-predictive-control problem. At each generation, the system should estimate the marginal value of spending one additional unit on each component:

$$
\chi_j
=
\frac{\partial\eta/\partial u_j}
{\partial C/\partial u_j}.
$$

The next investment should go to the component with the largest reliable shadow value $\chi_j$, not automatically to the model or to the currently fashionable part of the stack.

Examples:

- low proposal quality, high verifier fidelity: invest in $M$, $H$, or $I$;
- high proposal quality, low verifier fidelity: invest in $V$;
- high visible gain, low transfer: invest in task diversity, time-forward evaluation, and data curation;
- high harness gain, low amortization: compress or train the gain into $M$;
- strong one-step gain, $\mathcal R\le1$: improve the improver rather than the target system.

---

## 14. System identification

The theory becomes predictive only when its terms are estimated experimentally.

### Step 1: choose measurable macrovariables

Measure intrinsic model capability, harness contribution, improver quality, data value, evaluator fidelity, cost, and regressions.

### Step 2: perturb one component at a time

Hold the rest fixed and change one of $M,H,I,D,V$. Use paired tasks and common random seeds.

### Step 3: estimate the block Jacobian

Finite differences give

$$
K_{ab}
\approx
\frac{F_a(x+\delta e_b)-F_a(x)}{\delta}.
$$

The matrix predicts which couplings are beneficial, weak, unstable, or redundant.

### Step 4: fit candidate and evaluator distributions

Estimate $\mu_g$, $\sigma_g$, evaluator noise, exploit bias, and selection fidelity as candidate count changes.

### Step 5: run the model–harness cross

Estimate $\Delta_M$, $\Delta_H$, and $\Gamma_{MH}$ on hidden and time-forward tasks.

### Step 6: compare parent and successor as improvers

Give $S_t$ and $S_{t+1}$ the same unseen improvement problem and budget. Estimate $\mathcal R_t$ directly.

### Step 7: fit nonlinear dynamics

Use the observed sequence to estimate $g(C)$, $d(C)$, saturation, and external input. Simulate alternative budget allocations before running expensive updates.

This is ordinary system identification applied to an AI system whose controller is itself part of the state.

---

## 15. Predictions

The model yields falsifiable predictions.

1. **Harness-first efficiency.** Early harness changes will often have higher gain per unit cost than model retraining, but will saturate sooner and transfer less reliably.
2. **Moving harness optimum.** After a substantial model update, the old best harness will cease to be optimal; some formerly rejected branches will become useful again.
3. **Verification threshold.** Increasing candidate count beyond a finite optimum will reduce improvement efficiency when evaluator fidelity is low or exploitability grows with search pressure.
4. **Co-adaptation trap.** Paired model–harness performance will overstate general improvement unless cross-version swaps are measured.
5. **D2 is common; D3 is rare.** Many systems will produce transferable successors without making those successors better improvers.
6. **Portfolio advantage.** A lineage portfolio will outperform a single greedy incumbent under nonstationary models and moving task distributions.
7. **Data bottleneck migration.** Once proposal and execution improve, verified trajectory quality and causal credit assignment will become the limiting factors.
8. **Complexity debt controls takeoff.** Capability growth will saturate whenever verification and integration difficulty grow faster than recursive design gain.
9. **Improver lag.** Task capability will generally improve faster than improvement capability unless $I$ is explicitly trained and evaluated.
10. **Bounded domains first.** Positive recursive gain will appear first in domains with cheap execution, dense feedback, and reliable evaluators; broad open-world RSI requires transfer of that gain across environments.

Each prediction can be tested with the experiments already defined in this repository.

---

## 16. Architecture implied by the theory

The mathematics implies a small set of necessary system objects:

1. **Versioned system state** for $M,H,I,D$;
2. **Harness portfolio and lineage**, not one unqualified incumbent;
3. **Protected evaluator** that cannot be silently rewritten by candidates;
4. **Evidence-bearing trajectory store** with provenance, cost, counterfactuals, and validation;
5. **Model trainer** that consumes selected evidence rather than raw logs;
6. **Improver policy** that proposes changes to model, harness, data, verifier candidates, and itself;
7. **Component-cross evaluator** for attribution;
8. **Resource ledger** covering improvement and task-time cost;
9. **System-identification layer** that estimates transfer, coupling, verification fidelity, and recursive gain;
10. **Budget controller** that allocates the next unit of resource to the current bottleneck.

These objects are not an arbitrary software decomposition. Each corresponds to a state variable, coupling term, or measurement required by the theory.

---

## 17. The irreducible core

The complete theory can be reduced to four equations.

### System update

$$
S_{t+1}\sim K_{S_t}(\cdot\mid S_t,E_t,V^*,B_t).
$$

### Transferable capability gain

$$
\Delta_Q=J_Q(S_{t+1})-J_Q(S_t).
$$

### Improvement efficiency

$$
\eta_t
=
\frac{\mathbb E[\Delta_Q-\lambda L]}
{C_{\mathrm{improve}}}.
$$

### Recursive condition

$$
\eta_{t+1}>\eta_t
$$

on new improvement problems under matched resources.

Model–harness coevolution supplies the positive cross-couplings. The improver turns those couplings into candidate updates. Persistent experience carries verified information across generations. Protected evaluation keeps the vector field pointed toward real capability rather than its proxy.

The central scientific question is therefore precise:

> Under what measurable conditions does recursive design gain exceed complexity and verification debt, causing improvement efficiency to increase across generations?

That question can be modeled, estimated, simulated, and experimentally falsified.