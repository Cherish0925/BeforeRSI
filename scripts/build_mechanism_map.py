#!/usr/bin/env python3
"""Explicit per-work mechanism interpretations; no automatic literature claims."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
# Each entry supplies cause, condition/failure, and a separating counterfactual.
ROWS={
"good-1965":("Reuse of improved design operations can increase future design yield.","The feedback coefficient and resource costs are unspecified; positive feedback need not outrun difficulty.","Instantiate a design operation, pin its ancestor and compare continuation yield."),
"eurisko":("Retained heuristics alter which future hypotheses are generated and pursued.","Useful edits must remain expressible in the heuristic representation and interpretable by its runtime.","Freeze meta-heuristics while giving both arms the same discovered object-level rules."),
"godel-machine":("A proof can authorize a change by comparing future utility, including continued proof search.","The relevant claim must be provable in the axioms and discoverable within available resources.","Hold utility and axioms fixed; compare rewrite availability under different proof-search allocations."),
"maml":("Initialization shapes the effect of a later task-specific gradient update.","Source and target adaptation geometry must align; a good initial score alone is insufficient.","Compare initializations with matched initial task score under the same adaptation examples and steps."),
"alphago-zero":("Search improves behavior; self-play supplies consequences; policy/value training amortizes this computation.","Search quality, imitation error and the evolving opponent distribution jointly matter.","Match search calls and independently vary search-target quality and training fit."),
"automl-zero":("Program mutation and selection discover reusable learning procedures.","The primitive language, task distribution and evolutionary search determine accessible algorithms.","Change the primitive representation while fixing evaluation and total search budget."),
"stop":("An improver edits an executable improver, potentially retaining better candidate-generation operations.","The edit must improve future output distributions rather than only the currently edited target.","Run old and revised improver programs on identical external target copies."),
"promptbreeder":("Mutation prompts alter the proposal distribution used to evolve task prompts.","A better task prompt need not be a better mutation instruction on other targets.","Cross mutation-prompt versions with a fixed panel of task prompts."),
"funsearch":("A language prior proposes programs; executable scoring and an archive retain useful discoveries.","Evaluation must represent the intended property and the representation must expose useful programs.","Remove evaluator detail or archive diversity separately, matching generated candidates or compute."),
"spin":("Training contrasts generated responses with a reference data distribution and changes later response probabilities.","The reference data are an anchor; this is not unfiltered self-copying.","Replace reference responses by draws from the current model while holding the optimizer fixed."),
"self-rewarding-lm":("Self-generated preferences reweight the training target; learning changes both answer and judgment behavior.","Judge-answer dependence can retain systematic errors even when internal reward increases.","Pin the judge while updating the answerer, then reverse the intervention on the same candidates."),
"godel-agent":("Self-edited control logic changes accessible actions and the way feedback is used.","Arbitrary editability does not imply positive proposal or transfer quality.","Transplant the retained code change across unchanged target models and tasks."),
"adas":("A fixed designer conditions architecture proposals on an archive of previous designs and outcomes.","Target-agent gains can arise without any learned change to the designer.","Reset or shuffle archive information while retaining the same designer and search budget."),
"aflow":("Tree search allocates trials among workflow designs and composes available operators.","Search efficiency depends on branching, feedback and the expressiveness of workflow operators.","Hold operators fixed and replace tree allocation by equal-budget flat search."),
"sica":("Code and tool changes can reduce execution failures and improve useful work per budget.","A local repair may not improve successor production or transfer outside its failure mode.","Replay matched failure states through ancestor and successor tools before a common-target actor test."),
"dgm":("Reusable coding operations and retained alternative parents change subsequent proposal opportunities.","Archive cost and target difficulty can confound the benefit of successor reuse.","Cross pinned/refreshed actor with archive/last-parent policies on common starting targets."),
"gepa":("Trace-conditioned reflection localizes repairs; instance-specialist parents preserve alternative solutions.","Diagnostics must contain usable information, and specialist branches must justify their cost.","Return the same final score but remove diagnostic content; separately replace specialist selection by greedy selection."),
"agentbreeder":("Evolution changes coordination and communication among component agents.","Extra roles can add redundant errors and overhead rather than independent information.","Match total calls and change routing while holding component models and candidate counts fixed."),
"statistical-limits":("The reachable hypothesis class and feedback sample determine what generalization can be learned.","Its stated capacity and sampling assumptions cannot be discarded when applying the bound.","Vary reachable policy capacity and sample size within the theorem's task assumptions."),
"seal":("Self-edit generation is trained on utility after the learner consumes that edit.","Teaching value depends on learner state; old edit rewards can become stale.","Compare current-learner rewards with stale rewards for the same edit pool and adaptation budget."),
"hyperagents":("Editable meta code changes diagnosis, proposal and reuse, with task and meta roles sharing a program.","Transfer requires reusable improvement operations, not merely source-domain facts.","Transfer meta code to new task-agent initializations while preserving the target evaluation interface."),
"harness-updating-benefit":("Proposal competence and ability to execute the proposed computation are distinct causal factors.","Weak executors may not follow a harness; strong executors may have less recoverable headroom.","Cross creator and executor versions and measure adherence as well as final score."),
"sia":("Feedback directs updates to code or weights, changing execution and later learning data.","Different update surfaces may repair different bottlenecks and interfere on other tasks.","Apply matched model-only, harness-only and combined changes with crossed execution."),
"rhi":("Workflow specifications condition information flow and are revised from outcome comparisons.","A weak proposal distribution can bottleneck progress even under improved evaluation.","Replace proposer and evaluator separately with the executor fixed."),
"rethink-harness-eval":("Task-time search and persistent harness changes compete for the same resource budget.","A persistent update only amortizes if reused enough and still relevant.","Vary future reuse count and include development cost in the comparison."),
"co-harness":("Diagnosed runtime failures guide harness repairs that change subsequent model-training experience.","Schema, memory and middleware fixes differ from weight-level skill acquisition.","Preserve final rewards while hiding failure localization; compare training on repaired versus original traces."),
"helix":("Harness variants yield both task outcomes and contrasting records potentially useful for learning.","Portfolio coverage and record count do not measure post-update student improvement.","Train matched students from competing harness sources with decision inputs and task mixtures controlled."),
"hsi":("Meta-evolver changes can alter the distribution and allocation of future harness edits.","Meta-level code change may overfit the particular improvement problem.","Move only the meta-evolver to new target harnesses under matched budgets."),
"evoharness-rl":("Learned coordination changes when external state is written, retrieved and used.","External support can become redundant or harmful as policy competence changes.","Cross policy checkpoints with fixed external-state interfaces and measure redundant operations."),
"harness-tampering":("Changing the measurement path can increase observed score without improving intended utility.","Selection covariance with true utility can become nonpositive.","Recompute outcomes through an independently preserved measurement path."),
"harnessdev":("Creator search changes executable scaffolds consumed by a potentially different executor.","A creator's design can exceed the executor's interface-following capacity.","Run a creator-by-executor matrix at fixed runtime budgets."),
"rrsi":("Proposal and acceptance constraints favor transferable, affordable edits over source-score fitting.","Edit size alone is not the mechanism; overly restrictive search can also exclude useful changes.","Hold a candidate pool fixed to separate acceptance effects from changes to proposal distribution."),
"meta-harness":("Search changes which information is stored, retrieved and exposed to a fixed model.","Interface changes must preserve decision-relevant inputs and avoid costly irrelevant context.","Replay histories through competing context policies while matching model calls and task distribution."),
"aide2":("Search and memory rewrites improve the inner research agent under a fixed main outer proposer.","A stronger research target need not beat the original outer proposer at producing later agents.","Separate equal-call memory/search comparisons from the common-target outer-agent ignition test."),
"openrsi":("Execution-grounded training improves shared program-editing operators used by long-horizon search.","Operator competence and search allocation both contribute and can saturate separately.","Cross trained/base operators with fixed/changed search control on held-out research tasks."),
"mass":("Workflow-conditioned trajectories train shared weights used in solving, proposing and judging.","Training value depends on retained inputs and task alignment; correlated errors can persist.","Hold teacher quality approximately fixed while altering context preservation and source-task weighting."),
"rsi-anything":("Interaction and world-model predictions guide updates in an environment.","Simulated utility must predict external consequences; model error can steer search incorrectly.","Compare predicted and actual update rankings on interventions not used to fit the world model."),
"dream-rsi":("Replayed discovery trees train exploration choices before expensive online research.","Historical branching support and changed task dynamics limit off-policy transfer.","Evaluate exploration policies on new live branches with replay cost counted."),
"hgm":("Descendant-informed allocation estimates future branch value instead of current score alone.","Adaptive descendant sampling can bias the estimate; larger clades have unequal opportunity.","Predict later, unobserved branch outcomes under equal continuation budgets."),
"ace":("Persistent contextual lessons alter later decisions without changing weights.","Destructive compression or missing prerequisites can erase useful distinctions.","Compare incremental retention against full rewriting with the same new experiences and context cap."),
"alphaevolve":("Executable search can improve algorithms or infrastructure reused by later model development.","Feedback through infrastructure depends on real deployment and resource savings, not the label of the target.","Measure downstream work completed under the same physical resource budget before and after adoption."),
"opro":("The optimizer conditions proposals on a history of candidate-value pairs.","History is useful only insofar as it predicts better candidates within the new target problem.","Compare true, shuffled and reset histories with the same model and evaluation allowance."),
"learned-optimizer-2016":("A learned update rule exploits structure shared among training optimizees.","Meta-training distribution and recurrent state affect transfer and stability.","Hold optimizee initialization fixed and change optimizer weights on unseen loss geometries."),
"poet":("Environment generation and cross-environment transfer create alternative learning paths.","Transfer must connect useful states; environmental novelty alone is insufficient.","Remove cross-environment transfer while preserving total optimization work."),
"self-training-optimizer-2020":("A learned optimizer can execute the updates that train another optimizer.","Longer horizons can shift state distributions and stability beyond its training regime.","Cross optimizer versions, clipping rules and training horizons on common optimizer targets."),
"star":("Correctness-filtered rationales and answer-conditioned rationalization alter the learning target.","Hints can expose solutions but training must support inference without those hints.","Separate rationalization, filtering and per-task sample balancing at equal generation cost."),
"rest-em":("Reward-weighted sampling and likelihood projection alternate as an approximate EM procedure.","Approximate learning, rare success and changed task weights can prevent practical improvement.","Compare pooled filtering with per-task-balanced filtering and measure projection error."),
}
FULL={"dgm","hgm","hyperagents","aide2","gepa","seal","helix","mass","openrsi","rrsi","co-harness","harness-updating-benefit","star","rest-em"}


def main():
    corpus=json.loads((ROOT/"data/works.json").read_text())["works"]
    assert set(ROWS)=={w["id"] for w in corpus}
    rows=[]
    for w in corpus:
        mechanism,condition,intervention=ROWS[w["id"]]
        rows.append({"id":w["id"],"name":w["name"],"sources":w["sources"],
            "mechanism_interpretation":mechanism,"condition_or_failure":condition,
            "separating_intervention":intervention,
            "review_scope":"primary methods/results read this pass" if w["id"] in FULL else
            "prior corpus source check; mechanism interpretation, not a fresh full-method audit",
            "status":"conditional interpretation; no independent reproduction claimed"})
    (ROOT/"data/mechanisms.json").write_text(json.dumps({"updated":"2026-10-18",
        "scope":"every current corpus entry; explanatory hypotheses with explicit counterfactuals",
        "works":rows},indent=2,ensure_ascii=False)+"\n")
    lines=["# Per-work mechanism map","",
        "All 47 current corpus entries are included. These are our conditional mechanism",
        "interpretations and proposed interventions, not new empirical claims about each work.",
        "A star marks primary methods/results read in this pass; other rows retain the prior",
        "source-review boundary. Source reports and our derivations are separated in MECHANISMS.md.","",
        "| Work | Causal operation | Condition or failure | Separating intervention |",
        "|---|---|---|---|"]
    for r in rows:
        name=r["name"]+(" *" if r["id"] in FULL else "")
        lines.append(f"| [{name}]({r['sources'][0]['url']}) | {r['mechanism_interpretation']} | {r['condition_or_failure']} | {r['separating_intervention']} |")
    lines += ["","The next research question is which of these conditions is shared across tasks",
        "and predicts interventions, not how many entries can be assigned a label.",
        "See ../MECHANISMS.md for derivations and ../PROGRAM.md for the resulting route."]
    (ROOT/"research/mechanism-map.md").write_text("\n".join(lines)+"\n")


if __name__=="__main__":main()
