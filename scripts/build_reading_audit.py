#!/usr/bin/env python3
"""Write the release's counting rules directly from the reviewed inventory."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
c=json.loads((ROOT/'data/corpus-review.json').read_text())
a=json.loads((ROOT/'data/literature-atlas.json').read_text())
n=c['counts'];sel=n['selection'];reading=n['reading'];rel=c.get('relation_counts',{})
lines=['# RSI 全量来源审查与取舍说明','',
 '版本日期：2026-10-19。固定清单的来源、逐项分析、选择理由及研究关系均保存在离线 HTML 和结构化记录中。','',
 '## 这次完成了什么','',
 f'固定清单 **{n["total"]} 条来源记录**，完成 **{n["reviewed"]} 条**，待完成 **{n["pending"]} 条**。清单由 567 条检索线索与 55 条未被该检索池覆盖的既有目录来源组成。按来源记录去重，并未声称这是全球全部论文，也没有把每个入口等同于一个独立 RSI 系统。','',
 '每条记录都分析实际更新对象、固定组件、反馈与继承、实验划分、基线、消融、计算成本、泛化证据、贡献、局限和相近工作。正文或附录未披露的条件保持未知。参数规模按实际被训练的对象判断，冻结教师和推理模型不充当训练规模。','',
 f'阅读依据：{reading.get("full_primary",0)} 条原文与相关技术附录；{reading.get("previous_primary_rechecked",0)} 条继承此前原文研读并在本次复核；{reading.get("public_materials",0)} 条官方报告、文档、博客或代码材料；{reading.get("blocked",0)} 条原文获取受阻。每条卡片列出具体阅读范围。阅读与推理分析不等于独立运行、训练或复现实验。','',
 '原始审查记录来自并行阅读批次，汇总时检查唯一 ID、来源位置、真实训练角色、关系类型及主图挂接。不是通过标题或摘要批量补写详细卡片。公开公司材料只支持已公开的实现与成果，不填补私有系统细节。','',
 '## 最终取舍及其含义','',
 '| 取舍 | 记录数 | 含义 |','|---|---:|---|']
meanings={
 'core':'对研究路线有代表性机制、强比较证据或关键反例；不等于每个结论都成立。',
 'support':'提供互补方法、评价、实证、工程实现或基础条件，保留完整阅读依据。',
 'mechanism_supplement':'有可解释机制，但与本图重点范围、模型规模或系统对象不完全一致。',
 'redundant':'机制或研究入口高度重叠，比较后不另占重点图谱位置。',
 'outside':'研究对象不符合本综述当前范围。',
 'insufficient':'可读材料不足以支持某项核心机制或结果判断；不等于证明研究劣质。',
 'blocked':'无法取得必要原文，记录障碍，不作贡献优劣判断。'}
for k,label in c['decisions'].items():lines.append(f'| {label} | {sel.get(k,0)} | {meanings[k]} |')
lines+=['',f'重点选择为 **{sel.get("core",0)} / {n["total"]}**（{sel.get("core",0)/n["total"]:.1%}）。这一比例是当前范围与证据比较的结果，没有预设 20% 配额。其余记录仍可搜索、阅读和沿关系访问，并未被统称为“无价值”。','',
 '## 三条路线与跨路线支撑','',
 '| 研究位置 | 已审查 | 重点 | 方法 / 证据补充 | 范围 / 机制参考 | 其他取舍 |','|---|---:|---:|---:|---:|---:|']
for rid,title in [('harness','Harness'),('model','Model'),('hybrid','Model × Harness'),('crosscut','跨路线支撑'),('background','历史与基础'),('outside','范围外')]:
 z=n['routes'].get(rid,{})
 lines.append(f'| {title} | {z.get("reviewed",0)} | {z.get("core",0)} | {z.get("support",0)} | {z.get("mechanism_supplement",0)} | {sum(z.get(k,0) for k in ("redundant","outside","insufficient","blocked"))} |')
lines+=['',
 'Harness：可跨任务或跨轮继承的提示、程序、记忆、技能、工具或控制机制更新。Model：基础模型权重或 adapter 更新，模型可扮演执行者、评价者、出题者或记忆管理者。Model × Harness：两类学习共同发生并有明确交互。任务内重试、固定训练程序更新数据池、外部候选程序变好，都需要与研究系统自身学习区别。','',
 '评价、理论和外部 AI4AI 研发可支撑三条路线，但不因此成为第四条系统路线。主图的 ≥27B 重点范围是显示与选题偏好，不是科学质量定理；小模型与未公开参数量分别记录。','',
 '规模未公开的核心工作会明确保留“不确定”，不会算作已经确认 ≥27B。若只公开某个 3B 子模型、同时实际训练另一规模未公开的模型，整个系统不能简写成“只训练 3B”，也不能宣称已经证实大模型规模。各角色与规模依据均在卡片中列出。','',
 '## 图、卡片与机构如何连接','',
 f'首页三张领域图先呈现研究主题及机制联系，再挂接工作。当前导航目录共 {a["counts"]["total"]} 项，重点选择全部挂接；完整来源索引仍为 {n["total"]} 条。目录数量、重点数量和阅读总量不可互相替代。','',
 'A–F 是阅读视角：目标与价值、关键思想、结构与原理、方法与比较、反馈与演化、成果与迁移。它不表示每篇论文都在六个方面有原创贡献。完整卡片另保留具体实验、资源、限制及来源定位。','',
 '机构类型与研究路线是两条独立维度。高校与科研机构、成熟工业研究团队、初创公司及独立研究者按来源分类；同一研究可以有多类机构合作，不能把交叉矩阵各行相加当总量。创始人以前的论文不会自动归入后来创办的公司。','',
 f'全量索引解析出 {rel.get("resolved",0)} 条记录间关系；其中原文明示 {rel.get("by_basis",{}).get("source_explicit",0)} 条，综述机制对照 {rel.get("by_basis",{}).get("analytical_comparison",0)} 条。另有 {rel.get("unresolved",0)} 条指向外部或尚未唯一匹配的名称，保留文字和来源，不制造节点。','',
 '采用、扩展仅用于原文明示的复用或继承；普通讨论不写成技术继承。综述比较另作标记。引用关系也不等于认同或验证了被引用工作。别名仅在可唯一核对时合并，保留 SWE-bench / SWE-Bench+ 等有意义的名称差别。','',
 '## 仍然存在的边界','',
 '这是固定清单的完整审查，不是对未公开研究、所有新论文或全球所有公司的完备证明。经验结果的适用范围由每篇论文的任务划分、预算、随机性与评价规则决定；未提供的多代增益、迁移或因果归因不由综述补出。','',
 '图谱是可修订的研究地图。选择理由、负结果和证据不足均公开保留，后续原文版本或独立复现可以改变当前判断。','',
 '离线 HTML 的搜索、卡片、分页、图谱筛选、双向关系和嵌入数据由自动检查验证。当前运行环境没有完成真实浏览器截图验收，不声称已做该项视觉验证。','',
 '数据文件：`data/full-reading-entries.json`、`data/reading-reviews/`、`data/corpus-review.json`、`data/corpus-curation.json`、`data/corpus-relation-aliases.json`（如有）。公开原文链接和内容摘要哈希保留；离线包不重新分发整篇第三方论文。','']
(ROOT/'research/atlas/reading-audit.md').write_text('\n'.join(lines))
print(f'Reading audit written: {n["reviewed"]}/{n["total"]}; core {sel.get("core",0)}.')

# The distribution README is generated from the same ledger, avoiding stale
# counts from the former 138/141-item catalog.
readme = [
 '# RSI Field Atlas · 全量来源审查版', '',
 '本地打开 **RSI_Field_Atlas_v5_1.html**。不需要服务器、API key 或联网；点击原文链接时才需要网络。`index.html` 是相同文件。', '',
 f'截至 2026-10-19，固定清单 {n["total"]} 条来源记录中已完成 {n["reviewed"]} 条逐项分析，待完成 {n["pending"]} 条。重点 {sel.get("core",0)} 条，其余保留方法补充、机制参考、相近、范围外或证据不足等具体理由。完整口径见 [审查与取舍说明](reading-audit.md)。', '',
 '## 从三张知识图谱开始', '',
 '首页直接呈现 Harness、Model、Model × Harness 三张领域图，包含 29 个主题、146 个子问题和 60 条机制联系。先看研究问题与更新对象，再查看对应论文、团队及原文。评价、理论和外部 AI4AI 作为跨路线支撑展示。', '',
 '默认论文图呈现重点研究；可切换到方法与证据补充，并开启小模型机制参考。所有来源仍能从全量搜索进入完整阅读记录。领域图的主题联系与论文之间的来源关系分别说明。', '',
 '## 阅读顺序', '',
 '1. 首页选择一条路线，点击主题，了解问题、机制与相邻联系。',
 '2. 打开论文卡片，先读 A–F，再查看更新对象、实验、资源、局限及原文位置。',
 '3. 通过关系查看前作、采用的方法、比较对象和互补机制；综述分析与作者明示分开标记。',
 '4. 在机构视图按高校科研、工业研究团队、初创公司与独立研究者交叉浏览。联合工作可属于多个机构类别，不能按类别相加计总数。',
 '5. 用全量搜索或取舍页查阅未进主图的来源及原因；未入重点不等于劣质。', '',
 f'导航目录 {a["counts"]["total"]} 项与完整来源清单 {n["total"]} 条是不同口径。公司入口有 27 个公开资料档案，不能当作全球公司普查或 27 个已验证 RSI 系统。', '',
 '## 证据与范围', '',
 '实际学习的权重或 adapter 决定 Model 归属；冻结教师不计入训练规模。持久提示、代码、记忆、工具和控制机制决定 Harness 归属。两种学习共同发生且有交互才归混合路线。任务内重试或外部候选程序变好不自动成立系统自改进。', '',
 '≥27B 是 Model/混合主图的选题范围偏好，不是质量定理。小模型和参数未公开分别记录，未披露的训练成本、迁移与多代进步不会补写成事实。全文分析不等于独立复现，也不意味着全球资料已经穷尽。', '',
 '## 数据与重建', '',
 '`data/full-reading-entries.json` 固定来源清单；`data/reading-reviews/` 逐项审查与横向综合；`data/corpus-review.json` 全量索引；`data/corpus-curation.json` 主图挂接；`data/corpus-relation-aliases.json` 经核对的别名。其他图谱、机构和公司数据分别保留来源。', '',
 '```bash',
 'python scripts/build_corpus_review.py --require-complete',
 'python scripts/integrate_corpus_reviews.py',
 'python scripts/integrate_corpus_relations.py',
 'python scripts/build_literature_graphs.py',
 'python scripts/build_reading_audit.py',
 'python scripts/check_literature_graphs.py',
 'node scripts/check_atlas_ui.cjs',
 '```', '',
 '自动检查覆盖数据一致性、三图、搜索、卡片、分页、筛选和双向关系。真实浏览器截图检查需另设 CHROMIUM_PATH；本轮没有完成这项视觉验收。离线包不分发整篇第三方论文，仅保留分析、公开链接与来源哈希。', '',
 '[领域结构](field-guide.md) · [图谱阅读档案](literature-cards.md) · [参考文献](references.md) · [机构](actor-guide.md) · [公司](industry-guide.md)', ''
]
(ROOT/'research/atlas/README.md').write_text('\n'.join(readme))
