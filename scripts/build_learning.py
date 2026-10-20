#!/usr/bin/env python3
"""Build the Chinese learning guide and standalone RSI atlas from repository sources."""
from pathlib import Path
import re, json, html, math, base64, io, hashlib
from xml.sax.saxutils import escape
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, CondPageBreak, Table, TableStyle, Image, Flowable, KeepTogether
from reportlab.platypus.tableofcontents import TableOfContents
from fontTools import subset
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs'; OUT.mkdir(exist_ok=True)
PDF=OUT/'Model_LLM_Learning_Manual.pdf'
ASSET=ROOT/'.cache/learning'; ASSET.mkdir(parents=True,exist_ok=True)
TMP=ASSET
plt.rcParams['svg.hashsalt']='BeforeRSI'

# Fixed upstream font revision; cache derived static faces locally.
FONT_REV='2894aab31764f10f29c421bdfd2340d3b382d384'
FONT_SHA='a3041811a78c361b1de50f953c805e0244951c21c5bd412f7232ef0d899af0da'
def prepare_fonts():
 from urllib.request import urlopen
 from fontTools.ttLib import TTFont as FontToolsFont
 from fontTools.varLib.instancer import instantiateVariableFont
 variable=ASSET/'NotoSansSC.ttf'
 if not variable.exists():
  url=f'https://raw.githubusercontent.com/google/fonts/{FONT_REV}/ofl/notosanssc/NotoSansSC%5Bwght%5D.ttf'
  variable.write_bytes(urlopen(url,timeout=60).read())
 if hashlib.sha256(variable.read_bytes()).hexdigest()!=FONT_SHA:
  raise ValueError('Unexpected Noto Sans SC font checksum')
 for name,weight in [('Regular',400),('Bold',700)]:
  path=ASSET/f'NotoSansSC-{name}.ttf'
  if not path.exists():
   font=FontToolsFont(variable,recalcTimestamp=False)
   instantiateVariableFont(font,{'wght':weight},inplace=True)
   font.save(path)
prepare_fonts()
FONT='NotoSC';BOLD='NotoSC-Bold'
pdfmetrics.registerFont(TTFont(FONT,str(ASSET/'NotoSansSC-Regular.ttf')))
pdfmetrics.registerFont(TTFont(BOLD,str(ASSET/'NotoSansSC-Bold.ttf')))
pdfmetrics.registerFontFamily(FONT,normal=FONT,bold=BOLD,italic=FONT,boldItalic=BOLD)
pdfmetrics.registerFont(TTFont('Code',str(Path(matplotlib.get_data_path())/'fonts/ttf/DejaVuSansMono.ttf')))
INK='#233746'; TEAL='#376d74'; PURPLE='#7759a3'; GOLD='#b98145'; LIGHT='#eef5f5';GRAY='#657783'; LINE='#d3e0e5'

