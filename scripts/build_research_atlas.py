#!/usr/bin/env python3
"""Build the curated atlas from claim reviews and the existing corpus (no web inference)."""
import json, html, math, os, textwrap, re
from pathlib import Path
from collections import Counter
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image as RLImage, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
R=Path(__file__).resolve().parents[1]
J=lambda p:json.loads((R/p).read_text())
Q=J('data/quality-review.json');W=J('data/works.json')['works'];S={x['id']:x for x in J('data/scope-review.json')['works']};M={x['id']:x for x in J('data/mechanisms.json')['works']};X={x['id']:x for x in J('data/expansion-reviews.json')['works']};D={x['id']:x for x in Q['decisions']};C={x['id']:x for x in Q['core_cards']}
LABEL={'core':'核心命题','pending':'候选待审','historical':'历史与机制参考','background':'背景移出','low_value':'低价值排除'}
rows=[]
for n,w in enumerate(W,1):
 k=w['id'];r={**w,**S[k],**D[k],'number':n,'mechanism':M[k]['mechanism_interpretation'],'intervention':M[k]['separating_intervention'],'reading_scope':S[k]['reading_scope'],'tasks_and_resources':X.get(k,{}).get('tasks_and_resources','本轮未统一提取；不可据机构或模型名称推测。')}
 if k in C:r.update(C[k]);r['tasks_and_resources']=C[k]['scale'];r['reading_scope']=C[k]['source_location']+'；选定方法/证据阅读，未声明逐页完整精读。'
 if k=='openrsi':r['name']='Frontis-MA1 / OpenMLE（原目录入口 OpenRSI）'
 rows.append(r)
ids={r['id'] for r in rows};core={r['id'] for r in rows if r['admission']=='core'}
assert len(rows)==len(ids)==123
assert core==set(C) and all(C[k]['family'] in {f['id'] for f in Q['families']} for k in core)
assert all(x['source'] in core and x['target'] in core for x in Q['relations'])
counts=dict(Counter(r['admission'] for r in rows));counts['low_value']=0
nodes=[{'id':'family:'+f['id'],'type':'mechanism','label':f['title']} for f in Q['families']]+[{'id':k,'type':'admitted_claim','label':C[k]['short']} for k in C]
edges=[{'source':'family:'+C[k]['family'],'target':k,'type':'curated_membership'} for k in C]+Q['relations']
a={'updated':Q['updated'],'counts':counts,'scope_counts':J('data/scope-review.json')['counts'],'discovery_count':len(J('data/discovery-pool.json')['entries']),'warning':Q['status'],'criteria':Q['criteria'],'families':Q['families'],'works':rows,'nodes':nodes,'edges':edges,'priority_queue':Q['priority_queue'],'rejection_policy':Q['rejection_policy']}
(R/'data/research-atlas.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')

# The canonical graph now contains only admitted works; keep full-corpus indexing separate.
canonical_nodes=[{'id':'mechanism-'+f['id'],'type':'concept','label':f['title']} for f in Q['families']]+[{'id':k,'type':'work','label':C[k]['short']} for k in C]
canonical_edges=[{'source':'mechanism-'+C[k]['family'],'target':k,'relation':'curated_membership'} for k in C]+[{'source':r['source'],'target':r['target'],'relation':r['type']} for r in Q['relations']]
canonical={'schema_version':'2.0.0','updated':Q['updated'],'nodes':canonical_nodes,'edges':canonical_edges,'work_bindings':[{'work_id':k,'node_ids':['mechanism-'+C[k]['family']]} for k in C]}
(R/'data/knowledge-graph.json').write_text(json.dumps(canonical,ensure_ascii=False,indent=2)+'\n')

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
f=Figure(1500,1440)
f.text(60,38,'BeforeRSI  /  核心研究知识树',42)
f.text(62,108,'按具体贡献纳入 23 项工作；不是整个领域的完备性或质量排名',24,MUTED)
f.rect(60,166,1380,72,INK,INK);f.text(86,181,'主问题：AI 怎样改善产生后续能力的过程，并让有用改进进入下一轮？',29,WHITE)
for i,fam in enumerate(Q['families']):
 col=i%2;row=i//2;x=60+col*710;y=272+row*268;ww=670 if i<6 else 1380
 f.rect(x,y,ww,242);f.text(x+22,y+16,f'{i+1:02d}  '+fam['title'],28,TEAL)
 f.para(x+22,y+65,fam['question'],ww-44,24,INK)
 names=' / '.join(C[k]['short'] for k in C if C[k]['family']==fam['id'])
 yy=f.para(x+22,y+109,names,ww-44,23,MUTED)
 if i==6:f.text(x+22,y+174,'图上纳入的是限定的机制/证据；待审、历史参考、背景与低价值排除均不充入主图。',24,MUTED)
