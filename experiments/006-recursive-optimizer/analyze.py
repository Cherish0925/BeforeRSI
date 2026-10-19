#!/usr/bin/env python3
"""Generate the result report and scientific figure from preserved observations."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import run as b

ROOT=Path(__file__).parent


def read(folder,name="summary.json"):
    return json.loads((ROOT/folder/name).read_text())


def fmt(v):
    lo,hi=v["bootstrap_95"]
    return f'{100*v["mean"]:+.3f} [{100*lo:+.3f}, {100*hi:+.3f}]'


def main():
    typed=read("results")
    obj=read("objective_results")
    order=read("order_results")
    pilot=read("pilot_results")
    raw=read("results","assessment.json")
    dev=read("results","development.json")
    snapshots=read("results","snapshots.json")
    gain=np.mean([x["initial_loss"]-x["selected_loss"] for x in dev
                  if x["mode"]=="recursive"])
    changed=sum(x["recursive"][-1][3:]!=x["recursive"][0][3:] for x in snapshots)
    calls=sum(x["accounting"]["objective_calls"] for x in (typed,obj,order,pilot))
    lines=[
        "# Executed results: recursive numerical optimizer",
        "",
        "**Result.** The tested self-reuse procedure did not establish a final-task",
        "or common-target improver advantage over the pinned ancestor. Training the",
        "improver objective directly also did not establish improved improver",
        "performance at the tested budget. Update order mattered for new instances",
        "of development families, but superiority across new families was not shown.",
        "",
        "These are measured results from a six-coordinate numerical optimizer,",
        "not LLM experiments or evidence that all RSI routes fail. The general",
        "mathematical result is in THEORY.md Section 9; this benchmark tests one",
        "specified implementation, with computed objective values rather than an",
        "assumed capability trajectory.",
        "",
        "## Recursive reuse, 32 independent lineages",
        "",
        f"Each feedback update improved the selected six-task score by {100*gain:.3f}",
        "percentage points on average. Each generation uses new feedback tasks, so",
        "these local gains cannot be added to obtain one common-task gain.",
        f"The final harness changed in {changed}/32 recursive lineages.",
        "",
        "| Comparison | New instances, percentage points [95% interval] | New families, percentage points [95% interval] |",
        "|---|---:|---:|",
        f'| Recursive endpoint minus initial | {fmt(typed["performance"]["recursive_id"])} | {fmt(typed["performance"]["recursive_ood"])} |',
        f'| Recursive endpoint minus frozen route | {fmt(typed["performance"]["recursive_minus_frozen_id"])} | {fmt(typed["performance"]["recursive_minus_frozen_ood"])} |',
        f'| Final actor minus initial actor, common-target gain | {fmt(typed["common_target_actor_advantage"]["id_generation_4"])} | {fmt(typed["common_target_actor_advantage"]["ood_generation_4"])} |',
        f'| Actor effect with one-step assessment | {fmt(typed["two_step_branch_advantage"]["id_horizon_1"])} | {fmt(typed["two_step_branch_advantage"]["ood_horizon_1"])} |',
        f'| Actor effect after common pinned continuation | {fmt(typed["two_step_branch_advantage"]["id_horizon_2"])} | {fmt(typed["two_step_branch_advantage"]["ood_horizon_2"])} |',
        "",
        "Visible selection gains did not transfer into a positive mean endpoint",
        "gain on new instances. This is evidence of selection/generalization",
        "failure in this procedure. It does not identify one unique cause or",
        "establish that the recursive and frozen routes are exactly equivalent.",
        "",
        "## Training objective, 16 independent lineages",
        "",
        "J-training and G-training consume exactly 7,296 primitive calls per",
        "outer candidate on the same pool of 24 task definitions. The outer",
        "proposal actor is pinned. G-training allocates these calls to producing",
        "and assessing descendants of two common targets; J-training allocates",
        "them to task executions. This isolates the change in training objective",
        "and computation allocation rather than granting G-training extra compute.",
        "",
        "| G-trained minus J-trained | New instances, pp [95% interval] | New families, pp [95% interval] |",
        "|---|---:|---:|",
        f'| Task score | {fmt(obj["task_score_id_G_minus_J"])} | {fmt(obj["task_score_ood_G_minus_J"])} |',
        f'| Common-target improvement gain | {fmt(obj["improvement_id_G_minus_J"])} | {fmt(obj["improvement_ood_G_minus_J"])} |',
        "",
        "Directly changing the objective to G did not establish the intended",
        "actor improvement and reduced task performance on new instances.",
        "A separate improver objective is therefore not sufficient in this",
        "search class and budget. The data do not distinguish limited search,",
        "noisy gain estimates and inadequate inductive bias as sole causes.",
        "",
        "## Update order, 32 independent lineages",
        "",
        "Both ordered routes and joint search use 34 configuration evaluations",
        "(6,528 primitive calls). M denotes the controller coefficients and H",
        "the three discrete search settings. These are update operations, not",
        "only static cross-pair execution.",
        "",
        "| Comparison | New instances, pp [95% interval] | New families, pp [95% interval] |",
        "|---|---:|---:|",
        f'| M then H minus H then M | {fmt(order["id_MH_minus_HM"])} | {fmt(order["ood_MH_minus_HM"])} |',
        f'| M then H minus joint | {fmt(order["id_MH_minus_joint"])} | {fmt(order["ood_MH_minus_joint"])} |',
        f'| H then M minus joint | {fmt(order["id_HM_minus_joint"])} | {fmt(order["ood_HM_minus_joint"])} |',
        "",
        "The observed order effect supports testing update-order dependence.",
        "It does not establish that alternation beats joint search or that one",
        "order is preferable on every task distribution.",
        "",
        "![Measured outcomes](results.svg)",
        "",
        "## Reproduction and scope",
        "",
        f"Four runs, including the retained pilot, executed {calls:,} primitive",
        "objective calls. Each result directory contains a source-hashed manifest,",
        "frozen configurations and summaries. Full candidate and task records are",
        "in [raw-results.tar.gz](raw-results.tar.gz);",
        "[raw-results.manifest.json](raw-results.manifest.json) records their hashes.",
        "The archive is lossless and was checked against every original file.",
        "",
        "Intervals are paired bootstrap intervals over independent lineages",
        "(5,000 resamples), not over correlated candidates or task rows. They are",
        "descriptive and not corrected for every reported comparison. The pilot",
        "led to an explicit discrete-edit correction; subsequent objective/order",
        "comparisons are declared follow-ups, not an untouched original study.",
        "Task families, dimensionality, search class and budgets remain limited.",
        "No energy measurements, neural-weight training, or frontier-model",
        "transfer result is claimed.",
        "",
        "The immediate research decision is to reject automatic promotion based",
        "only on feedback-task gain, one-step G, or recursive lineage. These runs",
        "supply no empirically justified universal update schedule. The remaining",
        "budget and attainable continuation outcomes must enter the comparison;",
        "the exact identity states how, without asserting those values are known.",
        "",
        "See [PROTOCOL.md](PROTOCOL.md) for interventions and resource accounting.",
        "Run analyze.py after the experiments, or after extracting the raw archive",
        "into this directory, to regenerate this report and figure.",
        ""
    ]
    (ROOT/"RESULTS.md").write_text("\n".join(lines))
    plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
    fig,axes=plt.subplots(1,3,figsize=(13.2,3.8),layout="constrained")
    colors={"recursive":"#146c94","frozen":"#777777"}
    for mode in ("recursive","frozen"):
        means,low,high=[],[],[]
        for g in range(5):
            vals=[r["mean"] for r in raw["performance"]
                  if r["mode"]==mode and r["generation"]==g and r["cohort"]=="id"]
            ci=b.interval(vals)
            means.append(100*ci["mean"]);low.append(100*ci["bootstrap_95"][0])
            high.append(100*ci["bootstrap_95"][1])
        axes[0].plot(range(5),means,"o-",label=mode,color=colors[mode])
        axes[0].fill_between(range(5),low,high,alpha=.12,color=colors[mode])
    axes[0].set(title="Task performance on new instances",xlabel="Generation",
                ylabel="Mean objective reduction (%)",xticks=range(5))
    axes[0].legend(frameon=False)
    for cohort,color in (("id","#146c94"),("ood","#b85c38")):
        vals=[typed["common_target_actor_advantage"][f"{cohort}_generation_{g}"] for g in range(5)]
        ys=np.array([100*v["mean"] for v in vals])
        lo=np.array([100*v["bootstrap_95"][0] for v in vals])
        hi=np.array([100*v["bootstrap_95"][1] for v in vals])
        axes[1].errorbar(np.arange(5)+(0 if cohort=="id" else .07),ys,
                        yerr=np.vstack([ys-lo,hi-ys]),fmt="o-",capsize=3,
                        label="new instances" if cohort=="id" else "new families",color=color)
    axes[1].axhline(0,color="#555",lw=.8)
    axes[1].set(title="Common-target improver change",xlabel="Actor generation",
                ylabel="Gain difference (percentage points)",xticks=range(5))
    axes[1].legend(frameon=False)
    labels=["M→H − H→M","M→H − joint","H→M − joint"]
    for cohort,color,offset in (("id","#146c94",-.08),("ood","#b85c38",.08)):
        vals=[order[f"{cohort}_{key}"] for key in ("MH_minus_HM","MH_minus_joint","HM_minus_joint")]
        means=np.array([100*v["mean"] for v in vals])
        lo=np.array([100*v["bootstrap_95"][0] for v in vals])
        hi=np.array([100*v["bootstrap_95"][1] for v in vals])
        axes[2].errorbar(means,np.arange(3)+offset,xerr=np.vstack([means-lo,hi-means]),
                        fmt="o",capsize=3,color=color)
    axes[2].axvline(0,color="#555",lw=.8)
    axes[2].set(title="Equal-call update schedules",yticks=range(3),yticklabels=labels,
                xlabel="Score difference (percentage points)")
    fig.savefig(ROOT/"results.svg")
    fig.savefig(ROOT/"results.png",dpi=160)
    plt.close(fig)
    print(json.dumps({"report":str(ROOT/"RESULTS.md"),"objective_calls":calls}))


if __name__=="__main__":
    main()
