#!/usr/bin/env python3
"""Build offline atlas, three-route graph and PDF from reviewed, versioned facts."""
import json, html, os, re
from pathlib import Path
from collections import Counter
from PIL import Image, ImageDraw, ImageFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image as RLImage, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
R=Path(__file__).resolve().parents[1]
J=lambda p:json.loads((R/p).read_text())
BR=J('data/research-brief.json')
Q=J('data/quality-review.json'); L=J('data/layer-review.json'); W=J('data/works.json')['works']
S={x['id']:x for x in J('data/scope-review.json')['works']}; M={x['id']:x for x in J('data/mechanisms.json')['works']}; X={x['id']:x for x in J('data/expansion-reviews.json')['works']}
D={x['id']:x for x in Q['decisions']}; C={x['id']:x for x in Q['core_cards']}; B={x['id']:x for x in L['works']}
LABEL={'core':'有命题研究卡片','pending':'候选待审','historical':'历史与机制参考','background':'背景移出','low_value':'低价值排除'}
PL=L['placement_labels']; routes={x['id']:x for x in L['routes']}; rows=[]
for n,w in enumerate(W,1):
 k=w['id'];r={**w,**S[k],**D[k],'number':n,'mechanism':M[k]['mechanism_interpretation'],'intervention':M[k]['separating_intervention'],'reading_scope':S[k]['reading_scope'],'tasks_and_resources':X.get(k,{}).get('tasks_and_resources','本轮未统一提取，不能据机构或模型名称推测。')}
 if k in C:r.update(C[k]);r['tasks_and_resources']=C[k]['scale'];r['reading_scope']=C[k]['source_location']+'；选定方法/证据阅读，未声明全文与附录全部精读。'
 r['layer']=B[k];r['main_view']=B[k]['placement']=='main';rows.append(r)
byid={r['id']:r for r in rows};main=[r for r in rows if r['main_view']];reviewed=[r for r in rows if r['id'] in C]
counts=dict(Counter(r['admission'] for r in rows));counts.setdefault('low_value',0)
placements=dict(Counter(r['layer']['placement'] for r in rows));route_counts={k:sum(r['layer']['route']==k for r in main) for k in routes}
for r in main:
 assert r['admission']=='core' and r['layer']['route'] in routes
 if r['layer']['route']!='harness':assert any(max(m['total_b'] or 0,m.get('total_lower_bound_b',0))>=L['minimum_total_parameters_b'] for m in r['layer']['models'])
mainids={r['id'] for r in main}
nodes=[{'id':'route-'+k,'type':'concept','label':v['title']} for k,v in routes.items()]+[{'id':r['id'],'type':'work','label':r['short']} for r in main]
edges=[{'source':'route-'+r['layer']['route'],'target':r['id'],'relation':'route_membership'} for r in main]+[{'source':r['source'],'target':r['target'],'relation':r['type']} for r in Q['relations'] if r['source'] in mainids and r['target'] in mainids]
canonical={'schema_version':'3.0.0','updated':L['updated'],'nodes':nodes,'edges':edges,'work_bindings':[{'work_id':r['id'],'node_ids':['route-'+r['layer']['route']]} for r in main]}
spaces=[]
for slot in L['spaces']:
 s={**slot};s['main_ids']=[k for k in s['evidence_ids'] if k in mainids and B[k]['route']==s['route']];s['reference_ids']=[k for k in s['evidence_ids'] if k not in s['main_ids']]
 s['coverage']='主图有对应实例' if s['main_ids'] else ('只有候选 / 范围外参考' if s['reference_ids'] else '本次调查未确认实例');spaces.append(s)
