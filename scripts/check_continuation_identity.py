#!/usr/bin/env python3
"""Exact rational witnesses for finite-horizon recursive-reuse value."""
from fractions import Fraction as F
import json
import random


def apply(kernel, vector):
    return [sum((p*v for p,v in zip(row,vector)), F(0)) for row in kernel]


def power(kernel, vector, n):
    for _ in range(n):
        vector = apply(kernel, vector)
    return vector


def subtract(a,b):
    return [x-y for x,y in zip(a,b)]


def deterministic(destinations):
    return [[F(j==destination) for j in range(len(destinations))]
            for destination in destinations]


def check(p,r,j,n):
    lhs = subtract(power(r,j,n),power(p,j,n))
    rhs = [F(0)]*len(j)
    for t in range(n):
        continuation = power(p,j,n-t-1)
        advantage = subtract(apply(r,continuation),apply(p,continuation))
        term = power(r,advantage,t)
        rhs = [a+b for a,b in zip(rhs,term)]
    assert lhs == rhs
    return lhs


def main():
    j = [F(0),F(2,5),F(1),F(3,5),F(7,10)]
    # a -> b -> c under P; a -> d -> e under R.
    p = deterministic([1,2,2,3,4])
    r = deterministic([3,2,2,4,4])
    pj,rj = apply(p,j),apply(r,j)
    one_step = subtract(rj,pj)
    assert all(x>=0 for x in one_step)
    assert all(new>=old for new,old in zip(pj,j))
    assert all(new>=old for new,old in zip(rj,j))
    effect = check(p,r,j,2)[0]
    assert effect == F(-3,10)
    first = subtract(apply(r,pj),apply(p,pj))[0]
    second = apply(r,one_step)[0]
    assert first == F(-2,5) and second == F(1,10)
    assert first+second == effect

    rng=random.Random(20261018)
    cases=0
    for _ in range(40):
        size=4
        kernels=[]
        for _ in range(2):
            rows=[]
            for _ in range(size):
                raw=[rng.randrange(1,10) for _ in range(size)]
                rows.append([F(v,sum(raw)) for v in raw])
            kernels.append(rows)
        utility=[F(rng.randrange(11),10) for _ in range(size)]
        for horizon in range(1,7):
            check(*kernels,utility,horizon)
            cases+=1
    print(json.dumps({
        "status":"exact rational checks passed",
        "stochastic_kernel_horizon_cases":cases,
        "one_step_dominance_at_all_states":[str(v) for v in one_step],
        "both_kernels_never_reduce_current_utility":True,
        "two_step_value_ancestor":str(power(p,j,2)[0]),
        "two_step_value_refreshed":str(power(r,j,2)[0]),
        "two_step_difference":str(effect),
        "continuation_advantage_terms":[str(first),str(second)],
        "interpretation":"mathematical witness, not an empirical AI result"
    },indent=2))


if __name__=="__main__":
    main()