def node(x,y,w,h,ls,fill='#ffffff',stroke=TEAL):return dict(x=x,y=y,w=w,h=h,lines=ls,fill=fill,stroke=stroke)
def arrow(*points,color=TEAL,dash=False):return dict(points=points,color=color,dash=dash)
FIGS={
'map':dict(w=900,h=335,caption='图 1　同一学习闭环：架构与计算规定可能性，反馈和更新决定经验怎样被保留。',
 nodes=[node(15,35,240,80,['任务、数据、环境','决定获得什么经验']),node(330,35,240,80,['模型 θ ＋ 上下文','产生回答、工具行动或新任务']),node(645,35,240,80,['反馈与选择','答案、偏好、执行、下游增益']),node(645,215,240,80,['训练目标与更新','SFT / DPO / RL / 元学习']),node(330,215,240,80,['新参数 θ′','保留可复用的行为变化']),node(15,215,240,80,['下一轮学习条件','新任务、评价、课程或改进器'],fill='#f4eff9',stroke=PURPLE)],
 arrows=[arrow((255,75),(330,75)),arrow((570,75),(645,75)),arrow((765,115),(765,215)),arrow((645,255),(570,255)),arrow((330,255),(255,255)),arrow((135,215),(135,115),color=PURPLE)],texts=[(450,164,'架构 A · 数据 D · 目标 O · 更新 U · 计算 C',20,GRAY)]),
'transformer':dict(w=900,h=460,caption='图 2　常见 pre-norm decoder block 示意。训练可并行计算位置，生成仍依赖已产生的前缀。',
 nodes=[node(35,180,155,90,['输入表示 X','token ＋ 位置']),node(280,50,255,70,['Norm → Attention','Q/K/V · 因果 mask']),node(280,180,255,70,['残差相加','X ＋ attention output']),node(280,310,255,70,['Norm → FFN → 残差','位置内非线性特征计算']),node(645,150,220,125,['重复 L 层','Norm → LM Head','logits → token 概率'])],
 arrows=[arrow((190,225),(235,225),(235,85),(280,85)),arrow((407,120),(407,180)),arrow((407,250),(407,310)),arrow((535,345),(590,345),(590,213),(645,213)),arrow((190,225),(280,225),color=GOLD),arrow((535,215),(560,215),(560,285),(510,285),(510,310),color=GOLD)],texts=[(133,292,'残差直连',18,GOLD),(748,328,'读取上下文 ＋ 变换特征',18,GRAY),(450,431,'KV cache 保存前缀的键和值；不等于跨会话知识记忆。',19,GRAY)]),
'bilevel':dict(w=900,h=380,caption='图 3　双层学习：改进器的反馈来自学习者更新后的下游效果。',
 nodes=[node(15,55,245,90,['改进器 φ','生成数据 / 更新指令']),node(330,55,245,90,['内层更新 U','θ ＋ 学习材料 → θ′']),node(645,55,240,90,['下游任务评价','J(θ′) 与代价']),node(330,245,245,80,['外层更新 φ','学习哪些改进真正有效'],fill='#f4eff9',stroke=PURPLE)],
 arrows=[arrow((260,100),(330,100)),arrow((575,100),(645,100)),arrow((765,145),(765,285),(575,285),color=PURPLE),arrow((330,285),(137,285),(137,145),color=PURPLE)],texts=[(450,202,'内层：学任务　　外层：学怎样让学习更有效',20,GRAY)]),
'coupling':dict(w=900,h=380,caption='图 4　双向耦合：外部流程改变经验，参数更新改变可用的流程。四种组合帮助定位收益。',
 nodes=[node(30,40,340,85,['模型参数 θ','行动、求解、评价与改进策略']),node(530,40,340,85,['外部系统 H','工具、工作流、技能、记忆']),node(30,220,340,90,['经验 → 参数','轨迹筛选、纠错、蒸馏、RL']),node(530,220,340,90,['参数 → 系统','生成、运行、选择并保留修改'])],
 arrows=[arrow((370,75),(530,75)),arrow((530,105),(370,105),color=PURPLE),arrow((200,125),(200,220)),arrow((700,125),(700,220)),arrow((370,265),(530,265),color=GOLD)],texts=[(450,169,'共同目标 J(θ,H)',23,TEAL),(450,354,'旧/旧　·　旧/新　·　新/旧　·　新/新',21,GRAY)]),
'signals':dict(w=900,h=350,caption='图 5　同一批轨迹可构成不同训练目标。算法名不决定反馈来自哪里。',
 nodes=[node(20,25,860,65,['候选 A、B、C、D　→　执行奖励 [1, 0, 1, 0]'],fill=LIGHT),node(20,155,260,145,['SFT','保留 A、C','模仿成功序列']),node(320,155,260,145,['DPO','构造成对偏好 A>B、C>D','优化相对 log-odds']),node(620,155,260,145,['GRPO','组内优势 [1, -1, 1, -1]','受控策略更新'])],
 arrows=[arrow((150,90),(150,155)),arrow((450,90),(450,155)),arrow((750,90),(750,155))],texts=[])
}

