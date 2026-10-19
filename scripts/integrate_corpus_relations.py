#!/usr/bin/env python3
"""Resolve only unambiguous relation targets; preserve explicit vs editorial basis."""
import hashlib,json,re
from collections import defaultdict,Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(n):return json.loads((ROOT/'data'/n).read_text())
def norm(s):return re.sub(r'[^a-z0-9\u4e00-\u9fff]+','',s.lower())
def main():
    corpus=read('corpus-review.json');ed=read('literature-editorial.json');bib=read('works.json');entries=corpus['entries'];byid={e['entry_id']:e for e in entries};works={w['id']:w for w in ed['works']}
    aliases=defaultdict(set)
    for e in entries:
        for name in [e['entry_id'],e.get('arxiv_id') or '',e['title'],e.get('work_id') or '']:
            if name:aliases[norm(name)].add(e['entry_id'])
        if e.get('work_id') in works:aliases[norm(works[e['work_id']]['short'])].add(e['entry_id'])
    def resolve(target):
        key=norm(target);ids=aliases.get(key,set())
        if len(ids)==1:return next(iter(ids))
        # Explicit arXiv identifiers embedded in a title are unambiguous too.
        m=re.search(r'\b\d{4}\.\d{4,5}\b',target)
        if m:
            ids=aliases.get(norm(m.group()),set())
            if len(ids)==1:return next(iter(ids))
        return None
    resolved=[];unresolved=[]
    for e in entries:
        if not e.get('review'):continue
        for r in e['review'].get('relations',[]):
            target=resolve(r['target'])
            if not target:
                unresolved.append({'source':e['entry_id'],**r});continue
            if target==e['entry_id']:continue
            assert r['basis'] in {'source_explicit','analytical_comparison'},r
            assert r.get('explanation') and r.get('source_url') and r.get('location'),r
            resolved.append({'source':e['entry_id'],'target':target,**{k:v for k,v in r.items() if k!='target'}})
    corpus['relations']=resolved
    corpus['unresolved_relations']=unresolved
    corpus['relation_counts']={'resolved':len(resolved),'unresolved':len(unresolved),'by_basis':dict(Counter(e['basis'] for e in resolved))}
    graph_edges=[];seen=set()
    for e in resolved:
        source=byid[e['source']].get('work_id');target=byid[e['target']].get('work_id')
        if source not in works or target not in works or source==target:continue
        explicit=e['basis']=='source_explicit'
        kind=e['kind'] if explicit and e['kind'] in {'uses','extends','compares','discusses'} else 'discusses' if explicit else 'method_comparison'
        # Corpus facts read "current uses/extends cited"; the landscape arrow
        # follows the established prior -> later convention for inheritance.
        if kind in {'uses','extends','compares','discusses'}:source,target=target,source
        key=(source,target,kind,e['explanation'])
        if key in seen:continue
        seen.add(key)
        rid=hashlib.sha256(json.dumps(key,ensure_ascii=False).encode()).hexdigest()[:12]
        graph_edges.append({'id':'corpus-rel-'+rid,'source':source,'target':target,'kind':kind,'label':{'uses':'采用方法','extends':'扩展前作','compares':'原文比较','discusses':'原文讨论','method_comparison':'机制与证据对照'}[kind],'evidence':'source_explicit' if explicit else 'survey_comparison','explanation':e['explanation'],'sources':[{'url':e['source_url'],'location':e['location']}],'provenance':'full_corpus_reading'})
    # Existing curated relations remain; exact duplicates of new relations are
    # folded by source/target/type and substantive explanation, never keyword.
    old=[e for e in ed['relations'] if e.get('provenance')!='full_corpus_reading']
    old_keys={(e['source'],e['target'],e['kind'],e.get('explanation')) for e in old}
    ed['relations']=old+[e for e in graph_edges if (e['source'],e['target'],e['kind'],e['explanation']) not in old_keys]
    for name,obj in [('corpus-review.json',corpus),('literature-editorial.json',ed),('corpus-unresolved-relations.json',{'updated':'2026-10-19','entries':unresolved})]:
        (ROOT/'data'/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({**corpus['relation_counts'],'graph_edges_from_corpus':len(graph_edges)},ensure_ascii=False))
if __name__=='__main__':main()
