#!/usr/bin/env python3
"""Build the literature-only, three-route knowledge graph and offline reader."""
import json,re,html
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1]
def read(p):return json.loads((R/p).read_text())
def write(p,d):(R/p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
BIB={w['id']:w for w in read('data/works.json')['works']}
E=read('data/literature-editorial.json');old={r['id']:r for r in read('data/research-atlas.json')['works']}
assert set(old)=={w['id'] for w in E['works']}
route_specs=[
 dict(id='harness',title='Harness',zh='外部系统的学习与自修改',color='#187c80',short='经验、程序与改进过程',definition='基础模型可以冻结。系统通过提示、代码、记忆、技能、工具、控制流、评价程序或运行机制的更新，改变后续行为。',distinction='重点追踪：改的是任务执行系统，还是产生下一次改进的程序？经验积累、自动优化与改进器自修改是不同过程。'),
 dict(id='model',title='Model',zh='参数中的学习与反馈闭环',color='#7253a0',short='训练信号、权重与学习角色',definition='训练实际更新模型权重或 adapter。模型生成的数据、偏好、奖励、任务或验证结果进入后续学习；执行者、评价器和出题者都可能是被训练模型。',distinction='重点追踪：谁生成训练信号、谁更新参数、什么进入下一轮？多个模型共同训练不必然是 Model × Harness；数据变化也不等于运行程序自修改。'),
 dict(id='hybrid',title='Model × Harness',zh='外部系统与参数共同适配',color='#bd7036',short='工作流、训练与双向适配',definition='模型参数与外部执行或训练系统都发生更新。harness 改变经验与训练轨迹，参数更新改变代理的行为及后续系统设计。',distinction='重点追踪：两类更新是否真正相互影响？一次联合适配、顺序内化、多轮交替及持续共同进化分别标明。这里也保留尚未闭合自改进的 AI4AI 支撑工作。')]
# Common aliases support institution browsing without turning funding into authorship.
alias={'UC Berkeley':'Berkeley','University of California Berkeley':'Berkeley','UC Santa Barbara':'UCSB','UC Santa Cruz':'UCSC','University of Waterloo':'Waterloo','Stanford University':'Stanford','University of Bristol':'Bristol','University of British Columbia':'UBC','Google Deepmind':'Google DeepMind','DeepSeek-AI':'DeepSeek','Moonshot AI（月之暗面）':'Moonshot AI','Meta':'Meta AI','Meta FAIR':'Meta AI','FAIR at Meta':'Meta AI','University of Illinois Urbana-Champaign':'UIUC','Washington University':'WashU','University of Washington':'UW','University of Oxford':'Oxford','The Ohio State University':'Ohio State','University of Minnesota':'Minnesota','Tianjin University':'Tianjin','Shanxi University':'Shanxi','Shanghai Jiao Tong University':'SJTU','University of California San Diego':'UCSD','UNC-Chapel Hill':'UNC','Pennsylvania State University':'Penn State','Nanyang Technological University':'NTU','The Chinese University of Hong Kong':'CUHK','University of Chicago':'UChicago','University of Science and Technology of China':'USTC','Zhejiang University':'Zhejiang','Carnegie Mellon University':'Carnegie Mellon','Microsoft Research Asia':'Microsoft Research Asia','The University of Hong Kong':'HKU','University of Toronto':'Toronto','Vector Institute':'Vector','iGent AI':'iGent AI','Microsoft Research':'Microsoft Research','Google Research':'Google Research'}
works=[];orgs={};nodes=[];edges=[]
for r in E['works']:
 w=old[r['id']];b=w['layer'];urls=list(dict.fromkeys([r['primary_url']]+[s['url'] for s in BIB[r['id']]['sources']]))
 # Keep readable bibliography names while maintaining stable work identifiers.
 title=BIB[r['id']]['name']; resources=r.get('resources') or w.get('scale') or w.get('tasks_and_resources','')
 if resources.startswith('本轮未统一'):resources=''
 resources=resources.replace('本卡只纳入','本条讨论').replace('本卡未提取统一总算力','总训练或搜索成本尚未提取')
 for sec in r['sections']:
  sec['text']=sec['text'].replace('本卡纳入','这里讨论').replace('已核对','论文给出').replace('本卡不推测','未明确').replace('本轮','当前').replace('我们的贡献不能是组件改名；需额外给出可识别量与跨机制预测。','形式表示的贡献应与经验预测的效力区分。')
 tnames=[]
 if '机构待核' not in r['team'] and '机构未核准' not in r['team'] and r['team']!='署名机构尚未整理':
  for name in r['team'].split(' / '):
   name=re.sub(r'（.*?）','',name).strip()
   if name.startswith('MIT ·'):name='MIT'
   if name.startswith('UCLA ·'):name='UCLA'
   if name.startswith('HKU ·'):name='HKU'
   if name.startswith('Douglas B. Lenat'):name='Stanford'
   name=alias.get(name,name)
   if name and name not in tnames:tnames.append(name)
  for name in tnames:
   oid='org-'+re.sub(r'[^a-z0-9]+','-',name.lower()).strip('-')
   if oid in orgs and orgs[oid]['label']!=name:raise ValueError('institution id collision')
   orgs[oid]={'id':oid,'label':name,'type':'institution'}
   edges.append(dict(id=f'aff-{r["id"]}-{oid}',source=oid,target=r['id'],kind='affiliation',label='署名机构 / 团队',evidence='source_metadata',sources=[dict(url=r['team_source'],location=r.get('team_location','论文首页署名；官方报告团队'))]))
 wr={**r,'number':w['number'],'title':title,'year':w['year'],'sources':urls,'resources':resources,'models':r.get('models',b.get('models',[])),'training':b.get('training',{}),'parameter_note':b.get('parameter_check',''),'scale_status':r.get('scale_status',b.get('scale_status','unverified')),'organizations':tnames,'main_case':bool(w.get('main_view')),'reading_note':('已读相关方法与结果段落；不表示全文和实现均已复现。' if r['status']=='methods' else '仅作摘要与来源初筛；下面说明研究问题和已公开的基本方法。' if r['status']=='screened' else '历史或背景阅读，不计作当代 RSI 系统。')}
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
counts=dict(Counter(w['status'] for w in works));counts.update(total=len(works),routed=sum(w['route'] in ['harness','model','hybrid'] for w in works),crosscut=sum(w['route']=='crosscut' for w in works),relations=len(E['relations']),institutions=len(orgs))
a={'version':'4.0.0','updated':E['updated'],'title':'RSI 研究图谱','scope':E['scope'],'routes':route_specs,'groups':E['groups'],'works':works,'relations':E['relations'],'paths':E['reading_paths'],'counts':counts,'search_leads':len(read('data/discovery-pool.json')['entries']),'relation_types':{'extends':'明确扩展','uses':'采用方法','compares':'论文比较','discusses':'原文讨论','method_comparison':'方法对照'},'institutions':sorted(orgs.values(),key=lambda x:x['label'].lower())}
write('data/literature-atlas.json',a)
write('data/knowledge-graph.json',{'schema_version':'4.0.0','updated':E['updated'],'scope':E['scope'],'nodes':nodes,'edges':edges,'route_views':{rt['id']:[w['id'] for w in works if w['route']==rt['id']] for rt in route_specs},'work_bindings':[dict(work_id=w['id'],node_ids=[m for m in w['methods'] if m in {g['id'] for g in E['groups']}]) for w in works]})
template=(R/'scripts/atlas-template.html').read_text();assert '__LITERATURE_DATA__' in template
(R/'research/atlas/index.html').write_text(template.replace('__LITERATURE_DATA__',json.dumps(a,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')))
md=['# RSI 三路线知识图谱','','[打开交互式综述](research/atlas/index.html)','','以公开研究为对象；图中的关系、团队和研究卡片共同解释三条路线。本综述不讨论项目自身理论或方案。','','| 路线 | 收录研究 | 方法段落已读 | 摘要初筛 |','|---|---:|---:|---:|']
for r in route_specs:md.append(f'| {r["title"]} | {r["counts"]["catalog"]} | {r["counts"]["methods"]} | {r["counts"]["screened"]} |')
md+=['',f'合计 {counts["routed"]} 项路线研究，另有 {counts["crosscut"]} 项跨路线评测/形式研究与 22 项历史、背景材料，共 {len(works)} 项。路线数量包括相关技术和初筛候选，不等于认证的高质量 RSI 系统数。','',f'{counts["relations"]} 条逐项解释的论文关系；机构署名与方法归类作为单独边类型。','', '## 阅读方式','','1. 进入任一路线，沿问题与方法节点查看研究分布。','2. 点击论文，看相邻研究及团队；点击关系，看关系含义与原文定位。','3. 打开阅读卡片，按目标、思想、原理、方法、迭代、成果六个角度阅读已有内容。摘要档案不冒充完整方法审阅。','4. 使用全局检索查论文、机构、算法或任务，并定位回图。','','已确认低于 27B 的 Model / 混合机制参考默认不出现在路线主图，可在补充区或搜索中读取。未公开规模与低质量不是同一判断。','', '## 数据与复建','','`data/literature-editorial.json` 保存人工叙述、路线位置与关系；`data/literature-atlas.json` 是阅读数据，`data/knowledge-graph.json` 是带来源的多关系图。','','```bash','python scripts/build_literature_graphs.py','python scripts/check_literature_graphs.py','node scripts/check_atlas_ui.cjs','```','', '上一轮九页 PDF 是 2026-10-18 的导读快照；当前图谱以 HTML 与上述数据为准。']
(R/'RESEARCH_ATLAS.md').write_text('\n'.join(md)+'\n')
# A complete textual companion, using exactly the content visible in the page.
cm=['# RSI 公开研究阅读档案','', '方法卡片、摘要档案与历史阅读分开标明。A–F 是阅读角度；没有材料支持的部分不填充套话。','']
for w in works:
 cm+=['## '+w['short'], '',f'{w["year"]} · {w["team"]} · {w["status"]}','','[原文]('+w['primary_url']+') · '+w['source_location'],'']
 for s in w['sections']:cm += [f'**{s["axis"]} · {s["title"]}**',s['text'],'']
 if w['resources']:cm+=['**实验与资源：** '+w['resources'],'']
(R/'research/atlas/literature-cards.md').write_text('\n'.join(cm)+'\n')
print(json.dumps({'counts':counts,'routes':{r['id']:r['counts'] for r in route_specs},'nodes':len(nodes),'edges':len(edges)},ensure_ascii=False))

# The reference index follows the current reader; the earlier review queue stays dated.
route_names={r['id']:r['title'] for r in route_specs}|{'crosscut':'跨路线评测 / 理论','archive':'历史 / 背景'}
status_names={'methods':'方法段落已读','screened':'摘要初筛','archive':'历史 / 背景'}
refs=['# 参考文献与阅读位置','','127 个稳定编号是引用索引，不是质量排名。当前路线归属、阅读深度和来源如下；完整解释见 [阅读档案](literature-cards.md)。','']
for w in works:
 refs += [f'## [{w["number"]:03d}] {w["short"]} · {w["year"]}','',w['title'],'',f'{route_names[w["route"]]} · {status_names[w["status"]]} · {w["team"]}','',w['source_location'],'']
 refs += [f'- [来源 {i+1}]({url})' for i,url in enumerate(w['sources'])]
 refs += ['']
(R/'research/atlas/references.md').write_text('\n'.join(refs)+'\n')
