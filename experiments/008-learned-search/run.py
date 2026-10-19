#!/usr/bin/env python3
"""Small, independent search-and-learn experiment. Python, NumPy and SciPy."""
from __future__ import annotations
import argparse, gzip, hashlib, heapq, itertools, json, math, os, time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from scipy.special import logsumexp

ROOT = Path(__file__).resolve().parent
GOAL = (1,2,3,4,5,6,7,8,0)
MOVES = {}
for b in range(9):
    r,c=divmod(b,3)
    MOVES[b]=tuple((a,b+delta) for a,delta,ok in
                  [(0,-3,r>0),(1,3,r<2),(2,-1,c>0),(3,1,c<2)] if ok)
NCTX=648

def contexts(s):
    pos=[0]*9
    for i,t in enumerate(s): pos[t]=i
    return [(t-1)*81+pos[0]*9+pos[t] for t in range(1,9)]

def move(s,j):
    a=list(s); b=a.index(0); a[b],a[j]=a[j],a[b]; return tuple(a)

def sample_tasks(rng,n,lo,hi,used):
    out=[]
    while len(out)<n:
        s=GOAL; prev=-1
        for _ in range(int(rng.integers(lo,hi+1))):
            b=s.index(0); opts=[j for _,j in MOVES[b] if j!=prev]
            j=opts[int(rng.integers(len(opts)))]; prev=b; s=move(s,j)
        if s!=GOAL and s not in used:
            used.add(s); out.append(s)
    return out

class Policy:
    def __init__(self,w=None,uniform_mix=0.0):
        self.w=w; self.mix=uniform_mix; self.cache={}; self.calls=0
    def probs(self,s):
        if s in self.cache: return self.cache[s]
        self.calls+=1
        legal=MOVES[s.index(0)]; aa=[a for a,_ in legal]
        if self.w is None:
            p=np.full(len(aa),1/len(aa))
        else:
            z=self.w[contexts(s)].sum(axis=0)[aa]
            p=np.exp(z-logsumexp(z))
            p=(1-self.mix)*p+self.mix/len(aa)
        result=tuple((a,j,float(math.log(v))) for (a,j),v in zip(legal,p))
        self.cache[s]=result
        return result

class Search:
    def __init__(self,start,policy):
        self.policy=policy; self.nodes=[(start,-1,-1,0.,0)]
        self.queue=[(-math.inf,0)]; self.visited={}
        self.pops=0; self.edges=0; self.solution=None
    def step(self):
        if not self.queue: return
        _,i=heapq.heappop(self.queue); self.pops+=1
        s,parent,action,logp,d=self.nodes[i]
        if s==GOAL:
            path=[]
            while self.nodes[i][1]>=0:
                node=self.nodes[i]; par=self.nodes[node[1]]
                path.append((par[0],node[2])); i=node[1]
            self.solution=list(reversed(path)); return
        if self.visited.get(s,-math.inf)>=logp: return
        self.visited[s]=logp
        for a,j,lp in self.policy.probs(s):
            t=move(s,j); k=len(self.nodes); newlp=logp+lp
            self.nodes.append((t,i,a,newlp,d+1)); self.edges+=1
            heapq.heappush(self.queue,(math.log(d+1)-newlp,k))

def solve(start,w,cap,mode='learned'):
    t=time.process_time()
    if mode=='uniform': searches=[Search(start,Policy())]
    elif mode=='portfolio': searches=[Search(start,Policy()),Search(start,Policy(w))]
    else: searches=[Search(start,Policy(w,.25 if mode=='local' else 0.))]
    path=None
    for k in range(cap):
        si=(0 if k%4==0 else 1) if len(searches)==2 else 0
        searches[si].step()
        if searches[si].solution is not None:
            path=searches[si].solution; break
    result={'solved':path is not None,'pops':sum(s.pops for s in searches),
            'policy_calls':sum(s.policy.calls for s in searches),
            'edges':sum(s.edges for s in searches),'length':len(path) if path else None,
            'cpu_s':time.process_time()-t}
    # Verify the returned witness in the environment, independently of the heap.
    if path is not None:
        s=start
        for obs,a in path:
            assert s==obs
            s=move(s,dict(MOVES[s.index(0)])[a])
        assert s==GOAL
    return result,path

