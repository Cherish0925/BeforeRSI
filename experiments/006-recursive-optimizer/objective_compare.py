#!/usr/bin/env python3
"""Matched-call comparison: train task score J or common-target gain G."""
from dataclasses import replace
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time

import numpy as np
import run as b


def main():
    started=time.monotonic()
    out=Path(__file__).parent/"objective_results"
    out.mkdir(exist_ok=True)
    cfg={"seed":20261020,"lineages":16,"generations":3,"outer_budget":9,
         "meta_budget":17,"task_budget":32,"dimension":6,
         "feedback_each":2,"assessment_each":4,"common_problems":4}
    manifest={"config":cfg,"started_utc":datetime.now(timezone.utc).isoformat(),
              "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "optimizer_source_sha256":hashlib.sha256(Path(b.__file__).read_bytes()).hexdigest(),
              "primitive_calls_per_candidate":7296,
              "outer_actor":"fixed initial optimizer",
              "purpose":"compare training objectives under matched primitive calls"}
    (out/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    snapshots,trace=[],[]
    for line in range(cfg["lineages"]):
        states={"J":b.BASE.copy(),"G":b.BASE.copy()}
        paths={k:[v.copy()] for k,v in states.items()}
        for generation in range(1,cfg["generations"]+1):
            feedback=[b.tasks(b.TRAIN_FAMILIES,2,6,b.seed(cfg["seed"],10,line,generation,k))
                      for k in range(2)]
            checks=[b.tasks(b.TRAIN_FAMILIES,2,6,b.seed(cfg["seed"],11,line,generation,k))
                    for k in range(2)]
            rng=np.random.default_rng(b.seed(cfg["seed"],12,line,generation))
            targets=[]
            for k in range(2):
                x=np.clip(b.BASE+rng.normal(0,.45,6),-1,1)
                x[-3:]=np.where(rng.random(3)<.5,-1.,1.)
                targets.append(x)
            pool=feedback[0]+feedback[1]+checks[0]+checks[1]
            # Same 24 task definitions available to both objectives.
            # J spends its budget on repeated task executions, G on descendants.
            task_repeats=[replace(pool[k%len(pool)],
                                  search_seed=b.seed(cfg["seed"],13,line,generation,k))
                          for k in range(228)]

            def objective(candidate,kind):
                before=b.COUNTS["objective_calls"]
                if kind=="J":
                    value=-float(b.score(candidate,task_repeats,32).mean())
                else:
                    gains=[]
                    for k in range(2):
                        child,_=b.improve(targets[k],candidate,feedback[k],cfg,
                                          b.seed(cfg["seed"],14,line,generation,k))
                        gains.append(float((b.score(child,checks[k],32)
                                            -b.score(targets[k],checks[k],32)).mean()))
                    value=-float(np.mean(gains))
                assert b.COUNTS["objective_calls"]-before==7296
                return value

            for kind in ("J","G"):
                log=[]
                child,loss,initial=b.optimize(
                    lambda x:objective(x,kind),states[kind],b.BASE,cfg["outer_budget"],
                    b.seed(cfg["seed"],15,line,generation),log,binary_tail=3)
                trace.append({"lineage":line,"generation":generation,"objective":kind,
                              "target":states[kind].tolist(),"child":child.tolist(),
                              "initial_loss":initial,"selected_loss":loss,"candidates":log})
                states[kind]=child
                paths[kind].append(child.copy())
        snapshots.append(paths)
        print(json.dumps({"stage":"objective_training","lineage":line+1}),flush=True)
    serial=[{k:[x.tolist() for x in path] for k,path in row.items()} for row in snapshots]
    (out/"snapshots.json").write_text(json.dumps(serial,indent=2)+"\n")
    (out/"development.json").write_text(json.dumps(trace,separators=(",",":"))+"\n")
    digest=hashlib.sha256((out/"snapshots.json").read_bytes()).hexdigest()
    performance,improvement=[],[]
    for line,paths in enumerate(snapshots):
        actors={"initial":b.BASE,"J":paths["J"][-1],"G":paths["G"][-1]}
        for cohort,families in (("id",b.TRAIN_FAMILIES),("ood",b.OOD_FAMILIES)):
            ts=b.tasks(families,4,6,b.seed(cfg["seed"],20,line,cohort=="ood"))
            for name,actor in actors.items():
                vals=b.score(actor,ts,32)
                performance.append({"lineage":line,"actor":name,"cohort":cohort,
                                    "scores":vals.tolist(),"mean":float(vals.mean())})
        for problem in range(4):
            rng=np.random.default_rng(b.seed(cfg["seed"],30,line,problem))
            target=np.clip(b.BASE+rng.normal(0,.45,6),-1,1)
            target[-3:]=np.where(rng.random(3)<.5,-1.,1.)
            feedback=b.tasks(b.TRAIN_FAMILIES,2,6,b.seed(cfg["seed"],31,line,problem))
            for name,actor in actors.items():
                child,audit=b.improve(target,actor,feedback,cfg,
                                     b.seed(cfg["seed"],32,line,problem),audit=True)
                for cohort,families in (("id",b.TRAIN_FAMILIES),("ood",b.OOD_FAMILIES)):
                    ts=b.tasks(families,4,6,b.seed(cfg["seed"],33,line,problem,cohort=="ood"))
                    gains=b.score(child,ts,32)-b.score(target,ts,32)
                    improvement.append({"lineage":line,"problem":problem,"actor":name,
                                        "cohort":cohort,"target":target.tolist(),
                                        "child":child.tolist(),"mean":float(gains.mean()),
                                        "gains":gains.tolist(),"candidates":audit["candidates"]})
        print(json.dumps({"stage":"objective_assessment","lineage":line+1}),flush=True)
    assert hashlib.sha256((out/"snapshots.json").read_bytes()).hexdigest()==digest
    summary={}
    for metric,rows in (("task_score",performance),("improvement",improvement)):
        for cohort in ("id","ood"):
            for new,old in (("J","initial"),("G","initial"),("G","J")):
                effects=[]
                for line in range(cfg["lineages"]):
                    subset=[r for r in rows if r["lineage"]==line and r["cohort"]==cohort]
                    effects.append(np.mean([r["mean"] for r in subset if r["actor"]==new])
                                   -np.mean([r["mean"] for r in subset if r["actor"]==old]))
                summary[f"{metric}_{cohort}_{new}_minus_{old}"]=b.interval(effects)
    summary["accounting"]={**b.COUNTS,"elapsed_seconds":time.monotonic()-started,
                           "snapshot_sha256":digest}
    (out/"assessment.json").write_text(json.dumps(
        {"performance":performance,"improvement":improvement},separators=(",",":"))+"\n")
    (out/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")
    print(json.dumps({"finished":True,"summary":summary}),flush=True)


if __name__=="__main__":
    main()
