#!/usr/bin/env python3
"""Exact enumeration of a finite learner class; no sampled training curve."""
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
# Four equally likely task types, identical observations for both data sources.
# Entries give each policy's probability of the correct answer on that type.
learners={"A":[.99,.99,.99,.001],"B":[.6,.6,.4,.4]}
teachers={"perfect":[1.,1.,1.,1.],"compatible":learners["A"]}


def bernoulli_kl(q,p):
    return (q*math.log(q/p) if q else 0)+((1-q)*math.log((1-q)/(1-p)) if q<1 else 0)


results={}
for name,q in teachers.items():
    divergence={key:sum(bernoulli_kl(a,b) for a,b in zip(q,p))/4
                for key,p in learners.items()}
    chosen=min(divergence,key=divergence.get)
    results[name]={"teacher_expected_accuracy":sum(q)/4,
        "teacher_greedy_accuracy":sum(x>.5 for x in q)/4,
        "KL_to_learners":divergence,"selected_student":chosen,
        "student_expected_accuracy":sum(learners[chosen])/4,
        "student_greedy_accuracy":sum(x>.5 for x in learners[chosen])/4}
assert results["perfect"]["selected_student"]=="B"
assert results["compatible"]["selected_student"]=="A"
assert results["perfect"]["teacher_expected_accuracy"]>results["compatible"]["teacher_expected_accuracy"]
assert results["perfect"]["student_expected_accuracy"]<results["compatible"]["student_expected_accuracy"]
assert results["perfect"]["student_greedy_accuracy"]<results["compatible"]["student_greedy_accuracy"]
out={"kind":"finite-class analytic counterexample, not an empirical LLM result",
     "conditions":"same uniform tasks, observations, learner class and exact global likelihood projection",
     "learner_class":learners,"results":results}
(ROOT/"research/teacher-projection-witness.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