def svg_figure(key):
 f=FIGS[key];s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f["w"]} {f["h"]}" role="img" aria-label="{html.escape(f["caption"])}"><defs><marker id="ar-{key}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10Z" fill="{TEAL}"/></marker></defs>']
 for a in f['arrows']:
  p=' '.join(f'{x},{y}' for x,y in a['points']);s.append(f'<polyline points="{p}" fill="none" stroke="{a["color"]}" stroke-width="2" marker-end="url(#ar-{key})"/>')
 for n in f['nodes']:
  s.append(f'<rect x="{n["x"]}" y="{n["y"]}" width="{n["w"]}" height="{n["h"]}" rx="10" fill="{n["fill"]}" stroke="{n["stroke"]}" stroke-width="1.5"/>')
  top=n['y']+n['h']/2-(len(n['lines'])-1)*14
  for i,line in enumerate(n['lines']):s.append(f'<text x="{n["x"]+n["w"]/2}" y="{top+i*28+6}" text-anchor="middle" fill="{INK if i==0 else GRAY}" font-size="{22 if i==0 else 18}" font-weight="{650 if i==0 else 400}">{html.escape(line)}</text>')
 for x,y,t,size,col in f['texts']:s.append(f'<text x="{x}" y="{y}" text-anchor="middle" fill="{col}" font-size="{size}">{html.escape(t)}</text>')
 s.append('</svg>');return ''.join(s)

class Diagram(Flowable):
 def __init__(self,key,width=482):
  Flowable.__init__(self);self.key=key;self.width=width;self.height=width*FIGS[key]['h']/FIGS[key]['w']
 def draw(self):
  c=self.canv;f=FIGS[self.key];scale=self.width/f['w'];c.saveState();c.scale(scale,scale)
  def Y(y):return f['h']-y
  for a in f['arrows']:
   c.setStrokeColor(colors.HexColor(a['color']));c.setFillColor(colors.HexColor(a['color']));c.setLineWidth(2)
   p=c.beginPath();p.moveTo(a['points'][0][0],Y(a['points'][0][1]))
   for x,y in a['points'][1:]:p.lineTo(x,Y(y))
   c.drawPath(p)
   (x0,y0),(x1,y1)=a['points'][-2:];ang=math.atan2(y1-y0,x1-x0);ln=9
   p=c.beginPath();p.moveTo(x1,Y(y1));p.lineTo(x1-ln*math.cos(ang-.45),Y(y1-ln*math.sin(ang-.45)));p.lineTo(x1-ln*math.cos(ang+.45),Y(y1-ln*math.sin(ang+.45)));p.close();c.drawPath(p,stroke=0,fill=1)
  for n in f['nodes']:
   c.setFillColor(colors.HexColor(n['fill']));c.setStrokeColor(colors.HexColor(n['stroke']));c.setLineWidth(1.5);c.roundRect(n['x'],Y(n['y']+n['h']),n['w'],n['h'],10,fill=1)
   top=n['y']+n['h']/2-(len(n['lines'])-1)*14
   for i,t in enumerate(n['lines']):
    c.setFont(BOLD if i==0 else FONT,22 if i==0 else 18);c.setFillColor(colors.HexColor(INK if i==0 else GRAY));c.drawCentredString(n['x']+n['w']/2,Y(top+i*28+6),t)
  for x,y,t,size,col in f['texts']:c.setFont(FONT,size);c.setFillColor(colors.HexColor(col));c.drawCentredString(x,Y(y),t)
  c.restoreState()

source_md=(ROOT/'docs/model-llm.md').read_text()
raw=re.sub(r'<a id="chapter-[^"]+"></a>\s*','',source_md)
raw=re.sub(r'^\$\$\n(.*?)\n\$\$',lambda m:'$$ '+m[1]+' $$',raw,flags=re.M|re.S)
raw=re.sub(r'!\[[^\]]*\]\(figures/([a-z]+)\.svg\)',lambda m:'[[FIG:'+m[1]+']]',raw)
for key in FIGS:
 (OUT/'figures'/f'{key}.svg').write_text(svg_figure(key))