def dataset(paths):
    states=[]; acts=[]; tids=[]
    for t,path in enumerate(paths):
        for s,a in path: states.append(s); acts.append(a); tids.append(t)
    ctx=np.array([contexts(s) for s in states],dtype=int)
    mask=np.full((len(states),4),-np.inf)
    for i,s in enumerate(states): mask[i,[a for a,_ in MOVES[s.index(0)]]]=0
    return ctx,mask,np.array(acts),np.array(tids),np.array([len(p) for p in paths],float)

def objective(wflat,data,kind):
    ctx,mask,acts,tids,depth=data
    w=wflat.reshape(NCTX,4); z=w[ctx].sum(axis=1)+mask
    lp=z-logsumexp(z,axis=1,keepdims=True)
    nll=-lp[np.arange(len(acts)),acts]
    if kind=='ce':
        loss=float(nll.mean()); sw=np.full(len(acts),1/len(acts))
    else:
        totals=np.bincount(tids,weights=nll,minlength=len(depth))
        q=np.log(depth)+totals; lognorm=logsumexp(q)
        loss=float((lognorm-math.log(len(depth)))/depth.mean())
        sw=(np.exp(q-lognorm)/depth.mean())[tids]
    g=np.exp(lp); g[np.arange(len(acts)),acts]-=1; g*=sw[:,None]
    grad=np.zeros_like(w)
    for j in range(ctx.shape[1]): np.add.at(grad,ctx[:,j],g)
    loss+=.5e-4*float(np.square(w).sum()); grad+=1e-4*w
    return loss,grad.ravel()

def fit(paths,w,kind):
    if not paths: return w.copy(),{'paths':0,'tokens':0,'cpu_s':0.,'nfev':0}
    data=dataset(paths); t=time.process_time()
    res=minimize(objective,w.ravel(),args=(data,kind),method='L-BFGS-B',jac=True,
                 bounds=[(-3.,3.)]*w.size,
                 options={'maxiter':120,'maxfun':160,'ftol':1e-9,'gtol':1e-5,'maxls':20})
    return res.x.reshape(w.shape),{'paths':len(paths),'tokens':int(len(data[2])),
        'cpu_s':time.process_time()-t,'nfev':int(res.nfev),'nit':int(res.nit),
        'success':bool(res.success),'message':str(res.message),'loss':float(res.fun),
        'token_gradient_evaluations':int(len(data[2])*res.nfev)}

def evaluate(tasks,w,caps,modes,tag):
    rows=[]
    for cohort,starts in tasks.items():
        for i,s in enumerate(starts):
            for cap in caps:
                for mode in modes:
                    r,_=solve(s,w,cap,mode)
                    rows.append(dict(tag=tag,cohort=cohort,task=i,start=s,cap=cap,mode=mode,**r))
    return rows

