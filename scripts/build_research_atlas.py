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
 if r['layer']['route']!='harness':assert any((m['total_b'] or 0)>=L['minimum_total_parameters_b'] for m in r['layer']['models'])
mainids={r['id'] for r in main}
nodes=[{'id':'route-'+k,'type':'concept','label':v['title']} for k,v in routes.items()]+[{'id':r['id'],'type':'work','label':r['short']} for r in main]
edges=[{'source':'route-'+r['layer']['route'],'target':r['id'],'relation':'route_membership'} for r in main]+[{'source':r['source'],'target':r['target'],'relation':r['type']} for r in Q['relations'] if r['source'] in mainids and r['target'] in mainids]
canonical={'schema_version':'3.0.0','updated':L['updated'],'nodes':nodes,'edges':edges,'work_bindings':[{'work_id':r['id'],'node_ids':['route-'+r['layer']['route']]} for r in main]}
spaces=[]
for slot in L['spaces']:
 s={**slot};s['main_ids']=[k for k in s['evidence_ids'] if k in mainids and B[k]['route']==s['route']];s['reference_ids']=[k for k in s['evidence_ids'] if k not in s['main_ids']]
 s['coverage']='主图有对应实例' if s['main_ids'] else ('只有候选 / 范围外参考' if s['reference_ids'] else '本次调查未确认实例');spaces.append(s)
a={'updated':L['updated'],'version':'2.0.0','counts':counts,'placement_counts':placements,'route_counts':route_counts,'main_count':len(main),'reviewed_count':len(reviewed),'scope_counts':J('data/scope-review.json')['counts'],'discovery_count':len(J('data/discovery-pool.json')['entries']),'warning':Q['status'],'criteria':Q['criteria'],'families':Q['families'],'works':rows,'nodes':nodes,'edges':edges,'relations':Q['relations'],'routes':L['routes'],'spaces':spaces,'placement_labels':PL,'contribution_axes':L['contribution_axes'],'threshold':L['threshold_basis'],'minimum_total_parameters_b':L['minimum_total_parameters_b'],'priority_queue':Q['priority_queue'],'rejection_policy':Q['rejection_policy']}
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
 y=180+i*280;f.rect(60,y,1380,250);f.text(85,y+18,f'{i+1:02d}  {rt["title"]}',34,TEAL)
 f.text(85,y+75,rt['subtitle'],25,INK)
 f.para(85,y+120,rt['criterion'],410,23)
 f.line(530,y+26,530,y+224)
 names=' / '.join(r['short'] for r in main if r['layer']['route']==k)
 yy=f.para(560,y+24,names,850,26,INK)
 details={'harness':'功能：信息记忆 · 工具行动 · 组织搜索 · 学习研发 · 评价选择 · 执行资源','model':'已纳入：70B 自评价 SFT；70B 迭代 DPO。参数化评价器归 Model。','hybrid':'27B MASS：两轮交替；30B-A3B：序列联合适配。后者未实证持续多轮闭环。'}
 f.para(560,max(y+132,yy+16),details[k],850,23,TEAL)