chapters=[]
for match in re.finditer(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)',raw,re.M|re.S):
 title=match.group(1);chap_id=title.split('｜')[0];chapters.append({'title':title,'key':chap_id,'text':match.group(2).strip()})

math_cache={}
def equation(eq):
 if eq in math_cache:return math_cache[eq]
 idx=len(math_cache)+1;prefix=ASSET/f'equation-{idx:02}'
 # Matplotlib's mathtext is deterministic and works offline.
 fig=plt.figure(figsize=(12,1),dpi=220);fig.patch.set_alpha(0);t=fig.text(.02,.5,'$'+eq+'$',fontsize=15,color=INK,ha='left',va='center')
 fig.canvas.draw();box=t.get_window_extent().expanded(1.035,1.8).transformed(fig.dpi_scale_trans.inverted())
 fig.savefig(str(prefix)+'.png',transparent=True,bbox_inches=box,dpi=300,pad_inches=.015)
 fig.savefig(str(prefix)+'.svg',transparent=True,bbox_inches=box,pad_inches=.015);plt.close(fig)
 svg=Path(str(prefix)+'.svg').read_text();svg=svg[svg.index('<svg'):]
 # Strip title/metadata; preserve paths for offline math rendering.
 svg=re.sub(r'<metadata>.*?</metadata>','',svg,flags=re.S)
 from PIL import Image as PImage
 im=PImage.open(str(prefix)+'.png');width=min(480,im.width*72/300);height=im.height*width/im.width
 math_cache[eq]=(str(prefix)+'.png',width,height,svg);return math_cache[eq]

def inline(s,pdf=False):
 s=html.escape(s)
 if pdf:
  for a,b in [('⁺','<super>+</super>'),('⁻','<super>-</super>'),('₁','<sub>1</sub>'),('₂','<sub>2</sub>')]:s=s.replace(a,b)
 s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>' if pdf else r'<strong>\1</strong>',s)
 s=re.sub(r'`([^`]+)`',r'<font name="Code">\1</font>' if pdf else r'<code>\1</code>',s)
 s=re.sub(r'\[([^\]]+)\]\((https://[^)]+)\)',lambda m:f'<a href="{m[2]}" color="{TEAL}">{m[1]}</a>' if pdf else f'<a href="{m[2]}" target="_blank" rel="noopener">{m[1]}</a>',s)
 if not pdf:s=re.sub(r'\[(\d+)\](?!\()',r'<button class="ml-ref" data-learn-ref="\1">[\1]</button>',s)
 return s

styles={
 'body':ParagraphStyle('Body',fontName=FONT,fontSize=10.5,leading=17.8,textColor=colors.HexColor(INK),spaceAfter=10,wordWrap='CJK',allowWidows=0,allowOrphans=0),
 'h2':ParagraphStyle('H2',fontName=BOLD,fontSize=21,leading=31,textColor=colors.HexColor(INK),spaceAfter=17,keepWithNext=1,wordWrap='CJK'),
 'h3':ParagraphStyle('H3',fontName=BOLD,fontSize=12,leading=19,textColor=colors.HexColor(TEAL),spaceBefore=12,spaceAfter=8,keepWithNext=1,wordWrap='CJK'),
 'small':ParagraphStyle('Small',fontName=FONT,fontSize=8.2,leading=12.6,textColor=colors.HexColor(GRAY),spaceAfter=10,wordWrap='CJK'),
 'table':ParagraphStyle('Table',fontName=FONT,fontSize=9.1,leading=14.2,textColor=colors.HexColor(INK),wordWrap='CJK'),
 'th':ParagraphStyle('TH',fontName=BOLD,fontSize=9.1,leading=14.2,textColor=colors.HexColor(TEAL),wordWrap='CJK'),
 'code':ParagraphStyle('Code',fontName='Code',fontSize=8,leading=12,textColor=colors.HexColor(INK),leftIndent=10,rightIndent=10,spaceAfter=3),
}

