# RSI 领域知识图谱 · v5.1

[打开三张领域图谱](research/atlas/RSI_Field_Atlas_v5_1.html) · [文字版研究结构](research/atlas/field-guide.md)

![首页三张领域图谱](assets/atlas/landscape-overview.png)

首页直接显示 Harness、Model、Model × Harness 三张领域图。29 个研究主题、其下的具体子问题以及 60 条机制联系先组织研究空间；论文、团队和机构再挂接到对应位置。主题间联系是综述归纳，论文间的引用、扩展和方法对照另行标注。

点击主题可展开关键问题、原理、技术、相邻关系与对应研究；点击箭头可看联系的含义和原文例证。本综述仅讨论公开研究，不包含项目自身理论或设计。

## 当前收录进度

| 路线 | 收录研究 | 方法段落已读 | 摘要初筛 |
|---|---:|---:|---:|
| Harness | 49 | 26 | 23 |
| Model | 36 | 16 | 20 |
| Model × Harness | 22 | 8 | 14 |

合计 107 项路线研究，另有 9 项跨路线评测/形式研究与 22 项历史、背景材料，共 138 项。路线数量包括相关技术和初筛候选，不等于认证的高质量 RSI 系统数。

49 条逐项解释的论文关系；机构署名与方法归类作为单独边类型。

## 阅读方式

1. 首页先读三张领域图；点击主题，展开子问题与具体方法。
2. 沿主题联系看经验、反馈、参数和程序怎样相互作用；论文不决定主题是否存在。
3. 读主题下的论文与团队，打开 A–F 研究卡片；卡片可以定位回相关领域主题。
4. 切换论文关系图，看明确引用、扩展与综述方法对照。
5. 使用全局检索查论文、机构、算法或任务。

已确认低于 27B 的 Model / 混合机制参考默认不出现在路线论文主视图，可在补充区或搜索中读取。未公开规模与低质量不是同一判断。

## 数据与复建

`data/field-knowledge.json` 保存领域主题、子问题、机制联系和论文挂接；`data/literature-editorial.json` 保存逐篇叙述与论文关系；`data/literature-atlas.json` 是阅读数据，`data/knowledge-graph.json` 是带来源的多关系图。

```bash
python scripts/build_literature_graphs.py
python scripts/check_literature_graphs.py
node scripts/check_atlas_ui.cjs
```

上一轮九页 PDF 是 2026-10-18 的导读快照；当前图谱以 v5.1 HTML 与上述数据为准。

## 公司与产业团队

公司索引共 27 项：24 项关联具体研究、1 项仅公开方向、2 项邻近研究待确认。关联 34 项去重研究；不是全球公司总数。

[公司与研究关联表](research/atlas/industry-guide.md) · 来源：`data/industry-landscape.json`。公司索引与各领域主题双向连接。