f.rect(60,1050,1380,105,INK,INK)
f.text(84,1066,f'{len(main)} 项主视图  /  {len(reviewed)} 项命题卡片  /  {len(rows)} 项书目',28,WHITE)
f.text(84,1110,'Model / 混合：实际训练总参数 ≥27B；未知、低于门槛与非闭环支撑另列。',23,WHITE)
f.text(62,1180,'2026-10-18  |  这是已审样本，不是全领域分布或完备性证明。',21,MUTED);f.save('knowledge-tree')
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
md=['# BeforeRSI 三层研究地图','',f'更新：{L["updated"]}。入口为 Harness、Model、Model × Harness；角色、算法、时间尺度、闭环与证据在各层内部说明。','', '**[打开可搜索离线 HTML](research/atlas/index.html)** · [图文导读 PDF](output/pdf/beforersi-research-atlas.pdf) · [分类原理与边界](research/atlas/classification.md)','', '![三层研究地图](assets/atlas/knowledge-tree.png)','', '## 先区分三个统计','',f'- 主视图 **{len(main)} 项**：Harness {route_counts["harness"]}、Model {route_counts["model"]}、混合 {route_counts["hybrid"]}。混合中的一次联合适配不冒充多轮递归。',f'- 已有 **{len(reviewed)} 项限定命题卡片**；有价值的参考不一定满足主图的规模与 RSI 边界。',f'- 完整书目 **{len(rows)} 项**，另有 {a["discovery_count"]} 个去重发现线索；线索与书目重叠，不相加、不作为覆盖率分母。','', '## 主线及其功能结构','', '| 主线 | 核心问题 | 主视图实例 |','|---|---|---|']
for k,rt in routes.items():md.append('| '+rt['title']+' | '+rt['question']+' | '+'、'.join(r['short'] for r in main if r['layer']['route']==k)+' |')
md+=['','Model / 混合的实际训练目标按总参数 ≥27B 筛选；MoE 激活量另报，教师/评审规模不能替代。Harness 主线不训练基座，不能套用被训练模型的门槛。该门槛是研究范围，不是质量定理。','', '## 三层之下不能再混淆的维度','', '- **Harness 的六类功能**：信息与记忆；工具与行动；组织与搜索；学习与研发；评价与选择；执行与资源。文件、MCP、skills 等是具体载体。','- **Model 的六个描述轴**：被训练角色；训练阶段；学习目标；参数更新算法；数据/时间方式；继承回流。on-policy 采样不等于在线 RL。','- **混合的关系强度**：并存 → 单向作用 → 序列联合适配 → 双向多轮回流；协同收益须另测。','- **A–F 贡献标签**：每项只提炼 1–3 个主要贡献，不填写六大类全部子项，不推测作者个人品味。','', '![对象与反馈关系](assets/atlas/feedback-map.png)','', '## 研究空间与未确认的位置','', '下表的候选与背景关联仅作检索线索，不能读成已审实例或全球研究空白。','', '| 主线 / 功能位置 | 当前证据状态 | 下一步应回答的问题 |','|---|---|---|']
for s in spaces:md.append('| '+routes[s['route']]['title']+' / '+s['title']+' | '+s['coverage']+' | '+s['open_question']+' |')
md+=['','## 逐项退出主图的理由','', '| 工作 | 当前去向 | 理由 |','|---|---|---|']
for r in reviewed:
 if not r['main_view']:md.append(f'| {r["short"]} | {PL[r["layer"]["placement"]]} | {r["layer"]["why"]} |')
