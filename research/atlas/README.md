# RSI Field Atlas · 全量来源审查版

本地打开 **RSI_Field_Atlas_v5_1.html**。不需要服务器、API key 或联网；点击原文链接时才需要网络。`index.html` 是相同文件。

截至 2026-10-19，固定清单 622 条来源记录中已完成 622 条逐项分析，待完成 0 条。重点 77 条，其余保留方法补充、机制参考、相近、范围外或证据不足等具体理由。完整口径见 [审查与取舍说明](reading-audit.md)。

## 从三张知识图谱开始

首页直接呈现 Harness、Model、Model × Harness 三张领域图，包含 29 个主题、146 个子问题和 60 条机制联系。先看研究问题与更新对象，再查看对应论文、团队及原文。评价、理论和外部 AI4AI 作为跨路线支撑展示。

默认论文图呈现重点研究；可切换到方法与证据补充，并开启小模型机制参考。所有来源仍能从全量搜索进入完整阅读记录。领域图的主题联系与论文之间的来源关系分别说明。

## 阅读顺序

1. 首页选择一条路线，点击主题，了解问题、机制与相邻联系。
2. 打开论文卡片，先读 A–F，再查看更新对象、实验、资源、局限及原文位置。
3. 通过关系查看前作、采用的方法、比较对象和互补机制；综述分析与作者明示分开标记。
4. 在机构视图按高校科研、工业研究团队、初创公司与独立研究者交叉浏览。联合工作可属于多个机构类别，不能按类别相加计总数。
5. 用全量搜索或取舍页查阅未进主图的来源及原因；未入重点不等于劣质。

导航目录 174 项与完整来源清单 622 条是不同口径。公司入口有 27 个公开资料档案，不能当作全球公司普查或 27 个已验证 RSI 系统。

## 证据与范围

实际学习的权重或 adapter 决定 Model 归属；冻结教师不计入训练规模。持久提示、代码、记忆、工具和控制机制决定 Harness 归属。两种学习共同发生且有交互才归混合路线。任务内重试或外部候选程序变好不自动成立系统自改进。

≥27B 是 Model/混合主图的选题范围偏好，不是质量定理。小模型和参数未公开分别记录，未披露的训练成本、迁移与多代进步不会补写成事实。全文分析不等于独立复现，也不意味着全球资料已经穷尽。

## 数据与重建

`data/full-reading-entries.json` 固定来源清单；`data/reading-reviews/` 逐项审查与横向综合；`data/corpus-review.json` 全量索引；`data/corpus-curation.json` 主图挂接；`data/corpus-relation-aliases.json` 经核对的别名。其他图谱、机构和公司数据分别保留来源。

```bash
python scripts/build_corpus_review.py --require-complete
python scripts/integrate_corpus_reviews.py
python scripts/integrate_corpus_relations.py
python scripts/build_literature_graphs.py
python scripts/build_reading_audit.py
python scripts/check_literature_graphs.py
node scripts/check_atlas_ui.cjs
```

自动检查覆盖数据一致性、三图、搜索、卡片、分页、筛选和双向关系。真实浏览器截图检查需另设 CHROMIUM_PATH；本轮没有完成这项视觉验收。离线包不分发整篇第三方论文，仅保留分析、公开链接与来源哈希。

[领域结构](field-guide.md) · [图谱阅读档案](literature-cards.md) · [参考文献](references.md) · [机构](actor-guide.md) · [公司](industry-guide.md)