sector_counts={k:dict(Counter(r['layer']['provenance']['sector'] for r in main if r['layer']['route']==k)) for k in routes}
a={'brief':BR,'sector_counts':sector_counts,'updated':L['updated'],'version':'3.0.0','counts':counts,'placement_counts':placements,'route_counts':route_counts,'main_count':len(main),'reviewed_count':len(reviewed),'scope_counts':J('data/scope-review.json')['counts'],'discovery_count':len(J('data/discovery-pool.json')['entries']),'warning':Q['status'],'criteria':Q['criteria'],'families':Q['families'],'works':rows,'nodes':nodes,'edges':edges,'relations':Q['relations'],'routes':L['routes'],'spaces':spaces,'placement_labels':PL,'contribution_axes':L['contribution_axes'],'threshold':L['threshold_basis'],'minimum_total_parameters_b':L['minimum_total_parameters_b'],'priority_queue':Q['priority_queue'],'rejection_policy':Q['rejection_policy']}
for p,obj in [('data/research-atlas.json',a),('data/knowledge-graph.json',canonical)]: (R/p).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
fontpath=os.environ.get('ATLAS_CJK_FONT','/usr/local/share/fonts/qiushi/NotoSansCJKsc-Report.ttf')
if not Path(fontpath).exists():raise SystemExit('Set ATLAS_CJK_FONT to a Chinese-capable TrueType font.')
FONT=lambda n:ImageFont.truetype(fontpath,n)
INK='#152C42';TEAL='#126C72';GOLD='#AB5D28';MUTED='#516577';BG='#F4F7F8';LINE='#CCD9DF';WHITE='#FFFFFF'
class Figure:
 def __init__(self,w,h):self.w=w;self.h=h;self.im=Image.new('RGB',(w,h),BG);self.d=ImageDraw.Draw(self.im);self.s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>BeforeRSI 核心研究地图</title><rect width="100%" height="100%" fill="{BG}"/>']
 def rect(self,x,y,w,h,fill=WHITE,stroke=LINE):self.d.rounded_rectangle((x,y,x+w,y+h),radius=14,fill=fill,outline=stroke,width=2);self.s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="{stroke}"/>')
 def line(self,x1,y1,x2,y2,color=LINE,width=3,dashed=False):
  self.d.line((x1,y1,x2,y2),fill=color,width=width);self.s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(' stroke-dasharray="9 7"' if dashed else '')+'/>')
 def text(self,x,y,t,size=24,color=INK):
  self.d.text((x,y),t,font=FONT(size),fill=color);self.s.append(f'<text x="{x}" y="{y+size*1.1}" font-family="Noto Sans CJK SC,Microsoft YaHei,sans-serif" font-size="{size}" fill="{color}">{html.escape(t)}</text>')
 def para(self,x,y,t,width,size=24,color=MUTED,leading=None):
  leading=leading or int(size*1.4);line='';yy=y
  for c in re.findall(r'[A-Za-z0-9À-ž]+(?:[._–²-][A-Za-z0-9À-ž]+)*|\s+|.',t):
   if line and self.d.textlength(line+c,font=FONT(size))>width:
    self.text(x,yy,line,size,color);yy+=leading;line=c.lstrip()
   else:line+=c
  if line:self.text(x,yy,line,size,color);yy+=leading
  return yy
 def save(self,name):
  self.s.append('</svg>');(R/f'assets/atlas/{name}.svg').write_text('\n'.join(self.s));self.im.save(R/f'assets/atlas/{name}.png',optimize=True)
f=Figure(1500,1220)
f.text(60,38,'BeforeRSI  /  三层研究地图',42)
f.text(62,110,'按实际更新对象组织；闭环深度、贡献与规模另行核验',25,MUTED)
for i,(k,rt) in enumerate(routes.items()):
 y=180+i*280;f.rect(60,y,1380,250);f.text(85,y+18,f'{i+1:02d}  {rt["title"]} · {route_counts[k]}项',34,TEAL)
 f.text(85,y+75,rt['subtitle'],25,INK)
 f.para(85,y+120,rt['criterion'],410,23)
 f.line(530,y+26,530,y+224)
 names=' / '.join(r['short'] for r in main if r['layer']['route']==k)
 yy=f.para(560,y+24,names,850,26,INK)
 details={'harness':'包括提示、经验与代码的更新；改进器自改与固定外层搜索分别注明。','model':'反馈主线：自生成数据 → 偏好 / 奖励 → 评价器与生成器共同训练。','hybrid':'27B MASS：两轮交替；30B-A3B：序列联合适配。后者未实证持续多轮闭环。'}
 f.para(560,max(y+132,yy+16),details[k],850,23,TEAL)
f.rect(60,1050,1380,105,INK,INK)
f.text(84,1066,f'{len(main)} 项重点案例  /  {len(reviewed)} 项机制审查  /  {len(rows)} 项书目',28,WHITE)
f.text(84,1110,'Model / 混合：实际训练总参数 ≥27B；未知、低于门槛与非闭环支撑另列。',23,WHITE)
f.text(62,1180,'调查进行中；重点案例包括不同证据强度的机制研究，不是全球 RSI 总数。',21,MUTED);f.save('knowledge-tree')
g=Figure(1500,1040);g.text(60,38,'同一个角色，可能在不同层实现',40);g.text(62,105,'判断“改了哪里”之后，还要追踪“为什么改善、是否进入下一轮”。',25,MUTED)
for x,title,body,example in [(60,'Model：参数化组件','执行者、评价模型、世界模型、提案模型；权重 / adapter / 模型结构','自评价 SFT、偏好学习、RL、蒸馏、元学习'),(800,'Harness：外部机制','知识与记忆、工具、组织控制、学习研发、评价选择、执行资源','代码、提示、skills、MCP、数据库、runtime')]:
 g.rect(x,190,640,235);g.text(x+24,211,title,30,TEAL);g.para(x+24,268,body,590,25);g.para(x+24,365,example,590,21)
