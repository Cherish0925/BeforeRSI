#!/usr/bin/env python3
"""Equal-call comparison of model/harness update orders and joint search."""
from pathlib import Path
import hashlib
import json
import time
import numpy as np
import run as b


def main():
    begin=time.monotonic()
    out=Path(__file__).parent/"order_results"
    out.mkdir(exist_ok=True)
    cfg={"seed":20261021,"lineages":32,"task_budget":32,"meta_budget":17,
         "dimension":6,"feedback_each":2,"assessment_each":4}
    (out/"manifest.json").write_text(json.dumps({
        "config":cfg,"source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "optimizer_source_sha256":hashlib.sha256(Path(b.__file__).read_bytes()).hexdigest(),
        "equal_budget_paths":["MH","HM","joint"],"meta_evaluations_per_path":34
    },indent=2)+"\n")
    development,snapshots=[],[]
    for line in range(cfg["lineages"]):
        feedback=b.tasks(b.TRAIN_FAMILIES,2,6,b.seed(cfg["seed"],10,line))

        def update(target,part):
            indices=np.arange(3) if part=="M" else np.arange(3,6)
            log=[]
            def objective(partial):
                candidate=target.copy()
                candidate[indices]=partial
                b.COUNTS["meta_evaluations"]+=1
                return float(1-b.score(candidate,feedback,32).mean())
            partial,_,_=b.optimize(
                objective,target[indices],target,17,
                b.seed(cfg["seed"],11,line,part=="H"),log,
                binary_tail=0 if part=="M" else 3)
            child=target.copy()
            child[indices]=partial
            development.append({"lineage":line,"part":part,"target":target.tolist(),
                                "child":child.tolist(),"candidates":log})
            return child

        m=update(b.BASE,"M")
        h=update(b.BASE,"H")
        mh=update(m,"H")
        hm=update(h,"M")
        joint_cfg={**cfg,"meta_budget":34}
        joint,audit=b.improve(b.BASE,b.BASE,feedback,joint_cfg,
                             b.seed(cfg["seed"],12,line),audit=True)
        development.append({"lineage":line,"part":"joint","target":b.BASE.tolist(),
                            "child":joint.tolist(),"candidates":audit["candidates"]})
        snapshots.append({"initial":b.BASE.tolist(),"M":m.tolist(),"H":h.tolist(),
                          "MH":mh.tolist(),"HM":hm.tolist(),"joint":joint.tolist()})
    (out/"development.json").write_text(json.dumps(development,separators=(",",":"))+"\n")
    (out/"snapshots.json").write_text(json.dumps(snapshots,indent=2)+"\n")
    raw=[]
    for line,configs in enumerate(snapshots):
        for cohort,families in (("id",b.TRAIN_FAMILIES),("ood",b.OOD_FAMILIES)):
            ts=b.tasks(families,4,6,b.seed(cfg["seed"],20,line,cohort=="ood"))
            for name,config in configs.items():
                values=b.score(np.asarray(config),ts,32)
                raw.append({"lineage":line,"cohort":cohort,"schedule":name,
                            "mean":float(values.mean()),"scores":values.tolist()})
    summary={}
    for cohort in ("id","ood"):
        values={name:[] for name in ("MH_minus_HM","MH_minus_joint","HM_minus_joint",
                                     "M_to_H","H_to_M")}
        for line in range(cfg["lineages"]):
            cells={r["schedule"]:r["mean"] for r in raw
                   if r["lineage"]==line and r["cohort"]==cohort}
            a=cells["MH"]-cells["M"]-cells["H"]+cells["initial"]
            c=cells["HM"]-cells["M"]-cells["H"]+cells["initial"]
            assert abs((a-c)-(cells["MH"]-cells["HM"]))<1e-12
            values["M_to_H"].append(a);values["H_to_M"].append(c)
            for name,new,old in [("MH_minus_HM","MH","HM"),
                                 ("MH_minus_joint","MH","joint"),
                                 ("HM_minus_joint","HM","joint")]:
                values[name].append(cells[new]-cells[old])
        for key,v in values.items():summary[cohort+"_"+key]=b.interval(v)
    summary["accounting"]={**b.COUNTS,"elapsed_seconds":time.monotonic()-begin}
    (out/"assessment.json").write_text(json.dumps(raw,separators=(",",":"))+"\n")
    (out/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")
    print(json.dumps(summary),flush=True)


if __name__=="__main__":
    main()
