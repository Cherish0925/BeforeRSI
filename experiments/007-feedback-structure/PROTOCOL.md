# Feedback structure and inheritance

This experiment executes a finite active-identification problem. It is a
mechanism experiment, not an LLM benchmark or a reproduction of GEPA/MASS.
It distinguishes a concrete pair of explanations: successful improvement
depends only on the number of trials, versus it also depends on whether
feedback exposes reusable subproblems.

## Frozen design

A hidden specification contains d independent symbols, each with m choices.
A candidate succeeds exactly when all symbols match. The hidden specification
is uniform; no strategy receives a better initial prior. Every query evaluates
all d components, so one query costs d primitive checks in every condition.
Only the returned information differs.

- Scalar feedback: exact whole-candidate pass/fail. Distinct random guesses
  implement an optimal strategy under the uniform prior and equality oracle.
- Local feedback: the same pass/fail plus the first mismatching component.
  The learner preserves the certified prefix and tests untried symbols at that
  component. It neither observes the target nor receives the correct symbol.
- Erased feedback: run the scalar strategy when localization is unavailable.
  This is the information-removal intervention, not a new baseline.

Primary prediction: with B distinct scalar queries, success probability is
min(B/m^d,1). Local search needs at most 1+d(m-1) queries for certain success;
its exact query count is 1 plus a sum of d independent uniforms on 0,...,m-1.
The implementation samples hidden specifications and executes actual queries,
then compares the distribution to this prospectively stated exact law.

Use m=4, d in {2,4,8,16}, 2,000 independent hidden specifications, seed
2026101807. Report cumulative success at B in {4,8,16,32,64}; pair the same
hidden specifications across strategies. Preserve per-instance query counts.
There is no parameter fitting. All dimensions test the same analytical law.

Two further exact constructions test whether a perfect teacher necessarily
produces an improved student. A hidden bit determines the right action. The
teacher sees the bit; a restricted student either sees or loses it. Calculate
the optimal likelihood projection in both cases. Then calculate the task
mixture created by globally filtering successes when easy and hard tasks have
different success probabilities. These are analytic witnesses, not measured
neural learning curves.

Failure condition: if localization is untrustworthy, correct local choices do
not compose, or task dependencies invalidate a certified prefix, the local
guarantee does not apply. No inference is made that natural-language traces
always supply such an oracle. The explicit construction establishes that
feedback structure can change query complexity, rather than estimating the
size of that effect in any cited agent.

Run `python experiments/007-feedback-structure/run.py`. NumPy is the sole
non-standard dependency. It writes per-instance records, exact predictions,
summary, a source-hashed manifest, and a human-readable result table. The
randomized equality search is simulated on a small synthetic oracle; no
physical-world forecast is claimed.
