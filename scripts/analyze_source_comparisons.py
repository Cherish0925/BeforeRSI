#!/usr/bin/env python3
"""Arithmetic and Pareto comparisons of published aggregates, without pseudo-replication."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/"research/source-comparisons.json").read_text())
r={row[0]:row[1:] for row in d["rrsi"]["rows"]}
full,unreg=r["rrsi"],r["unregularized"]
dominated=[name for name,v in r.items() if name!="rrsi" and
           full[1]>=v[1] and full[2]>=v[2] and full[3]<=v[3] and
           (full[1]>v[1] or full[2]>v[2] or full[3]<v[3])]
m={row[0]:row[1:] for row in d["mass"]["rows"]}
low,high,team=m["S_plus"],m["S_double_plus"],m["M_plus"]
interpolated=low[1]+(high[1]-low[1])*(team[0]-low[0])/(high[0]-low[0])
out={"status":"derived from reported aggregate points; no statistical significance inferred",
     "rrsi":{
       "full_minus_unregularized":{"evolve_pp":full[0]-unreg[0],
         "heldout_pp":full[1]-unreg[1],"ood_pp":full[2]-unreg[2],
         "million_tokens":full[3]-unreg[3]},
       "dominated_on_heldout_ood_and_cost":dominated,
       "maximum_evolve_weight_favoring_rrsi_without_cost_penalty":
          (full[2]-unreg[2])/((full[2]-unreg[2])-(full[0]-unreg[0]))},
     "mass":{"M_plus_minus_S_double_plus_score_pp":team[1]-high[1],
        "processed_token_reduction_fraction":1-team[0]/high[0],
        "single_agent_interpolated_score_at_M_plus_tokens":interpolated,
        "M_plus_above_interpolation_pp":team[1]-interpolated,
        "interpretation":"interpolation is not a measured matched-budget control"}}
(ROOT/"research/source-comparison-results.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