g.line(705,275,795,275,TEAL,4);g.line(785,267,795,275,TEAL);g.line(785,283,795,275,TEAL)
g.line(795,338,705,338,TEAL,4);g.line(715,330,705,338,TEAL);g.line(715,346,705,338,TEAL)
g.rect(60,475,1380,205);g.text(85,496,'混合需要实际反馈路径，不能由组件同时存在推出',30,INK)
g.para(85,553,'H → M：轨迹 / 课程 / 奖励进入训练。M → H：新模型改变可行策略，再产生和选择新外部机制。单向作用、一次联合适配、真实多轮回流，分别记录。',1325,27)
g.rect(60,730,670,190);g.text(84,750,'评价既是可改对象，也是外部检验',28,TEAL);g.para(84,805,'评价代码归 H，评价模型归 M；独立审计锚点不能与被优化的内部评分混同。',618,25)
g.rect(770,730,670,190);g.text(794,750,'结构共演不保证正协同',28,TEAL);g.para(794,805,'交叉替换 M / H，检查收益、回退、迁移和总成本；后继改进能力另做共同目标比较。',618,25)
g.text(62,975,'本图是分析框架；箭头表示待追踪的作用方向，不代表所有论文已证明闭环。',23,MUTED);g.save('feedback-map')
# Markdown: main view and exhaustive audit trail are distinct.
md=['# RSI 三条路线：数量、团队与研究方向','', '**调查仍在进行。以下是已核对的重点案例，不是最终领域总数。**','', '[离线 HTML](research/atlas/index.html) · [简明 PDF](output/pdf/beforersi-research-atlas.pdf)','',BR['correction'],'','| 路线 | 重点案例 | 工业独立 | 学术独立 | 产学联合 |','|---|---:|---:|---:|---:|']
for k,rt in routes.items():
 sc=sector_counts[k];md.append(f'| {rt["title"]} | {route_counts[k]} | {sc.get("industry",0)} | {sc.get("academic",0)} | {sc.get("joint",0)} |')
md+=['',BR['sector_rule'],'','## 三条路线分别在推进什么','']
for k,rt in routes.items():
 b=BR['routes'][k];md += ['### '+rt['title'],'',b['essence']+' '+b['direction'],'','- 工业应用目标：'+b['industry_goal'],'- 研究问题：'+b['research_goal'],'- 当前证据：'+b['evidence'],'- 判断边界：'+b['caution'],'','**已核对重点名单：** '+ '、'.join(r['short'] for r in main if r['layer']['route']==k),'']
md+=['目标与方向为对所列论文的综合判断，不是全行业意见调查，也不是按论文数量推算的趋势。','','## 调查账本','',f'完整目录 {len(rows)} 项；其中 {len(reviewed)} 项有机制审查卡片，{counts.get("pending",0)} 项仍待审，另有 {counts.get("historical",0)} 项历史材料与 {counts.get("background",0)} 项背景。已审卡片中只有 {len(main)} 项进入重点视图。','',f'另有 {placements.get("scale_unverified",0)} 项已审机制但规模待核准；{placements.get("adjacent",0)} 项关键前身/支撑；{placements.get("small",0)} 项低于27B的机制参考；{placements.get("crosscut",0)} 项评测/形式工具。','', 'Model / 混合规模门槛保留。AlphaProof 的3B主网络说明：不满足门槛不等于研究劣质。','', '## 原文与审查记录','', '- [逐项研究卡片](research/atlas/core-cards.md)','- [完整参考索引](research/atlas/references.md)','- [待审和筛选理由](research/atlas/review-queue.md)','- [分类原理附录](research/atlas/classification.md)','']
(R/'RESEARCH_ATLAS.md').write_text('\n'.join(md))
fields=[('principle','原理与操作'),('distinct_contribution','最值得保留的贡献'),('evidence','证据'),('scale','规模'),('limit','边界'),('insight','研究含义')]
ordered=main+[r for r in reviewed if not r['main_view']]
cm=['# 研究卡片：主视图与参考分列','',f'{len(main)} 项进入三层主图；共 {len(reviewed)} 项限定命题有卡片。结果为作者报告，未在本项目独立复现。','']
for r in ordered:
 b=r['layer'];cm+=['<a id="'+r['id']+'"></a>',f'## [{r["number"]:03d}] {r["short"]}','',f'**位置：** {routes.get(b["route"],{}).get("title","横向工具")} / {PL[b["placement"]]}。{b["why"]}','', '**团队：** '+r.get('institutions','未核准'),'', '**改变与回流：** '+b['changed']+'。'+b['return_path'],'']
 for key,title in fields:cm+=['**'+title+'：** '+r[key],'']
 if b['route'] in ['model','hybrid']:cm+=['**训练说明：** '+'；'.join(b['training'].values()),'']
 cm+=['**定位：** ['+b['source_location']+']('+b['source_url']+')；方法/证据摘读，未声明完整逐页审核。','']