f.text(62,1375,'2026-10-18  |  原文、定位、规模、限制与判读见逐项卡片  |  关系不自动代表论文引用',23,MUTED)
f.save('knowledge-tree')
g=Figure(1500,870);g.text(60,35,'从“任务做得更好”到“更会产生下一代改进”',39)
g.text(62,96,'这是分析图：箭头表示过程依赖，不保证收益为正，也不预设唯一更新顺序。',24,MUTED)
boxes=[(60,185,420,195,'1  产生干预','改代码、更新权重、造数据、造奖励、调课程与环境','SEAL / DERL / HyperAgents'),(540,185,420,195,'2  执行并获得反馈','实际训练或运行，保留决策输入、失败与外部结果','EvoTrainer / GPT-Red / RLAnything'),(1020,185,420,195,'3  选择与继承','接受、组合、蒸馏或保留谱系；同时计成本与回退','DGM / MASS / ModularRSI')]
for x,y,w,h,title,body,ex in boxes:
 g.rect(x,y,w,h);g.text(x+22,y+18,title,29,TEAL);g.para(x+22,y+67,body,w-44,25);g.para(x+22,y+144,ex,w-44,20)
for x in [480,960]:g.line(x+5,285,x+54,285,TEAL,4);g.line(x+45,278,x+54,285,TEAL);g.line(x+45,292,x+54,285,TEAL)
g.line(1220,380,1220,450,TEAL,4);g.line(1220,450,270,450,TEAL,4);g.line(270,450,270,382,TEAL,4);g.text(420,409,'实际回流：后继参与下一轮干预生成',26,TEAL)
g.rect(60,510,670,220);g.text(84,530,'共同目标比较',29,INK);g.para(84,585,'固定目标初态、反馈与预算，更换父代/后继改进者，比较它们产生的目标增益。',620,26);g.text(84,678,'AIDE² / HGM / Harness Updating ≠ Benefit',22,TEAL)
g.rect(770,510,670,220);g.text(794,530,'外部评价与资源',29,INK);g.para(794,585,'任务与评分也可能变化；检验新任务、成本、回退和反馈来源，避免内部得分自证。',620,26);g.text(794,678,'RQGM / Rethinking Evaluation / SoL-Pi',22,TEAL)
g.text(62,794,'M / H / D 是工件坐标；解释需要指出改了哪条反馈、学习、选择和复用路径。',26,MUTED);g.save('feedback-map')
# Markdown entry point and full cards, linked to machine-readable evidence.
md=['# BeforeRSI 中文研究地图','',f'更新：{Q["updated"]}。这是可核对的当前研究底稿，不是“全领域已经调研完”的宣告。','',
'**先看 [图文导读 PDF](output/pdf/beforersi-research-atlas.pdf)，或下载打开 [可搜索离线地图](research/atlas/index.html)。** HTML 默认只显示核心；候选须主动切换，不能混入核心知识树。','',
'![核心知识树](assets/atlas/knowledge-tree.png)','',
'## 目前实际收集与筛选结果','',
'| 层级 | 数量 | 如何使用 |','|---|---:|---|',
'| 核心命题 | 23 | 方法/证据或形式定义有定位，明确说明纳入价值；只进入这部分的主图 |',
'| 候选待审 | 78 | 不等于低质量，也不作为已确认价值的核心文献；需进一步深读 |',
'| 历史与机制参考 | 16 | 包括 14 个基础条目及 Good / Gödel Machine；单列溯源 |',
'| 背景移出 | 6 | 普通模型训练与外围背景，不作为直接 RSI 成果 |',
'| 已具名判为低价值 | 0 | 本轮未完成这种判定，不表示所有工作优质 |','',
'另有 **567 个去重 arXiv 发现线索**，来自四份文献 README 快照。它们与 123 条目录存在重叠，不能相加为 690，也不能作为质量或覆盖率分母。发现线索不进入核心图。','',
'旧目录的 63 直接主题 / 30 支撑 / 7 评测 / 3 理论 / 14 基础 / 6 背景是**相关性分类**；此处 23 / 78 / 16 / 6 是**图谱纳入决定**，两套统计用途不同。','',
'## 质量门槛与阅读边界','']+['- '+t for t in Q['criteria']]+['',
'核心卡片是有理由的研究选择，仍不是独立复现或整篇质量认证。EvoTrainer 按训练侧系统设计纳入；GAI 按形式区分纳入，不能读成因果效果或增长定理。其余卡片也只支持各自写明的命题。','',
'新增 56 项中的 46 项最初仅做摘要筛查，均未直接升级为主图文献。原有目录也不一律视为全文精读。每项的新阅读记录在卡片中给出。','',
'## 七条机制线','', '| 分支 | 核心问题 | 代表工作 |','|---|---|---|']
for fam in Q['families']:md.append('| '+fam['title']+' | '+fam['question']+' | '+'、'.join(C[k]['short'] for k in C if C[k]['family']==fam['id'])+' |')
md+=['','![反馈与继承分析图](assets/atlas/feedback-map.png)','',
'## 关系的含义','',
'关系数据区分 **原文明示扩展**、**原文明示比较**、**我们的机制比较**。当前只记录 2 条经本轮定位确认的论文关系和 6 条分析关系；这不是已经构建完的引文网络。`data/knowledge-graph.json` 现在仅含核心工作；完整书目留在独立目录。图中机制归类与分析比较不是引用关系。','',
'| 两项工作 | 关系与依据 |','|---|---|']
for rel in Q['relations']:md.append('| '+C[rel['source']]['short']+' / '+C[rel['target']]['short']+' | '+rel['label']+(f'；[定位]({rel["source_url"]}) {rel["location"]}' if rel.get('source_url') else '')+' |')
md+=['','## 对当前理论的约束','',
'1. **描述对象不等于解释机制。** M/H/D 可记录工件，真正比较的是干预如何改变信息、学习、选择与后续改进。',
'2. **固定外层并不排除有价值学习。** 但它与后继接管外层是不同命题；AIDE² 为此另设测试。',
'3. **协同收益不预设为正。** MASS 的回退及 on-policy 研究的模仿退化要求显式记录不匹配。',
'4. **反馈来源是理论的一部分。** 搜索引入外部信息，构造标签提供锚点，对手与评价器改变评分语义。',
'5. **成本至少分研发、目标训练、部署与评价。** token、GPU 小时、动作数、墙钟时间不能无转换地横比。',
'6. **通用性要落实到预测。** 这些工作要求的机制已被整理，但尚未证明一个统一模型能定量预测全部家族。','',
'## 深读的次序','',
'先用 **SEAL → DERL → AIDE²** 分清“学会回答、学会构造更新、学会继续研发”；再用 **HyperAgents / HGM** 理解元层与延续价值；用 **Skill-SP / GPT-Red / RQGM** 理解协同反馈；最后用 **MASS / On-policy co-evolution / Rethinking Evaluation** 检验负迁移与成本。箭头只表示建议阅读顺序。','',
'## 文件入口','',
'- [23 项中文研究卡片](research/atlas/core-cards.md)：原理、差异、证据、规模、边界、思想与路线含义。',
'- [123 项完整参考索引](research/atlas/references.md)：有稳定编号、纳入状态和全部原文链接。',
'- [候选与暂不纳入理由](research/atlas/review-queue.md)：按每一项给出决定，不以“未读”冒充“低质”。',
'- [质量与纳入数据](data/quality-review.json)、[整合图谱数据](data/research-atlas.json)。',
'- [旧机制目录](research/mechanism-map.md)、[相关性目录](research/scope-catalog.md)、[理论](THEORY.md)。','']
(R/'RESEARCH_ATLAS.md').write_text('\n'.join(md))
cm=['# 核心研究卡片（23 项）','','限定命题纳入；所有结果为作者报告，未在本项目独立复现。差异、价值与路线含义属于本项目判读，不宣称穷尽创新优先权。','']
fields=[('principle','原理与操作'),('distinct_contribution','差异与价值判读'),('evidence','已核对的证据'),('scale','规模与范围'),('limit','不能推出的结论'),('insight','对我们研究的含义'),('source_location','阅读定位')]
for r in rows:
 if r['admission']!='core':continue
 cm+=['<a id="'+r['id']+'"></a>',f'## [{r["number"]:03d}] {r["short"]} · {r["year"]}','','[原始来源]('+r['source_url']+') · '+r['institutions'],'']
 for key,title in fields:cm+=['**'+title+'：** '+r[key],'']
 cm+=['**阅读状态：** 选定方法/证据段落，未声明逐页完整精读；全文附录、实现重跑和所有统计细节并未全部完成。','']
