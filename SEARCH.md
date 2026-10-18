# A computable bridge from learned behavior to improvement cost

The mechanism model needs a quantitative bridge to an executable algorithm.
For verifiable, deterministic search problems, policy-guided search supplies
one: assign probability to solution paths and spend computation in a way that
has a bound in terms of those probabilities. This is a scoped algorithmic
model, not a universal quantitative law for every RSI method.

## 1. Recovering the missing prior mechanisms

[Expert Iteration](https://arxiv.org/pdf/1705.08439) couples search-based planning
with a learned policy that generalizes its results and guides subsequent
search. [DreamCoder](https://www.neurosymbolic.org/papers/EllisWNSMHCST21.pdf)
also changes the library in which solutions are expressed. Its recognition
model guides program search, while reusable abstractions change the language.
These are concrete precedents for coupled learning and external computation.

[LevinTS](https://arxiv.org/pdf/1811.10928) provides a policy-dependent search
bound. [LTS with context models](https://www.ijcai.org/proceedings/2023/0624.pdf)
turns that bound into a convex learning objective for a particular policy
class. [Policy-guided Heuristic Search](https://cdn.aaai.org/ojs/17469/17469-13-20963-1-2-20210518.pdf)
also incorporates heuristic estimates and nonuniform expansion loss.
These results provide more structure than labelling the interaction M/H.

They do not force all self-improvement into tree search. SEAL changes the
value of an update; POET changes environments and transfer routes; a physical
experiment can acquire unavailable facts. Those operations change the search
problem or its transition law, and need their own assumptions.

## 2. Search effort connects learning to subsequent computation

Let a locally finite rooted tree describe a deterministic search. Its nodes
are action prefixes, with a decidable goal predicate. A policy gives each
child a nonnegative conditional probability, summing to at most one.
The path probability is

$$
p_\theta(\tau)=\prod_{t<d(\tau)}\pi_\theta(a_t\mid h_t).
$$

For a non-root goal with positive probability, expand prefixes in increasing
order of depth divided by path probability. The LTS bound is

$$
N_\theta(\tau)\le 1+\frac{d(\tau)}{p_\theta(\tau)}.
$$

Here the right side bounds reaching this specified goal, and the algorithm
may stop at another goal earlier. This is an existing theorem, not a new
BeforeRSI discovery. State pruning needs additional conditions; Markov-state
probability dominance is used in Experiment 008.

The counting argument makes the mechanism transparent. All expanded nodes
have depth/probability at most that of the goal. For the leaves L of that
prefix tree, the number of non-root nodes is at most the sum of leaf depths.
Hence it is at most `sum_L p(l)*[d(l)/p(l)]`, which is bounded by
`d(goal)/p(goal)` because prefix-free leaf probabilities sum to at most one.

Define trajectory surprise `ell_theta(tau)=-log p_theta(tau)`. The bound term
is `d*exp(ell)`. A particular path's bound changes by

$$
\frac{B_{\theta'}(\tau')}{B_\theta(\tau)}
=\frac{d(\tau')}{d(\tau)}
\exp\{\ell_{\theta'}(\tau')-\ell_\theta(\tau)\},
\qquad B_\theta(\tau)=d(\tau)/p_\theta(\tau).
$$

This is an exact ratio of **bounds**, not of realized runtimes. For changed
representations, tau and tau' must satisfy the same external specification;
macro execution and verification costs must be counted. A shorter symbolic
description may hide expensive execution. A faster probability model may
offset a slightly worse policy. Node counts alone cannot settle these trades.

The bridge identifies separate interventions: learning changes path mass;
library abstraction changes available paths and their length; search order and
heuristics change how that mass translates to computation; verification defines
which paths are acceptable. Search-generated solutions then become learning
inputs. The same mathematics allows a fixed harness with improving weights.

## 3. The loss must match the operation being improved

For a fixed set of successful paths, mean action cross entropy and

$$
\mathcal L_{\rm effort}(\theta)
=\frac1n\sum_{i=1}^n d_i\exp(\ell_\theta(\tau_i))
$$

can rank policies differently. For equal unit depths, take successful-path
probabilities `(0.1,0.1)` versus `(0.99,0.02)` on two tasks. The latter has
lower mean negative log probability (1.961 versus 2.303), but a higher mean
inverse probability (25.505 versus 10). Improving the geometric average need
not improve the arithmetic mean of search-effort bounds. This is an exact
loss-mismatch example, not a statement that CE always gives slower search.

For legal-action logits linear in parameters, each path NLL is convex: it is
a sum of log-sum-exp terms minus linear terms. Its exponential is convex and
nondecreasing in that NLL, so the effort loss is convex. This recovers the
relevant context-model result. It does not imply convexity for arbitrary neural
networks, nor success on paths absent from the data. Experiment 008 optimizes
a regularized log mean bound, with its exact normalization specified.

Different valid paths can solve one task. Choosing one path as the training
target can produce an unnecessarily poor bound. Candidate-path search,
representation learning and the learner's capacity remain consequential.
Optimizing an upper bound alone does not guarantee improving realized search:
the bound may be loose and held-out task structure may differ.

## 4. Retain a whole computation, not just a local action preference

Suppose the ancestor and successor define path distributions p0 and p1.
Mixing complete paths gives

$$
q(\tau)=w p_0(\tau)+(1-w)p_1(\tau)\ge w p_0(\tau).
$$

For an ancestor solution of depth d, its LTS bound under q is at most
`1+d/[w*p0(tau)]`: only a factor 1/w in the nonconstant bound term.
The exact sequential implementation updates mixture weights after every prefix:

$$
q(a\mid h)=\sum_i w_i(h)p_i(a\mid h),\qquad
w_i(h)=\frac{w_i p_i(h)}{\sum_j w_j p_j(h)}.
$$

The prefix posterior is part of the state. Treating this history-dependent
policy as Markov in the environment state alone can invalidate state pruning.

By contrast, mixing with the same weights at every action gives only
`q_local(tau)>=w^d*p0(tau)`. If the two policies deterministically choose
opposite actions and the old solution takes d old actions, this is equality.
The lost path mass is exponential in d. Local random mixing can repeatedly
interrupt a coherent old strategy; complete-path mixing pays for choosing it
once. The probability identity is standard mixture reasoning, applied here to
preserving a long-horizon search capability.

A more general implementation needs no shared action space: keep two complete,
resumable search processes and allocate each a fixed fraction of computation.
For the Experiment 008 schedule `[old,new,new,new]`, if their solo completion
costs are T0 and T1 pops, then the portfolio completion cost satisfies

$$
T_{\rm portfolio}\le
\min\{4T_0,\;4\lceil T_1/3\rceil\}.
$$

**Proof.** Every four scheduled pops give the old process one and the new
process three. By the respective right-side times the corresponding process
has received enough pops to complete. Return the first verified solution.
No advance estimate of which process will win is required. This is classical
fair interleaving, not a new universal-search theorem.

There is a distribution-independent consequence. Write
`F_i(x,b)=1[T_i(x)<=b]`. For budgets B divisible by four,

$$
F_{\rm portfolio}(x,B)\ge
\max\{F_0(x,B/4),F_1(x,3B/4)\}.
$$

This holds pointwise in x, so it also holds after averaging over **any** task
distribution, without estimating a transfer distribution. For stochastic
searches, couple each process to its own fixed random stream and then average.
The guarantee compares an ancestor at B/4, not at B; it promises a coverage
floor at a resource share, not monotone full-budget task scores. More generally,
any finite set of independently resumable solvers can be scheduled by shares
w_i, yielding the corresponding per-task floor after rounding and overhead.
The guarantee does not require their model/harness decompositions to agree.

This guarantee is about actual completion in the chosen work unit, unlike a
ratio of loose LTS bounds. It requires resumable independent processes,
preserved state, compatible acceptance criteria, and accounted scheduler and
memory overhead. Unequal-cost pops do not imply the same wall-time factor.
Use measured CPU quanta for a time guarantee, with bounded preemption overhead.
Unrepeatable physical interactions cannot simply be forked under this model.

The generalization is useful: weights, code, memories, architectures and action
languages may differ, because the protected object is a running computation.
Keep an anchor's allocation fixed if its protection is meant to persist;
repeatedly replacing it or diluting its weight across generations loses that
constant guarantee. Protecting every past version has a growing cost.

## 5. When to spend computation choosing a computation

For a fixed set of candidate values V_i with uncertainty, an experiment Y has
one-step information value

$$
\operatorname{VOI}(Y)=
\mathbb E_Y\max_i\mathbb E[V_i\mid Y]-\max_i\mathbb E[V_i].
$$

It is nonnegative by conditional Jensen and at most
`E[max_i V_i]-max_i E[V_i]`, the value of perfect information. Subtract the
experiment's cost under an explicit utility conversion, or debit a resource
budget. An experiment whose outcome cannot change the selected action has
zero value under this one-step model. Several experiments can be jointly
useful even if each alone is not. Physical improvement of a candidate changes
V itself and must not be counted as information alone.

This is established metareasoning, including
[Hay et al.](https://arxiv.org/pdf/1207.5879). It explains why a metacontroller
can spend more than it saves, and why infinite recursion into increasingly
expensive selection is not an algorithm. The complete-search portfolio offers
a different option when rankings are uncertain: buy a known overhead bound
instead of first paying to predict the winner.

If a learned route costs C extra to build, and saves Delta>0 expected seconds
per future task at the required success level, N stationary future tasks
justify it when `N*Delta>C`. If it also changes success probability, keep the
success/cost frontier or specify the value of a solved task. The quantity C
must include probe training and selection, not just the chosen final update.

## 6. Executable test and resulting route

[Experiment 008](experiments/008-learned-search/PROTOCOL.md) implements learned
context policies, actual Levin search, five search-and-learn rounds, frozen
versus reused collectors, CE versus search-bound learning, and local mixture
versus whole-search preservation. A second intervention uses the final actors
to produce training data for identical fresh learners on common target tasks.
All found training paths come from executed searches, not an optimal-distance
oracle. It records resource differences rather than equating pops with FLOPs.

The executed results support reuse in this small domain. On the new uniform
state cohort at 256 pops, reuse-CE solves 369/512 starts, versus 25/512 after
frozen collection; the effort-loss route solves 404/512. On identical fresh
learner targets, data produced by the reused CE actor yield 344/512 solutions,
versus 176/512 from the frozen-collection actor. These are different causal
comparisons. The second changes the data producer while controlling the learner;
it includes both data quantity and data quality, and the full costs are reported.
Neither result identifies a generally optimal research schedule.

The resulting engineering route is specific: learn reusable search operations
from verified paths, optimize the cost of the operation where a defensible
objective is available, retain a complete anchor computation while trying a
new one, and spend on selector calibration only when its reuse justifies that
cost. This does not prescribe one loss or one fixed schedule across methods.
Actual outcomes and changes forced by them belong in the experiment's report.

The conceptual framework remains broader than this tractable subclass.
Stochastic environments, unknown/verifier-free goals, expensive measurements,
representation changes and unsolved scientific conjectures require further
models. A representation can contain them without making this search bound
an explanation of every result. The useful generality here is an explicit
bridge from a stated mechanism to an executable update and a scoped guarantee.
