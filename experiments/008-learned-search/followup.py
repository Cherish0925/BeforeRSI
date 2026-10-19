#!/usr/bin/env python3
import argparse,gzip,hashlib,json
from pathlib import Path
import numpy as np
from run import ROOT,GOAL,evaluate

def even(s):
    v=[x for x in s if x]
    return sum(a>b for i,a in enumerate(v) for b in v[i+1:])%2==0

def main(seed):
    used={GOAL}
    for k in [18,29,43,71]:
        t=json.loads((ROOT/'runs'/str(k)/'tasks.json').read_text())
        for starts in t['training']+[t['common_target_generation']]+list(t['test'].values()):
            used.update(tuple(s) for s in starts)
    cohorts={}
    for k in [18,29,43,71]:
        rng=np.random.default_rng(100000+k); out=[]
        while len(out)<128:
            s=tuple(map(int,rng.permutation(9)))
            if s not in used and even(s):used.add(s);out.append(s)
        cohorts[k]=out
    dest=ROOT/'followup'/str(seed);dest.mkdir(parents=True,exist_ok=True)
    tasks={'uniform_states':cohorts[seed]}
    (dest/'tasks.json').write_text(json.dumps(tasks,separators=(',',':'))+'\n')
    weights=np.load(ROOT/'runs'/str(seed)/'weights.npz')
    rows=evaluate(tasks,None,[64,256,1024],['uniform'],'uniform')
    for route in ['frozen_ce','reuse_ce','reuse_lts']:
        w=weights[route+'_round_5']
        rows+=evaluate(tasks,w,[64,256,1024],['learned','local','portfolio'],route)
    for actor in ['uniform','frozen_ce','reuse_ce','reuse_lts']:
        tag='common_student_'+actor
        rows+=evaluate(tasks,weights[tag],[64,256,1024],['learned'],tag)
    payload=(json.dumps(rows,separators=(',',':'))+'\n').encode()
    (dest/'records.json.gz').write_bytes(gzip.compress(payload,mtime=0))
    files=[Path(__file__),ROOT/'FOLLOWUP.md',ROOT/'run.py',dest/'tasks.json',dest/'records.json.gz',ROOT/'runs'/str(seed)/'weights.npz']
    (dest/'manifest.json').write_text(json.dumps({'seed':seed,'raw_sha256':hashlib.sha256(payload).hexdigest(),
        'files':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}},indent=2)+'\n')
    print(json.dumps({'seed':seed,'followup_done':True}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--seed',type=int,required=True);main(p.parse_args().seed)