md+=['','## 文件与证据','', '- [完整研究卡片](research/atlas/core-cards.md)：先列主图，后列规模参考、AI4AI 支撑与横向工具。','- [完整参考索引](research/atlas/references.md)：保留全部条目、阅读范围、纳入和规模决定。','- [筛选与待审](research/atlas/review-queue.md)：未知不伪装成低质量。','- [分类与原理](research/atlas/classification.md)：对象划分的相对完备性，以及它不能证明的事情。','- [层级和规模人工记录](data/layer-review.json)、[贡献记录](data/quality-review.json)、[生成图谱](data/research-atlas.json)。','', '三分法只解决对象表示；统一解释还需要机制和失效条件，统一预测还需要实测参数与跨分布检验。当前不宣称全领域已穷尽，亦不宣称建立了普适增长定律。','']
(R/'RESEARCH_ATLAS.md').write_text('\n'.join(md))
fields=[('principle','原理与操作'),('distinct_contribution','最值得保留的贡献'),('evidence','证据'),('scale','规模'),('limit','边界'),('insight','研究含义')]
ordered=main+[r for r in reviewed if not r['main_view']]
cm=['# 研究卡片：主视图与参考分列','',f'{len(main)} 项进入三层主图；共 {len(reviewed)} 项限定命题有卡片。结果为作者报告，未在本项目独立复现。','']
for r in ordered:
 b=r['layer'];cm+=['<a id="'+r['id']+'"></a>',f'## [{r["number"]:03d}] {r["short"]}','',f'**位置：** {routes.get(b["route"],{}).get("title","横向工具")} / {PL[b["placement"]]}。{b["why"]}','', '**主要贡献点：** '+'；'.join(k+' '+L['contribution_axes'][k] for k in b['focus'])+'。此为编辑判断，非作者个人能力评分。','', '**改变与回流：** '+b['changed']+'。'+b['return_path'],'']
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
(R/'research/atlas/index.html').write_text((R/'scripts/atlas-template.html').read_text().replace('__ATLAS_DATA__',json.dumps(a,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')))
# PDF uses the same records as the HTML, with explicit source links.
pdfmetrics.registerFont(TTFont('CJK',fontpath))
styles={name:ParagraphStyle(name,fontName='CJK',fontSize=size,leading=leading,wordWrap='CJK',textColor=colors.HexColor(color),spaceAfter=after) for name,size,leading,color,after in [('title',28,38,INK,16),('h1',20,29,INK,16),('h2',13,20,TEAL,9),('body',10,15.5,INK,8),('small',8.3,12.3,MUTED,6)]}
P=lambda t,style='body':Paragraph(t,styles[style]);safe=lambda t:html.escape(str(t));story=[]
def page(title,sub=None):
 if story:story.append(PageBreak())
 story.append(P(title,'h1'))
 if sub:story.append(P(sub,'small'))
page('BeforeRSI<br/>三层研究地图','2026-10-18 / v2.0 / 对象 → 机制 → 反馈 → 证据')
story += [P('Harness · Model · Model × Harness','h2'),P(f'{len(main)} 项主视图，{len(reviewed)} 项命题卡片，{len(rows)} 项完整书目。主图按实际改变的对象组织；规模、闭环与贡献分别核验。'),RLImage(str(R/'assets/atlas/knowledge-tree.png'),width=490,height=398.5),P('Model / 混合主视图：实际训练模型总参数 ≥27B。MoE 激活量单列；教师和评审的规模不替代训练对象。'),P('主图包含有明确边界的联合适配研究，不把一次联合适配说成多轮闭环。未声明全领域覆盖或独立复现。','small')]
page('01  分类简洁，解释不能简化','相对于已声明的系统边界，模型改变 / 外部机制改变组成三个非空组合。对象覆盖不等于机制解释或预测。')
story +=[RLImage(str(R/'assets/atlas/feedback-map.png'),width=490,height=339.7),P('Harness 的六类功能','h2'),P('信息与记忆；工具与行动；组织与搜索；学习与研发；评价与选择；执行、环境与资源。知识库、数据库、skills、MCP 和文件属于具体载体。'),P('评价为什么不能单独固定归类？','h2'),P('改测评代码是 H；训练评价器是 M；二者都更新才可能是混合。内部评分变化还需独立评价锚点。'),P('A–F 只标主要贡献','h2'),P('每项只选 1–3 个贡献点。不逐篇填写所有目标、思想、理论、创新和迁移维度；不据机构推断作者的个人品味。')]
page('02  Model 与混合：怎样读训练')
for title,body in [('谁在学','执行者、评价者、奖励模型、世界模型、出题者或改进者。按实际改变的参数记录。'),('什么时候学','从零/继续预训练、后训练、测试时与持续适应；阶段与算法是两条轴。'),('怎样学','SFT、DPO、RL、蒸馏、元学习、结构变化；全参或 adapter 另报。on-policy 描述数据分布，不自动意味着 RL。'),('怎样进入下一轮','接续上轮参数；每轮重置学生但继承教师；群体继承；数据、奖励或改进行为反馈。'),('混合的证据强度','同时拥有 M/H → 单向作用 → 一次联合适配 → 实际双向多轮 → 在可比预算下测协同收益。每一步都需要新证据。'),('完备性的正确边界','三分法可覆盖已声明系统边界内的非空对象变化；不能据此声称已读完全部研究、已证明递归增长或建立物理普适定律。')]:story +=[P(title,'h2'),P(body)]
for k,rt in routes.items():
 page('03  研究空间 / '+rt['title'],'有主图实例、只有候选/范围外参考、本次未确认，三种状态分开。不能由本次缺项推出全球空白。')
 for s in [s for s in spaces if s['route']==k]:
  story +=[P(s['title']+' · '+s['coverage'],'h2'),P(s['objects'],'small'),P(s['open_question']),P('主图实例：'+(' / '.join(byid[x].get('short',byid[x]['name']) for x in s['main_ids']) or '无已确认主图实例')+'。候选/参考：'+(' / '.join(byid[x].get('short',byid[x]['name']) for x in s['reference_ids']) or '本次未确认'),'small')]
for k,rt in routes.items():
 rs=[r for r in main if r['layer']['route']==k]
 for start in range(0,len(rs),2):
  page('04  主视图 / '+rt['title'],'限定命题；证据为作者报告。主要贡献标签为本项目判读。')
  for r in rs[start:start+2]:
   b=r['layer'];story +=[P(f'[{r["number"]:03d}] '+safe(r['short']),'h2'),P('贡献点：'+' / '.join(x+' '+L['contribution_axes'][x] for x in b['focus']),'small'),P('<b>改变：</b>'+safe(b['changed'])),P('<b>回流：</b>'+safe(b['return_path'])),P('<b>价值：</b>'+safe(r['distinct_contribution'])),P('<b>证据：</b>'+safe(r['evidence'])),P('<b>边界：</b>'+safe(r['limit']))]
   if k!='harness':story +=[P('<b>训练：</b>'+safe(b['training']['algorithm']+'；'+b['training']['data_regime']),'small'),P('<b>规模：</b>'+safe(r['scale']),'small')]
   story +=[P(f'<link href="{safe(b["source_url"])}" color="{TEAL}">原文定位</link>：'+safe(b['source_location']),'small'),Spacer(1,13)]
excluded=[r for r in reviewed if not r['main_view']]
for start in range(0,len(excluded),4):
 page('05  保留参考，退出主图','范围或证据不满足主图，不等于具名质量否定。完整贡献卡片在离线 HTML 与 Markdown。')
 for r in excluded[start:start+4]:
  b=r['layer'];story +=[P(f'[{r["number"]:03d}] '+safe(r['short']),'h2'),P(PL[b['placement']]+'：'+safe(b['why'])),P('<b>可保留的机制：</b>'+safe(r['principle']),'small'),P(f'<link href="{safe(b["source_url"])}" color="{TEAL}">来源</link>：'+safe(b['source_location']),'small'),Spacer(1,12)]
for start in range(0,len(rows),12):
 page(f'06  完整书目 {start+1:03d}–{min(start+12,len(rows)):03d}','编号稳定，不代表重要性；尚未统一核准所有条目的首次发表年份。')
 for r in rows[start:start+12]:
  u=r.get('source_url') or r['primary_source'];story.append(KeepTogether([P(f'[{r["number"]:03d}] <link href="{safe(u)}" color="{TEAL}">{safe(r["name"])}</link> · {r["year"]}'),P(PL[r['layer']['placement']]+' | '+LABEL[r['admission']],'small')]))
def footer(c,doc):
 width,height=A4;c.setStrokeColor(colors.HexColor(LINE));c.line(46,39,width-46,39);c.setFont('CJK',8);c.setFillColor(colors.HexColor(MUTED));c.drawString(46,25,'BeforeRSI / 2026-10-18 / 三层研究地图 v2');c.drawRightString(width-46,25,str(doc.page))
out=R/'output/pdf/beforersi-research-atlas.pdf'
SimpleDocTemplate(str(out),pagesize=A4,rightMargin=46,leftMargin=46,topMargin=42,bottomMargin=52,title='BeforeRSI 三层研究地图',author='BeforeRSI research').build(story,onFirstPage=footer,onLaterPages=footer)
print(json.dumps({'main':len(main),'route_counts':route_counts,'reviewed':len(reviewed),'counts':counts,'placements':placements,'pdf_bytes':out.stat().st_size},ensure_ascii=False))