(R/'research/atlas/core-cards.md').write_text('\n'.join(cm))
ref=[f'# 全部 {len(rows)} 项参考索引','','稳定编号不代表名次；候选不进入主图。旧主题归类保留为历史相关性记录；新层级由人工审查单独给出。','']
for r in rows:
 b=r['layer'];ref += [f'### [{r["number"]:03d}] {r["name"]} ({r["year"]})',f'阅读/贡献状态：{LABEL[r["admission"]]}；展示位置：**{PL[b["placement"]]}**。',b['why'],'既有阅读：'+r['reading_scope']]
 if b['audit']=='selected_sections':ref+=['层级/规模定位：'+b['source_location']]
 urls=list(dict.fromkeys([s['url'] for s in r['sources']]+([r['source_url']] if r.get('source_url') else [])));ref+=[' · '.join(f'[来源 {i+1}]({u})' for i,u in enumerate(urls)),'']
(R/'research/atlas/references.md').write_text('\n'.join(ref))
queue=['# 筛选、规模与待审记录','','主图须同时通过贡献证据、系统边界和规模检查。旧 `core` 表示有命题卡片，已不等于主图资格。','', '| 展示位置 | 数量 |','|---|---:|']
for k,n in placements.items():queue.append(f'| {PL[k]} | {n} |')
queue+=['', '未做新层级核准的条目保持 unresolved；不自动用标题推断模型大小和更新对象。以下是完整的非主图记录。','', '| 编号 | 工作 | 去向与理由 |','|---|---|---|']
for r in rows:
 if not r['main_view']:queue.append(f'| {r["number"]:03d} | [{r["name"]}]({r["primary_source"]}) | {PL[r["layer"]["placement"]]}：{r["layer"]["why"]} |')
queue+=['','具名低价值判定仍为 0；待审、规模不符、非闭环支撑、已证低价值不互相替代。完整理解仍需全文附录、实现、消融统计、资源账本和复现。','']
(R/'research/atlas/review-queue.md').write_text('\n'.join(queue))
# The current reader is rendered by build_literature_graphs.py after this legacy evidence join.
# PDF uses the same records as the HTML, with explicit source links.
pdfmetrics.registerFont(TTFont('CJK',fontpath))
styles={name:ParagraphStyle(name,fontName='CJK',fontSize=size,leading=leading,wordWrap='CJK',textColor=colors.HexColor(color),spaceAfter=after) for name,size,leading,color,after in [('title',28,38,INK,16),('h1',20,29,INK,16),('h2',13,20,TEAL,9),('body',10,15.5,INK,8),('small',8.3,12.3,MUTED,6)]}
P=lambda t,style='body':Paragraph(t,styles[style]);safe=lambda t:html.escape(str(t));story=[]
def page(title,sub=None):
 if story:story.append(PageBreak())
 story.append(P(title,'h1'))
 if sub:story.append(P(sub,'small'))
page('RSI 三条研究路线','2026-10-18 / 调查进度版 / 数量 · 团队 · 方向')
story += [P('数量、团队与研究方向','title'),P('调查进行中。此前 8 / 2 / 2 的案例视图遗漏了重要工业研究；以下更新反映当前审阅进度，尚不能给出全球最终筛选总数。'),P('当前已核对重点案例','h2')]
from reportlab.platypus import Table,TableStyle
def tbl(headers,items,widths):
 t=Table([[P(safe(v),'small') for v in headers]]+[[P(safe(v),'small') for v in row] for row in items],colWidths=widths,repeatRows=1,hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EAF0F3')),('VALIGN',(0,0),(-1,-1),'TOP'),('BOTTOMPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8),('LINEBELOW',(0,0),(-1,-1),.4,colors.HexColor(LINE))]));return t