(R/'research/atlas/core-cards.md').write_text('\n'.join(cm))
ref=['# 全部 123 项参考索引','','编号固定于本次目录顺序，不代表质量名次；年份沿用原始目录，不是统一核准的首次发表年份。论文、博客与代码若属于同一工作，合并列出。这里只是书目，不是核心知识图。','']
for r in rows:
 ref += [f'### [{r["number"]:03d}] {r["name"]} ({r["year"]})',f'状态：**{LABEL[r["admission"]]}**；主题：{S[r["id"]]["scope"]}。',r['reason'],'阅读：'+r['reading_scope']]
 urls=list(dict.fromkeys([s['url'] for s in r['sources']]+([r['source_url']] if r.get('source_url') else [])))
 ref += [' · '.join(f'[来源 {i+1}]({u})' for i,u in enumerate(urls)),'']
(R/'research/atlas/references.md').write_text('\n'.join(ref))
queue=['# 深读队列与暂不纳入决定','','未纳入不等于已证明低质量。以下工作不进入当前核心图；优先次序由能否改变我们的机制判断决定。','']
for t in Q['priority_queue']:queue+=['## '+t['question'],'、'.join(next(w['name'] for w in W if w['id']==k) for k in t['ids']),'']
queue+=['## 候选逐项决定','','| 编号 | 工作 | 理由 |','|---|---|---|']
for r in rows:
 if r['admission']=='pending':queue.append(f'| {r["number"]:03d} | [{r["name"]}]({r["primary_source"]}) | {r["reason"]} |')
