#!/usr/bin/env python3
"""Exact witnesses for path mixtures and complete-search scheduling."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,math

root=Path(__file__).resolve().parents[1]
w=F(1,4)
rows=[]
for d in [4,8,16,32]:
    global_p=w; local_p=w**d
    rows.append({'depth':d,'whole_path_probability':str(global_p),
                 'local_path_probability':str(local_p),
                 'bound_ratio_local_over_whole':str(global_p/local_p)})
    assert global_p/local_p==4**(d-1)

# Sequential posterior-weight mixing exactly recovers the complete-path mixture.
checks=0
for bits in product([0,1],repeat=6):
    pis=[F(1),F(1)]; q=F(1)
    for bit in bits:
        probs=[F(3,4) if bit else F(1,4),F(1,3) if bit else F(2,3)]
        denom=w*pis[0]+(1-w)*pis[1]
        cond=(w*pis[0]*probs[0]+(1-w)*pis[1]*probs[1])/denom
        q*=cond
        pis=[p*t for p,t in zip(pis,probs)]
    assert q==w*pis[0]+(1-w)*pis[1]
    assert q>=w*pis[0]
    checks+=1

# Check actual scheduler completion against the derived bound.
for t0 in range(1,60):
    for t1 in range(1,60):
        count=[0,0]
        for k in range(1,4*max(t0,t1)+1):
            arm=0 if (k-1)%4==0 else 1; count[arm]+=1
            if count[0]>=t0 or count[1]>=t1: break
        assert k<=min(4*t0,4*((t1+2)//3))
        checks+=1

probs=[[.1,.1],[.99,.02]]
loss=[{'probabilities':p,'mean_nll':sum(-math.log(x) for x in p)/2,
       'mean_inverse_probability':sum(1/x for x in p)/2} for p in probs]
assert loss[1]['mean_nll']<loss[0]['mean_nll']
assert loss[1]['mean_inverse_probability']>loss[0]['mean_inverse_probability']
out={'mixture_rows':rows,'exact_checks':checks,'loss_reversal':loss}
(root/'research/search-preservation-witness.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
