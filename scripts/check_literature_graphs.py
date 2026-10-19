#!/usr/bin/env python3
"""Check graph provenance, bibliographic preservation, and the exact offline payload."""
import json,re
from collections import Counter
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def read(p):return json.loads((R/p).read_text())
def check():
 a=read('data/literature-atlas.json');e=read('data/literature-editorial.json');g=read('data/knowledge-graph.json')
 works={w['id']:w for w in a['works']};ids=set(works)
 assert len(ids)==len(a['works'])
 assert ids=={w['id'] for w in read('data/works.json')['works']}=={w['id'] for w in e['works']}
 assert set(g)=={'schema_version','updated','scope','nodes','edges','route_views','work_bindings','field_views'}
 assert g['schema_version']=='5.1.0'
 ns={n['id']:n for n in g['nodes']};assert len(ns)==len(g['nodes'])
 assert {n['id'] for n in g['nodes'] if n['type']=='work'}==ids
 assert all(n['type'] in {'work','mechanism','institution','field_topic','field_subtopic','company','research_actor'} for n in ns.values())
 edgeids=set()
 for x in g['edges']:
  assert x['id'] not in edgeids;edgeids.add(x['id'])
  assert x['source'] in ns and x['target'] in ns and x['source']!=x['target']
  assert x['sources'] and all(s['url'].startswith('https://') and s['location'] for s in x['sources'])
  if x['kind']=='method_comparison':assert x['evidence']=='survey_comparison'
  elif x['kind'] in {'extends','uses','compares','discusses'}:assert x['evidence']=='source_explicit'
  elif x['kind']=='affiliation':assert ns[x['source']]['type']=='institution' and x['evidence']=='source_metadata'
  elif x['kind']=='mechanism':assert ns[x['source']]['type']=='mechanism' and x['evidence']=='survey_classification'
  elif x['kind'] in {'topic_contains','concept_relation'}:assert x['evidence']=='survey_structure'
  elif x['kind']=='addresses_topic':assert ns[x['source']]['type']=='work' and ns[x['target']]['type']=='field_topic' and x['evidence']=='survey_classification'
  elif x['kind']=='research_participation':assert ns[x['source']]['type']=='research_actor' and ns[x['target']]['type']=='work' and x['evidence']=='source_metadata'
  elif x['kind']=='company_work':assert ns[x['source']]['type']=='company' and ns[x['target']]['type']=='work' and x['evidence']=='source_metadata'
  elif x['kind']=='company_topic':assert ns[x['source']]['type']=='company' and ns[x['target']]['type']=='field_topic' and x['evidence']=='survey_classification'
  elif x['kind']=='company_direction':assert ns[x['source']]['type']=='company' and ns[x['target']]['type']=='field_topic' and x['evidence']=='declared_direction'
  else:raise AssertionError('Unknown relationship type: '+x['kind'])
 assert {b['work_id'] for b in g['work_bindings']}==ids
 for b in g['work_bindings']:assert set(b['node_ids'])<={n['id'] for n in ns.values() if n['type']=='mechanism'}
 counts=Counter(w['status'] for w in works.values())
 for status,n in counts.items():assert a['counts'][status]==n
 assert a['counts']['total']==len(ids)
 routeids={r['id'] for r in a['routes']};assert routeids=={'harness','model','hybrid'}
 routed=set()
 for r in a['routes']:
  ws=[w for w in works.values() if w['route']==r['id']];current={w['id'] for w in ws}
  assert not current&routed;routed|=current
  assert set(g['route_views'][r['id']])==current
  assert r['counts']['catalog']==len(ws)
  assert r['counts']['methods']==sum(w['status']=='methods' for w in ws)
  assert r['counts']['screened']==sum(w['status']=='screened' for w in ws)
  assert r['counts']['small']==sum(w['placement']=='small' for w in ws)
 assert a['counts']['routed']==len(routed)
 for w in works.values():
  assert w['sections'] and w['team'] and w['team_source'].startswith('https://')
  axes=[s['axis'] for s in w['sections']];assert len(axes)==len(set(axes)) and set(axes)<=set('ABCDEF')
  if w['status']=='methods':assert set(axes)==set('ABCDEF')
  assert all(s['text'].strip() and s['title'].strip() for s in w['sections'])
  if w['placement']=='small':
   assert w['scale_status']=='below' and w['models']
   trained=[m for m in w['models'] if not any(t in m.get('role','') for t in ['固定','冻结','非训练','不是训练'])]
   assert trained and all(m.get('total_b') and m['total_b']<27 for m in trained),w['id']
  assert w.get('review') and w['review']['sources'],w['id']
  assert w['review']['source_coverage'] in {'main_text_and_relevant_appendix','paper_sections_read','public_materials','abstract_only','unavailable'}
 assert a['relations']==e['relations'] and len(a['relations'])==a['counts']['relations']
 for rel in a['relations']:assert rel in g['edges']
 page=(R/'research/atlas/index.html').read_text()
 m=re.search(r'<script id="literature-data" type="application/json">(.*?)</script>',page,re.S)
 assert m and json.loads(m.group(1))==a
 assert '__LITERATURE_DATA__' not in page and '__DOMAIN_' not in page
 assert page==(R/'research/atlas/RSI_Field_Atlas_v5_1.html').read_text()
 assert '__INDUSTRY_' not in page and '__ACTOR_' not in page
 actors={x['id']:x for x in a['actors']['actors']}
 assert len(actors)==len(a['actors']['actors'])
 for w in works.values():
  assert set(w['actor_ids'])<=set(actors)
  assert len(w['actor_ids'])==len(set(w['actor_ids']))
  assert w['actor_types'] and all(t in {x['id'] for x in a['actors']['types']} for t in w['actor_types'])
 assert 'profile-apex' not in works['asi-bench']['actor_ids'] # Hosting is not authorship.
 assert works['rl-tango']['actor_ids'].count('mit')==1
 assert 'ibm' in works['rl-tango']['actor_ids']
 assert works['rl-tango']['cooperation']=='academic_industry'
 assert works['ace']['cooperation']=='academic_industry'
 industry=a['industry'];profiles=industry['companies']
 assert len({c['id'] for c in profiles})==len(profiles)==industry['counts']['total']
 assert {n['id'] for n in ns.values() if n['type']=='company'}=={'company-'+c['id'] for c in profiles}
 assert industry['counts']['linked_works']==len({x['work_id'] for c in profiles for x in c['work_links']})
 for c in profiles:
  assert c['sources'] and c['focus'] and c['boundary']
  assert all(x['work_id'] in ids and x['relationship'] in {'published','coauthored','hosted'} for x in c['work_links'])
  assert all('topic-'+tid in ns for tid in c['topic_ids'])
  assert set(c['primary_routes'])=={works[x['work_id']]['route'] for x in c['work_links'] if works[x['work_id']]['route'] in routeids}
  if c['status']=='direction':assert not c['work_links'] and c['directions']
  if c['status']=='adjacent':assert not c['work_links'] and not c['topic_ids'] and not c['directions']
 for rt in routeids:assert industry['route_counts'][rt]==sum(rt in c['primary_routes'] for c in profiles)
 for st in ['research','direction','adjacent']:assert industry['counts'][st]==sum(c['status']==st for c in profiles)
 source_industry=read('data/industry-landscape.json')
 assert all(industry[k]==v for k,v in source_industry.items())
 assert len({w['number'] for w in works.values()})==len(works)
 f=read('data/field-knowledge.json');assert f==a['field']
 assert len({n['id'] for rt in f['routes'] for n in rt['nodes']})==29
 assert sum(len(rt['edges']) for rt in f['routes'])==60
 for rt in f['routes']:
  tids={n['id'] for n in rt['nodes']}
  assert set(g['field_views'][rt['id']])=={'topic-'+tid for tid in tids}
  assert {w['id'] for w in works.values() if w['route']==rt['id']}<={q['work_id'] for q in rt['mappings']}
  for q in rt['mappings']:assert set(q['topic_ids'])<=tids and q['source_urls']
  for q in rt['edges']:assert {q['source'],q['target']}<=tids and q['source_urls']
  for n in rt['nodes']:assert n['subtopics'] and n['mechanisms'] and n['question'] and n['source_urls']
 assert not re.search(r'<script[^>]+src=|<link[^>]+href=',page)
 # Stable scope regressions: historical items stay outside route landscapes;
 # teacher or transferred-to model scale cannot admit a small trained policy.
 assert works['eurisko']['route']=='archive'
 for k in ['skillrl','harness-r1','harness-zero','rstar-math','skillos','socratic-swe']:assert works[k]['placement']=='small'
 assert works['webrl']['scale_status']=='eligible'
 assert any(m['total_b']==70 and '实际训练' in m.get('role','') for m in works['webrl']['models'])
 assert works['automated-alignment-researchers']['route']=='crosscut' and works['automated-alignment-researchers']['scale_status']=='not_applicable' # Fixed AI researchers optimize external target models.
 for wid,route in [('dream-rsi','harness'),('rewardharness','harness'),('seed-distillation','model'),('webevolver','model')]:assert works[wid]['route']==route
 assert works['memskill']['route']=='harness' and works['memskill']['scale_status']=='not_applicable'
 assert works['execution-grounded-research']['route']=='model'
 assert works['continual-harness']['route']=='hybrid' and works['continual-harness']['scale_status']=='unverified'
 print(f'PASS: {len(ids)} preserved works, {len(routed)} route positions, {len(a["relations"])} sourced/typed relations, exact offline data.')
if __name__=='__main__':check()