def parse_blocks(text):
 lines=text.splitlines();out=[];i=0
 while i<len(lines):
  line=lines[i].strip()
  if not line:i+=1;continue
  if line.startswith('### '):out.append(('heading',line[4:]));i+=1;continue
  if line.startswith('$$ '):out.append(('eq',line[3:-3].strip()));i+=1;continue
  if line.startswith('[[FIG:'):out.append(('fig',line[6:-2]));i+=1;continue
  if line.startswith('```'):
   code=[];i+=1
   while i<len(lines) and not lines[i].startswith('```'):code.append(lines[i]);i+=1
   i+=1;out.append(('code','\n'.join(code)));continue
  if line.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    row=[c.strip() for c in lines[i].strip().strip('|').split('|')]
    if not all(re.match(r'^:?-+:?$',x) for x in row):rows.append(row)
    i+=1
   out.append(('table',rows));continue
  parts=[line];i+=1
  while i<len(lines) and lines[i].strip() and not re.match(r'^(###|\$\$|\[\[FIG:|\||```)',lines[i]):parts.append(lines[i].strip());i+=1
  out.append(('p',' '.join(parts)))
 return out

def table_widths(rows,ch):
 cols=len(rows[0]);width=482
 if ch=='A':return [126,100,196,60]
 if ch=='B':return [45,320,117]
 if ch=='C':return [104,310,68]
 if cols==4:return [87,132,129,134]
 if cols==3:return [106,178,198]
 return [241,241]

def make_blocks(ch):
 flow=[];web=[]
 for typ,item in parse_blocks(ch['text']):
  if typ=='p':flow.append(Paragraph(inline(item,True),styles['body']));web.append('<p>'+inline(item)+'</p>')
  elif typ=='heading':
   hs=styles['h3']
   if ch['key']=='C':
    hs=ParagraphStyle('IndexHeading',parent=styles['h3'],keepWithNext=0);flow.append(CondPageBreak(120))
   flow.append(Paragraph(inline(item,True),hs));anchor=''
   m=re.match(r'\[(\d+)\]',item)
   if m:anchor=f' id="ml-source-{m[1]}"'
   web.append('<h3'+anchor+'>'+html.escape(item)+'</h3>')
  elif typ=='eq':
   f,w,h,svg=equation(item);flow.extend([Spacer(1,4),Image(f,w,h),Spacer(1,11)])
   web.append(f'<div class="ml-equation" aria-label="{html.escape(item)}">{svg}</div>')
  elif typ=='fig':
   flow.extend([Spacer(1,6),Diagram(item),Paragraph(FIGS[item]['caption'],styles['small'])]);web.append('<figure>'+svg_figure(item)+'<figcaption>'+FIGS[item]['caption']+'</figcaption></figure>')
  elif typ=='code':
   codes=[Paragraph(html.escape(line).replace(' ','&#160;'),styles['code']) for line in item.splitlines()]
   tab=Table([[x] for x in codes],colWidths=[482]);tab.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor(LIGHT)),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]));flow.extend([tab,Spacer(1,12)]);web.append('<pre><code>'+html.escape(item)+'</code></pre>')
  elif typ=='table':
   dat=[[Paragraph(inline(cell,True),styles['th'] if n==0 else styles['table']) for cell in row] for n,row in enumerate(item)]
   tab=Table(dat,colWidths=table_widths(item,ch['key']),repeatRows=1,hAlign='LEFT')
   tab.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),colors.HexColor(LIGHT)),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#fafcfc')]),('LINEBELOW',(0,0),(-1,0),.65,colors.HexColor(TEAL)),('LINEBELOW',(0,1),(-1,-1),.3,colors.HexColor(LINE)),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7)]))
   flow.extend([tab,Spacer(1,13)])
   web.append('<div class="ml-table-wrap"><table><thead><tr>'+''.join('<th>'+inline(c)+'</th>' for c in item[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in row)+'</tr>' for row in item[1:])+'</tbody></table></div>')
 ch['html']=''.join(web);return flow

