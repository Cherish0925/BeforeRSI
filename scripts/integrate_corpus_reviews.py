#!/usr/bin/env python3
"""Integrate completed primary reviews, preserving stable bibliography IDs.

New graph entries require an explicit, human-readable curation binding. A core
decision never silently becomes an invented institution, graph topic or scale.
Unselected records remain in the complete corpus ledger.
"""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def read(name): return json.loads((ROOT/'data'/name).read_text())
def write(name, obj): (ROOT/'data'/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def prose(value):
    if value is None:return '未披露'
    if isinstance(value,list):return '；'.join(prose(x) for x in value) or '不适用或未披露'
    if isinstance(value,dict):return '；'.join(str(k)+'：'+prose(v) for k,v in value.items())
    return str(value)

def converted(r):
    m,x,c=r['mechanism'],r['experiment'],r['contribution']
    return {
        'source_coverage':'public_materials' if r['reading']['status']=='public_materials' else 'main_text_and_relevant_appendix',
        'sources':[{k:s[k] for k in ('url','location') if k in s} for s in r['reading']['sources']],
        'mechanism':{'changed':m.get('changed',''),'fixed':m.get('fixed',''),'feedback':m.get('feedback',''),'inheritance':m.get('inherited',''),'loop':m.get('loop','')},
        'results':{'setup':prose(x.get('task_split','')),'training_objects':prose(x.get('trained_models','')),'comparison':prose(x.get('baselines','')),'result':prose(x.get('main_result','')),'ablation':prose(x.get('ablation','')),'cost':prose(x.get('cost','')),'generalization':prose(x.get('generalization',''))},
        'contribution':{'bottleneck':c.get('problem',''),'insight':c.get('new_idea',''),'value':c.get('why_it_matters',''),'relation_to_rsi':r['selection']['reason'],'comparison':c.get('relative_to_prior_work','')},
        'scope_decision':'background' if r['route'] in {'background','outside'} else 'insufficient_disclosure' if r['selection']['decision'] in {'insufficient','blocked'} else 'enabling_method' if r['route']=='crosscut' else 'route_research',
        'scope_reason':r['selection']['reason'],
    }

def concise_sections(r):
    c,m,x=r['contribution'],r['mechanism'],r['experiment']
    return [
        {'axis':'A','title':'目标与问题','text':c['problem']},
        {'axis':'B','title':'关键思想与价值','text':c['new_idea']+' '+c['why_it_matters']},
        {'axis':'C','title':'系统与原理','text':m['changed']+'；'+m['fixed']+'。反馈：'+m['feedback']},
        {'axis':'D','title':'方法与比较','text':m['loop']+' '+c['relative_to_prior_work']},
        {'axis':'E','title':'实验与继承','text':prose(x['task_split'])+' '+m['inherited']},
        {'axis':'F','title':'结果、边界与迁移','text':prose(x['main_result'])+' '+prose(x['generalization'])+' '+c['important_limit']},
    ]

def main():
    corpus=read('corpus-review.json');bib=read('works.json');ed=read('literature-editorial.json');field=read('field-knowledge.json');scope=read('scope-review.json');primary=read('primary-reading.json')
    manifest=read('corpus-curation.json')['bindings'];bw={w['id']:w for w in bib['works']};ew={w['id']:w for w in ed['works']};sw={w['id']:w for w in scope['works']};pr={w['id']:w for w in primary['reviews']}
    method_ids={g['id'] for g in ed['groups']}|{'historical','background','cross-evaluation'}
    topic_ids={n['id'] for route in field['routes'] for n in route['nodes']}
    for entry_id,binding in manifest.items():
        assert set(binding.get('methods',[]))<=method_ids, ('Unknown method binding',entry_id,set(binding.get('methods',[]))-method_ids)
        assert set(binding.get('topic_ids',[]))<=topic_ids, ('Unknown topic binding',entry_id,set(binding.get('topic_ids',[]))-topic_ids)
    new_ids=[];updated=[];next_number=max(w.get('number',0) for w in ed['works'])+1
    legacy=read('research-atlas.json')['works'];next_number=max(next_number,max(w['number'] for w in legacy)+1)
    for e in corpus['entries']:
        r=e.get('review');binding=manifest.get(e['entry_id'],{})
        if not r or r['reading']['status']=='blocked':continue
        wid=e.get('work_id') or binding.get('work_id')
        if not wid:
            if r['selection']['decision']=='core':raise ValueError('Core work needs curation binding: '+e['entry_id'])
            continue
        e['work_id']=wid
        route={'background':'archive','outside':'archive'}.get(r['route'],r['route'])
        if wid not in ew:
            required={'short','cluster','methods','topic_ids','scope_kind','reported_depth','changed_objects'}
            assert required<=set(binding),(e['entry_id'],required-set(binding))
            b={'id':wid,'name':r['title'],'year':e['year'],'role':binding.get('role','empirical'),'reported_depth':binding['reported_depth'],'changed_objects':binding['changed_objects'],'evidence_status':'reported','audit_status':'primary_source_read','central_limit':'','sources':[]}
            w={'id':wid,'short':binding['short'],'number':next_number,'year':e['year'],'route':route,'cluster':binding['cluster'],'methods':binding['methods'],'scope_kind':binding['scope_kind'],'scope_label':{'direct':'自改进研究','enabler':'AI4AI 支撑','evaluation':'评测与反例','theory':'形式与理论'}.get(binding['scope_kind'],'相关研究'),'placement':'main','models':binding.get('models',[]),'training':{},'scale_status':'not_applicable' if route=='harness' else 'unverified'}
            next_number+=1;bw[wid]=b;ew[wid]=w;bib['works'].append(b);ed['works'].append(w);new_ids.append(wid)
        b,w=bw[wid],ew[wid];rv=converted(r);sources=rv['sources'];loc='；'.join(dict.fromkeys(s.get('location','') for s in sources if s.get('location')))
        if w['route']!=route:
            assert {'cluster','methods','topic_ids','scope_kind'}<=set(binding), ('Route change needs explicit binding',wid,w['route'],route)
        source_urls=list(dict.fromkeys([s['url'] for s in sources]+[s['url'] for s in b['sources']]))
        # Keep the established bibliography schema; the full training-object
        # field is retained in editorial/corpus reviews as well as the setup.
        evidence={k:v for k,v in rv['results'].items() if k!='training_objects'}
        evidence['setup']='训练对象：'+rv['results']['training_objects']+'。 '+evidence['setup']
        b.update(name=r['title'],audit_status='public_materials_read' if rv['source_coverage']=='public_materials' else 'primary_source_read',central_limit=r['contribution']['important_limit'],reading_scope=r['reading']['coverage'],mechanism_review=rv['mechanism'],evidence_review=evidence,contribution_review=rv['contribution'],scope_decision=rv['scope_decision'],source_locations=sources)
        for key in ['reported_depth','changed_objects','role']:
            if key in binding:b[key]=binding[key]
        b['sources']=[{'type':'repository' if 'github.com' in u else 'paper' if 'arxiv.org' in u or u.endswith('.pdf') else 'project_page', 'url':u} for u in source_urls]
        w.update(route=route,purpose=r['contribution']['problem'],summary=r['contribution']['new_idea'],sections=r.get('sections') or concise_sections(r),status='archive' if route=='archive' else 'methods',primary_url=sources[0]['url'],source_location=loc,reading_scope=r['reading']['coverage'],limitations=r['contribution']['important_limit'],resources=prose(r['experiment']['cost']),classification_note=r['selection']['reason'],review=rv,corpus_entry_id=e['entry_id'],corpus_selection=r['selection'])
        if r.get('institutions'):
            w.update(team=' / '.join(r['institutions']),team_source=sources[0]['url'],team_location=r.get('institution_source') or '原文作者署名')
        elif not w.get('team'):
            w.update(team='署名机构尚未整理',team_source=sources[0]['url'],team_location=r.get('institution_source') or '原文未能核准机构署名')
        if binding.get('models') is not None:w['models']=binding['models']
        for key in ['cluster','methods','placement','scale_status','parameter_note','scope_kind','scope_label']:
            if key in binding:w[key]=binding[key]
        if route=='harness':w.update(scale_status='not_applicable',placement='main')
        w['trained_max_total_b']=r['experiment'].get('max_trained_total_b');w['parameter_note']=r['experiment'].get('scale_basis') or w.get('parameter_note','')
        n=w['trained_max_total_b']
        if route in {'model','hybrid'}:
            w.update(scale_status=('eligible' if n>=27 else 'below') if n is not None else 'unverified',placement=('main' if n>=27 else 'small') if n is not None else 'main')
        elif route=='crosscut':w.update(placement='main',scale_status='not_applicable')
        elif route=='archive':w.update(placement='historical',scale_status='not_applicable')
        # Some papers disclose only part of their trained-model set. A known
        # 9B experiment cannot establish that every undisclosed target is <27B.
        for key in ['scale_status','placement']:
            if key in binding:w[key]=binding[key]
        sc={'id':wid,'name':w['short'],'year':e['year'],'scope':w.get('scope_kind','enabler'),'closure_assessment':rv['source_coverage'],'operation':rv['mechanism']['loop'],'boundary':w['classification_note']+' '+w['limitations'],'reading_scope':w['reading_scope'],'primary_source':w['primary_url'],'provenance':'2026-10-19 full-corpus primary reading and comparative selection'}
        sw[wid]=sc
        pr[wid]={**pr.get(wid,{}),'id':wid,'status':w['status'],'reading_scope':w['reading_scope'],'source_location':loc,'sections':w['sections'],'resources':w['resources'],'limitations':w['limitations'],'classification_note':w['classification_note'],'review':rv}
        if 'topic_ids' in binding:
            for fr in field['routes']:
                fr['mappings']=[x for x in fr['mappings'] if x['work_id']!=wid]
                topics=[t for t in binding['topic_ids'] if t in {n['id'] for n in fr['nodes']}]
                if topics:
                    fr['mappings'].append({'work_id':wid,'topic_ids':topics,'summary':w['summary'],'source_urls':[w['primary_url']],'source_location':loc})
        updated.append(wid)
    scope['works']=list(sw.values());primary['reviews']=list(pr.values())
    scope['counts']=dict(Counter(w['scope'] for w in scope['works']))
    # Earlier abstract-screening notes remain a dated history, never the current
    # decision after a primary review has been completed.
    reviewed_arxiv={e['arxiv_id']:e['review'] for e in corpus['entries'] if e.get('arxiv_id') and e.get('review')}
    for item in scope.get('deferred_or_excluded',[]):
        if item.get('arxiv_id') in reviewed_arxiv:
            r=reviewed_arxiv[item['arxiv_id']]
            item.update(status=r['selection']['decision'],reason=r['selection']['reason'],superseded_by_full_reading=True)
    for obj in [bib,ed,field,scope,primary]:obj['updated']='2026-10-19'
    for name,obj in [('works.json',bib),('literature-editorial.json',ed),('field-knowledge.json',field),('scope-review.json',scope),('primary-reading.json',primary),('corpus-review.json',corpus)]:write(name,obj)
    print(json.dumps({'updated':len(updated),'new':new_ids},ensure_ascii=False))

if __name__=='__main__':main()
