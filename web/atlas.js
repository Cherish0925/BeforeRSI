"use strict";
const A = JSON.parse(document.getElementById("literature-data").textContent);
const E = JSON.parse(document.getElementById("locale-en").textContent);
const M = JSON.parse(
  document.getElementById("model-learning-data").textContent,
);
const REPO = "https://github.com/Cherish0925/BeforeRSI";
const works = new Map(A.works.map((w) => [w.id, w]));
const nodes = new Map(
  A.field.routes.flatMap((r) => r.nodes).map((n) => [n.id, n]),
);
const actors = A.actors.actors;
let lang = new URLSearchParams(location.search).get("lang");
if (!["en", "zh"].includes(lang)) {
  try {
    lang = localStorage.getItem("beforersi-language");
  } catch {}
  lang = lang || "zh";
}
const L = (en, zh) => (lang === "en" ? en : zh);
const esc = (s) =>
  String(s ?? "").replace(
    /[&<>"']/g,
    (c) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[
        c
      ],
  );
const href = (s) => esc(s);
const workLink = (id) =>
  `<a href="#work=${encodeURIComponent(id)}">${esc(works.get(id)?.short || id)}</a>`;
const sourceLink = (url, label) =>
  `<a href="${href(url)}" target="_blank" rel="noopener">${esc(label)} ↗</a>`;
const routeName = (id) =>
  ({
    harness: "Harness",
    model: "Model",
    hybrid: "Model × Harness",
    crosscut: L("Evaluation & synthesis", "评测与综述"),
    archive: L("Foundations & context", "基础与背景"),
  })[id] || id;
const scopeName = (id) =>
  ({
    direct: L("Self-improvement", "自改进"),
    enabler: L("Enabling method", "支撑机制"),
    evaluation: L("Evaluation", "评测"),
    theory: L("Theory", "理论"),
    foundation: L("Foundation", "基础"),
    background: L("Context", "背景"),
    disclosure: L("Public release", "公开发布"),
  })[id] || id;
const typeName = (id) =>
  ({
    academic: L("Universities & research institutes", "高校与科研机构"),
    tech: L("Technology companies", "综合科技企业"),
    ai: L("AI companies", "AI 专业公司"),
    independent: L("Independent researchers", "独立研究者"),
    unresolved: L("Affiliation pending", "署名待整理"),
  })[id] || id;
const relationName = (id) =>
  ({
    extends: L("Explicit extension", "明确扩展"),
    uses: L("Uses a method", "采用方法"),
    compares: L("Paper comparison", "论文比较"),
    discusses: L("Source discussion", "原文讨论"),
    method_comparison: L("Editorial comparison", "方法对照"),
  })[id] || id;
const colors = {
  harness: "var(--harness)",
  model: "var(--model)",
  hybrid: "var(--hybrid)",
  crosscut: "var(--muted)",
  archive: "var(--muted)",
};
const secTitles = () =>
  L(
    [
      "Purpose",
      "Core idea",
      "Mechanism",
      "Experiments",
      "Learning and inheritance",
      "Results and scope",
    ],
    [
      "目标与价值",
      "思想与洞察",
      "结构与原理",
      "算法与实验",
      "反馈与演化",
      "成果与迁移",
    ],
  );
const sections = (w) =>
  lang === "en" ? E.works[w.id].sections : w.sections.map((s) => s.text);
const nodeData = (n) => (lang === "en" ? { ...n, ...E.nodes[n.id] } : n);
const routeData = (r) =>
  lang === "en"
    ? E.routes[r.id]
    : {
        title: r.title,
        tagline: r.tagline,
        definition: r.definition,
        question: r.research_question,
        scene: r.scene,
        loop: r.loop,
        open_questions: r.open_questions.map((q) => q.title),
      };
const companyData = (c) => (lang === "en" ? { ...c, ...E.companies[c.id] } : c);
const nodeTitle = (id) => nodeData(nodes.get(id)).title;
let filters = { q: "", route: "all", scope: "all", scale: "all" };
const fieldWorkIds = (id) => [
  ...new Set(
    A.field.routes
      .flatMap((r) => r.mappings)
      .filter((m) => m.topic_ids.includes(id))
      .map((m) => m.work_id),
  ),
];
const stat = (n, t) =>
  `<div class="stat"><strong>${n}</strong><span>${t}</span></div>`;
const pathTexts = {
  harness: [
    [
      "From prompts to editable improvers",
      "How does the editable object expand from task instructions to the program producing edits?",
    ],
    [
      "Experience as reusable capability",
      "Is capability retained as executable skills, textual experience, or memory utility?",
    ],
    [
      "Architecture and search efficiency",
      "How are candidates represented, experiments allocated, and useful structures combined?",
    ],
  ],
  model: [
    [
      "From generated data to weight updates",
      "What feedback supports filtering, self-rewarding, and preference learning?",
    ],
    [
      "Learning to evaluate",
      "How do evaluators or opponents keep pace with the current policy?",
    ],
    [
      "Curricula and improvement policies",
      "How does a system learn what tasks, data, or updates help the learner?",
    ],
  ],
  hybrid: [
    [
      "Internalization and workflow adaptation",
      "When do workflow-supported capabilities transfer into weights, and when does mismatch emerge?",
    ],
    [
      "Changing the external learning system",
      "How do training procedures, environments, rewards, and skills participate in joint updates?",
    ],
  ],
};
function workCard(w) {
  return `<a class="work-card" href="#work=${w.id}" style="--route:${colors[w.route]}"><div class="pill-row"><span class="pill route">${routeName(w.route)}</span><span class="pill">${scopeName(w.scope_kind)}</span><span class="quiet">${w.year}</span></div><h3>${esc(w.short)}</h3>${w.title && w.title !== w.short ? `<div class="title">${esc(w.title)}</div>` : ""}<p class="summary">${esc(sections(w)[0])}</p><div class="work-meta"><span>${esc(w.team || w.organizations?.join(" · ") || "")}</span><span>${L("Read", "阅读")} →</span></div></a>`;
}
function options(items, selected) {
  return items
    .map(
      ([value, label]) =>
        `<option value="${value}" ${value === selected ? "selected" : ""}>${esc(label)}</option>`,
    )
    .join("");
}
function library(route) {
  if (route) filters.route = route;
  return `<div class="eyebrow">LITERATURE / ${A.works.length}</div><h1>${L("Research catalog", "研究目录")}</h1><p class="intro">${L("Search the full catalog by title, mechanism, institution or result. Each record has six sections and direct primary-source links.", "按标题、机制、机构或结果检索完整目录。每条工作提供六个维度的解读，并链接原始来源。")}</p><div class="filters"><input id="work-search" type="search" placeholder="${L("Search works, methods, institutions…", "搜索工作、方法、机构……")}" aria-label="${L("Search research", "搜索研究")}" value="${esc(filters.q)}"><select id="route-filter" aria-label="${L("Route", "路线")}">${options([["all", L("All routes", "全部路线")], ...["harness", "model", "hybrid", "crosscut", "archive"].map((x) => [x, routeName(x)])], filters.route)}</select><select id="scope-filter" aria-label="${L("Type", "类型")}">${options([["all", L("All types", "全部类型")], ...["direct", "enabler", "evaluation", "theory", "foundation", "background", "disclosure"].map((x) => [x, scopeName(x)])], filters.scope)}</select><select id="scale-filter" aria-label="${L("Trained model scale", "训练模型规模")}">${options(
    [
      ["all", L("All scales", "全部规模")],
      ["eligible", "≥27B"],
      ["below", "<27B"],
      ["unverified", L("Unverified", "未核实")],
      ["not_applicable", L("Not applicable", "不适用")],
    ],
    filters.scale,
  )}</select><button id="clear-filters">${L("Reset", "重置")}</button></div><div class="results-line"><span id="result-count"></span><a href="#scope">${L("How records are counted", "统计口径")} ↗</a></div><div id="work-results" class="work-list"></div>`;
}
function updateWorks() {
  const q = filters.q.trim().toLowerCase();
  const list = A.works
    .filter(
      (w) =>
        (filters.route === "all" || w.route === filters.route) &&
        (filters.scope === "all" || w.scope_kind === filters.scope) &&
        (filters.scale === "all" || w.scale_status === filters.scale) &&
        (!q ||
          [
            w.id,
            w.short,
            w.title,
            w.team,
            ...(w.organizations || []),
            ...sections(w),
            ...(w.actor_ids || []).flatMap((id) => {
              const a = actors.find((a) => a.id === id);
              return a
                ? [a.name, ...(a.aliases || []), ...(a.search_aliases || [])]
                : [];
            }),
          ]
            .join(" ")
            .toLowerCase()
            .includes(q)),
    )
    .sort((a, b) => b.year - a.year || a.number - b.number);
  document.getElementById("work-results").innerHTML =
    list.map(workCard).join("") ||
    `<p class="empty">${L("No matching records. Try a broader search.", "没有匹配记录，请调整搜索词或筛选条件。")}</p>`;
  document.getElementById("result-count").textContent = L(
    `${list.length} of ${A.works.length} records`,
    `${list.length} / ${A.works.length} 条记录`,
  );
}
function sources(w) {
  return [
    ...new Set(
      [
        w.primary_url,
        ...(w.sources || []),
        ...(w.review?.sources || []).map((s) => s.url),
      ].filter(Boolean),
    ),
  ];
}
function workArticle(id) {
  const w = works.get(id);
  if (!w) return missing();
  const ss = sections(w),
    rs = A.relations.filter((r) => r.source === id || r.target === id);
  const topics = [
    ...new Set(
      A.field.routes
        .flatMap((r) => r.mappings)
        .filter((m) => m.work_id === id)
        .flatMap((m) => m.topic_ids),
    ),
  ];
  return `<a class="breadcrumb" href="#works">← ${L("Research catalog", "研究目录")}</a><div class="article-header" style="--route:${colors[w.route]}"><div class="pill-row"><a class="pill route" href="#${["harness", "model", "hybrid"].includes(w.route) ? "route=" + w.route : "works&route=" + w.route}">${routeName(w.route)}</a><span class="pill">${scopeName(w.scope_kind)}</span><span class="quiet">${w.year} · ${esc(w.id)}</span></div><h1>${esc(w.short)}</h1><p class="full-title">${esc(w.title || "")}</p><div class="quiet">${esc(w.team || "")}</div></div><div class="article-grid"><article class="article">${ss.map((s, i) => `<section><h2><span>${"ABCDEF"[i]}</span>${secTitles()[i]}</h2><p>${esc(s)}</p></section>`).join("")}${rs.length ? `<section><h2>${L("Connections", "研究关系")}</h2>${rs.map(relationCard).join("")}</section>` : ""}</article><aside class="article-aside"><div class="aside-box"><h3>${L("Primary sources", "原始来源")}</h3><ol class="source-list">${sources(
    w,
  )
    .map(
      (u, i) =>
        `<li>${sourceLink(u, L("Source " + (i + 1), "来源 " + (i + 1)))}<br><small>${esc(new URL(u).hostname)}</small></li>`,
    )
    .join(
      "",
    )}</ol></div><div class="aside-box"><h3>${L("Mechanism map", "机制位置")}</h3><div class="mini-list">${topics.map((t) => `<a href="#route=${A.field.routes.find((r) => r.nodes.some((n) => n.id === t)).id}&node=${t}">${esc(nodeTitle(t))}</a>`).join("") || L("Historical or cross-cutting context", "历史或横向背景")}</div></div><div class="aside-box"><h3>${L("Research participants", "研究参与者")}</h3><div class="mini-list">${(
    w.actor_ids || []
  )
    .map((id) => {
      const a = actors.find((a) => a.id === id);
      return a ? `<a href="#people&actor=${id}">${esc(a.name)}</a>` : "";
    })
    .join(
      "",
    )}</div></div>${w.models?.length ? `<div class="aside-box"><h3>${L("Models in the record", "记录涉及的模型")}</h3>${w.models.map((m) => `<div class="model-row"><strong>${esc(m.name)}</strong>${m.total_b ? `<br>${m.total_b}B ${L("total", "总参数")}` : ""}${m.active_b ? ` · ${m.active_b}B ${L("active", "激活参数")}` : ""}</div>`).join("")}<p>${L("Training, teacher, judge and baseline roles are specified in the six sections.", "训练对象、教师、评价器与基线的角色见正文。")}</p></div>` : ""}</aside></div>`;
}
function workPage(id) {
  const w = works.get(id);
  if (!w) return missing();
  return workArticle(id).replace(
    "</article>",
    originalReview(w) + "</article>",
  );
}
function relationCard(r) {
  return `<div class="relation-card"><h3>${workLink(r.source)} → ${workLink(r.target)}<span class="kind">${relationName(r.kind)}</span></h3><p>${esc(lang === "en" ? E.relations[r.id].explanation : r.explanation)}</p><div class="refs">${(r.sources || []).map((s, i) => sourceLink(s.url, L("Source " + (i + 1), "来源 " + (i + 1)))).join("")}</div></div>`;
}
function relationsPage() {
  return `<div class="eyebrow">CONNECTIONS / ${A.relations.length}</div><h1>${L("How the work connects", "研究怎样相互连接")}</h1><p class="intro">${L("Trace explicit extensions, method use, comparisons and discussions. Editorial comparisons identify a useful contrast without claiming code or historical inheritance.", "追踪明确扩展、方法采用、实验比较与原文讨论。方法对照用于解释异同，并保留它与实际继承关系的区别。")}</p><div class="filters"><input id="relation-search" type="search" aria-label="${L("Search connections", "搜索研究关系")}" placeholder="${L("Search connections…", "搜索研究关系……")}"><select id="relation-kind" aria-label="${L("Relation type", "关系类型")}">${options([["all", L("All connections", "全部关系")], ...Object.keys(A.relation_types).map((k) => [k, relationName(k)])], "all")}</select></div><div id="relation-results">${A.relations.map(relationCard).join("")}</div>`;
}
function companyCard(raw) {
  const c = companyData(raw);
  return `<div class="actor-card"><div class="eyebrow">${L({ research: "RESEARCH", direction: "DIRECTION", adjacent: "ADJACENT" }[c.status], { research: "公开研究", direction: "研究方向", adjacent: "相邻研究" }[c.status])}</div><h3><a href="#company=${c.id}">${esc(c.name)}</a></h3><p>${esc(c.focus)}</p><div class="mini-list">${c.work_links.map((w) => workLink(w.work_id)).join("")}</div><details><summary>${L("Sources and scope", "来源与范围")}</summary><p>${esc(c.boundary)}</p><div class="source-list">${c.sources.map((s, i) => sourceLink(s, L("Source " + (i + 1), "来源 " + (i + 1)))).join(" · ")}</div></details></div>`;
}
function companyPage(id) {
  const raw = A.industry.companies.find((c) => c.id === id);
  if (!raw) return missing();
  const c = companyData(raw);
  return `<a class="breadcrumb" href="#people">← ${L("Companies and industry teams", "公司与产业研究团队")}</a><div class="eyebrow">INDUSTRY / ${esc(c.id)}</div><h1>${esc(c.name)}</h1><p class="intro">${esc(c.focus)}</p><div class="prose"><p>${esc(c.boundary)}</p><div class="mini-list">${c.topic_ids.map((id) => `<a href="#route=${A.field.routes.find((r) => r.nodes.some((n) => n.id === id)).id}&node=${id}">${esc(nodeTitle(id))}</a>`).join("")}</div><h3 style="margin-top:24px">${L("Primary sources", "原始来源")}</h3><ol class="source-list">${c.sources.map((u, i) => `<li>${sourceLink(u, L("Source " + (i + 1), "来源 " + (i + 1)))}</li>`).join("")}</ol></div><div class="section-head"><h2>${L("Linked research", "关联研究")}</h2><span class="quiet">${c.work_links.length}</span></div><div class="work-list">${c.work_links.map((w) => workCard(works.get(w.work_id))).join("") || `<p>${L("Public research direction; no linked work record in this snapshot.", "公开研究方向；当前快照暂无关联工作记录。")}</p>`}</div>`;
}

function peoplePage(actorId) {
  const actor = actors.find((a) => a.id === actorId);
  if (actor)
    return `<a class="breadcrumb" href="#people">← ${L("Research participants", "研究主体")}</a><div class="eyebrow">${typeName(actor.kind)}</div><h1>${esc(actor.name)}</h1><p class="intro">${esc((actor.aliases || []).join(" · "))}</p><p>${actor.work_ids.length} ${L("linked works in this catalog", "项目录中的关联工作")}</p><div class="work-list">${actor.work_ids
      .map((id) => works.get(id))
      .filter(Boolean)
      .map(workCard)
      .join("")}</div>`;
  return `<div class="eyebrow">PEOPLE & ORGANIZATIONS</div><h1>${L("Who is building the field", "谁在建设这个领域")}</h1><p class="intro">${L("Research affiliations link universities, institutes, technology companies and AI teams to specific work. Company profiles add published directions and technical releases.", "从具体工作的署名连接高校、科研机构、科技企业与 AI 团队。公司条目进一步整理公开研究方向与技术发布。")}</p><div class="stats">${stat(actors.length, L("normalized participants", "归一研究主体"))}${stat(170, L("source affiliation names", "原始机构名称"))}${stat(27, L("company profiles", "公司条目"))}</div><div class="section-head"><h2>${L("Companies and industry teams", "公司与产业研究团队")}</h2></div><div class="filters"><input id="company-search" type="search" aria-label="${L("Search companies", "搜索公司")}" placeholder="${L("Search companies and directions…", "搜索公司与研究方向……")}"></div><div id="company-results" class="actor-grid">${A.industry.companies.map(companyCard).join("")}</div><div class="section-head"><h2>${L("All research participants", "全部研究主体")}</h2></div><div class="filters"><input id="actor-search" type="search" aria-label="${L("Search participants", "搜索研究主体")}" placeholder="${L("Search affiliations and aliases…", "搜索机构与别名……")}"><select id="actor-kind" aria-label="${L("Participant type", "主体类型")}">${options([["all", L("All types", "全部类型")], ...A.actors.types.map((t) => [t.id, typeName(t.id)])], "all")}</select></div><div id="actor-results" class="actor-grid">${actorCards(actors)}</div>`;
}
function actorCards(list) {
  return [...list]
    .sort(
      (a, b) =>
        b.work_ids.length - a.work_ids.length || a.name.localeCompare(b.name),
    )
    .map(
      (a) =>
        `<a class="actor-card" href="#people&actor=${a.id}"><small>${typeName(a.kind)}</small><h3>${esc(a.name)}</h3><p>${a.work_ids.length} ${L("linked works", "项关联工作")} →</p></a>`,
    )
    .join("");
}
function guidePage(key) {
  const g = M[lang];
  const ch = g.chapters.find((c) => c.key === key) || g.chapters[0];
  const i = g.chapters.indexOf(ch);
  return `<div class="guide-bar"><div><div class="eyebrow">LEARNING MANUAL / ${g.pages} ${L("PAGES", "页")}</div><h1>${L("Model / LLM", "Model / LLM 学习手册")}</h1></div><div class="actions"><button class="button" data-pdf>${L("Download PDF", "下载 PDF")} ↓</button><a class="button" href="${REPO}/blob/main/docs/model-llm${lang === "en" ? ".en" : ""}.md" target="_blank" rel="noopener">Markdown ↗</a></div></div><div class="filters"><input id="guide-search" type="search" placeholder="${L("Search chapters, equations and terminology…", "搜索章节、公式与术语……")}" aria-label="${L("Search manual", "搜索教程")}"></div><div id="guide-search-results" class="guide-search-results"></div><div class="guide-layout"><aside class="guide-nav" aria-label="${L("Contents", "目录")}">${g.chapters.map((c) => `<a class="${c.key === ch.key ? "active" : ""}" href="#learn=${c.key}">${esc(c.title.replace("｜", " · "))}</a>`).join("")}</aside><article class="guide-content"><h2>${esc(ch.title.replace("｜", " · "))}</h2>${ch.html}<div class="chapter-pager">${i ? `<a href="#learn=${g.chapters[i - 1].key}">← ${esc(g.chapters[i - 1].title.replace("｜", " · "))}</a>` : "<span></span>"}${i < g.chapters.length - 1 ? `<a href="#learn=${g.chapters[i + 1].key}">${esc(g.chapters[i + 1].title.replace("｜", " · "))} →</a>` : ""}</div></article></div>`;
}
const researchDocs = [
  [
    "MAP",
    "Historical and causal map",
    "历史与因果图景",
    "How the major traditions connect.",
    "主要研究传统怎样连接。",
  ],
  [
    "THEORY",
    "Mathematical model",
    "数学模型",
    "State, updates, improvement and evaluation.",
    "系统状态、更新、改进与评价。",
  ],
  [
    "EVIDENCE",
    "Public evidence",
    "公开证据",
    "What published work establishes.",
    "公开研究支持了哪些结论。",
  ],
  [
    "HYPOTHESES",
    "Working hypotheses",
    "待检验假设",
    "Predictions and decisive tests.",
    "预测与能够区分解释的实验。",
  ],
  [
    "PROGRAM",
    "Research program",
    "研究计划",
    "A sequence of concrete interventions.",
    "可执行干预与实验顺序。",
  ],
  [
    "EVALUATION",
    "Evaluation protocol",
    "评价协议",
    "Transfer, resource use and regressions.",
    "迁移、资源成本与能力回退。",
  ],
  [
    "RESEARCH_LOG",
    "Research history",
    "研究记录",
    "Material changes in the model and direction.",
    "模型与研究方向的重要变化。",
  ],
  [
    "SIMULATION",
    "Illustrative dynamics",
    "动力学示例",
    "Explicit toy models and identification questions.",
    "参数明确的示例模型与识别问题。",
  ],
];
function researchPage() {
  return `<div class="eyebrow">FROM LANDSCAPE TO EXPERIMENT</div><h1>${L("The research program", "研究主线")}</h1><p class="intro">${L("BeforeRSI asks when a system becomes better at producing its next improvement. The research documents develop a testable model of inherited state, improvement procedures, transfer and evaluator drift.", "BeforeRSI 追问：系统在什么条件下会更善于产生下一次改进？研究文档围绕可继承状态、改进程序、迁移与评价器漂移建立可检验的模型。")}</p><div class="notice">${L("The landscape contains 141 records. The research claim index contains 38 selected works tied to this program. They serve different purposes and are not additive.", "领域目录包含 141 条记录；研究论证索引选取 38 项工作，服务于本研究计划。两者用途不同，数量不能相加。")}</div><div class="research-list">${researchDocs.map(([id, en, zh, ed, zd]) => `<a href="${REPO}/blob/main/${lang === "zh" ? "docs/zh/" : ""}${id}.md" target="_blank" rel="noopener"><strong>${L(en, zh)} ↗</strong><span>${L(ed, zd)}</span></a>`).join("")}</div><div class="section-head"><h2>${L("Five discriminating experiments", "五个判别实验")}</h2></div><div class="research-list">${[
    ["001-harness-transfer", "Harness transfer", "Harness 迁移"],
    [
      "002-model-harness-cross",
      "Model–harness cross-evaluation",
      "模型与 Harness 交叉评价",
    ],
    [
      "003-successor-as-improver",
      "Successor as improver",
      "后继系统作为改进器",
    ],
    ["004-repeated-coevolution", "Repeated coevolution", "多轮共同演化"],
    [
      "005-evaluator-phase-boundary",
      "Evaluator phase boundary",
      "评价器相变边界",
    ],
  ]
    .map(
      ([id, en, zh]) =>
        `<a href="${REPO}/blob/main/${lang === "zh" ? "docs/zh/" : ""}experiments/${id}.md" target="_blank" rel="noopener"><strong>${L(en, zh)} ↗</strong></a>`,
    )
    .join("")}</div>`;
}
function scopePage() {
  return `<div class="eyebrow">SCOPE & SOURCES</div><h1>${L("What this atlas contains", "收录范围与数据口径")}</h1><div class="prose"><p class="intro">${L("A curated map of mechanisms and public evidence, with source material reviewed through 19 October 2026. The bilingual release is dated 20 October 2026.", "本图谱整理机制与公开证据，资料快照截至 2026 年 10 月 19 日；双语整理版发布于 2026 年 10 月 20 日。")}</p><h2>${L("One record, two languages", "同一记录，两种语言")}</h2><p>${L("Chinese and English share record IDs, routes, sources and counts. English work cards provide edited counterparts to the six Chinese sections. Original Chinese review notes can be expanded within each study and remain in the source dataset.", "中英文共享记录 ID、路线、来源与统计。英文工作条目按中文六个维度整理，保留机制与结果口径；原始中文阅读记录可在研究卡片中展开，并完整保存在源数据中。")}</p><div class="table-wrap"><table><thead><tr><th>${L("Collection", "内容")}</th><th>${L("Count", "数量")}</th><th>${L("Meaning", "含义")}</th></tr></thead><tbody><tr><td>${L("Atlas catalog", "领域目录")}</td><td>141</td><td>${L("118 method records, 1 screened record, 22 historical/context records", "118 条方法记录、1 条初筛记录、22 条历史与背景记录")}</td></tr><tr><td>${L("Route placement", "路线位置")}</td><td>110 + 9 + 22</td><td>${L("110 across the three routes; 9 cross-cutting; 22 foundations/context", "110 条分布在三条路线，9 条横向研究，22 条基础与背景")}</td></tr><tr><td>${L("Mechanism maps", "机制图")}</td><td>29 / 60</td><td>${L("29 nodes and 60 conceptual links", "29 个节点、60 条概念连接")}</td></tr><tr><td>${L("Work relationships", "工作关系")}</td><td>69</td><td>${L("Source-supported relations and explicitly labeled editorial comparisons", "来源支持的关系与明确标注的方法对照")}</td></tr><tr><td>${L("Participants", "研究主体")}</td><td>157 / 170</td><td>${L("157 normalized entries; 170 original affiliation names", "157 个归一主体，170 个原始机构名称")}</td></tr><tr><td>${L("Industry profiles", "产业条目")}</td><td>27</td><td>${L("24 with linked research, 1 direction, 2 adjacent", "24 项有关联研究、1 项研究方向、2 项相邻研究")}</td></tr><tr><td>${L("Research claim index", "研究论证索引")}</td><td>38</td><td>${L("A separate selection for the theoretical and experimental program", "用于理论与实验研究主线的独立选集")}</td></tr></tbody></table></div><h2>${L("Reading evidence", "怎样阅读证据")}</h2><p>${L("A work card identifies the update object, feedback, experimental setup, inherited state and result. Sources include papers, code, technical reports, benchmarks and official releases. A company direction, a runnable artifact, a measured result and an independently reproduced result carry different information; the card records the available basis.", "工作条目说明更新对象、反馈、实验设置、继承状态与结果。来源包括论文、代码、技术报告、基准和官方发布。公司方向、可运行产物、测量结果与独立复现提供的信息不同，条目按已获得的材料说明。")}</p><p>${L("The catalog shows every model scale by default. The ≥27B filter refers to the model actually trained, not a frozen teacher, judge or baseline. Model names and roles remain separate. Most records summarize public reports rather than independent reproductions.", "目录默认显示全部模型规模。≥27B 筛选针对实际接受训练的模型，教师、评价器和基线的规模单独记录。多数条目是对公开报告的整理，未进行独立复现。")}</p><h2>${L("Attribution and counting", "归属与去重")}</h2><p>${L("Affiliations follow authorship and official releases. A jointly authored work can appear under multiple participants but counts once in the work catalog. Aliases are normalized for browsing while source labels remain available. Company profiles describe the reviewed work, not a complete company inventory.", "研究归属依据署名和官方发布。合作工作可出现在多个主体下，但在工作目录中只计一次。浏览入口归一别名，原始署名保留在数据中。公司条目反映已整理的公开研究，不代表公司全部业务。")}</p><h2>${L("Data and maintenance", "数据与维护")}</h2><p>${L("The atlas data, English editorial layer and both manuals are version-controlled sources. The standalone page embeds them, its fonts and both PDFs, so local browsing and downloads work offline. Source links and repository documents open online.", "图谱数据、英文编辑层和两种语言的教程均纳入版本管理。独立页面内置数据、字体和两份 PDF，可离线阅读与下载；原始来源和仓库文档在线打开。")}</p><div class="actions"><button data-download="atlas">${L("Download atlas JSON", "下载图谱 JSON")}</button><button data-download="en">${L("Download English text", "下载英文文本")}</button><a class="button" href="${REPO}/blob/main/${lang === "en" ? "CONTRIBUTING.md" : "CONTRIBUTING.zh-CN.md"}" target="_blank" rel="noopener">${L("Contribute a correction", "参与修订")} ↗</a></div></div>`;
}
function missing() {
  return `<h1>${L("Record not found", "未找到记录")}</h1><p><a href="#overview">${L("Return to overview", "返回总览")} →</a></p>`;
}
function routeState() {
  const h = location.hash.slice(1) || "overview";
  const p = new URLSearchParams(h);
  if (p.has("work") || p.has("paper"))
    return { page: "work", id: p.get("work") || p.get("paper") };
  if (p.has("company")) return { page: "company", id: p.get("company") };
  if (h.startsWith("route="))
    return {
      page: "route",
      id: p.get("route"),
      node: p.get("node"),
      edge: p.get("edge"),
      mode: p.get("mode"),
      selected: p.get("selected"),
      relation: p.get("relation"),
    };
  if (p.has("learn")) return { page: "learn", id: p.get("learn") };
  return {
    page: h.split("&")[0],
    route: p.get("route"),
    actor: p.get("actor"),
    kind: p.get("kind"),
    mode: p.get("mode"),
  };
}
function render() {
  const s = routeState();
  document.documentElement.lang = lang;
  document.getElementById("language").textContent = L("中文", "English");
  document
    .getElementById("language")
    .setAttribute("aria-label", L("Switch to Chinese", "切换到英文"));
  document.title = "BeforeRSI · " + L("Research Atlas", "递归自改进研究图谱");
  const current =
    s.page === "work" ? "works" : s.page === "company" ? "people" : s.page;
  document.getElementById("global-query").placeholder = L(
    "Search papers, teams or mechanisms…",
    "搜索论文、团队或研究问题……",
  );
  document.getElementById("global-submit").textContent = L("Search", "搜索");
  document.getElementById("nav").innerHTML = [
    [
      "overview",
      "Landscape overview",
      "领域全景",
      "Three routes · research participants",
      "三条路线 · 研究主体",
    ],
    [
      "route=harness",
      "01  Harness",
      "01  Harness",
      "External systems and improvers",
      "外部系统的学习与自修改",
    ],
    [
      "route=model",
      "02  Model",
      "02  Model",
      "Learning in model weights",
      "参数中的学习与反馈",
    ],
    [
      "route=hybrid",
      "03  Model × Harness",
      "03  Model × Harness",
      "Joint adaptation and evolution",
      "共同适配与共同演化",
    ],
    [
      "guide",
      "Understand RSI",
      "读懂 RSI",
      "Mechanisms · comparisons",
      "机制 · 对照",
    ],
    [
      "participants",
      "Institutions and teams",
      "机构与团队",
      "Universities · companies · collaboration",
      "高校 · 企业 · 合作",
    ],
    [
      "works",
      "Research search",
      "研究检索",
      "Papers · reports · methods",
      "论文 · 报告 · 方法",
    ],
    [
      "learn=00",
      "Model / LLM manual",
      "Model / LLM 教程",
      "Foundations · bilingual PDF",
      "基础原理 · 双语 PDF",
    ],
    [
      "discovery",
      "Discovery pool",
      "检索文献池",
      "567 entries · relevance decisions",
      "567 条线索 · 范围判断",
    ],
    [
      "research",
      "Research program",
      "研究主线",
      "Theory · experiments",
      "理论 · 实验",
    ],
    [
      "scope",
      "Scope and sources",
      "收录说明",
      "Coverage · data",
      "范围 · 数据",
    ],
  ]
    .map(
      ([id, en, zh, es, zs], i) =>
        `<a href="#${id}" class="${i === 4 ? "nav-break" : ""}" ${(id === "route=" + s.id && s.page === "route") || id === current || (id === "learn=00" && s.page === "learn") || (id === "participants" && ["people", "company"].includes(s.page)) ? 'aria-current="page"' : ""}>${L(en, zh)}<small>${L(es, zs)}</small></a>`,
    )
    .join("");
  const main = document.getElementById("main");
  main.innerHTML = (
    {
      overview: () => overview(),
      guide: readerPage,
      participants: participantsPage,
      actors: participantsPage,
      discovery: discoveryPage,
      route: () => routePage(s.id, s.node),
      works: () => library(s.route),
      search: () => library(s.route),
      work: () => workPage(s.id),
      company: () => companyPage(s.id),
      relations: relationsPage,
      people: () => peoplePage(s.actor),
      learn: () => guidePage(s.id),
      research: researchPage,
      scope: scopePage,
      coverage: scopePage,
    }[s.page] || missing
  )();
  if (["works", "search"].includes(s.page)) updateWorks();
  document.getElementById("footer").innerHTML =
    `<span>BeforeRSI · ${L("Mechanisms, evidence, and experiments.", "机制、证据与实验。")}</span><span>${L("Bilingual edition", "双语版")} · 2026.10.20 · <a href="${REPO}">GitHub ↗</a></span>`;
}
function download(blob, name) {
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = name;
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
document.addEventListener("click", (e) => {
  if (e.target.closest(".skip")) {
    e.preventDefault();
    document.getElementById("main").focus();
    return;
  }
  if (e.target.closest("#language, [data-dialog-language]")) {
    lang = lang === "en" ? "zh" : "en";
    try {
      localStorage.setItem("beforersi-language", lang);
    } catch {}
    const url = new URL(location.href);
    url.searchParams.set("lang", lang);
    history.replaceState(null, "", url);
    render();
  }
  if (e.target.closest("[data-pdf]")) {
    const bytes = Uint8Array.from(atob(M[lang].pdf), (c) => c.charCodeAt(0));
    download(
      new Blob([bytes], { type: "application/pdf" }),
      "Model_LLM_Learning_Manual" + (lang === "en" ? ".en" : "") + ".pdf",
    );
  }
  const dl = e.target.closest("[data-download]");
  if (dl)
    download(
      new Blob(
        [JSON.stringify(dl.dataset.download === "atlas" ? A : E, null, 2)],
        { type: "application/json" },
      ),
      dl.dataset.download === "atlas" ? "atlas.json" : "atlas.en.json",
    );
  const ref = e.target.closest("[data-learn-ref]");
  if (ref) {
    location.hash = "learn=D";
    setTimeout(
      () =>
        document
          .getElementById("ml-source-" + ref.dataset.learnRef)
          ?.scrollIntoView(),
      30,
    );
  }
  if (e.target.closest("#clear-filters")) {
    filters = { q: "", route: "all", scope: "all", scale: "all" };
    if (location.hash !== "#works") location.hash = "works";
    else render();
  }
});
document.addEventListener("change", (e) => {
  if (e.target.id === "node-select") {
    const s = routeState();
    location.hash = `route=${s.id}&node=${e.target.value}`;
  }
  const key = {
    "route-filter": "route",
    "scope-filter": "scope",
    "scale-filter": "scale",
  }[e.target.id];
  if (key) {
    filters[key] = e.target.value;
    updateWorks();
  }
  if (e.target.id === "actor-kind") updateActors();
  if (e.target.id === "relation-kind") updateRelations();
});
function updateActors() {
  const q = document.getElementById("actor-search").value.toLowerCase(),
    k = document.getElementById("actor-kind").value;
  document.getElementById("actor-results").innerHTML = actorCards(
    actors.filter(
      (a) =>
        (k === "all" || a.kind === k) &&
        [a.name, ...(a.aliases || []), ...(a.search_aliases || [])]
          .join(" ")
          .toLowerCase()
          .includes(q),
    ),
  );
}
function updateRelations() {
  const q = document.getElementById("relation-search").value.toLowerCase(),
    k = document.getElementById("relation-kind").value;
  document.getElementById("relation-results").innerHTML = A.relations
    .filter(
      (r) =>
        (k === "all" || r.kind === k) &&
        [
          works.get(r.source).short,
          works.get(r.target).short,
          lang === "en" ? E.relations[r.id].explanation : r.explanation,
        ]
          .join(" ")
          .toLowerCase()
          .includes(q),
    )
    .map(relationCard)
    .join("");
}
document.addEventListener("input", (e) => {
  const v = e.target.value?.toLowerCase();
  if (e.target.id === "work-search") {
    filters.q = e.target.value;
    updateWorks();
  }
  if (e.target.id === "actor-search") updateActors();
  if (e.target.id === "relation-search") updateRelations();
  if (e.target.id === "company-search")
    document.getElementById("company-results").innerHTML = A.industry.companies
      .filter((raw) => {
        const c = companyData(raw);
        return [c.name, c.focus, ...c.aliases]
          .join(" ")
          .toLowerCase()
          .includes(v);
      })
      .map(companyCard)
      .join("");
  if (e.target.id === "guide-search") {
    const matches = v
      ? M[lang].chapters.filter((c) =>
          (c.title + " " + c.text).toLowerCase().includes(v),
        )
      : [];
    document.getElementById("guide-search-results").innerHTML =
      matches
        .map((c) => {
          const i = c.text.toLowerCase().indexOf(v);
          return `<a href="#learn=${c.key}"><strong>${esc(c.title.replace("｜", " · "))}</strong><p>${esc(c.text.slice(Math.max(0, i - 45), Math.max(0, i - 45) + 180).replace(/[#$*|]/g, ""))}…</p></a>`;
        })
        .join("") ||
      (v ? `<p>${L("No matching chapters.", "没有匹配章节。")}</p>` : "");
  }
});
window.addEventListener("hashchange", () => {
  render();
  window.scrollTo({ top: 0, behavior: "instant" });
});
