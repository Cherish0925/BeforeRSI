#!/usr/bin/env python3
"""Summarize paired independent lineages; keep pilot and follow-up separate."""
import gzip,hashlib,io,json,platform,tarfile
from pathlib import Path
import numpy as np
import scipy

ROOT=Path(__file__).resolve().parent
SEEDS=[18,29,43,71]

def loadgz(p): return json.loads(gzip.decompress(p.read_bytes()))
def groups(rows):
    out={}
    for r in rows:
        key='|'.join(str(r[x]) for x in ['tag','cap','mode'])
        out.setdefault(key,[]).append(r)
    return {k:{'n':len(v),'solved':sum(r['solved'] for r in v),
               'rate':float(np.mean([r['solved'] for r in v])),
               'mean_pops':float(np.mean([r['pops'] for r in v])),
               'cpu_s':sum(r['cpu_s'] for r in v)} for k,v in out.items()}

def main():
    allrows={'initial':[],'uniform_states':[]}; perseed={}; accounting={}
    checked=0
    for base in [ROOT/'pilot'/'1']+[ROOT/p/str(s) for p in ['runs','followup'] for s in SEEDS]:
        man=json.loads((base/'manifest.json').read_text())
        for path,sha in man['files'].items():
            assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==sha,(base,path)
            checked+=1
        raw=gzip.decompress((base/'records.json.gz').read_bytes())
        assert hashlib.sha256(raw).hexdigest()==man['raw_sha256']
    for seed in SEEDS:
        r=loadgz(ROOT/'runs'/str(seed)/'records.json.gz')
        f=loadgz(ROOT/'followup'/str(seed)/'records.json.gz')
        for cohort,rows in [('initial',r['evaluations']),('uniform_states',f)]:
            allrows[cohort]+=rows; perseed.setdefault(cohort,{})[seed]=groups(rows)
        costs={}
        for route in ['frozen_ce','reuse_ce','reuse_lts']:
            collect=[x for x in r['collection'] if x['route']==route]
            fit=[x for x in r['rounds'] if x['route']==route]
            costs[route]={'collection_pops':sum(x['pops'] for x in collect),
                'collection_policy_calls':sum(x['policy_calls'] for x in collect),
                'collection_cpu_s':sum(x['cpu_s'] for x in collect),
                'fit_cpu_s':sum(x['cpu_s'] for x in fit),
                'fit_token_gradient_evaluations':sum(x.get('token_gradient_evaluations',0) for x in fit),
                'final_solved_paths':fit[-1]['paths'],
                'max_nfev':max(x['nfev'] for x in fit)}
        costs['common_target_collection']={a:{'solved':sum(x['solved'] for x in r['common_target'] if x['actor']==a),
            'pops':sum(x['pops'] for x in r['common_target'] if x['actor']==a),
            'cpu_s':sum(x['cpu_s'] for x in r['common_target'] if x['actor']==a)}
            for a in ['uniform','frozen_ce','reuse_ce','reuse_lts']}
        costs['common_target_fit']={x['route']:{k:x[k] for k in ['paths','tokens','cpu_s','nfev']}
            for x in r['rounds'] if x['route'].startswith('common_student_')}
        costs['external_assessment_cpu_s']=sum(x['cpu_s'] for x in r['evaluations']+f)
        accounting[seed]=costs
        assert all(x['nfev']<=160 for x in r['rounds'])
        # A concrete cross-cap implication of the complete-search schedule.
        for rows in [r['evaluations'],f]:
            lookup={(x['tag'],x['cohort'],x['task'],x['cap'],x['mode']):x for x in rows}
            for x in rows:
                if x['tag']=='uniform' and x['cap']==256 and x['solved']:
                    for route in ['frozen_ce','reuse_ce','reuse_lts']:
                        assert lookup[(route,x['cohort'],x['task'],1024,'portfolio')]['solved']
    agg={k:groups(v) for k,v in allrows.items()}
    comparisons={}
    pairs=[('reuse_ce','frozen_ce'),('reuse_lts','reuse_ce'),
           ('common_student_reuse_ce','common_student_frozen_ce'),
           ('common_student_reuse_lts','common_student_frozen_ce')]
    for cohort in agg:
        for a,b in pairs:
            for cap in [64,256,1024]:
                ka=f'{a}|{cap}|learned';kb=f'{b}|{cap}|learned'
                if ka not in agg[cohort] or kb not in agg[cohort]: continue
                diffs=[100*(perseed[cohort][s][ka]['rate']-perseed[cohort][s][kb]['rate']) for s in SEEDS]
                comparisons[f'{cohort}|{cap}|{a}-{b}']={'mean_pp':float(np.mean(diffs)),
                    'paired_seed_pp':diffs,'range_pp':[min(diffs),max(diffs)]}
    amortization={}
    for cohort in agg:
        for cap in [256,1024]:
            values={}
            for route in ['frozen_ce','reuse_ce','reuse_lts']:
                build=sum(accounting[s][route]['collection_cpu_s']+accounting[s][route]['fit_cpu_s'] for s in SEEDS)
                deployment=agg[cohort][f'{route}|{cap}|learned']
                values[route]={'build_cpu_s_total':build,'deployment_cpu_s_total':deployment['cpu_s'],
                    'build_plus_this_deployment_cpu_s':build+deployment['cpu_s'],
                    'solved':deployment['solved'],'tasks':deployment['n']}
            amortization[f'{cohort}|{cap}']=values
    summary={'scope':'four paired lineages; synthetic puzzle environment with actual learned parameters and executed search',
             'seeds':SEEDS,'aggregate':agg,'comparisons':comparisons,'resource_accounting':accounting,
             'one_build_one_deployment_cohort':amortization,
             'checks':{'source_artifact_hashes':checked,'schedule_implications':'passed'},
             'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,
                            'system':platform.platform()}}
    (ROOT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    lines=['# Learned-search results','',
        'Four independent lineages (18, 29, 43, 71), with paired task sets and zero-initialized',
        '2,592-parameter context policies. All training solution paths were found by executed',
        'search. Pilot seed 1 is excluded. This is a small sliding-tile environment, not an LLM',
        'experiment or a reproduction of published 24-tile-puzzle results.','',
        '![Held-out search and common-target learner results](results.png)','',
        'Reused collection substantially improves both the final solver and the downstream',
        'learner in this setting. The effort objective has a visible advantage at smaller',
        'budgets on the uniform-state follow-up, while the original 1,024-pop test is near',
        'a ceiling. The complete-search portfolio outperforms local action mixing here, but',
        'usually gives up performance relative to the learned search alone: preserving an',
        'anchor costs computation. These results support this bounded loop, not indefinite growth.','',
        '## Original random-walk cohorts','',
        '| Route | Harness | Solved / 768 at 256 pops | Solved / 768 at 1,024 pops | Mean capped pops at 1,024 |',
        '|---|---|---:|---:|---:|']
    for tag in ['uniform','frozen_ce','reuse_ce','reuse_lts']:
        for mode in (['uniform'] if tag=='uniform' else ['learned','local','portfolio']):
            v=agg['initial'][f'{tag}|1024|{mode}'];v0=agg['initial'][f'{tag}|256|{mode}']
            lines.append(f"| {tag} | {mode} | {v0['solved']} | {v['solved']} | {v['mean_pops']:.2f} |")
    lines+=['','## New uniform-state distribution','',
        'The FOLLOWUP protocol was written after the original ceiling effect, before drawing',
        '512 new uniformly sampled solvable starts. No weights or algorithm settings changed.',
        'This is a harder sampling distribution in the same domain, not a new task domain.','',
        '| Route | Harness | Solved / 512 at 64 | At 256 | At 1,024 | Mean capped pops at 256 |',
        '|---|---|---:|---:|---:|---:|']
    for tag in ['uniform','frozen_ce','reuse_ce','reuse_lts']:
        for mode in (['uniform'] if tag=='uniform' else ['learned','local','portfolio']):
            vals=[agg['uniform_states'][f'{tag}|{cap}|{mode}'] for cap in [64,256,1024]]
            lines.append(f"| {tag} | {mode} | {vals[0]['solved']} | {vals[1]['solved']} | {vals[2]['solved']} | {vals[1]['mean_pops']:.2f} |")
    lines+=['','## Common-target improvement operation','',
        'Each final actor collected solution paths on the same 96 new starts per lineage.',
        'Identical fresh zero-weight CE learners then consumed the respective datasets.',
        'All students used learned-only Levin search. This tests the value of the actor as',
        'a data-producing improver, conditional on this learner, task panel and resource convention.','',
        '| Data-producing actor | Original starts: solved / 768 at 1,024 | Uniform starts: / 512 at 64 | At 256 | At 1,024 |',
        '|---|---:|---:|---:|---:|']
    for actor in ['uniform','frozen_ce','reuse_ce','reuse_lts']:
        tag='common_student_'+actor
        vals=[agg['uniform_states'][f'{tag}|{cap}|learned']['solved'] for cap in [64,256,1024]]
        v=agg['initial'][f'{tag}|1024|learned']['solved']
        lines.append(f'| {actor} | {v} | {vals[0]} | {vals[1]} | {vals[2]} |')
    lines+=['','## Paired lineage differences','',
        'Differences below are percentage points. The four seed values, rather than thousands',
        'of correlated training steps or individual task outcomes, are the replication units.',
        'No significance or precise population interval is inferred from four lineages.','',
        '| Cohort / cap | Comparison | Mean pp | Four seed differences |','|---|---|---:|---|']
    for key,v in comparisons.items():
        cohort,cap,pair=key.split('|')
        lines.append(f"| {cohort} / {cap} | {pair} | {v['mean_pp']:+.3f} | "+', '.join(f'{x:+.3f}' for x in v['paired_seed_pp'])+' |')
    lines+=['','## Cost of producing the learned solvers','',
        'Totals across four lineages. Shared per-task pop caps and optimization ceilings do',
        'not equalize FLOPs, token gradients, or wall time. CPU seconds are process CPU time',
        'on this runtime; no accelerator or energy measurements were made. Assessment is',
        'external to training and is recorded separately in summary.json.','',
        '| Route | Collection pops | Collection CPU s | Fit CPU s | Token-gradient evaluations | Retained paths |',
        '|---|---:|---:|---:|---:|---:|']
    for route in ['frozen_ce','reuse_ce','reuse_lts']:
        cs=[accounting[s][route] for s in SEEDS]
        sums={k:sum(c[k] for c in cs) for k in cs[0]}
        lines.append(f"| {route} | {sums['collection_pops']} | {sums['collection_cpu_s']:.3f} | {sums['fit_cpu_s']:.3f} | {sums['fit_token_gradient_evaluations']} | {sums['final_solved_paths']} |")
    lines+=['','## Build plus deployment cost','',
        'For each predeclared route, add its one build to one deployment of the stated cohort',
        'at the stated cap. This does not charge the route for the research comparison of other',
        'routes, other cap settings, or external common-target assessment. A selector that tried',
        'all of them would have to pay those additional costs. Values are measured process CPU',
        'seconds summed across four lineages, not predictions for other hardware.','',
        '| Cohort / cap | Route | Build + deployment CPU s | Solved / tasks |',
        '|---|---|---:|---:|']
    for case,vals in amortization.items():
        for route,v in vals.items():
            lines.append(f"| {case.replace('|',' / ')} | {route} | {v['build_plus_this_deployment_cpu_s']:.3f} | {v['solved']} / {v['tasks']} |")
    lines+=['','## Interpretation boundaries and reproduction','',
        '- Reuse versus frozen collection changes future training data through the learned policy.',
        '  It does not isolate data quantity from data quality; both are parts of this operation.',
        '- Common targets control the downstream learner initialization and update rule, but',
        '  the actor policy has a different evaluation cost and produces different dataset sizes.',
        '- The frontier and acceptance test are fixed; this is not self-rewriting code or open-ended growth.',
        '- Whole-search preservation has a worst-case scheduling guarantee, not guaranteed superiority',
        '  over the best individual search at the same cap. Its guarantee is in pops.',
        '- The search-bound objective is established prior work. Its fit value alone does not',
        '  certify transfer; the report retains every CE/LTS comparison and both harness controls.','',
        'Run `python run.py --check`, then `python run.py --seed SEED` for each declared seed,',
        'then `python followup.py --seed SEED`, and `python analyze.py`. Set',
        '`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1` for comparable CPU accounting.',
        'The lossless [artifacts.tar.gz](artifacts.tar.gz) contains task starts, full training',
        'paths, per-task outcomes, parameters and source-hashed manifests for the pilot, original',
        'runs and follow-up. Extract it into this directory to inspect or re-analyze the stored runs.',
        'The original two analytic gradient checks had maximum absolute error below 2e-11.','']
    (ROOT/'RESULTS.md').write_text('\n'.join(lines))
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    fig,axes=plt.subplots(1,2,figsize=(11,4.5),sharey=True)
    colors={'frozen_ce':'#404b5a','reuse_ce':'#b18430','reuse_lts':'#207e7a'}
    labels={'frozen_ce':'Frozen collector + CE','reuse_ce':'Reused collector + CE','reuse_lts':'Reused collector + effort loss'}
    for ax,prefix,title in zip(axes,['','common_student_'],['Final solver','Fresh learner trained by the final actor']):
        for route in colors:
            caps=[64,256,1024];tag=prefix+route
            ys=[100*agg['uniform_states'][f'{tag}|{c}|learned']['rate'] for c in caps]
            lo=[min(100*perseed['uniform_states'][s][f'{tag}|{c}|learned']['rate'] for s in SEEDS) for c in caps]
            hi=[max(100*perseed['uniform_states'][s][f'{tag}|{c}|learned']['rate'] for s in SEEDS) for c in caps]
            ax.plot(caps,ys,'o-',color=colors[route],label=labels[route],lw=2)
            ax.fill_between(caps,lo,hi,color=colors[route],alpha=.10,linewidth=0)
        ax.set_xscale('log',base=2);ax.set_xticks(caps,labels=list(map(str,caps)))
        ax.set_xlabel('Search pop cap');ax.set_title(title,loc='left',fontweight='bold')
        ax.set_ylim(-2,103);ax.grid(axis='y',alpha=.18)
    axes[0].set_ylabel('Held-out starts solved (%)')
    fig.suptitle('Learning to search, then learning to produce useful training paths',x=.06,ha='left',fontweight='bold',fontsize=14)
    fig.legend(*axes[0].get_legend_handles_labels(),loc='lower center',ncol=3,frameon=False,bbox_to_anchor=(.5,.025))
    fig.text(.06,.005,'Uniform solvable 8-puzzle states; 4 lineages, 512 starts. Bands show seed ranges, not confidence intervals.',fontsize=9,color='#55606b')
    fig.tight_layout(rect=[0,.13,1,.91]);fig.savefig(ROOT/'results.png',dpi=180);plt.close(fig)
    # A deterministic lossless bundle avoids duplicating thousands of task records in the tree.
    stream=io.BytesIO()
    with tarfile.open(fileobj=stream,mode='w') as tf:
        for parent in ['pilot','runs','followup']:
            for p in sorted((ROOT/parent).rglob('*')):
                if not p.is_file() or p.suffix=='.log':continue
                content=p.read_bytes();info=tarfile.TarInfo(str(p.relative_to(ROOT)))
                info.size=len(content);info.mtime=0;info.mode=0o644
                tf.addfile(info,io.BytesIO(content))
    (ROOT/'artifacts.tar.gz').write_bytes(gzip.compress(stream.getvalue(),mtime=0))
    manifest={'artifact_sha256':hashlib.sha256((ROOT/'artifacts.tar.gz').read_bytes()).hexdigest(),
        'bundle_bytes':(ROOT/'artifacts.tar.gz').stat().st_size,
        'environment':summary['environment'],
        'sources':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
                   [ROOT/'run.py',ROOT/'followup.py',Path(__file__),ROOT/'PROTOCOL.md',ROOT/'FOLLOWUP.md']}}
    (ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'comparisons':comparisons,'bundle_bytes':manifest['bundle_bytes']},indent=2))

if __name__=='__main__':main()