story.append(tbl(['路线','重点数','工业独立','学术独立','产学联合'],[[routes[k]['title'],route_counts[k],sector_counts[k].get('industry',0),sector_counts[k].get('academic',0),sector_counts[k].get('joint',0)] for k in routes],[175,65,82,82,90]))
story +=[Spacer(1,12),P(BR['sector_rule'],'small'),P('三条方向','h2')]
for k,rt in routes.items():story +=[P(rt['title']+'：'+BR['routes'][k]['direction'])]
story +=[P(f'调查账本：{len(rows)} 项书目；{len(reviewed)} 项机制审查；{counts.get("pending",0)} 项候选待审。重点案例含不同证据强度，不代表 {len(main)} 个已实现强 RSI 的系统。','small'),P('工业和研究目标依据论文综合提炼；不是全行业意见调查或按数量外推的增长趋势。','small')]
for k,rt in routes.items():
 rs=[r for r in main if r['layer']['route']==k]
 chunk=3 if k=='model' else 4
 for start in range(0,len(rs),chunk):
  page(rt['title']+' / 已核对重点案例',f'{start+1}–{min(start+chunk,len(rs))} / {len(rs)}；结果均为作者报告，未独立复现。')
  if start==0:story +=[P('<b>工业目标：</b>'+safe(BR['routes'][k]['industry_goal'])),P('<b>研究问题：</b>'+safe(BR['routes'][k]['research_goal']))]
  for r in rs[start:start+chunk]:
   b=r['layer'];story +=[P(f'[{r["number"]:03d}] '+safe(r['short'])+' · '+safe(BR['claim_labels'][r['id']]),'h2'),P(safe(b['provenance']['institutions']),'small'),P(safe(r['principle']))]
   if k!='harness':story +=[P('<b>规模：</b>'+safe(r['scale']),'small')]
   story +=[P('<b>证据：</b>'+safe(r['evidence']),'small'),P('<b>边界：</b>'+safe(r['limit']),'small'),P(f'<link href="{safe(b["source_url"])}" color="{TEAL}">原文</link> · '+safe(b['source_location']),'small'),Spacer(1,7)]
page('主图之外：哪些重要工作仍须看','规模未核准、机制前身与证据待审，不能笼统写成“低质量”。')
for k in ['rest-em','sima2','gpt-red','evotrainer','constitutional-ai','llm-can-self-improve','alphaproof','co-harness']:
 r=byid[k];b=r['layer'];story +=[P(r.get('short',r['name'])+' · '+PL[b['placement']],'h2'),P(safe(b['why']),'small'),P(safe(r.get('scale',r.get('tasks_and_resources',''))),'small'),P(f'<link href="{safe(b.get("source_url") or r["primary_source"])}" color="{TEAL}">原文与机制依据</link>','small')]
page('完整名单与调查缺口','本页不把未审论文假装成已淘汰论文。')
story +=[P('当前统计','h2'),tbl(['状态','数量'],[[PL[k],v] for k,v in placements.items()],[390,104]),Spacer(1,14),P('缺口仍然实质存在','h2'),P('本轮补入 STOP、Promptbreeder、SICA、ACE、Iterative RPO、DeepSeekMath-V2 与 Kimi K2 的重点记录，补审自训练、AI反馈和工业具身学习谱系。尚有67项候选未完成同等审查；也未穷尽目录外工作。'),P('下一步统计必须以明确检索范围、去重、机制与证据审查为基础；不能预设“应有100项”，也不能把小样本包装成“只剩19项”。'),P('详细研究卡片、127项索引和分类附录均保留在离线HTML与仓库。','small'),P('<link href="https://github.com/Cherish0925/BeforeRSI/pull/5" color="'+TEAL+'">研究 PR #5 / 全部证据文件</link>','small')]
def footer(c,doc):
 width,height=A4;c.setStrokeColor(colors.HexColor(LINE));c.line(46,39,width-46,39);c.setFont('CJK',8);c.setFillColor(colors.HexColor(MUTED));c.drawString(46,25,'BeforeRSI / 2026-10-18 / 三条路线 · 调查进度版');c.drawRightString(width-46,25,str(doc.page))
out=R/'output/pdf/beforersi-research-atlas.pdf'
SimpleDocTemplate(str(out),pagesize=A4,rightMargin=46,leftMargin=46,topMargin=42,bottomMargin=52,title='BeforeRSI 三条路线：数量、团队与方向',author='BeforeRSI research').build(story,onFirstPage=footer,onLaterPages=footer)
print(json.dumps({'main':len(main),'route_counts':route_counts,'reviewed':len(reviewed),'counts':counts,'placements':placements,'pdf_bytes':out.stat().st_size},ensure_ascii=False))

# Preserve the v3 review/PDF snapshot while rebuilding the current graph reader.
import runpy
runpy.run_path(str(R / "scripts/build_literature_graphs.py"), run_name="__main__")
