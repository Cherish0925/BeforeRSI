# Data / 数据

Two collections serve different purposes. 两套目录分别服务于领域浏览与研究论证。

| File | Purpose / 用途 |
|---|---|
| [atlas.json](atlas.json) | 141-record landscape: works, routes, sources, reviews, relations, participants and companies / 141 条领域记录与其机制、来源、关系和机构 |
| [locales/en.json](locales/en.json) | English editorial text for every work, route, mechanism, field edge, work relation and company / 完整对应的英文编辑层 |
| [works.json](works.json) | 38 selected works linked to the research program's claims / 38 项研究论证索引 |
| [works.schema.json](works.schema.json) | Schema for the research claim index / 研究论证索引结构 |
| [knowledge-graph.json](knowledge-graph.json) | Research-program concepts and claim bindings / 研究主线概念及论证关联 |
| [hypotheses.json](hypotheses.json) | Twelve working hypotheses and decisive tests / 12 个工作假设及判别实验 |

## Landscape structure / 图谱结构

- `works`: stable IDs, six reading sections, model roles, source links and structured review notes / 稳定 ID、六维解读、模型角色、来源及阅读笔记。
- `field.routes`: 29 nodes, 60 conceptual edges and work-to-topic mappings / 29 个机制节点、60 条概念关系与工作映射。
- `relations`: 69 work relationships; `evidence` distinguishes source statements from editorial comparisons / 69 条研究关系，注明来源陈述或方法对照。
- `actors`: 157 normalized participants and aliases / 157 个归一研究主体及别名。
- `institutions`: 170 original affiliation names / 170 个原始机构名称。
- `industry`: 27 company profiles with research links and public directions / 27 家公司条目及公开研究方向。
- Discovery and reading fields preserve the source-review trail; leads are not added to the work count / 发现与阅读字段保留整理过程，线索不计入工作总数。

## Language alignment / 语言对应

`atlas.json` retains the Chinese record and original review metadata. `locales/en.json` supplies English prose keyed by the same IDs. Its six work sections retain the mechanism, experimental setting, key numbers and result scope while using natural English exposition. Source URLs, years, model metadata and organization relationships are shared.

`atlas.json` 保留中文记录与原始阅读元数据；`locales/en.json` 按相同 ID 提供英文表达。六个工作段落保持机制、实验条件、关键数字和结论范围对应。来源、年份、模型信息与机构关系共用。

Raw review notes preserve their original language. They are provenance records; the bilingual public reading surface uses the edited sections. 新的实质性修订应同步两种语言；原始笔记保留原语言，双语阅读使用编辑后的条目。

## Counts and filters / 统计与筛选

The 141 records comprise 118 method records, 1 screened record and 22 historical/context records. Route placement is 52 Harness, 36 Model, 22 Hybrid, 9 cross-cutting and 22 archive records. The default browser includes all records.

141 条记录包括 118 条方法记录、1 条初筛记录和 22 条历史背景记录；路线分布为 Harness 52、Model 36、Hybrid 22、横向研究 9、基础背景 22。默认显示全部记录。

The scale filter uses the actually trained model. A fixed teacher, judge, executor or baseline has its own role; its size does not determine trainable-model eligibility. Affiliation counts can overlap across works; joint research is counted once in the catalog.

规模筛选依据实际训练模型；固定教师、评价器、执行器与基线的角色另记。机构参与关系可交叉，合作研究在工作目录只计一次。

## Validation / 校验

Run `python scripts/validate.py` from the repository root. It checks IDs, references, translation coverage, manual chapters, embedded PDF identity, source hashes and local Markdown links. Rebuild with `python scripts/build_learning.py` after changing documentation sources.

在仓库根目录运行上述校验；修改源内容后重新构建。页面数据由源文件生成，避免直接编辑 `docs/index.html`。
