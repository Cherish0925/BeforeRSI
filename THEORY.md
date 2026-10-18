# Model, harness, and recursive self-improvement

**Status:** operational definitions, mathematical counterexamples, and open empirical questions. This document does not establish a growth law for real AI systems. The 2026-10-17 audit below replaces the earlier interpretation of the differential “recursive term” and the sign-only growth threshold.

The research question is: **which persistent changes make a system better at producing further useful changes, on comparable problems and budgets?**

## 1. Implementation and role are different distinctions

A versioned system can be packaged as

$$
S=(M,H,D).
$$

| Object | What is recorded |
|---|---|
| Model $M$ | Learned parameters and the architectures that execute them; there may be several models |
| Harness $H$ | Executable orchestration: context construction, tool interfaces, memory access, search, routing, training code, evaluation calls, and stopping |
| Persistent data $D$ | Memory contents, datasets, skills stored as data, retained experience, and other information available to future runs |

Every artifact has one declared owner in the manifest. For example, memory-access code is in $H$ and stored memories are in $D$. Optimizer state, learned controllers, and executable skills must be assigned explicitly. This is a useful experimental boundary, not a unique decomposition of intelligence.

**Solver and improver are roles.** The same model, harness, and persistent information can solve a task or propose and test a system modification. Calling the second execution an improver does not introduce a necessarily independent fourth component. If a separate improver is deployed, record its own models, code, data, and dependencies.

A model update can therefore improve the improver without any separate improver-code update. Conversely, a source-code change can improve future research while model weights stay fixed. A fixed outer training loop does not settle whether effective improvement behavior changed: the learned policy, generated data, experiment choices, and retained information may all change inside it.

The task environment, external services, hardware, resource limits, and evaluation protocol are declared separately. A system may learn from new external observations. “Self” concerns the causal source and reuse of modifications, not isolation from the world. A stronger external teacher or human-designed change must be recorded rather than attributed to the learner.

## 2. Task performance and improvement performance

For task $x$, environment $E$, and execution budget $b$, the assembled system induces

$$
\tau\sim P(\tau\mid S,x,E,b).
$$

For a declared task distribution $Q$ and utility $u$,

$$
J_Q(S;b)=\mathbb E_{x\sim Q,\tau}[u(x,\tau)].
$$

Report domain scores, cost, reliability, and important regressions separately when no agreed scalar utility exists. One score does not identify a universal capability.

To describe improvement, distinguish **the system doing the work**, $A$, from **the target being changed**, $T$:

$$
T'\sim K_A(\cdot\mid T,p,B).
$$

Here $p$ specifies the editable surface, visible tasks, feedback, tools, and execution conditions; $B$ is the improvement budget. The kernel is a distribution because proposal, execution, training, and selection can be stochastic. Self-modification is the case in which $A$ and $T$ initially refer to the same system version.

For a common distribution $\mu$ of target/problem pairs, define

