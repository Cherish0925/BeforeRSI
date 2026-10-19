#!/usr/bin/env python3
"""Build the literature-only, three-route knowledge graph and offline reader."""
import json,re,html,hashlib
from pathlib import Path
from collections import Counter
from research_actors import build_actors
R=Path(__file__).resolve().parents[1]
def read(p):return json.loads((R/p).read_text())
def write(p,d):(R/p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
BIB={w['id']:w for w in read('data/works.json')['works']}
E=read('data/literature-editorial.json');F=read('data/field-knowledge.json');I=read('data/industry-landscape.json');old={r['id']:r for r in read('data/research-atlas.json')['works']}
assert set(old)<={w['id'] for w in E['works']}==set(BIB)
route_specs=[
 dict(id='harness',title='Harness',zh='外部系统的学习与自修改',color='#187c80',short='经验、程序与改进过程',definition='系统通过提示、代码、记忆、技能、工具、控制流、评价程序或运行机制的学习更新，改变后续任务行为。基础LLM权重保持固定；轻量检索头或MLP控制器的学习另行披露。',distinction='重点追踪：改的是任务执行系统，还是产生下一次改进的程序？经验积累、自动优化与改进器自修改是不同过程。'),
 dict(id='model',title='Model',zh='参数中的学习与反馈闭环',color='#7253a0',short='训练信号、权重与学习角色',definition='训练实际更新基础模型权重或 adapter，角色可为执行者、评价者、出题者或记忆管理者。自生成的数据、偏好、奖励、任务或验证结果进入后续学习。',distinction='重点追踪：谁生成训练信号、谁更新参数、什么进入下一轮？固定流程下的训练集、回放样本和目标程序档案更新，本身不构成Harness学习；可跨任务部署的记忆、技能、工具或控制程序学习须另行计入。'),
 dict(id='hybrid',title='Model × Harness',zh='外部系统与参数共同适配',color='#bd7036',short='工作流、训练与双向适配',definition='模型参数与外部执行或训练系统都发生更新。harness 改变经验与训练轨迹，参数更新改变代理的行为及后续系统设计。',distinction='重点追踪：两类更新是否真正相互影响？一次联合适配、顺序内化、多轮交替及持续共同进化分别标明。这里也保留尚未闭合自改进的 AI4AI 支撑工作。')]
# Common aliases support institution browsing without turning funding into authorship.
alias={'UC Berkeley':'Berkeley','University of California Berkeley':'Berkeley','UC Santa Barbara':'UCSB','UC Santa Cruz':'UCSC','University of Waterloo':'Waterloo','Stanford University':'Stanford','University of Bristol':'Bristol','University of British Columbia':'UBC','Google Deepmind':'Google DeepMind','DeepSeek-AI':'DeepSeek','Moonshot AI（月之暗面）':'Moonshot AI','Meta':'Meta AI','Meta FAIR':'Meta AI','FAIR at Meta':'Meta AI','University of Illinois Urbana-Champaign':'UIUC','Washington University':'WashU','University of Washington':'UW','University of Oxford':'Oxford','The Ohio State University':'Ohio State','University of Minnesota':'Minnesota','Tianjin University':'Tianjin','Shanxi University':'Shanxi','Shanghai Jiao Tong University':'SJTU','University of California San Diego':'UCSD','UNC-Chapel Hill':'UNC','Pennsylvania State University':'Penn State','Nanyang Technological University':'NTU','The Chinese University of Hong Kong':'CUHK','University of Chicago':'UChicago','University of Science and Technology of China':'USTC','Zhejiang University':'Zhejiang','Carnegie Mellon University':'Carnegie Mellon','Microsoft Research Asia':'Microsoft Research Asia','The University of Hong Kong':'HKU','University of Toronto':'Toronto','Vector Institute':'Vector','iGent AI':'iGent AI','Microsoft Research':'Microsoft Research','Google Research':'Google Research'}
alias.update({'清华大学':'Tsinghua','浙江大学':'Zhejiang','上海交通大学':'SJTU'})
ACTOR_SPEC=read('data/research-actors.json')
actor_names={label:a['name'] for a in ACTOR_SPEC['actors'] for label in a['aliases']+[a['name']]}
works=[];orgs={};nodes=[];edges=[]
for r in E['works']:
 w=old.get(r['id'],r);b=w.get('layer',r);urls=list(dict.fromkeys([r['primary_url']]+[s['url'] for s in BIB[r['id']]['sources']]))
 # Keep readable bibliography names while maintaining stable work identifiers.
 title=BIB[r['id']]['name']; resources=r.get('resources') or w.get('scale') or w.get('tasks_and_resources','')
 if resources.startswith('本轮未统一'):resources=''
 resources=resources.replace('本卡只纳入','本条讨论').replace('本卡未提取统一总算力','总训练或搜索成本尚未提取')
 # Preserve review wording: an analyst's check must not become an author claim.
 tnames=[]
 if '机构待核' not in r['team'] and '机构未核准' not in r['team'] and r['team']!='署名机构尚未整理':
  for name in r['team'].split(' / '):
   name=re.sub(r'（.*?）','',name).strip()
   if name.startswith('MIT ·'):name='MIT'
   if name.startswith('UCLA ·'):name='UCLA'
   if name.startswith('HKU ·'):name='HKU'
   if name.startswith('Douglas B. Lenat'):name='Stanford'
   name=alias.get(name,name)
   if name in ACTOR_SPEC.get('non_affiliation_labels',[]):continue
   name=actor_names.get(name,name)
   if name and name not in tnames:tnames.append(name)
  for name in tnames:
   oid='org-'+re.sub(r'[^a-z0-9]+','-',name.lower()).strip('-')+'-'+hashlib.sha256(name.encode()).hexdigest()[:8]
   if oid in orgs and orgs[oid]['label']!=name:raise ValueError('institution id collision: '+name+' / '+orgs[oid]['label'])
   orgs[oid]={'id':oid,'label':name,'type':'institution'}
   edges.append(dict(id=f'aff-{r["id"]}-{oid}',source=oid,target=r['id'],kind='affiliation',label='署名机构 / 团队',evidence='source_metadata',sources=[dict(url=r['team_source'],location=r.get('team_location','论文首页署名；官方报告团队'))]))
 wr={**r,'number':w['number'],'title':title,'year':w['year'],'sources':urls,'resources':resources,'models':r.get('models',b.get('models',[])),'training':r.get('training',b.get('training',{})),'parameter_note':r.get('parameter_note',b.get('parameter_check','')),'scale_status':r.get('scale_status',b.get('scale_status','unverified')),'organizations':tnames,'main_case':bool(w.get('main_view')),'reading_note':r.get('reading_scope',('已读相关方法与结果段落；不表示全文和实现均已复现。' if r['status']=='methods' else '摘要与来源初筛；研究结果和方法细节尚未完成逐项阅读。' if r['status']=='screened' else '历史或背景阅读，不计作当代 RSI 系统。'))}
 works.append(wr);nodes.append(dict(id=r['id'],type='work',label=r['short'],route=r['route'],year=w['year'],status=r['status']))
 for mid in r['methods']:
  if mid in {'historical','background','cross-evaluation'}:continue
  edges.append(dict(id=f'method-{mid}-{r["id"]}',source=mid,target=r['id'],kind='mechanism',label='研究该问题 / 使用该机制',evidence='survey_classification',sources=[dict(url=r['primary_url'],location=r['source_location'])]))
nodes.extend(dict(id=g['id'],label=g['title'],type='mechanism',route=g['route']) for g in E['groups']);nodes.extend(orgs.values());edges+=E['relations']
byid={w['id']:w for w in works}
for edge in E['relations']:
 assert edge['source'] in byid and edge['target'] in byid and edge['sources']
 if edge['kind']=='method_comparison':assert edge['evidence']=='survey_comparison'
for rt in route_specs:
 ws=[w for w in works if w['route']==rt['id']];rt['counts']={'catalog':len(ws),'methods':sum(w['status']=='methods' for w in ws),'screened':sum(w['status']=='screened' for w in ws),'small':sum(w['placement']=='small' for w in ws),'previous_main':sum(w['main_case'] for w in ws)}
 for g in E['groups']:
  if g['route']==rt['id']:assert any(w['cluster']==g['id'] for w in ws)
counts={**dict.fromkeys(['methods','screened','archive'],0),**dict(Counter(w['status'] for w in works))};counts.update(total=len(works),routed=sum(w['route'] in ['harness','model','hybrid'] for w in works),crosscut=sum(w['route']=='crosscut' for w in works),relations=len(E['relations']),institutions=len(orgs))
# Company profiles bind released works, publication roles and declared directions separately.
I['counts']={'total':len(I['companies']),'research':sum(c['status']=='research' for c in I['companies']),'direction':sum(c['status']=='direction' for c in I['companies']),'adjacent':sum(c['status']=='adjacent' for c in I['companies']),'linked_works':len({x['work_id'] for c in I['companies'] for x in c['work_links']})}
I['route_counts']={r['id']:sum(r['id'] in c['primary_routes'] for c in I['companies']) for r in route_specs}
for c in I['companies']:
 cid='company-'+c['id'];nodes.append(dict(id=cid,type='company',label=c['name'],status=c['status']))
 for x in c['work_links']:
  assert x['work_id'] in byid
  edges.append(dict(id=cid+'-work-'+x['work_id'],source=cid,target=x['work_id'],kind='company_work',label=x['relationship'],evidence='source_metadata',sources=[dict(url=x['source_url'],location=x['note'])]))
 for tid in c['topic_ids']:
  edges.append(dict(id=cid+'-topic-'+tid,source=cid,target='topic-'+tid,kind='company_topic',label='公开工作涉及',evidence='survey_classification',sources=[dict(url=u,location='公司关联工作的方法主题；具体署名和托管关系另列') for u in c['sources']]))
 for d in c['directions']:
  for tid in d['topic_ids']:
   edges.append(dict(id=cid+'-direction-'+tid,source=cid,target='topic-'+tid,kind='company_direction',label='公开方向 / 待确认闭环',evidence='declared_direction',sources=[dict(url=c['sources'][0],location=d['basis'])]))
a={'version':'5.1.0','updated':E['updated'],'title':'RSI 领域知识图谱','scope':E['scope'],'field':F,'industry':I,'routes':route_specs,'groups':E['groups'],'works':works,'relations':E['relations'],'paths':E['reading_paths'],'counts':counts,'search_leads':len(read('data/discovery-pool.json')['entries']),'relation_types':{'extends':'明确扩展','uses':'采用方法','compares':'论文比较','discusses':'原文讨论','method_comparison':'方法对照'},'institutions':sorted(orgs.values(),key=lambda x:x['label'].lower())}
pool={x['arxiv_id'] for x in read('data/discovery-pool.json')['entries'] if 'arxiv_id' in x}
catalog_arxiv={m.group(1) for w in works for u in w['sources'] if (m:=re.search(r'arxiv.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})',u))}
a['discovery_coverage']={'total':len(pool),'overlap':len(pool & catalog_arxiv),'unmatched':len(pool-catalog_arxiv),'rule':'exact arXiv identifier, ignoring version suffix'}
a['reading_coverage']={**dict.fromkeys(['main_text_and_relevant_appendix','paper_sections_read','public_materials','abstract_only','unavailable','unreviewed'],0),**dict(Counter(w.get('review',{}).get('source_coverage','unreviewed') for w in works))}
if (R/'data/discovery-review.json').exists():a['discovery_review']=read('data/discovery-review.json')
else:a['discovery_review']={'entries':[],'counts':{}}
# Full-corpus decisions are editorial evidence, separate from reading depth.
if (R/'data/corpus-review.json').exists():
 a['corpus_review']=read('data/corpus-review.json')
 for entry in a['corpus_review']['entries']:
  if entry.get('work_id') in byid and entry.get('review'):
   w=byid[entry['work_id']];w['corpus_entry_id']=entry['entry_id'];w['corpus_selection']=entry['review']['selection']
 for rt in route_specs:
  rt['counts']['core']=sum(w['route']==rt['id'] and w.get('corpus_selection',{}).get('decision')=='core' for w in works)

a['reader_guide']=read('data/reader-guide.json')
for c in a['reader_guide']['cases']:
 if c['id'] in byid and 'review' in byid[c['id']]:
  w=byid[c['id']];rv=w['review'];m=rv['mechanism']
  c.update(loop=m['loop'],changed=m['changed'],fixed=m['fixed'],feedback=m['feedback'],retained=m['inheritance'],insight=rv['contribution']['insight'],boundary=w['limitations'],basis=w['source_location'])
a['actors']=build_actors(ACTOR_SPEC,works,I)
for actor in a['actors']['actors']:
 nodes.append(dict(id='actor-'+actor['id'],type='research_actor',label=actor['name'],actor_kind=actor['kind']))
for w in works:
 for p in w['participants']:
  edges.append(dict(id='participation-'+p['actor_id']+'-'+w['id'],source='actor-'+p['actor_id'],target=w['id'],kind='research_participation',label='研究参与',evidence='source_metadata',roles=p['roles'],raw_labels=p['raw_labels'],sources=[dict(url=u,location='论文署名 / 官方发布；归并规则见 research-actors.json') for u in p['sources']]))
write('data/literature-atlas.json',a)
for rt in F['routes']:
 for n in rt['nodes']:
  nid='topic-'+n['id'];nodes.append(dict(id=nid,type='field_topic',route=rt['id'],label=n['title'],question=n['question'],definition=n['definition']))
  for i,label in enumerate(n['subtopics'],1):
   sid=nid+'-part-'+str(i);nodes.append(dict(id=sid,type='field_subtopic',route=rt['id'],label=label))
   edges.append(dict(id='contains-'+sid,source=nid,target=sid,kind='topic_contains',label='研究子问题',evidence='survey_structure',sources=[dict(url=u,location='方法主题的综述组织；原文例证') for u in n['source_urls']]))
 for q in rt['edges']:
  edges.append(dict(id=q['id'],source='topic-'+q['source'],target='topic-'+q['target'],kind='concept_relation',label=q['label'],explanation=q['explanation'],evidence='survey_structure',sources=[dict(url=u,location='机制联系的原文例证；此边为综述归纳') for u in q['source_urls']]))
 for q in rt['mappings']:
  for tid in q['topic_ids']:
   edges.append(dict(id='addresses-'+rt['id']+'-'+q['work_id']+'-'+tid,source=q['work_id'],target='topic-'+tid,kind='addresses_topic',label='研究此主题 / 相关机制',explanation=q['summary'],evidence='survey_classification',sources=[dict(url=u,location=q['source_location']) for u in q['source_urls']]))
write('data/knowledge-graph.json',{'schema_version':'5.1.0','updated':E['updated'],'scope':E['scope'],'nodes':nodes,'edges':edges,'field_views':{r['id']:['topic-'+n['id'] for n in r['nodes']] for r in F['routes']},'route_views':{rt['id']:[w['id'] for w in works if w['route']==rt['id']] for rt in route_specs},'work_bindings':[dict(work_id=w['id'],node_ids=[m for m in w['methods'] if m in {g['id'] for g in E['groups']}]) for w in works]})
template=(R/'scripts/atlas-template.html').read_text().replace('__ACTOR_STYLE__',(R/'scripts/actor-style.css').read_text()).replace('__ACTOR_SCRIPT__',(R/'scripts/actor-views.js').read_text());assert '__LITERATURE_DATA__' in template
page=template.replace('__CORPUS_STYLE__',(R/'scripts/corpus-style.css').read_text()).replace('__CORPUS_SCRIPT__',(R/'scripts/corpus-views.js').read_text()).replace('__READER_STYLE__',(R/'scripts/reader-guide.css').read_text()).replace('__READER_SCRIPT__',(R/'scripts/reader-guide.js').read_text()).replace('__DOMAIN_STYLE__',(R/'scripts/domain-style.css').read_text()).replace('__DOMAIN_SCRIPT__',(R/'scripts/domain-views.js').read_text()).replace('__INDUSTRY_SCRIPT__',(R/'scripts/industry-views.js').read_text()).replace('__INDUSTRY_STYLE__',(R/'scripts/industry-style.css').read_text()).replace('__LITERATURE_DATA__',json.dumps(a,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'))
for name in ['index.html','RSI_Field_Atlas_v5_1.html']:(R/'research/atlas'/name).write_text(page)
md=['# RSI 领域知识图谱 · v5.1','','[打开三张领域图谱](research/atlas/RSI_Field_Atlas_v5_1.html) · [文字版研究结构](research/atlas/field-guide.md)','','![三张领域图的界面示意；最新数字以 HTML 为准](assets/atlas/landscape-overview.png)','','首页直接显示 Harness、Model、Model × Harness 三张领域图。29 个研究主题、其下的具体子问题以及 60 条机制联系先组织研究空间；论文、团队和机构再挂接到对应位置。主题间联系是综述归纳，论文间的引用、扩展和方法对照另行标注。','','点击主题可展开关键问题、原理、技术、相邻关系与对应研究；点击箭头可看联系的含义和原文例证。本综述仅讨论公开研究，不包含项目自身理论或设计。','','## 当前收录进度','','| 路线 | 收录研究 | 论文原文研读 | 公开材料研读 |','|---|---:|---:|---:|']
if a.get('corpus_review'):
 cr=a['corpus_review'];cc=cr['counts'];reading=cc['reading'];sel=cc['selection']
 audit=['## 全量来源审查','',f'固定清单共 **{cc["total"]} 条来源记录**，已完成 **{cc["reviewed"]} 条**，待完成 **{cc["pending"]} 条**。这些数字不是独立 RSI 系统数，也不是全球文献总量。所有记录均可在 HTML 中搜索；图谱目录是其中用于导航的挂接层，并不限制阅读卡片的覆盖范围。','',f'阅读依据：{reading.get("full_primary",0)} 条原文与相关附录研读，{reading.get("previous_primary_rechecked",0)} 条既有研读加本次原文复核，{reading.get("public_materials",0)} 条官方技术材料。已读范围和未披露部分逐项记录；不把文献分析写成独立实验复现。','','| 研究位置 | 审查记录 | 重点研究 | 方法 / 证据补充 | 范围 / 机制参考 | 其他取舍 |','|---|---:|---:|---:|---:|---:|']
 for route,title in [(r['id'],r['title']) for r in route_specs]+[('crosscut','跨路线支撑'),('background','历史与基础'),('outside','范围外')]:
  z=cc['routes'].get(route,{})
  audit.append(f'| {title} | {z.get("reviewed",0)} | {z.get("core",0)} | {z.get("support",0)} | {z.get("mechanism_supplement",0)} | {sum(z.get(k,0) for k in ["redundant","outside","insufficient","blocked"])} |')
 audit+=['',f'重点研究合计 **{sel.get("core",0)} 条**，包括跨路线的评价与理论材料。未入重点图谱不等于劣质；相近工作、范围外、公开证据不足分别说明。没有按 20% 配额倒推筛选。','', '[完整审查说明](research/atlas/reading-audit.md) · 原始结构记录：`data/reading-reviews/`。','']
 pos=md.index('## 当前收录进度');md[pos:pos+1]=audit+['## 图谱挂接目录']
for r in route_specs:
 ws=[w for w in works if w['route']==r['id']];md.append(f'| {r["title"]} | {len(ws)} | {sum(w.get("review",{}).get("source_coverage")=="main_text_and_relevant_appendix" for w in ws)} | {sum(w.get("review",{}).get("source_coverage")=="public_materials" for w in ws)} |')
md+=['',f'目录挂接 {counts["routed"]} 项路线研究、{counts["crosscut"]} 项跨路线评测/形式研究及 {counts["archive"]} 项历史、背景材料，共 {len(works)} 项。此目录数量不同于全量审查记录数或重点研究数；完整索引中所有记录都有各自阅读卡片。','',f'{counts["relations"]} 条逐项解释的目录论文关系；机构署名与方法归类作为单独边类型。全量索引还保留目录之外的关系与解释。','', '## 阅读方式','','1. 首页先读三张领域图；点击主题，展开子问题与具体方法。','2. 沿主题联系看经验、反馈、参数和程序怎样相互作用；论文不决定主题是否存在。','3. 读主题下的论文与团队，打开 A–F 研究卡片；卡片可以定位回相关领域主题。','4. 切换论文关系图，看明确引用、扩展与综述方法对照。','5. 使用全局检索查全部来源记录中的论文、机构、算法或任务。','','已确认低于 27B 的 Model / 混合机制参考默认不出现在路线论文主视图，可在补充区或搜索中读取。未公开规模与低质量不是同一判断。','', '## 数据与复建','','`data/field-knowledge.json` 保存领域主题、子问题、机制联系和论文挂接；`data/literature-editorial.json` 保存逐篇叙述与论文关系；`data/literature-atlas.json` 是阅读数据，`data/knowledge-graph.json` 是带来源的多关系图。','','```bash','python scripts/build_corpus_review.py --require-complete','python scripts/integrate_corpus_reviews.py','python scripts/integrate_corpus_relations.py','python scripts/build_literature_graphs.py','python scripts/check_literature_graphs.py','node scripts/check_atlas_ui.cjs','```','', '上一轮九页 PDF 是 2026-10-18 的导读快照；当前图谱以 v5.1 HTML 与上述数据为准。']
md += ['', '## 公司与产业团队', '', f"公司索引共 {I['counts']['total']} 项：{I['counts']['research']} 项关联具体研究、{I['counts']['direction']} 项仅公开方向、{I['counts']['adjacent']} 项邻近研究待确认。关联 {I['counts']['linked_works']} 项去重研究；不是全球公司总数。", '', '[公司与研究关联表](research/atlas/industry-guide.md) · 来源：`data/industry-landscape.json`。公司索引与各领域主题双向连接。', '']
(R/'RESEARCH_ATLAS.md').write_text('\n'.join(md)+'\n')
actor_guide=['# 研究主体与三条 RSI 路线','','研究路线解释更新对象与机制；主体类别解释研究由谁开展。合作记录在具体工作上，不把合作团队另造为互斥的第四类机构。','','| 研究主体 | 定义 |','|---|---|']
for t in a['actors']['types']:
 actor_guide.append(f'| {t["title"]} | {t["description"]} |')
small_count=sum(w['placement']=='small' and w['route'] in {'harness','model','hybrid'} for w in works)
actor_guide+=['','## 交叉统计','',f'下表列出导航目录中全部 {counts["routed"]} 项主路线工作，包含 {small_count} 项 <27B 机制参考。HTML 默认矩阵按重点研究筛选，可另选方法补充与小模型；因此不能把此全目录表等同默认重点数量。单元格对工作去重；合作研究可出现在多个主体行中，不能将各行相加。','','| 主体 | Harness | Model | Model × Harness | 三条路线合计 |','|---|---:|---:|---:|---:|']
routed=[w for w in works if w['route'] in {'harness','model','hybrid'}]
for t in a['actors']['types']:
 ws=[w for w in routed if t['id'] in w['actor_types']]
 actor_guide.append('| '+t['title']+' | '+' | '.join(str(sum(w['route']==rt for w in ws)) for rt in ['harness','model','hybrid'])+f' | {len(ws)} |')
actor_guide+=['','## 归属规则','']+['- '+rule for rule in a['actors']['rules']]
actor_guide+=['','## 机构与工作索引','','机构名称用于归并浏览；完整原始署名与来源保留在每项研究的阅读卡片中。独立研究者仅为浏览分组，不计为一个机构。','']
for t in a['actors']['types']:
 actor_guide+=['### '+t['title'],'']
 for actor in sorted([q for q in a['actors']['actors'] if q['kind']==t['id']],key=lambda q:q['name'].lower()):
  current=[byid[wid] for wid in actor['work_ids'] if byid[wid]['status']!='archive']
  if not current and not actor.get('profile_id'):continue
  actor_guide+=['- **'+actor['name']+'**：'+('；'.join('['+w['short']+']('+w['primary_url']+')' for w in current) or '公开方向 / 邻近资料；见公司公开档案。')]
 actor_guide+=['']
(R/'research/atlas/actor-guide.md').write_text('\n'.join(actor_guide)+'\n')
with (R/'RESEARCH_ATLAS.md').open('a') as out:
 out.write('\n## 按研究主体交叉浏览\n\n[机构与合作索引](research/atlas/actor-guide.md)。HTML 首页保留三张领域图，随后提供“研究主体 × 技术路线”矩阵；机构页可按主体、路线、合作与阅读状态筛选。\n\n`data/research-actors.json` 保存规范机构、别名与归并规则；论文原始署名和公司托管关系保持独立。路线页使用可分页研究列表，完整 A–F 阅读卡片、全局搜索和论文关系图继续保留。\n')
fm=['# 三条 RSI 路线：领域主题与机制联系','','这是一份可修订的问题空间与方法索引。主题可以交叉；主路线以实际更新对象确定。没有对应论文的主题仍保留，暂未收录不等于研究不存在。','']
for rt in F['routes']:
 fm+=['## '+rt['title'],'',rt['definition'],'',rt['central_question'],'',rt['scene'],'']
 for n in rt['nodes']:
  fm+=['### '+n['title']+' · '+n['english'],'',n['question'],'',n['definition'],'','**研究子问题**','']+['- '+s for s in n['subtopics']]+['','**主要技术**','']+['- '+s for s in n['mechanisms']]+['','**机制联系**','']
  names={q['id']:q['title'] for q in rt['nodes']}
  fm+=['- '+names[q['source']]+' → '+names[q['target']]+'：'+q['label']+'。'+q['explanation'] for q in rt['edges'] if n['id'] in [q['source'],q['target']]]
  fm+=['','**论文与团队（包括跨路线联系）**','']
  for q in rt['mappings']:
   if n['id'] in q['topic_ids']:
    w=byid[q['work_id']];fm+=['- ['+w['short']+']('+w['primary_url']+') · '+w['team']+'。'+q['summary']]
  fm+=['']
 fm+=['### 持续研究的问题','']+['- **'+q['title']+'** '+q['text'] for q in rt['open_questions']]+['']
(R/'research/atlas/field-guide.md').write_text('\n'.join(fm)+'\n')
# A complete textual companion, using exactly the content visible in the page.
reading_names={'main_text_and_relevant_appendix':'论文主文、实验与相关附录研读','paper_sections_read':'选定方法与结果段落研读','public_materials':'公开材料研读'}
def reading_name(w):return reading_names.get(w.get('review',{}).get('source_coverage'),'来源阅读待补')
cm=['# RSI 公开研究阅读档案','', '论文主文与相关附录、选定方法/结果段落、公开技术资料分别标明。A–F围绕实际贡献组织；公开来源缺少的细节不作推断。','']
for w in works:
 cm+=['## '+w['short'], '',f'{w["year"]} · {w["team"]} · {reading_name(w)}','','[原文]('+w['primary_url']+') · '+w['source_location'],'']
 for s in w['sections']:cm += [f'**{s["axis"]} · {s["title"]}**',s['text'],'']
 if w['resources']:cm+=['**实验与资源：** '+w['resources'],'']
 if w.get('review'):
  v=w['review'];m=v['mechanism'];x=v['results']
  cm+=['### 机制、实验与原文证据','']
  for title,value in [('更新对象',m['changed']),('固定条件',m['fixed']),('反馈信号',m['feedback']),('跨轮继承',m['inheritance']),('更新循环',m['loop']),('实验设置',x['setup']),('比较基线',x['comparison']),('主要结果',x['result']),('消融与归因',x['ablation']),('资源代价',x['cost']),('泛化范围',x['generalization']),('与相关方法的差别',v['contribution']['comparison']),('收录范围判断',v['scope_reason'])]:
   cm+=['**'+title+'：** '+value,'']
  cm+=['**原文定位**','']+['- ['+s['location']+']('+s['url']+')' for s in v['sources']]+['']
(R/'research/atlas/literature-cards.md').write_text('\n'.join(cm)+'\n')
print(json.dumps({'counts':counts,'routes':{r['id']:r['counts'] for r in route_specs},'nodes':len(nodes),'edges':len(edges)},ensure_ascii=False))

# The reference index follows the current reader; the earlier review queue stays dated.
route_names={r['id']:r['title'] for r in route_specs}|{'crosscut':'跨路线评测 / 理论','archive':'历史 / 背景'}
status_names={'methods':'来源研读','screened':'机制披露不足','archive':'历史 / 背景'}
refs=['# 参考文献与阅读位置','',f'{len(works)} 个稳定编号是引用索引，不是质量排名；包含论文、技术报告、仓库和产品机制文档。当前路线归属、阅读深度和来源如下；完整解释见 [阅读档案](literature-cards.md)。','']
for w in works:
 refs += [f'## [{w["number"]:03d}] {w["short"]} · {w["year"]}','',w['title'],'',f'{route_names[w["route"]]} · {reading_name(w)} · {w["team"]}','',w['source_location'],'']
 refs += [f'- [来源 {i+1}]({url})' for i,url in enumerate(w['sources'])]
 refs += ['']
(R/'research/atlas/references.md').write_text('\n'.join(refs)+'\n')

# A human-readable counterpart of the company profiles and exact relationship types.
im=['# RSI 公司与产业研究团队','','本索引不是全球普查。技术论文、官网技术报告、仓库与产品机制文档共同构成证据；公司愿景不计作已发布的自进化系统。','']
for c in I['companies']:
 im+=['## '+c['name'],'',c['focus'],'',c['boundary'],'','**关联研究**','']
 for x in c['work_links']:
  w=byid[x['work_id']];im+=['- ['+w['short']+']('+x['source_url']+') · '+x['relationship']+' · '+route_names[w['route']]+'。'+x['note']]
 for d in c['directions']:im+=['- 方向：'+route_names[d['route']]+'。'+d['basis']]
 im+=['','**其他公开资料**','']+['- ['+d['title']+']('+d['url']+')：'+d['summary'] for d in c['disclosures']]+['']
(R/'research/atlas/industry-guide.md').write_text('\n'.join(im)+'\n')
