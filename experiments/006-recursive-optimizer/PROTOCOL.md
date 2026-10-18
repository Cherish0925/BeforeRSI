# Recursive optimizer experiment

This is an executed numerical optimization benchmark, not an LLM training run
or a simulation of an assumed capability-growth equation.

**Question.** Does feeding a changed optimizer back into the production of later
optimizers improve task performance or common-target improvement performance?
Do one-step and two-step actor comparisons agree?

**System.** A three-coefficient linear controller predicts log Gaussian mutation
scale from elapsed budget and recent success. Three binary harness settings
select coordinate/global proposals, antithetic proposals, and periodic restart.
Greedy incumbent retention and the meta-objective are fixed. The optimizer
searches this same six-coordinate configuration when producing a successor.
This is a deliberately small editable class; it is not a reproduction of a
neural learned optimizer or a claim about general-purpose AI.

**Interventions.** Four development routes start from the same configuration:
reuse the current successor as actor; keep the initial actor; global uniform
configuration search; fixed coordinate pattern search. Every update evaluates
17 candidates, including the target incumbent, on six feedback tasks with
32 objective calls per task: 3,264 primitive calls per update.
There are four generations. The first recursive and frozen updates must agree
exactly under the paired seeds.

**Tasks.** Six-dimensional shifted Sphere, diagonal Ellipsoid and Rosenbrock
form the development families. Each generation draws a fresh cohort.
Final assessment uses new instances of these families and separately reports
rotated Ellipsoid, Rastrigin and Ackley, which never supply development feedback.
Each assessment cohort has four instances per family. Scores are fractional
objective reduction relative to the zero-vector initial point, in [0,1].
No final score selects a development candidate.

**Common targets.** After all development snapshots are frozen, each actor
generation improves the same four reference targets per lineage. Feedback tasks,
search seeds, final task cohorts and budgets are paired across actor versions.
Reference targets and improvement problems are independent of development.
The primary actor statistic is final-minus-initial actor gain, averaged within
each lineage before uncertainty estimation.

**Continuation.** At the generation-two target, separately apply the initial
and final actors. Continue both resulting targets with the initial actor using
a fresh, common feedback cohort. Report one-step and two-step final-task
differences. This estimates the effect of the first actor under a declared
continuation; it is not the value of an arbitrarily long recursive process.

**Model/harness crossing.** Cross the initial/final recursive model coefficients
and harness settings under the same final tasks. Report all four cells and
their score-scale interaction. Shared effects need not imply portability.

**Resources.** Report primitive objective calls, nested meta-evaluations, and
local wall time separately. All within-experiment development routes have the
same primitive call budget. Assessment and branching costs are included in the
run total but do not enter development. CPU instructions or joules are not
measured, so call equality is not an energy-equivalence claim.

**Outcome.** A positive task gain alone does not establish improved improvement
ability. A positive common-target actor effect does not establish a positive
multi-generation route effect. Zero or negative results remain in the record.
Random and pattern search are simple controls, not asserted best-known
numerical optimizers.

**Pilot and frozen follow-up.** The pilot used eight independent lineages and
seed 20261018. It found no clear recursive-route advantage; inspection showed
that no retained recursive harness changed. Its continuous latent encoding
made discrete edits inaccessible at the chosen mutation scale. Its source and
results are retained as pilot_run.py and pilot_results/.

Before executing the follow-up, change only the binary search representation:
store harness coordinates as signs and propose explicit flips with probability
1/3 per coordinate during configuration search. Task search remains continuous.
Use 32 independent lineages and a new seed, 20261019, with the same task
families, budgets, scores and number of generations. This is a prospectively
specified follow-up after an exploratory pilot, not a preregistered first study.
There is no tuning on the follow-up assessment results.

**Training-objective follow-up.** After the typed run, compare training task
performance $J$ with training common-target improvement gain $G$ directly.
Use seed 20261020, 16 new lineages, three generations and nine outer candidates.
Keep the outer proposal actor fixed to isolate the objective change.
Each G candidate improves two reference targets with 17 evaluations on six
feedback tasks each, then evaluates child and parent on six separate internal
assessment tasks: exactly 7,296 primitive calls. Each J candidate receives the
same call allowance on the same 24 task definitions, with repeated search
seeds. Both objectives therefore have the same task-definition pool and
primitive-call cost, while using them for different computations.
Final task and common-target tests are separate from both training objectives.
This tests which quantity to train; it does not assume that G-training or
recursive reuse will win. The primary comparison is final G-trained versus
J-trained actor improvement gain on new common targets.

**Update-order comparison.** With seed 20261021 and 32 new lineages, compare
model-then-harness, harness-then-model, and joint search. Each ordered step
evaluates 17 configurations; joint search evaluates 34, so each full route
uses 6,528 primitive calls. Separate model-only and harness-only paths estimate
the change in the second operation's benefit. Feedback task definitions are
common, with action-specific random streams paired across orders. Freeze every
endpoint before new-instance and new-family assessment. Primary contrasts are
MH minus HM and each order minus joint search; no preferred winner is assumed.

**Artifacts.** Source hashes, configuration, software versions, frozen snapshots,
every development candidate and feedback score, assessment task-level scores,
common-target candidate traces and generation summaries are retained. Task
instances and random streams are exactly reconstructible from the recorded
generator and seeds. Bootstrap intervals resample independent lineages, with
5,000 replicates; they are descriptive and not simultaneous coverage guarantees
over every reported comparison.

Reproduce all four runs from the repository root in a fresh checkout, using
Python 3.12 and NumPy 2.3.5 as recorded in the main manifest. Matplotlib is
needed only for the report figure. The commands write their result directories;
timestamps and elapsed wall time will differ across runs.

~~~bash
OPENBLAS_NUM_THREADS=1 python experiments/006-recursive-optimizer/pilot_run.py \
  --output experiments/006-recursive-optimizer/pilot_results
OPENBLAS_NUM_THREADS=1 python experiments/006-recursive-optimizer/run.py \
  --output experiments/006-recursive-optimizer/results
OPENBLAS_NUM_THREADS=1 python experiments/006-recursive-optimizer/objective_compare.py
OPENBLAS_NUM_THREADS=1 python experiments/006-recursive-optimizer/order_compare.py
python experiments/006-recursive-optimizer/analyze.py
~~~

To regenerate the report from the preserved measurements without repeating
the experiments, first extract the raw records into the experiment directory:

~~~bash
tar -xzf experiments/006-recursive-optimizer/raw-results.tar.gz \
  -C experiments/006-recursive-optimizer
python experiments/006-recursive-optimizer/analyze.py
~~~