$$
G(A;\mu,B,b)=
\mathbb E_{\substack{(T,p)\sim\mu\\T'\sim K_A(\cdot\mid T,p,B)}}
\left[J_{Q_p}(T';b)-J_{Q_p}(T;b)\right].
$$

$Q_p$ specifies the assessment distribution; the distribution, task rules, and utility need not be secret. For empirical generalization claims, final test instances and their observed outcomes are withheld from candidate generation, selection, and stopping. Exact verification or formal proofs may instead establish a scoped claim under public specifications and explicit assumptions. These are different evidence routes, not different definitions of $G$. Regression constraints and any utility weights are specified before the comparison.

This distinguishes:

- $J_Q(S;b)$: how well the system performs tasks;
- $G(S;\mu,B,b)$: how much it improves the same reference targets at the same budget.

Compare the gain-versus-budget curve when budgets vary. CPU time, tokens, money, latency, and human effort are not interchangeable units. A scalar efficiency $G/c(B)$ is meaningful only after a cost function $c$ is declared. A ratio of efficiencies is unstable near a zero or negative denominator; a paired difference and uncertainty interval are usually more interpretable.

## 3. What would establish improved self-improvement?

First establish the lineage by which $S_0$ contributed to producing a persistent successor $S_1$. Then compare them as improvers on **identical copies of common targets**, not only on their different selves:

$$
T'_0\sim K_{S_0}(\cdot\mid T,p,B),
\qquad
T'_1\sim K_{S_1}(\cdot\mid T,p,B).
$$

The comparison is

$$
\Delta_{\rm rec}
=
G(S_1;\mu,B,b)-G(S_0;\mu,B,b).
$$

A reproducible positive difference supports the specific claim that this successor became a better improver on $\mu$. It does not by itself establish indefinite improvement, generality across all domains, or exponential growth.

Even pointwise one-step improvement on every target does not guarantee that
repeated reuse produces a better final system. Section 9 gives an exact
counterexample in which both routes always preserve or increase current
utility, and derives the finite-budget condition that accounts for remaining
improvement opportunities.

Comparing only $K_{S_0}(\cdot\mid S_0)$ with $K_{S_1}(\cdot\mid S_1)$ changes both the improver and the target. A stronger target can have less remaining room for improvement or can be harder to modify. Conversely, easy remaining defects can make an unchanged improver appear stronger.

For causal reuse, compare continued runs that use the successor as improver with runs that keep the ancestor improver frozen while giving both the same current target, feedback, and budget. Repeat the intervention across targets and independent runs. Record which model, code, or information change carried the effect.

The repository's D3 label denotes this stronger, controlled evidence for improved improvement ability. It is an operational convention, not a universal definition of RSI. Recursive reuse, growing improvement ability, sustained capability growth, and acceleration are separate claims. A useful recursive process need not accelerate every generation.

## 4. What model–harness co-evolution means

A harness controls what the model observes, which actions it can take, how much computation it spends, and which trajectories become available for learning. Model changes alter which harness policies it can use effectively and which modifications it can discover.

There are therefore two distinct questions:

1. Does the new model–harness pair perform better during execution?
2. Does changing one component improve the subsequent learning or search over the other?

For execution, evaluate all compatible combinations under a common data snapshot, environment, task budget, and metric:

$$
J_{ij}=J_Q(M_i,H_j,D;b),
\qquad
\Gamma_{MH}=J_{11}-J_{10}-J_{01}+J_{00}.
$$

$J_{10}-J_{00}$ and $J_{01}-J_{00}$ are effects conditional on the baseline counterpart. They are not context-independent component capabilities. Interface adaptations must be explicit and counted.

$\Gamma_{MH}$ is departure from additivity on the chosen score scale. It does not classify the cause:

| Example scores $(J_{00},J_{10},J_{01},J_{11})$ | Interaction | Interpretation |
|---|---:|---|
| $(50,60,60,60)$ | $-10$ | Both changes solve the same errors; neither harms performance |
| $(50,40,40,80)$ | $+50$ | The matched pair is strong, but both cross-pairs degrade |

Thus negative interaction need not mean conflict, and positive interaction need not mean portability. Nonlinear score transformations can change the interaction. Cross-version performance alone does not establish improved learning.

For learning, hold the initial model, training method, training budget, and evaluation fixed while varying the harness that generates training data. Separately, hold target harnesses and search budget fixed while varying the model used to propose edits. These interventions test the two directions of the proposed feedback.

The notation

$$
H^*(M,E,b)\in\arg\max_H J_Q(M,H;E,b)
$$

allows model-dependent optima; it does not prove that the optimum moves. For example, if $J(M,H)=a(M)+b(H)$, every model has the same harness ranking.

An alternating schedule—harness search, trajectory collection, model training, renewed harness search—is a candidate method. Joint optimization, model-only improvement, harness-only improvement, and adaptive schedules remain alternatives. Co-evolution does not require every component to change at every generation.

Internalization into weights can reduce repeated computation or improve generalization, but some functions should remain executable external operations. Exact computation, fresh retrieval, and interaction with physical instruments are not replaced merely by imitating their previous outputs.

### Update order and subsequent improvement

Let $P_M$ and $P_H$ be budgeted model-update and harness-update kernels on the
complete state, including generated data, archives and resources. Operators act
on observables: $(P_M f)(x)=\mathbb E[f(X')\mid x,\text{model update}]$.
Composition $P_M P_H J$ means model update followed by harness update.

The change in the value of a harness update caused by first updating the model is

$$
C_{M\to H}(x)=(P_M-I)(P_H-I)J(x).
$$

Consequently,

$$
(P_MP_H-I)J=(P_M-I)J+(P_H-I)J+C_{M\to H},
\qquad
C_{M\to H}-C_{H\to M}=(P_MP_H-P_HP_M)J.
$$

These are exact operator identities, not new optimization theorems. They work
for discrete edits and learned updates without a differentiable capability
coordinate. They distinguish the benefit of the *second learning operation*
from Section 4's static model/harness crossing. The update programs, feedback
cohorts, elapsed budgets and any actor refreshing must be specified. Compare
both orders at equal total resources to decide which schedule helps.
If the kernels commute, the two orders have identical expected endpoint
utility; co-evolution does not mathematically force an order advantage.
Their values still have to be measured or derived from a specified system.

## 5. Feedback and resource comparisons

Separate development feedback from final assessment. Search verifiers and learned judges may themselves be improved; changes to the evaluation protocol require a bridge comparison against previous versions. Protecting a benchmark against edits does not establish that it measures the desired objective.

Resource controls answer different questions:

- matched execution budgets compare deployed capability;
- matched improvement budgets compare improvers;
- lifecycle cost over a declared number of future tasks compares economic value.

Keep these comparisons separate. An expensive reusable improvement can be worthwhile after enough deployments even if it loses a one-task total-cost comparison.

Self-generated experience can contain useful solutions and failures. The value of a trajectory depends on the training rule, existing dataset, target model, and future tasks. Verification of the final answer alone does not prove that every intermediate step is useful to train on. Whether paired or evidence-rich trajectories outperform simpler data selection is an empirical question.

## 6. General representation and the limit of low-dimensional laws

The compatibility requirement has three levels: representing an algorithm's process, recovering its measured outcomes under its actual assumptions, and predicting new interventions. A general representation only establishes the first.

### Proposition 1: representation of digital adaptive systems

Consider a probabilistic digital system with finite description, finite stored state at each finite time, recorded external observations, and explicit resource accounting. State size may grow, code may rewrite itself, and episodes may be interrupted. Represent its complete execution state by $X_t$: executable descriptions, learned parameters, persistent and task-local memory, archives, pending computation, resource counters, and any relevant history. If no smaller sufficient state is known, take $X_t$ to include the full finite interaction history.

For an intervention $u_t$ and declared environment process, there is a transition law

$
X_{t+1}\sim\mathcal K^{u_t}(\cdot\mid X_t).
$

**Construction.** Encode the program and memory as finite strings and execute them with a fixed interpreter. Self-edits replace encoded code or data; they do not require rewriting the mathematical interpreter. Couple the original and encoded executions to the same random bits and external observations. Their next states, outputs, and resource records agree. Induction gives agreement of every finite trajectory distribution. Equivalently, define the conditional next-history distribution directly on the countable space of finite histories.

This construction includes parameter learning, prompt/data changes, arbitrary program rewrites, changing learning rules, populations, meta-agents, and simulated or real environment interaction. A neural model may be absent. The $M,H,D$ manifest is an implementation view of this larger $X$, not a claim that three scalar coordinates are sufficient.

An editable curriculum or simulator is inside the recorded system boundary; the external world and its response remain part of the declared environment. Changing a task generator must therefore appear in $X$ or as an explicit intervention, rather than being hidden behind an assumed fixed task distribution. The encoding preserves the original process's resource records; it does not assert that simulation on a different interpreter or hardware has identical runtime or energy cost.

Marginalizing over a budgeted improvement run gives the $K_A$ in Section 2. With a fixed intervention policy, the exact distribution evolves as

$
\nu_{t+1}=\nu_t\mathcal K,
\qquad
\mathbb E[J(X_{t+1})-J(X_t)]
=\nu_t(\mathcal K-I)J.
$

These are general probability identities. They require neither smoothness nor a fixed-dimensional parameter space. They preserve the processes studied in the compatibility table, but do not supply an efficient way to compute an unknown kernel.

### Proposition 2: when a smaller state has its own dynamics

Let $z=\phi(X)$ be a proposed summary, such as five scores for model, harness, improver, data, and evaluator. For a controlled Markov law on $z$ to represent all underlying states and interventions, the following condition is necessary and sufficient:

$
\phi(x)=\phi(y)
\ \Longrightarrow\
\mathcal K^u(x,\phi^{-1}(B))
=
\mathcal K^u(y,\phi^{-1}(B))
$

for every allowed intervention $u$ and measurable summary-state set $B$. A score predicted from $z$ must also be a function of $z$.

**Proof.** If the condition holds, define the summary transition using any representative $x$ with $\phi(x)=z$; the result is independent of that choice. Induction gives the same summary trajectory distribution. If it fails for $x,y,B$, a single summary transition starting at their common $z$ would have to assign two different probabilities to $B$, which is impossible.

For example, two states can share all recorded scores while one has a fixable parser defect and the other lacks a needed model capability. The same parser intervention need not have the same effect. The exact finite-state witness in the counterexample script assigns identical summaries to two states with different next-summary distributions.

For an approximate summary model, if every underlying state's next-summary law is within total variation $\epsilon$ of the proposed law, controls use only the summary, and initial summary distributions match, induction bounds the $T$-step marginal error by $\min(1,T\epsilon)$. A summary-measurable score in $[0,1]$ has expectation error no larger than that bound. This is a conditional quantitative prediction: measure one-step residual dependence on omitted information before trusting long-horizon projections.

Thus the earlier five-score Jacobian needs a state-sufficiency argument or an empirically measured approximation error. Writing $dx/dr=F(x)$ does not establish one.

### Proposition 3: general representation does not imply improvement on every task

Let $\delta(x)$ be the successor-minus-parent expected utility for task $x$ at a fixed budget. Then

$
\mathbb E_{x\sim Q}[\delta(x)]\ge0
\quad\text{for every distribution }Q
\quad\Longleftrightarrow\quad
\delta(x)\ge0\text{ for every task }x.
$

**Proof.** Pointwise nonnegativity implies nonnegative expectation. Conversely, if $\delta(x_0)<0$, the distribution concentrated at $x_0$ violates the assertion.

For normalized utilities in $[0,1]$,

$
\left|\mathbb E_Q\delta-\mathbb E_P\delta\right|
\le 2\,\operatorname{TV}(P,Q).
$

This follows because $\delta\in[-1,1]$. It is an explicit, generally loose transfer bound, not a claim that all interesting task shifts have small total variation.

A useful general theory must allow positive transfer, redundancy, regression, saturation, and changes of bottleneck. A universal guarantee of strictly improving every arbitrary task is already impossible for a task on which the parent attains the maximum utility.

These propositions use standard computation and probability constructions. The contribution here is the resulting correction to the research model and the conditions an RSI-specific predictive reduction must satisfy. No new physical law follows from calling selection “temperature,” resource use “energy,” or a change of sign a “phase transition.” A physical prediction requires measured physical variables, a specified link to computation, and validation at that level.

## 7. What a predictive theory still needs

A transition kernel specifies what must be measured; it does not predict its values. A low-dimensional state such as “model quality, harness quality, data quality” is justified only if it predicts interventions across systems with different implementations and histories.

### Proposition 4: the evidence must distinguish the predicted effect

Fix an admissible mechanism class $\mathfrak K$, an observation protocol, and a target intervention effect $\theta(K)$. Known source code, verified properties, and declared assumptions constrain this class. Let $P_{\rm obs}^{K}$ be the observation distribution under the interventions actually performed. The effect is identifiable from that distribution within the class exactly when

$$
P_{\rm obs}^{K_1}=P_{\rm obs}^{K_2}
\quad\Longrightarrow\quad
\theta(K_1)=\theta(K_2).
$$

**Derivation.** This condition makes $\theta$ a well-defined function of the observation distribution. If it fails, no function of that distribution can return the correct effect in both mechanisms. More strongly, an estimator $\widehat\theta$ based on the observations has the same distribution in the two mechanisms, so the triangle inequality gives

$$
\max_{i=1,2}\mathbb E_i\!\left[|\widehat\theta-\theta(K_i)|\right]
\ \ge\ \frac{|\theta(K_1)-\theta(K_2)|}{2}.
$$

This is an identification result, not a guarantee of accurate finite-sample estimation even when the condition holds. Identifying the requested effect need not identify the entire kernel.

**Exact witness.** The observation protocol records action/state/utility traces, with no additional evidence fixing untried transitions. A target starts with utility $1/2$. Every observed run keeps the ancestor as improver, intervention $u_0$, and retains utility $1/2$. Two complete controlled Markov mechanisms agree on all these observations. Under untested intervention $u_1$, reusing the successor as improver, one produces utility $1$ and the other utility $0$. Their gains relative to $u_0$ are $+1/2$ and $-1/2$. Both have a sufficient state and a valid common-target $G$; neither property distinguishes them. Any observation-based estimator has expected absolute error at least $1/2$ in one of these mechanisms, however many $u_0$ runs it sees.

**Measurable consequence.** Apply $u_0$ and $u_1$ to matched target copies under the same feedback and budgets, randomizing assignment when appropriate. The two witness mechanisms predict opposite signs and can be distinguished. For an untested method or domain, state which mechanism is assumed shared and what withheld result would refute that assumption. When compatible mechanisms still predict conflicting signs, report that ambiguity or perform the distinguishing experiment; do not resolve it by giving each paper a new fitted parameter.

Representation, state sufficiency, and identification answer different questions. None alone establishes predictive accuracy, useful computation time, or transfer to a new regime. A general theory must recover valid conditional results from different methods, including failures; it need not make contradictory or unsupported interpretations simultaneously true.

The present program should test:

- whether improved task capability predicts improved $G$ after controlling for target and budget;
- whether model changes alter harness rankings and learning-data value;
- when alternating model/harness updates outperform simpler schedules;
- whether reusing successors as improvers adds benefit over a frozen ancestor;
- how these effects transfer to new tasks, larger budgets, and later generations.

The per-work representation and remaining evidence obligations are recorded in [COMPATIBILITY.md](COMPATIBILITY.md).

These are open questions. A portfolio, separate improver process, singularly separated update timescales, and model-weight training are possible designs, not mathematical necessities for every self-improving system.

Primary work supports particular implementations: [DGM](https://arxiv.org/abs/2505.22954) studies agent-code self-modification; [Co-Harness](https://arxiv.org/abs/2607.22688) alternates harness and model optimization; [HELIX](https://arxiv.org/abs/2608.13951) reports one harness-evolution round and retained training records. These results do not imply that one schedule or representation is universally optimal.

## 8. Counterexamples to the earlier growth interpretation

These are mathematical objections to specific claims, not experimental results about AI. Reproduce the numerical witnesses with:

~~~bash
python scripts/check_model_counterexamples.py
~~~

### The proposed differential recursive term is coordinate dependent

For a deterministic smooth flow $ds/dr=F(s)$ and a smooth score $J$,

$$
\frac{d^2J}{dr^2}
=
F^\top\nabla^2J\,F+\nabla J^\top(DF)F.
$$

The identity is valid. The earlier interpretation of its second term as an isolated measure of recursion is not.

Take a fixed process with $x>0$,

$$
\frac{dx}{dr}=x,\qquad J(x)=x.
$$

Then $\nabla J^\top(DF)F=x>0$. In the coordinate $y=\log x$, the same process and score are

$$
\frac{dy}{dr}=1,\qquad \widetilde J(y)=e^y.
$$

Now $\nabla\widetilde J^\top(D\widetilde F)\widetilde F=0$; all acceleration lies in the curvature term. No behavior, algorithm, budget, or measured outcome changed. The split cannot identify causal improvement of the improver. Even a fixed optimizer generally has a state-dependent $F$.

The identity is deterministic. An Ito diffusion also has a second-order diffusion term in the expected score derivative; writing unspecified noise beside $F$ does not justify omitting it.

### The sign of gain minus debt is not the growth condition

For the illustrative equation

$$
\frac{d\eta}{dr}=(g-d)\eta-\kappa\eta^2+u,
$$

with $\eta>0$,

$$
\frac{d\eta}{dr}>0
\quad\Longleftrightarrow\quad
g-d>\kappa\eta-\frac{u}{\eta}.
$$

Hence $g>d$ is not sufficient for rising efficiency. For example, $g-d=1$, $\kappa=1$, $\eta=2$, and $u=0$ give $d\eta/dr=-2$.

With constant $g-d>0$, $\kappa>0$, and $u=0$, positive solutions tend to $\eta^*=(g-d)/\kappa$. Their asymptotic logarithmic growth rate is zero, not positive.

Moreover, replacing $(g,d)$ by $(g+q,d+q)$ leaves every trajectory unchanged. The separate causal quantities “recursive design gain” and “complexity debt” cannot be identified from the trajectory alone.

If $\eta$ is defined as $dC/dr$, it is a path slope, not the common-target improvement ability $G$. For a bounded score $C\le1$ and nonnegative $\eta$, $\int_0^R\eta\,dr\le1-C(0)$; indefinite positive efficiency growth on that same score scale is impossible.

### Evaluator noise does not imply a universal phase boundary

For independent identically distributed, jointly Gaussian pairs $(g_j,y_j)$, let $\rho=\operatorname{Corr}(g,y)$ and select the largest $y_j$. Then

$$
\mathbb E[g_{\rm selected}]
=
\mu_g+\rho\sigma_g\,a_n,
\qquad
a_n=\mathbb E\!\left[\max_{j\le n} Z_j\right],
$$

where the $Z_j$ are independent standard normal variables. This follows by conditioning on $y$ and using the Gaussian conditional mean. For large $n$, $a_n\sim\sqrt{2\log n}$.

With fixed $\rho>0$, expected true selected gain increases with $n$. Gain per unit cost can peak and then fall. Falling absolute gain requires additional assumptions, such as changing candidate distributions, adaptive exploitation, or budget-induced evaluation degradation. A cost optimum is not by itself a sharp phase transition. Correlation alone does not imply this formula outside the stated distributional assumptions.

### Engineering choices do not follow from notation

A timescale ordering does not establish stability or instability; the coupling and update rule matter. Writing a Jacobian does not show that chosen summary variables form a closed dynamical system. A portfolio can preserve useful diversity, but its value must exceed its search and maintenance cost. These remain hypotheses for intervention experiments.

The retained simulations illustrate consequences of chosen equations. They do not establish model–harness causality, recursive acceleration, or a forecast for real systems.

## 9. Finite-budget value of reusing successors

The more basic quantity for choosing a research route is its expected final
utility at a declared resource budget. The one-step $G$ is one observable of
that process. It does not replace the value of the remaining research.

### Proposition 5: exact continuation decomposition

Let $X$ contain the complete state required in Proposition 1, including time,
remaining resources and relevant external observations. Compare two declared
policies on the same state space:

- $P$: use a pinned ancestor as improver;
- $R$: reuse successors according to a specified refresh rule.

Allow either policy to modify model parameters, executable code, stored
information, populations, update rules or development tasks. The original
external world and its stochastic response are common to the comparison.
Assume a finite horizon $N$, integrable terminal utility $J$, and admissible
budgeted transitions. Stopping is an absorbing state. Unequal physical step
costs must enter the resource state and stopping rule; equal generation counts
alone do not constitute equal compute.

Define $V_0^P=J$ and $V_n^P=P V_{n-1}^P$. At a state with $n$ steps remaining,
define the continuation advantage

$$
a_n(x)=(R-P)V_{n-1}^P(x).
$$

It compares changing the next actor while continuing both resulting branches
with the same pinned policy. Then

$$
\boxed{\quad
V_N^R(x)-V_N^P(x)
=\mathbb E_R\!\left[\sum_{t=0}^{N-1}a_{N-t}(X_t)\mid X_0=x\right].
\quad}
$$

**Proof.** Subtract the Bellman recurrences:
$V_n^R-V_n^P=(R-P)V_{n-1}^P+R(V_{n-1}^R-V_{n-1}^P)$.
Iterate this equality to $V_0^R-V_0^P=0$. This proof requires neither
differentiability, fixed model size nor a particular implementation partition.
Equivalently, it is the noncommutative telescoping identity
$R^N-P^N=\sum_{t=0}^{N-1}R^t(R-P)P^{N-t-1}$.

This is a finite-horizon instance of the standard performance-difference
argument used in policy improvement; see
[Schulman et al., Section 2 and Appendix A](https://arxiv.org/abs/1502.05477).
The application here replaces the earlier coordinate-dependent recursive term
with a comparison of specified interventions. It is not an original general
growth theorem.

**Condition.** Nonnegative $a_{N-t}$ on all states reached by $R$ is sufficient
for nonnegative final reuse benefit. Positive expected accumulated advantage is
necessary and sufficient. Checking $a_1=(R-P)J$ alone cannot establish this
condition: earlier decisions act on future attainable outcomes.

### Exact failure of the one-step criterion

The following deterministic state transitions have utilities in [0,1]:

| State | Utility | Next under pinned $P$ | Next under refreshed $R$ |
|---|---:|---|---|
| $a$ | 0 | $b$ | $d$ |
| $b$ | 0.4 | $c$ | $c$ |
| $c$ | 1 | $c$ | $c$ |
| $d$ | 0.6 | $d$ | $e$ |
| $e$ | 0.7 | $e$ | $e$ |

At every state, $RJ\ge PJ$, and neither policy ever reduces current utility.
Starting at $a$, refreshed reuse wins the one-step comparison, $0.6>0.4$, but
loses after two steps, $0.7<1$. Its continuation advantages are $-0.4$ at
$a$ and $+0.1$ at $d$, totaling $-0.3$ exactly. Reversing the policy labels also
shows how an initially worse move can lead to a better endpoint.

Thus an improved one-step improver can steer toward a poorer future search
region. This is a limitation of the inference from D3 to sustained growth, even
with exact evaluation and monotone task gains. It is not evidence that a
particular real RSI implementation follows these transitions.

### Computable comparisons and error accounting

To estimate $a_n$, fork identical current states, change only the next actor,
and execute the same pinned continuation on each branch. The two-step version
is implemented in Experiment 006. Full long-horizon branching can be expensive;
the cost belongs in the resource budget of any method that uses it to select
updates.

If a continuation approximation satisfies
$\|\widehat V_{n-1}^P-V_{n-1}^P\|_\infty\le\epsilon_{n-1}$ and estimating its
two transition expectations adds at most $\delta_n$ error to their difference,
then

$$
|\widehat a_n-a_n|\le2\epsilon_{n-1}+\delta_n.
$$

Each stochastic kernel has sup-norm operator bound one, which proves this
inequality. A nonnegative lower bound
$\widehat a_n-2\epsilon_{n-1}-\delta_n$ at all reached states is therefore
sufficient for the preceding improvement condition. Estimated average accuracy
on a few tasks does not supply this uniform bound. If the extra measurement
cost changes the remaining budget, recompute the continuation comparison at
that remaining budget.

The measurable predictions concern declared actor choices, update order,
remaining budget and terminal outcomes. The formal identity applies to all
digital implementations admitted by Proposition 1; obtaining accurate and
affordable continuation estimates is a separate computational question.
Physical time and energy enter through measured transition costs, rather than
through an assumed universal acceleration law.