class ManualDoc(BaseDocTemplate):
 def __init__(self,path):
  super().__init__(str(path),pagesize=(595.28,841.89),leftMargin=56.64,rightMargin=56.64,topMargin=66,bottomMargin=53,title='Model / LLM：从原理到自我改进',author='BeforeRSI contributors',pageCompression=1,invariant=True)
  self.running='Model / LLM';self.page_map={}
  self.addPageTemplates(PageTemplate(id='normal',frames=[Frame(56.64,53,482,722.89,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=self.page_header))
 def page_header(self,c,doc):
  if doc.page==1:return
  c.saveState();c.setFont(FONT,8.1);c.setFillColor(colors.HexColor(GRAY));c.drawString(56.64,806,'MODEL / LLM   ·   从原理到自我改进');c.drawRightString(538.64,806,'2026.10.20')
  c.setStrokeColor(colors.HexColor(LINE));c.setLineWidth(.5);c.line(56.64,795,538.64,795);c.line(56.64,39,538.64,39)
  c.setFont(FONT,8);c.drawString(56.64,25,'原理 → 机制 → 设计 → 自我改进');c.drawRightString(538.64,25,str(doc.page));c.restoreState()
 def afterFlowable(self,f):
  if hasattr(f,'chapter_key'):
   key=f.chapter_key;title=getattr(f,'chapter_title',f.getPlainText());self.canv.bookmarkPage('ch-'+key);self.canv.addOutlineEntry(title,'ch-'+key,0,False);self.notify('TOCEntry',(0,title,self.page,'ch-'+key));self.page_map[key]=self.page

class Cover(Flowable):
 def __init__(self):Flowable.__init__(self);self.width=482;self.height=700
 def draw(self):
  c=self.canv;c.saveState();c.setFillColor(colors.HexColor(TEAL));c.rect(0,660,57,5,stroke=0,fill=1);c.setFont(BOLD,11);c.drawString(0,626,'MODEL / LLM   ·   LEARNING MANUAL')
  c.setFillColor(colors.HexColor(INK));c.setFont(BOLD,37);c.drawString(0,543,'从原理到');c.drawString(0,490,'自我改进')
  c.setFont(FONT,16);c.setFillColor(colors.HexColor(GRAY));c.drawString(0,441,'模型设计、训练、推理、测评与学习闭环')
  c.setStrokeColor(colors.HexColor(LINE));c.line(0,399,482,399)
  c.setFillColor(colors.HexColor(INK));c.setFont(FONT,12)
  for i,line in enumerate(['用一条连续的因果链理解模型层：','数据与经验怎样产生学习信号，','信号怎样改变参数，参数怎样形成可复用能力。']):c.drawString(0,355-i*24,line)
  c.setFillColor(colors.HexColor(LIGHT));c.roundRect(0,147,482,102,9,stroke=0,fill=1)
  c.setFillColor(colors.HexColor(TEAL));c.setFont(BOLD,14);c.drawString(20,219,'29 章正文  /  148 组术语  /  43 项原始文献')
  c.setFont(FONT,11);c.drawString(20,191,'61 个基础主题，连接图谱 19 个分支、95 个子项。')
  c.drawString(20,171,'阅读路径、机制图、公式、算例和逐项索引。')
  c.setFont(FONT,10);c.setFillColor(colors.HexColor(GRAY));c.drawString(0,72,'中文学习版 · 2026 年 10 月 20 日');c.drawString(0,48,'与 RSI 图谱「收录说明」中的完整教程共用正文。');c.restoreState()

story=[Cover(),PageBreak(),Paragraph('阅读目录',styles['h2']),Paragraph('从基础到机制连续阅读；查词用附录 A，查找主题与图谱分支用附录 B、C。目录与 PDF 书签可点击跳转。',styles['body'])]
toc=TableOfContents();toc.levelStyles=[ParagraphStyle('TOC',fontName=FONT,fontSize=10,leading=19,textColor=colors.HexColor(INK),leftIndent=0,firstLineIndent=0,rightIndent=30,spaceBefore=2,wordWrap='CJK')];story.append(toc)
for ch in chapters:
 if ch['key'] in ['00','A','B','C','D']:story.append(PageBreak())
 else:story.extend([CondPageBreak(275),Spacer(1,21)])
 title=html.escape(ch['title'])
 if '：' in title:
  first,last=title.split('：',1);title=first+'<br/><font size="14" color="'+GRAY+'">'+last+'</font>'
 heading=Paragraph(title,styles['h2']);heading.chapter_key=ch['key'];heading.chapter_title=ch['title'];story.append(heading);story.extend(make_blocks(ch))
doc=ManualDoc(PDF);doc.multiBuild(story)
pages=len(PdfReader(PDF).pages)
(ASSET/'page_map.json').write_text(json.dumps(doc.page_map,ensure_ascii=False,indent=2))

CSS=(ROOT/'web/learning.css').read_text()

JS=(ROOT/'web/learning.js').read_text()

atlas=json.loads((ROOT/'data/atlas.json').read_text())
original=(ROOT/'web/atlas.html').read_text().replace('{{ATLAS_DATA}}',json.dumps(atlas,ensure_ascii=False,separators=(',',':')).replace('</',r'<\/'))
assert 'function coverage(){const rc=' in original
new=original.replace('function coverage(){const rc=','function coverage(){if(state.learningOpen)return mlView();const rc=',1)
new=new.replace('pool=A.discovery_coverage;return `<div class="eyebrow">CORPUS','pool=A.discovery_coverage;return mlEntry()+`<div class="eyebrow">CORPUS',1)
new=new.replace('收录说明<small>数量与阅读范围</small>','收录说明<small>完整教程 · 数量与阅读范围</small>')
# Insert the tutorial functions before the existing first render call: no network dependencies.
assert '\nrender();try{' in new
data={'version':'1.0','updated':'2026-10-20','pages':pages,'pageMap':doc.page_map,'chapters':chapters,'pdf':base64.b64encode(PDF.read_bytes()).decode(),'source_sha256':hashlib.sha256(source_md.encode()).hexdigest()}
datatag='<script id="model-learning-data" type="application/json">'+json.dumps(data,ensure_ascii=False).replace('</',r'<\/')+'</script>'
new=new.replace('<script id="literature-data"',datatag+'<script id="literature-data"',1)
new=new.replace('\nrender();try{','\n'+JS+'\nrender();try{',1)
new=new.replace('</script></body></html>','\ntry{const p=new URLSearchParams(location.hash.slice(1));if(p.has("learn"))mlOpen(p.get("learn"));else if(location.hash==="#coverage")setPage("coverage");}catch(e){}\n</script></body></html>',1)

# Embed one subset font: tutorial and original atlas are both legible offline.
chars=''.join(set(raw+re.sub('<[^>]+>','',original)))
font_path=ASSET/'AtlasSC.woff'
if True:
 options=subset.Options();options.flavor='woff';options.desubroutinize=True
 font=subset.load_font(str(ASSET/'NotoSansSC-Regular.ttf'),options)
 sub=subset.Subsetter(options=options);sub.populate(text=chars);sub.subset(font);subset.save_font(font,str(font_path),options)
fontcss='@font-face{font-family:AtlasSC;src:url(data:font/woff;base64,'+base64.b64encode(font_path.read_bytes()).decode()+') format("woff");font-weight:400;font-display:swap;}body{font-family:AtlasSC,"Microsoft YaHei",sans-serif;}'
new=new.replace('</head>','<style id="model-learning-style">'+fontcss+CSS+'</style></head>',1)
new=new.replace('</head>','<!-- Embedded Noto Sans SC: SIL Open Font License 1.1; see assets/fonts/OFL.txt. -->\n</head>',1)
output=OUT/'index.html';output.write_text(new)
(ASSET/'build_stats.json').write_text(json.dumps({'pages':pages,'chapters':len(chapters),'pdf_bytes':PDF.stat().st_size,'html_bytes':output.stat().st_size,'equations':len(math_cache),'source_sha256':data['source_sha256'],'page_map':doc.page_map},ensure_ascii=False,indent=2))
print((ASSET/'build_stats.json').read_text())