def run(seed,pilot=False):
    out=ROOT/('pilot' if pilot else 'runs')/str(seed); out.mkdir(parents=True,exist_ok=True)
    rng=np.random.default_rng(seed); used={GOAL}; n=32 if pilot else 96
    training=[sample_tasks(rng,n,*lr,used) for lr in [(4,8),(6,10),(8,12),(10,14),(12,18)]]
    common=sample_tasks(rng,n,10,18,used)
    tasks={'near':sample_tasks(rng,n,10,16,used),'far':sample_tasks(rng,n,18,26,used)}
    task_spec={'seed':seed,'training':training,'common_target_generation':common,'test':tasks}
    (out/'tasks.json').write_text(json.dumps(task_spec,separators=(',',':'))+'\n')
    raw={'rounds':[],'collection':[],'paths':{},'evaluations':[],'common_target':[]}
    snapshots={}; final={}
    raw['evaluations']+=evaluate(tasks,None,[256,1024],['uniform'],'uniform')
    for route in ['frozen_ce','reuse_ce','reuse_lts']:
        w=np.zeros((NCTX,4)); paths=[]
        for rnd,starts in enumerate(training):
            actor=None if route=='frozen_ce' or rnd==0 else w
            new=[]
            for i,s in enumerate(starts):
                r,path=solve(s,actor,256)
                raw['collection'].append(dict(route=route,round=rnd+1,task=i,start=s,**r))
                if path: paths.append(path); new.append(path)
            w,stat=fit(paths,w,'lts' if route=='reuse_lts' else 'ce')
            snapshots[f'{route}_round_{rnd+1}']=w.copy()
            raw['rounds'].append(dict(route=route,round=rnd+1,new_solutions=len(new),**stat))
            print(json.dumps({'seed':seed,'route':route,'round':rnd+1,'new':len(new),'loss':stat.get('loss')}),flush=True)
        final[route]=w; raw['paths'][route]=paths
        raw['evaluations']+=evaluate(tasks,w,[256,1024],['learned','local','portfolio'],route)
    for actor in ['uniform','frozen_ce','reuse_ce','reuse_lts']:
        w=None if actor=='uniform' else final[actor]; paths=[]
        for i,s in enumerate(common):
            r,path=solve(s,w,256)
            raw['common_target'].append(dict(actor=actor,task=i,start=s,**r))
            if path: paths.append(path)
        student,stat=fit(paths,np.zeros((NCTX,4)),'ce')
        snapshots[f'common_student_{actor}']=student
        raw['rounds'].append(dict(route='common_student_'+actor,round=1,**stat))
        raw['paths']['common_student_'+actor]=paths
        raw['evaluations']+=evaluate(tasks,student,[1024],['learned'],'common_student_'+actor)
    np.savez_compressed(out/'weights.npz',**snapshots)
    payload=(json.dumps(raw,separators=(',',':'))+'\n').encode()
    (out/'records.json.gz').write_bytes(gzip.compress(payload,mtime=0))
    groups={}
    for r in raw['evaluations']:
        key='|'.join(str(r[k]) for k in ['tag','cohort','cap','mode'])
        groups.setdefault(key,[]).append(r)
    summary={k:{'n':len(rs),'solved':sum(r['solved'] for r in rs),
                'mean_pops':float(np.mean([r['pops'] for r in rs])),
                'cpu_s':sum(r['cpu_s'] for r in rs)} for k,rs in groups.items()}
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    paths=[Path(__file__),ROOT/'PROTOCOL.md',out/'tasks.json',out/'records.json.gz',out/'weights.npz',out/'summary.json']
    manifest={'seed':seed,'pilot':pilot,'numpy':np.__version__,'raw_sha256':hashlib.sha256(payload).hexdigest(),
              'files':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'seed':seed,'done':True}),flush=True)

def gradient_check():
    rng=np.random.default_rng(918); starts=sample_tasks(rng,4,2,4,{GOAL}); paths=[]
    for s in starts:
        _,p=solve(s,None,256); assert p; paths.append(p)
    data=dataset(paths); w=rng.normal(0,.05,NCTX*4)
    result={}
    for kind in ['ce','lts']:
        _,g=objective(w,data,kind); errors=[]
        for i in np.unique(data[0])[:12]*4:
            v=w.copy(); v[i]+=1e-5; f1=objective(v,data,kind)[0]
            v[i]-=2e-5; f0=objective(v,data,kind)[0]
            errors.append(abs((f1-f0)/2e-5-g[i]))
        assert max(errors)<1e-6
        result[kind]=max(errors)
    print(json.dumps({'gradient_max_absolute_error':result}))

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--seed',type=int,default=1)
    ap.add_argument('--pilot',action='store_true'); ap.add_argument('--check',action='store_true')
    a=ap.parse_args()
    gradient_check() if a.check else run(a.seed,a.pilot)