queue+=['','## 另行保留的发现记录','','5 项此前延后候选、3 个检索缺口和一次年份纠错仍在 [相关性目录](../scope-catalog.md) 及其数据中保留。它们不因标题含 RSI 自动进入核心。','',
'## 要完成“透彻理解”还差什么','','对每篇补齐：完整主文与附录、公式假设与推导、算法实现对应、消融和统计可信度、训练/筛选/测试边界、模型与 GPU/时间/人工成本、跨域外推范围、同机制先行工作比较。已有卡片未填的量必须保持未知。']
(R/'research/atlas/review-queue.md').write_text('\n'.join(queue))
# Offline HTML contains the complete data; no network or build server needed.
t=(R/'scripts/atlas-template.html').read_text();t=t.replace('__ATLAS_DATA__',json.dumps(a,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'))
(R/'research/atlas/index.html').write_text(t)
# PDF: curated guide and complete index, with explicit per-source locations.
pdfmetrics.registerFont(TTFont('CJK',fontpath))
styles={
 'title':ParagraphStyle('title',fontName='CJK',fontSize=30,leading=40,textColor=colors.HexColor(INK),spaceAfter=18),
 'h1':ParagraphStyle('h1',fontName='CJK',fontSize=20,leading=29,textColor=colors.HexColor(INK),spaceAfter=16),
 'h2':ParagraphStyle('h2',fontName='CJK',fontSize=13,leading=19,textColor=colors.HexColor(TEAL),spaceAfter=8),
 'body':ParagraphStyle('body',fontName='CJK',fontSize=10,leading=15.2,wordWrap='CJK',textColor=colors.HexColor(INK),spaceAfter=7),
 'card':ParagraphStyle('card',fontName='CJK',fontSize=10.2,leading=15.5,wordWrap='CJK',textColor=colors.HexColor(INK),spaceAfter=7),
 'small':ParagraphStyle('small',fontName='CJK',fontSize=8.3,leading=12,wordWrap='CJK',textColor=colors.HexColor(MUTED),spaceAfter=5)}
def P(t,style='body'):return Paragraph(t,styles[style])
def safe(t):return html.escape(t).replace('\n','<br/>')
story=[]
def page(title,sub=None):
 if story:story.append(PageBreak())
 story.append(P(title,'h1'))
 if sub:story.append(P(sub,'small'))
page('BeforeRSI<br/>核心研究地图','2026-10-18  /  中文图文导读与完整参考索引  /  v1.0')
story+=[P('从论文清单，进入可以比较的原理、证据与路线。','h2'),Spacer(1,9),P('当前 123 项已编目工作，被重新分成 23 项核心命题、78 项候选待审、16 项历史与机制参考、6 项背景。另有 567 个发现线索，不能当作已读论文或质量分母。'),RLImage(str(R/'assets/atlas/feedback-map.png'),width=500,height=290),Spacer(1,12),P('本册的核心选择','h2'),P('一项工作必须能改变我们的机制理解、实验判断、形式边界或实际研发路线，才进入主图。纳入的是明确的研究命题；不把整篇论文的宏大叙事一并接收。'),P('阅读导航：知识树 → 质量边界 → 关系与理论约束 → 23 项卡片 → 全部 123 项索引。可搜索 HTML 默认只显示核心，候选另页查看。'),P('全部原文链接可点击。研究结果均为作者报告；未宣称独立复现、逐页精读全部材料或完成全领域覆盖。','small')]
page('01  核心知识树','图中分组为本项目的机制归类。它不代表论文引用、历史传承、质量名次或已证明的递归层级。')
story.append(RLImage(str(R/'assets/atlas/knowledge-tree.png'),width=500,height=480))
story.append(P('七条线共同约束理论：谁产生改动、什么被改、反馈从哪里来、怎样被继承、是否进入下一轮，以及付出多少代价。','body'))
page('02  质量、规模与阅读深度')
for text in Q['criteria']:story.append(P('• '+safe(text)))
story += [Spacer(1,10),P('为什么没有把 123 项全部画进去？','h2'),P('旧目录按主题相关性收录。主图还需要贡献与证据判断，因此 78 项保留为候选，不会因为含“自进化”就升级。发现池更只承担召回作用。'),P('“低价值排除”当前具名计数为 0，表示尚未完成这种判定，不表示所有工作都好。证据不足与质量已被否定是两种状态。'),P('小规模与低价值怎样区别？','h2'),P('SEAL 的 ARC 子实验只有筛选后的 11 个训练任务与 8 个评测任务；这严重限制外推，但不抹去“按更新后的学习效果训练编辑生成策略”这一可复用原理。反之，大机构也不能靠品牌补足对照与成本。'),P('一次明确的降级','h2'),P('Co-Harness 仍在候选库：本轮补读的两轮、两尺度、三组各 30 题实验，所列基线未充分分离单独 SFT 与联合演化的贡献。它可以提供设计思路，目前不作为核心协同因果证据。'),P('核心也分证据类型','h2'),P('EvoTrainer 按训练侧系统设计纳入；Generalized Agent Iteration 按形式区分纳入。工程可运行、方法有价值、效应可信、可泛化，不能互相替代。')]
page('03  知识关系与理论约束')
for rel in Q['relations']:
 label='原文关系' if rel['type'].startswith('explicit') else '分析比较'
 story.append(P(f'<b>{safe(C[rel["source"]]["short"])} / {safe(C[rel["target"]]["short"])} [{label}]</b>','small'))
 story.append(P(safe(rel['label'])+(f'；{safe(rel["location"])}' if rel.get('location') else ''),'small'))
story += [Spacer(1,12),P('当前理论必须容纳的五个事实','h2')]
for t in ['任务分数与继续改进能力不同；未来分支价值也不同于当前分数。','固定训练器仍可训练出更好的改进行为；真正接管外层需另行比较。','模型和 harness 的联合更新可能负迁移，强教师不保证好训练数据。','评价器、课程、环境与对手变化会改变反馈语义，必须保留外部锚点。','研发、训练、部署和评价成本必须分开；形式覆盖尚不构成普适预测。']:story.append(P('• '+t))
story.append(P('M/H/D 是工件记录方式。若只把论文对象装入这三个桶，尚未解释论文为何成功或失败。统一理论的价值应表现为可检验的条件预测。','small'))
core_rows=[next(r for r in rows if r['id']==k) for k in C]
for start in range(0,len(core_rows),2):
 page(f'04  核心研究卡片  {start+1:02d}–{min(start+2,len(core_rows)):02d}','括号编号对应完整目录。差异与含义为本项目判读；证据和规模来自列出的原文段落。')
 for j,r in enumerate(core_rows[start:start+2]):
  if j:story +=[Spacer(1,18)]
  story.append(P(f'[{r["number"]:03d}] {safe(r["short"])} · {r["year"]}','h2'))
  for key,title in fields[:-1]:story.append(P(f'<b>{title}：</b>{safe(r[key])}','card'))
  story.append(P(f'<link href="{html.escape(r["source_url"],quote=True)}" color="{TEAL}">原文</link>：{safe(r["source_location"])}。<br/>阅读：方法/证据摘读；未声明完整逐页审核。','small'))
page('05  下一轮深读的实际问题')
for t in Q['priority_queue']:
 story.append(P(t['question'],'h2'));story.append(P(' / '.join(next(w['name'] for w in W if w['id']==k) for k in t['ids'])))
story +=[Spacer(1,10),P('每篇完整研究档案应补齐','h2'),P('原理与假设；与先行工作的真实差异；算法与实现对应；消融和统计；模型、任务、训练、部署、人工参与和资源；泛化边界；可复用的洞察；何种新证据会改变纳入决定。'),P('当前文件已将未知与已读分开。不能将这份整理说成已经完全理解全部 123 项，更不能说已经穷尽公开与未公开研究。','small')]
for start in range(0,len(rows),15):
 page(f'06  完整参考索引  {start+1:03d}–{min(start+15,len(rows)):03d}','相关性目录共有 123 项。这里的纳入状态不等于论文优劣排名；年份沿用原始目录。')
 for r in rows[start:start+15]:
  u=r.get('source_url') or r['primary_source']
  story.append(P(f'[{r["number"]:03d}] <link href="{html.escape(u,quote=True)}" color="{TEAL}">{safe(r["name"])}</link> · {r["year"]}','body'))
  story.append(P(LABEL[r['admission']]+' | '+('方法/证据摘读；定位见卡片' if r['admission']=='core' else ('摘要筛查；未升入主图' if 'abstract' in r['reading_scope'].lower() else '保留既有阅读边界；详见离线地图')),'small'))
# All page decorations are vector; charts are high-resolution original raster exports.
def footer(c,doc):
 w,h=A4;c.setStrokeColor(colors.HexColor(LINE));c.line(46,39,w-46,39);c.setFont('CJK',8);c.setFillColor(colors.HexColor(MUTED));c.drawString(46,25,'BeforeRSI  /  2026-10-18  /  当前证据底稿');c.drawRightString(w-46,25,f'{doc.page}')
out=R/'output/pdf/beforersi-research-atlas.pdf'
SimpleDocTemplate(str(out),pagesize=A4,rightMargin=46,leftMargin=46,topMargin=42,bottomMargin=52,title='BeforeRSI 核心研究地图',author='BeforeRSI research').build(story,onFirstPage=footer,onLaterPages=footer)
print(json.dumps({'works':len(rows),'counts':counts,'nodes':len(nodes),'edges':len(edges),'pdf_bytes':out.stat().st_size},ensure_ascii=False))
