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
 assert set(g)=={'schema_version','updated','scope','nodes','edges','route_views','work_bindings'}
 assert g['schema_version']=='4.0.0'
 ns={n['id']:n for n in g['nodes']};assert len(ns)==len(g['nodes'])
 assert {n['id'] for n in g['nodes'] if n['type']=='work'}==ids
 assert all(n['type'] in {'work','mechanism','institution'} for n in ns.values())
 edgeids=set()
 for x in g['edges']:
  assert x['id'] not in edgeids;edgeids.add(x['id'])
  assert x['source'] in ns and x['target'] in ns and x['source']!=x['target']
  assert x['sources'] and all(s['url'].startswith('https://') and s['location'] for s in x['sources'])
  if x['kind']=='method_comparison':assert x['evidence']=='survey_comparison'
  elif x['kind'] in {'extends','uses','compares','discusses'}:assert x['evidence']=='source_explicit'
  elif x['kind']=='affiliation':assert ns[x['source']]['type']=='institution' and x['evidence']=='source_metadata'
  elif x['kind']=='mechanism':assert ns[x['source']]['type']=='mechanism' and x['evidence']=='survey_classification'
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
   assert all(m.get('total_b') and m['total_b']<27 for m in w['models'])
 assert a['relations']==e['relations'] and len(a['relations'])==a['counts']['relations']
 for rel in a['relations']:assert rel in g['edges']
 page=(R/'research/atlas/index.html').read_text()
 m=re.search(r'<script id="literature-data" type="application/json">(.*?)</script>',page,re.S)
 assert m and json.loads(m.group(1))==a
 assert '__LITERATURE_DATA__' not in page
 assert not re.search(r'<script[^>]+src=|<link[^>]+href=',page)
 # Stable scope regressions: historical items stay outside route landscapes;
 # teacher or transferred-to model scale cannot admit a small trained policy.
 assert works['eurisko']['route']=='archive'
 for k in ['skillrl','harness-r1']:assert works[k]['placement']=='small'
 print(f'PASS: {len(ids)} preserved works, {len(routed)} route positions, {len(a["relations"])} sourced/typed relations, exact offline data.')
if __name__=='__main__':check()
