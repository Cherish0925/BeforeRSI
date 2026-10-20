// The landscape keeps the original two graph views: mechanisms and research relationships.
const mapState = {
  route: null,
  expanded: false,
  zoom: 0.9,
  methods: true,
  group: "all",
  kind: "all",
  org: "all",
  status: "all",
  small: false,
  page: 1,
};
const groupNames = {
  "h-prompt": "Prompt and context optimization",
  "h-memory": "Memory and reusable skills",
  "h-workflow": "Agent architecture and workflow search",
  "h-self": "Code self-modification and meta-improvement",
  "h-research": "Automated research and runtime efficiency",
  "h-evaluator": "Evaluator coevolution",
  "m-selftrain": "Self-generated data and iterative SFT",
  "m-preference": "Self-feedback and preference learning",
  "m-verifier": "Policy–evaluator learning",
  "m-curriculum": "Self-play and generated curricula",
  "m-meta": "Learned data, editing and update policies",
  "m-proof": "Search-guided training and test-time learning",
  "x-workflow": "Workflow evolution and internalization",
  "x-skills": "Skills, memory and policy coevolution",
  "x-environment": "Environment, reward and policy coevolution",
  "x-training": "Training systems and model co-optimization",
};
const groupName = (g) => (lang === "en" ? groupNames[g.id] : g.title);
const nodeRoute = (id) =>
  A.field.routes.find((r) => r.nodes.some((n) => n.id === id));
const nodeLink = (id) =>
  `<a href="#route=${nodeRoute(id).id}&node=${id}">${esc(nodeTitle(id))}</a>`;
const workOpen = (id) =>
  `<a href="#work=${id}" data-open-work="${id}">${esc(works.get(id).short)}</a>`;
const edgeText = (e) =>
  lang === "en" ? E.edges[e.id].explanation : e.explanation;
const readingName = (w) =>
  L(
    {
      methods: "Source reviewed",
      screened: "Pending full text",
      archive: "Historical / context",
    }[w.status],
    { methods: "来源已研读", screened: "原文待补", archive: "历史 / 背景" }[
      w.status
    ],
  );
const selectedRoute = () =>
  A.field.routes.find((r) => r.id === routeState().id) || A.field.routes[0];
const labelCanvas = document.createElement("canvas").getContext("2d");
function labelLines(text, width, size, weight = 400) {
  labelCanvas.font = `${weight} ${size}px ${getComputedStyle(document.body).fontFamily}`;
  const lines = [""];
  const append = (token) => {
    const line = lines.at(-1) + token;
    if (
      labelCanvas.measureText(line.trim()).width > width &&
      lines.at(-1).trim()
    )
      lines.push(token.trimStart());
    else lines[lines.length - 1] = line;
  };
  for (const token of text.match(/[^\x00-\x7F]|[^\s\x80-\uFFFF]+|\s+/gu) ||
    []) {
    if (labelCanvas.measureText(token).width > width)
      for (const character of token) append(character);
    else append(token);
  }
  return lines.map((line) => line.trim()).filter(Boolean);
}
function fitLabel(text, width, size, maxLines, weight = 400) {
  let lines = labelLines(text, width, size, weight);
  while (lines.length > maxLines && size > 10) {
    size -= 1;
    lines = labelLines(text, width, size, weight);
  }
  return { lines, size };
}
const labelSpans = (lines, x, leading) =>
  lines
    .map(
      (line, i) =>
        `<tspan x="${x}" dy="${i ? leading : 0}">${esc(line)}</tspan>`,
    )
    .join("");
function fieldMap(r, selected = null, edgeId = null, compact = false) {
  const deep = !compact && mapState.expanded,
    width = 1040,
    nw = 402,
    labels = new Map(
      r.nodes.map((n) => {
        const d = nodeData(n),
          title = compact && lang === "zh" ? n.short_title || d.title : d.title;
        return [
          n.id,
          {
            ...fitLabel(title, nw - 34, compact ? 34 : 23, 3, 650),
            subtopics: deep
              ? d.subtopics.map((t) => labelLines(t, nw - 34, 17))
              : [],
          },
        ];
      }),
    ),
    nh = compact
      ? 186
      : deep
        ? Math.max(
            ...[...labels.values()].map(
              (n) =>
                128 +
                n.subtopics.reduce(
                  (sum, lines) => sum + lines.length * 23 + 8,
                  0,
                ),
            ),
          )
        : 132,
    row = nh + (compact ? 74 : 42);
  const height = Math.ceil(r.nodes.length / 2) * row + 32;
  const positions = new Map(
    r.nodes.map((n, i) => [
      n.id,
      { x: i % 2 ? 598 : 40, y: 30 + Math.floor(i / 2) * row },
    ]),
  );
  const incidents = new Map(
    r.nodes.map((n) => [
      n.id,
      r.edges
        .filter((e) => e.source === n.id || e.target === n.id)
        .map((e) => e.id),
    ]),
  );
  const near = new Set(
    selected
      ? [
          selected,
          ...r.edges
            .filter((e) => e.source === selected || e.target === selected)
            .flatMap((e) => [e.source, e.target]),
        ]
      : [],
  );
  const port = (id, e) =>
    20 +
    ((nh - 40) * (incidents.get(id).indexOf(e.id) + 1)) /
      (incidents.get(id).length + 1);
  const arrows = r.edges
    .map((e) => {
      const a = positions.get(e.source),
        b = positions.get(e.target),
        cross = a.x !== b.x,
        forward = b.x > a.x;
      const x1 = a.x + (cross ? (forward ? nw : 0) : a.x < width / 2 ? 0 : nw),
        x2 = b.x + (cross ? (forward ? 0 : nw) : b.x < width / 2 ? 0 : nw),
        y1 = a.y + port(e.source, e),
        y2 = b.y + port(e.target, e),
        bend = cross ? (x1 + x2) / 2 : a.x < width / 2 ? 8 : 1032;
      const d = `M${x1} ${y1} C${bend} ${y1} ${bend} ${y2} ${x2} ${y2}`,
        active =
          e.id === edgeId ||
          (selected && (e.source === selected || e.target === selected)),
        dim = (selected || edgeId) && !active;
      return `<a class="concept-link ${active ? "active" : ""} ${dim ? "dim" : ""}" href="#route=${r.id}&edge=${e.id}" aria-label="${esc(nodeTitle(e.source) + " → " + nodeTitle(e.target))}"><title>${esc(edgeText(e))}</title><path class="concept-edge" d="${d}" marker-end="url(#arrow-${r.id}-${compact ? "s" : "l"})"/><path class="concept-hit" d="${d}"/></a>`;
    })
    .join("");
  const cards = r.nodes
    .map((n) => {
      const p = positions.get(n.id),
        d = nodeData(n),
        label = labels.get(n.id),
        meta = [
          "recursive_boundary",
          "boundary",
          "outcome",
          "crosscut",
          "cross_cutting_topic",
          "boundary_topic",
        ].includes(n.kind);
      let subY = p.y + 136;
      const sub = label.subtopics
        .map((lines, i) => {
          const text = `<text class="field-subtopic" x="${p.x + 15}" y="${subY}" font-size="17">${labelSpans(lines, p.x + 15, 23)}<title>${esc(d.subtopics[i])}</title></text>`;
          subY += lines.length * 23 + 8;
          return text;
        })
        .join("");
      const caption =
          lang === "zh"
            ? n.english
            : `${fieldWorkIds(n.id).length} mapped works`,
        captionLabel = fitLabel(caption, nw - 34, compact ? 21 : 15, 1);
      return `<a class="map-node concept-node ${n.id === selected ? "selected" : ""} ${selected && !near.has(n.id) ? "dim" : ""} ${meta ? "meta" : ""}" href="#route=${r.id}&node=${n.id}" aria-label="${esc(d.title)}"><title>${esc(d.title + " — " + d.question)}</title><rect class="concept-box" x="${p.x}" y="${p.y}" width="${nw}" height="${nh}" rx="8"/><rect class="concept-stripe" x="${p.x}" y="${p.y + 15}" width="3.5" height="${nh - 30}"/><text class="concept-title" x="${p.x + 15}" y="${p.y + (compact ? 43 : 32)}" font-size="${label.size}">${labelSpans(label.lines, p.x + 15, compact ? 39 : 27)}</text><text class="concept-subtitle" x="${p.x + 15}" y="${p.y + (deep ? 107 : nh - 18)}" font-size="${captionLabel.size}">${esc(caption)}</text>${sub}</a>`;
    })
    .join("");
  return `<svg xmlns="http://www.w3.org/2000/svg" class="field-network" viewBox="0 0 ${width} ${height}" role="group" aria-label="${esc(r.title + " " + L("mechanism map", "领域知识图谱"))}" style="--route:${colors[r.id]}"><defs><marker id="arrow-${r.id}-${compact ? "s" : "l"}" viewBox="0 0 7 7" refX="6" refY="3.5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="#8199a7"/></marker></defs>${arrows}${cards}</svg>`;
}
function overview() {
  return `<header class="landscape-heading"><div class="eyebrow">RSI RESEARCH LANDSCAPE · 2026.10.20</div><h1>${L("The RSI research landscape", "RSI 研究图谱")}</h1><p>${L("Three routes map the mechanisms. Select a topic or arrow to explore its subquestions, research, sources and participants.", "三条路线呈现研究机制。点击主题或箭头，进入子问题、具体研究、原始来源与参与团队。")}</p></header><div class="field-grid">${A.field.routes.map((r, i) => `<section class="field-card" style="--route:${colors[r.id]}"><div class="field-head"><div class="eyebrow">RESEARCH LANDSCAPE 0${i + 1}</div><h2>${r.title}</h2><p>${esc(routeData(r).tagline)}</p></div>${fieldMap(r, null, null, true)}<div class="field-foot"><a href="#route=${r.id}">${L("Explore the complete map", "展开整张图谱")} →</a><small>${r.nodes.length} ${L("topics", "主题")} · ${r.edges.length} ${L("links", "关系")}</small></div></section>`).join("")}</div><p class="map-caption">${L("Nodes are research topics; arrows show mechanism relationships. Research-to-research links have their own graph within each route.", "节点是研究主题，箭头是机制联系。每条路线另有研究关系图，可以查看论文之间的采用、扩展与对照。")}</p>${actorMatrix()}<div class="reader-entry"><div><h2>${L("Understand the mechanisms", "读懂 RSI")}</h2><p>${L("What changes, what provides feedback, and what survives into the next round? Compare six representative systems.", "改了哪里、靠什么改、什么进入下一轮？通过六项代表研究建立具体认识。")}</p></div><a class="button" href="#guide">${L("Open the reading guide", "阅读机制导读")} →</a><a class="button" href="#learn=00">${L("Model / LLM manual", "Model / LLM 教程")} →</a></div><section class="section-head"><h2>${L("How the routes connect", "三条路线怎样相接")}</h2></section><div class="grid-3">${A.field.bridges
    .map((b, i) => {
      const e = E.bridges[i];
      return `<article class="panel"><h3>${esc(L(e.title, b.title))}</h3><p>${esc(L(e.text, b.text))}</p><div class="mini-list">${b.topic_ids.map(nodeLink).join("")}</div></article>`;
    })
    .join(
      "",
    )}</div><div class="catalog-entry"><strong>${A.works.length} ${L("research records", "条研究记录")}</strong><a href="#works">${L("Search papers, methods and teams", "搜索论文、方法与团队")} →</a><a href="#discovery">${L("Explore the discovery pool", "浏览检索文献池")} →</a><a href="#research">${L("Research program", "研究主线")} →</a></div>`;
}
function actorMatrix() {
  const ws = A.works.filter((w) =>
    ["harness", "model", "hybrid"].includes(w.route),
  );
  const types = A.actors.types.filter((t) => t.main);
  const cell = (kind, route) => {
    const count = ws.filter(
      (w) =>
        (kind === "all" || w.actor_types.includes(kind)) &&
        (route === "all" || w.route === route),
    ).length;
    return `<td>${count ? `<a class="matrix-number" href="#participants&kind=${kind}&route=${route}&mode=works">${count}</a>` : "—"}</td>`;
  };
  return `<section class="actor-matrix-panel"><div class="section-head"><div><div class="eyebrow">RESEARCH PARTICIPANTS × ROUTES</div><h2>${L("Participants across the three routes", "研究主体与三条路线")}</h2></div><a href="#participants">${L("Browse institutions and collaboration", "浏览机构、团队与合作")} →</a></div><div class="table-wrap"><table class="actor-matrix"><thead><tr><th>${L("Research participants", "研究主体")}</th>${A.field.routes.map((r) => `<th>${r.title}</th>`).join("")}<th>${L("All routes", "全部路线")}</th></tr></thead><tbody>${types.map((t) => `<tr><th>${typeName(t.id)}</th>${A.field.routes.map((r) => cell(t.id, r.id)).join("")}${cell(t.id, "all")}</tr>`).join("")}<tr class="matrix-total"><th>${L("All participants · unique works", "全部主体 · 工作去重")}</th>${A.field.routes.map((r) => cell("all", r.id)).join("")}${cell("all", "all")}</tr></tbody></table></div><p class="matrix-note">${L("All model scales are included. Joint work can appear in more than one participant category; each work is counted once in the total.", "包含全部模型规模。合作工作可涉及多个主体类别；总数按工作去重。点击数量查看对应研究。")}</p></section>`;
}
function mechanismInspector(r, nodeId, edgeId) {
  const edge = r.edges.find((e) => e.id === edgeId),
    n = r.nodes.find((n) => n.id === nodeId),
    d = n && nodeData(n);
  if (edge)
    return `<div class="eyebrow">${L("MECHANISM RELATION", "机制关系")}</div><h2>${nodeLink(edge.source)} → ${nodeLink(edge.target)}</h2><p>${esc(edgeText(edge))}</p><h3>${L("Related research", "对应研究")}</h3><div class="mini-list">${edge.example_work_ids
      .filter((id) => works.has(id))
      .map(workOpen)
      .join(
        "",
      )}</div><h3>${L("Primary sources", "原始来源")}</h3><div class="source-list">${edge.source_urls.map((u, i) => sourceLink(u, L("Source " + (i + 1), "来源 " + (i + 1)))).join("<br>")}</div>`;
  if (d)
    return `<div class="eyebrow">${L("RESEARCH BRANCH", "研究分支")}</div><h2>${esc(d.title)}</h2><p><b>${esc(d.question)}</b></p><p>${esc(d.definition)}</p><h3>${L("Subquestions", "具体研究什么")}</h3><ul>${d.subtopics.map((t) => `<li>${esc(t)}</li>`).join("")}</ul><h3>${L("Methods and mechanisms", "主要方法与技术")}</h3><ul>${d.mechanisms.map((t) => `<li>${esc(t)}</li>`).join("")}</ul><h3>${L("Connections", "与其他分支的联系")}</h3>${r.edges
      .filter((e) => e.source === d.id || e.target === d.id)
      .map(
        (e) =>
          `<div class="topic-relation"><a href="#route=${r.id}&edge=${e.id}">${esc(nodeTitle(e.source === d.id ? e.target : e.source))} ↗</a><p>${esc(edgeText(e))}</p></div>`,
      )
      .join(
        "",
      )}<h3>${L("Mapped research", "相关研究")}</h3><div class="mini-list">${fieldWorkIds(d.id).map(workOpen).join("")}</div><h3>${L("Primary sources", "原始来源")}</h3>${n.source_urls.map((u, i) => sourceLink(u, L("Source " + (i + 1), "来源 " + (i + 1)))).join("<br>")}`;
  return `<div class="eyebrow">${r.title} / ${L("STRUCTURE", "研究结构")}</div><h2>${esc(routeData(r).question)}</h2><p>${L("Select a topic to inspect its subquestions, mechanisms and corresponding research. Select an arrow to read the relationship and its sources.", "点击主题查看子问题、机制与对应研究；点击箭头查看关系解释和原始来源。")}</p><h3>${L("Branches on this map", "图中各分支")}</h3><div class="node-index">${r.nodes.map((n) => nodeLink(n.id)).join("")}</div>`;
}
function routeRows(r, nodeId) {
  const mapped = new Set(
    (nodeId
      ? r.mappings.filter((m) => m.topic_ids.includes(nodeId))
      : r.mappings
    ).map((m) => m.work_id),
  );
  return A.works
    .filter(
      (w) =>
        mapped.has(w.id) &&
        (mapState.kind === "all" ||
          w.actor_types.includes(mapState.kind)) &&
        (mapState.org === "all" ||
          w.organizations.includes(mapState.org)) &&
        (mapState.status === "all" || w.status === mapState.status) &&
        (mapState.small || w.placement !== "small"),
    )
    .sort((a, b) => b.year - a.year || a.number - b.number);
}
function studyRow(w) {
  return `<article class="study-row"><div><div class="quiet">${routeName(w.route)} · ${w.year}</div><h3>${workOpen(w.id)}</h3><p>${esc(lang === "zh" ? w.summary : sections(w)[0])}</p></div><div class="study-team"><span class="quiet">${L("Participants", "参与团队")}</span><p>${(
    w.actor_ids || []
  )
    .map((id) => {
      const a = actors.find((a) => a.id === id);
      return `<a href="#people&actor=${id}">${esc(a?.name || id)}</a>`;
    })
    .join(
      " · ",
    )}</p><small>${w.actor_types.map(typeName).join(" × ")}</small></div><div class="study-action"><span>${readingName(w)}</span>${w.placement === "small" ? "<small>&lt;27B</small>" : ""}<a href="#work=${w.id}" data-open-work="${w.id}">${L("Read study", "阅读研究")} →</a></div></article>`;
}
function routeWorkList(r, nodeId) {
  const rows = routeRows(r, nodeId),
    size = 12,
    pages = Math.max(1, Math.ceil(rows.length / size));
  mapState.page = Math.min(mapState.page, pages);
  const orgs = [
    ...new Set(r.mappings.flatMap((m) => works.get(m.work_id).organizations)),
  ].sort();
  return `<div class="section-head"><h2>${nodeId ? esc(nodeTitle(nodeId)) + " · " : ""}${L("Research and participants", "研究工作与参与团队")}</h2><span>${rows.length} ${L("works", "项工作")}</span></div><div class="filter-chips">${[["all", L("All participants", "全部主体")], ...A.actors.types.filter((t) => t.main).map((t) => [t.id, typeName(t.id)])].map(([id, t]) => `<button data-route-kind="${id}" aria-pressed="${id === mapState.kind}">${t}</button>`).join("")}</div><details class="route-filters"><summary>${L("Affiliation, reading status and model scale", "机构、阅读状态与模型规模")}</summary><div class="filters"><select id="map-org" aria-label="${L("Affiliation", "机构")}">${options([["all", L("All affiliations", "全部机构")], ...orgs.map((x) => [x, x])], mapState.org)}</select><select id="map-status" aria-label="${L("Reading status", "阅读状态")}">${options(
    [
      ["all", L("All reading statuses", "全部阅读状态")],
      ["methods", L("Source reviewed", "来源已研读")],
      ["screened", L("Pending full text", "原文待补")],
    ],
    mapState.status,
  )}</select><label><input type="checkbox" id="map-small" ${mapState.small ? "checked" : ""}>${L("Include <27B mechanisms", "包含 <27B 补充机制")}</label></div></details><div class="study-list">${
    rows
      .slice((mapState.page - 1) * size, mapState.page * size)
      .map(studyRow)
      .join("") ||
    `<p class="empty">${L("No research matches these filters.", "当前筛选下没有对应研究。")}</p>`
  }</div>${pages > 1 ? `<div class="result-pager"><button data-route-page="${mapState.page - 1}" ${mapState.page === 1 ? "disabled" : ""}>←</button><span>${mapState.page} / ${pages}</span><button data-route-page="${mapState.page + 1}" ${mapState.page === pages ? "disabled" : ""}>→</button></div>` : ""}`;
}
function routePage(id, nodeId) {
  const r = A.field.routes.find((r) => r.id === id) || A.field.routes[0],
    s = routeState(),
    d = routeData(r);
  if (mapState.route !== r.id)
    Object.assign(mapState, {
      route: r.id,
      kind: "all",
      org: "all",
      status: "all",
      group: "all",
      page: 1,
    });
  const mode = s.mode || "domain";
  return `<header class="landscape-heading"><div class="eyebrow">${L("FIELD KNOWLEDGE GRAPH", "领域知识图谱")}</div><h1>${r.title}<small>${esc(d.tagline)}</small></h1><p>${esc(d.definition)}</p></header><div class="mode-bar"><a class="${mode === "domain" ? "active" : ""}" href="#route=${r.id}">${L("Mechanism landscape", "领域知识图谱")}</a><a class="${mode === "papers" ? "active" : ""}" href="#route=${r.id}&mode=papers">${L("Research relationship graph", "研究关系图")}</a><span>${L("Topics → subquestions → research → sources", "主题 → 子问题 → 研究 → 原文")}</span></div>${mode === "papers" ? paperGraphPage(r, s) : `<div class="domain-layout" style="--route:${colors[r.id]}"><section class="domain-canvas"><div class="canvas-toolbar"><b>${r.nodes.length} ${L("topics", "主题")} · ${r.nodes.reduce((n, x) => n + x.subtopics.length, 0)} ${L("subquestions", "子问题")}</b><div><button data-expand-map>${mapState.expanded ? L("Collapse subquestions", "收起子问题") : L("Expand all subquestions", "展开全部子问题")}</button><a class="button" href="#route=${r.id}">${L("Full map", "全图")}</a></div></div><div class="domain-scroll">${fieldMap(r, nodeId, s.edge)}</div><div class="map-caption">${L("Solid borders: objects, feedback and methods. Dashed borders: inheritance or recursive boundaries.", "实线边框：研究对象、反馈与方法；虚线边框：继承或递归边界。")}</div></section><aside class="domain-inspector" id="node-detail">${mechanismInspector(r, nodeId, s.edge)}</aside></div><section id="route-work-list">${routeWorkList(r, nodeId)}</section>`}<details class="route-context"><summary>${L("Reading paths, the update cycle and open questions", "阅读路径、运行过程与开放问题")}</summary><div class="grid-3">${A.paths[r.id].map((p, i) => `<article class="panel"><h3>${esc(L(pathTexts[r.id][i][0], p.title))}</h3><p>${esc(L(pathTexts[r.id][i][1], p.question))}</p><div class="mini-list">${p.ids.map(workOpen).join("")}</div></article>`).join("")}</div><h3>${L("The update cycle", "运行过程")}</h3><p>${esc(d.scene)}</p><div class="loop">${d.loop.map((x, i) => `<span><b>${i + 1}</b>${esc(x)}</span>`).join("")}</div><h3>${L("Key distinctions", "关键维度")}</h3><div class="grid-3">${r.facets.map((f, i) => `<article class="panel"><h4>${esc(L(E.routes[r.id].facets[i].title, f.title))}</h4><p>${esc(L(E.routes[r.id].facets[i].text, f.text))}</p></article>`).join("")}</div><h3>${L("Open questions", "开放问题")}</h3>${r.open_questions.map((q, i) => `<article class="open-question"><h4>${esc(L(d.open_questions[i], q.title))}</h4><p>${esc(L(E.routes[r.id].open_details[i], q.text))}</p></article>`).join("")}</details>`;
}
function graphWorks(r) {
  return A.works.filter(
    (w) =>
      w.route === r.id &&
      (mapState.group === "all" || w.methods.includes(mapState.group)) &&
      (mapState.org === "all" || w.organizations.includes(mapState.org)) &&
      (mapState.status === "all" || w.status === mapState.status) &&
      (mapState.small || w.placement !== "small"),
  );
}
function paperGraph(r, s) {
  const ws = graphWorks(r),
    active = new Set(ws.map((w) => w.id)),
    groups = A.groups.filter(
      (g) => g.route === r.id && ws.some((w) => w.cluster === g.id),
    ),
    positions = new Map(),
    hubs = new Map();
  let y = 28;
  const width = 1140,
    nw = 264,
    nh = 79;
  for (const g of groups) {
    const rows = ws
      .filter((w) => w.cluster === g.id)
      .sort((a, b) => a.year - b.year || a.number - b.number);
    hubs.set(g.id, {
      x: 18,
      y: y + Math.max(0, Math.ceil(rows.length / 3) - 1) * 54,
    });
    rows.forEach((w, i) =>
      positions.set(w.id, {
        x: 285 + (i % 3) * 280,
        y: y + Math.floor(i / 3) * 111,
      }),
    );
    y += Math.max(1, Math.ceil(rows.length / 3)) * 111 + 48;
  }
  const edge = A.relations.find((e) => e.id === s.relation),
    selected = s.selected,
    neighbors = new Set(
      selected
        ? [
            selected,
            ...A.relations
              .filter((e) => e.source === selected || e.target === selected)
              .flatMap((e) => [e.source, e.target]),
          ]
        : [],
    );
  let wires = "";
  if (mapState.methods)
    for (const w of ws) {
      const p = positions.get(w.id);
      for (const method of w.methods) {
        const h = hubs.get(method);
        if (h)
          wires += `<path class="method-wire" d="M${h.x + 230} ${h.y + 28} C${h.x + 250} ${h.y + 28} ${p.x - 25} ${p.y + nh / 2} ${p.x} ${p.y + nh / 2}"/>`;
      }
    }
  const edges = A.relations
    .filter((e) => active.has(e.source) && active.has(e.target))
    .map((e) => {
      const a = positions.get(e.source),
        b = positions.get(e.target),
        focus =
          e.id === s.relation ||
          (selected && (e.source === selected || e.target === selected)),
        dim = (selected || edge) && !focus;
      const x1 = a.x + nw / 2,
        y1 = a.y + nh,
        x2 = b.x + nw / 2,
        y2 = b.y,
        mid = (y1 + y2) / 2;
      return `<a href="#route=${r.id}&mode=papers&relation=${e.id}" class="paper-edge-link ${focus ? "active" : ""} ${dim ? "dim" : ""}" aria-label="${esc(works.get(e.source).short + " → " + works.get(e.target).short)}"><title>${esc(lang === "en" ? E.relations[e.id].explanation : e.explanation)}</title><path class="paper-edge ${e.kind === "method_comparison" ? "comparison" : ""}" d="M${x1} ${y1} C${x1} ${mid} ${x2} ${mid} ${x2} ${y2}" marker-end="url(#paper-arrow)"/><path class="concept-hit" d="M${x1} ${y1} C${x1} ${mid} ${x2} ${mid} ${x2} ${y2}"/></a>`;
    })
    .join("");
  const cards = ws
    .map((w) => {
      const p = positions.get(w.id),
        title = fitLabel(w.short, nw - 24, 16, 2, 600);
      return `<a class="paper-node ${w.id === selected ? "selected" : ""} ${selected && !neighbors.has(w.id) ? "dim" : ""}" href="#route=${r.id}&mode=papers&selected=${w.id}"><title>${esc(sections(w)[0])}</title><rect x="${p.x}" y="${p.y}" width="${nw}" height="${nh}" rx="7" ${w.status === "screened" ? 'stroke-dasharray="4 3"' : ""}/><text x="${p.x + 12}" y="${p.y + 23}" font-size="${title.size}" font-weight="600">${labelSpans(title.lines, p.x + 12, 20)}</text><text class="paper-year" x="${p.x + 12}" y="${p.y + 66}" font-size="12">${w.year} · ${esc(readingName(w))}</text></a>`;
    })
    .join("");
  const labels = groups
    .map((g) => {
      const p = hubs.get(g.id);
      const label = fitLabel(groupName(g), 206, 15, 3);
      return `<g class="paper-group"><rect x="${p.x}" y="${p.y}" width="230" height="80" rx="6"/><text x="${p.x + 12}" y="${p.y + 23}" font-size="${label.size}">${labelSpans(label.lines, p.x + 12, 21)}</text></g>`;
    })
    .join("");
  return `<svg class="paper-network" style="width:calc(max(780px, 100%) * ${mapState.zoom / 0.9});height:auto" width="${width * mapState.zoom}" height="${Math.max(y, 240) * mapState.zoom}" viewBox="0 0 ${width} ${Math.max(y, 240)}" role="group" aria-label="${L("Research relationship graph", "研究关系图")}"><defs><marker id="paper-arrow" viewBox="0 0 7 7" refX="6" refY="3.5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="#678997"/></marker></defs>${wires}${edges}${labels}${cards}</svg>`;
}
function paperInspector(r, s) {
  const edge = A.relations.find((e) => e.id === s.relation),
    w = works.get(s.selected);
  if (edge) return relationCard(edge);
  if (w)
    return `<div class="eyebrow">${w.year} · ${readingName(w)}</div><h2>${esc(w.short)}</h2><p>${esc(lang === "zh" ? w.summary : sections(w)[0])}</p><p class="quiet">${esc(w.team)}</p><a class="button primary" href="#work=${w.id}" data-open-work="${w.id}">${L("Read the complete study", "展开完整研究卡片")} →</a><h3>${L("Connected research", "相邻研究")}</h3>${A.relations
      .filter((e) => e.source === w.id || e.target === w.id)
      .map(relationCard)
      .join("")}`;
  return `<h2>${L("Follow the research relationships", "沿研究关系阅读")}</h2><p>${L("Select a study to highlight its neighbors. Select a line to read the relationship and original sources. Relationships crossing into another route remain visible in the inspector.", "点击研究节点突出相邻工作；点击连线阅读关系与原始来源。跨路线关系也会列在详情中。")}</p><p>${L("Solid lines: source-supported relations. Dashed lines: editorial method comparisons.", "实线：来源支持的关系；虚线：综述中的方法对照。")}</p>`;
}
function paperGraphPage(r, s) {
  const groups = A.groups.filter((g) => g.route === r.id),
    orgs = [
      ...new Set(
        A.works.filter((w) => w.route === r.id).flatMap((w) => w.organizations),
      ),
    ].sort();
  return `<div class="filters"><select id="paper-group" aria-label="${L("Method group", "方法分组")}">${options([["all", L("All methods", "全部问题与方法")], ...groups.map((g) => [g.id, groupName(g)])], mapState.group)}</select><select id="map-org" aria-label="${L("Affiliation", "机构")}">${options([["all", L("All affiliations", "全部机构")], ...orgs.map((o) => [o, o])], mapState.org)}</select><select id="map-status" aria-label="${L("Reading status", "阅读状态")}">${options(
    [
      ["all", L("All reading statuses", "全部阅读状态")],
      ["methods", L("Source reviewed", "来源已研读")],
      ["screened", L("Pending full text", "原文待补")],
    ],
    mapState.status,
  )}</select><label><input id="map-small" type="checkbox" ${mapState.small ? "checked" : ""}>${L("Include <27B", "包含 <27B")}</label><button data-reset-paper>${L("Reset", "重置")}</button></div><div class="domain-layout" style="--route:${colors[r.id]}"><section class="domain-canvas"><div class="canvas-toolbar"><b>${graphWorks(r).length} ${L("studies", "项研究")}</b><div><button data-zoom="out" aria-label="${L("Zoom out", "缩小")}">−</button><button data-zoom="reset">${Math.round((mapState.zoom / 0.9) * 100)}%</button><button data-zoom="in" aria-label="${L("Zoom in", "放大")}">+</button><button data-method-wires aria-pressed="${mapState.methods}">${L("Method links", "方法连线")}</button></div></div><div class="paper-viewport" id="paper-viewport">${paperGraph(r, s)}</div></section><aside class="domain-inspector">${paperInspector(r, s)}</aside></div>`;
}
const participantState = {
  key: "",
  kind: "all",
  route: "all",
  mode: "institutions",
  actor: null,
  coop: "all",
  q: "",
  page: 1,
};
function participantWorks() {
  return A.works.filter(
    (w) =>
      (participantState.actor
        ? w.actor_ids.includes(participantState.actor)
        : ["harness", "model", "hybrid"].includes(w.route)) &&
      (participantState.kind === "all" ||
        w.actor_types.includes(participantState.kind)) &&
      (participantState.route === "all" ||
        w.route === participantState.route) &&
      (participantState.coop === "all" ||
        w.cooperation === participantState.coop) &&
      (!participantState.q ||
        [w.short, w.title, w.team, ...sections(w)]
          .join(" ")
          .toLowerCase()
          .includes(participantState.q.toLowerCase())),
  );
}
function participantsPage() {
  const s = routeState(),
    key = [s.kind, s.route, s.mode, s.actor].join(":");
  if (key !== participantState.key)
    Object.assign(participantState, {
      key,
      kind: s.kind || "all",
      route: s.route || "all",
      mode: s.mode || "institutions",
      actor: s.actor || null,
      q: "",
      coop: "all",
      page: 1,
    });
  return `<header class="landscape-heading"><div class="eyebrow">PEOPLE, INSTITUTIONS & COLLABORATION</div><h1>${L("Institutions and teams", "机构与团队")}</h1><p>${L("Explore the work through its participants, research routes and collaboration.", "从研究主体进入具体工作，比较它们研究的对象、方法与合作关系。")}</p></header>${actorMatrix()}<div class="section-head"><h2>${L("Browse research and teams", "浏览研究与团队")}</h2><a href="#people">${L("Company profiles and all affiliations", "公司资料与全部机构")} →</a></div><div class="filters"><input id="participant-query" type="search" value="${esc(participantState.q)}" placeholder="${L("Institution, company, paper or method…", "机构、公司、论文或方法……")}" aria-label="${L("Search participants", "检索机构与工作")}"><select id="participant-kind" aria-label="${L("Participant type", "研究主体")}">${options([["all", L("All participants", "全部研究主体")], ...A.actors.types.map((t) => [t.id, typeName(t.id)])], participantState.kind)}</select><select id="participant-route" aria-label="${L("Research route", "技术路线")}">${options([["all", L("All three routes", "三条主路线")], ...A.field.routes.map((r) => [r.id, r.title]), ["crosscut", routeName("crosscut")]], participantState.route)}</select><select id="participant-coop" aria-label="${L("Collaboration", "合作关系")}">${options(
    [
      ["all", L("All collaboration", "全部合作关系")],
      ["academic_industry", L("Academia–industry", "产学合作")],
      ["multi_org", L("Multiple organizations", "跨机构合作")],
      ["single", L("Single organization", "单一机构")],
      ["unresolved", L("Independent / unresolved", "独立作者 / 待确认")],
    ],
    participantState.coop,
  )}</select></div><div class="mode-bar"><button data-participant-mode="institutions" aria-pressed="${participantState.mode === "institutions"}">${L("Institutions and teams", "机构与团队")}</button><button data-participant-mode="works" aria-pressed="${participantState.mode === "works"}">${L("Research works", "研究工作")}</button></div><div id="participant-results">${participantResults()}</div>`;
}
function participantResults() {
  const ws = participantWorks();
  let list;
  if (participantState.mode === "works") list = ws;
  else {
    const ids = new Set(ws.flatMap((w) => w.actor_ids));
    list = actors
      .filter(
        (a) =>
          (participantState.kind === "all" ||
            a.kind === participantState.kind) &&
          (!participantState.actor || a.id === participantState.actor) &&
          ((participantState.route === "all" &&
            participantState.coop === "all") ||
            ids.has(a.id)) &&
          (!participantState.q ||
            [a.name, ...a.aliases, ...(a.search_aliases || [])]
              .join(" ")
              .toLowerCase()
              .includes(participantState.q.toLowerCase())),
      )
      .sort(
        (a, b) =>
          b.work_ids.length - a.work_ids.length || a.name.localeCompare(b.name),
      );
  }
  const pages = Math.max(1, Math.ceil(list.length / 18));
  participantState.page = Math.min(participantState.page, pages);
  const rows = list.slice(
    (participantState.page - 1) * 18,
    participantState.page * 18,
  );
  return `<p class="quiet">${list.length} ${participantState.mode === "works" ? L("works", "项工作") : L("institutions / teams", "个机构 / 团队")}</p>${
    participantState.mode === "works"
      ? rows.map(studyRow).join("")
      : `<div class="table-wrap"><table class="participant-table"><thead><tr><th>${L("Institution / team", "机构 / 团队")}</th><th>${L("Type", "主体类型")}</th>${A.field.routes.map((r) => `<th>${r.title}</th>`).join("")}<th>${L("All work", "全部工作")}</th></tr></thead><tbody>${rows
          .map((a) => {
            const owned = A.works.filter((w) => w.actor_ids.includes(a.id));
            return `<tr><td><a href="#people&actor=${a.id}">${esc(a.name)}</a><small>${esc(
              a.aliases
                .filter((x) => x !== a.name)
                .slice(0, 2)
                .join(" · "),
            )}</small></td><td>${typeName(a.kind)}</td>${A.field.routes
              .map((r) => {
                const n = owned.filter((w) => w.route === r.id).length;
                return `<td>${n ? `<a href="#participants&actor=${a.id}&route=${r.id}&mode=works">${n}</a>` : "—"}</td>`;
              })
              .join(
                "",
              )}<td><a href="#people&actor=${a.id}">${owned.length} →</a></td></tr>`;
          })
          .join("")}</tbody></table></div>`
  }${!list.length ? `<p class="empty">${L("No matching records.", "没有匹配记录。")}</p>` : ""}${pages > 1 ? `<div class="result-pager"><button data-participant-page="${participantState.page - 1}" ${participantState.page === 1 ? "disabled" : ""}>←</button><span>${participantState.page} / ${pages}</span><button data-participant-page="${participantState.page + 1}" ${participantState.page === pages ? "disabled" : ""}>→</button></div>` : ""}`;
}
function originalReview(w) {
  const r = w.review;
  if (!r) return "";
  const pairs = [
    ["Loop", "运行闭环", r.mechanism.loop],
    ["Changed object", "更新对象", r.mechanism.changed],
    ["Fixed conditions", "固定条件", r.mechanism.fixed],
    ["Feedback", "反馈信号", r.mechanism.feedback],
    ["Inheritance", "跨轮继承", r.mechanism.inheritance],
    ["Setup", "实验设置", r.results.setup],
    ["Comparison", "比较基线", r.results.comparison],
    ["Results", "主要结果", r.results.result],
    ["Ablation", "消融与归因", r.results.ablation],
    ["Cost", "资源代价", r.results.cost],
    ["Generalization", "泛化范围", r.results.generalization],
    ["Bottleneck", "所针对的瓶颈", r.contribution.bottleneck],
    ["Key idea", "关键思想", r.contribution.insight],
    ["Contribution", "研究价值", r.contribution.value],
    ["Relation to RSI", "与 RSI 的关系", r.contribution.relation_to_rsi],
    ["Method comparison", "与相关方法的差别", r.contribution.comparison],
    ["Scope decision", "收录依据", r.scope_reason],
  ];
  return `<details class="source-review"><summary>${L("Original detailed review notes (Chinese)", "展开完整实验对照、反馈继承与原文定位")}</summary><dl>${pairs
    .filter((x) => x[2])
    .map(([en, zh, t]) => `<dt>${L(en, zh)}</dt><dd lang="zh">${esc(t)}</dd>`)
    .join(
      "",
    )}</dl><div class="source-list">${r.sources.map((s) => `<p>${sourceLink(s.url, L("Primary source", "原始资料"))} · ${esc(s.location)}</p>`).join("")}</div></details>`;
}
function readerPage() {
  const raw = A.reader_guide,
    g = lang === "en" ? E.reader_guide : raw,
    choice = new URLSearchParams(location.hash.slice(1)).get("case") || "dgm",
    c = g.cases.find((c) => c.id === choice) || g.cases[0];
  return `<header class="landscape-heading"><div class="eyebrow">READING THE RSI LANDSCAPE</div><h1>${L("Understand RSI mechanisms", "读懂 RSI：机制与研究对照")}</h1><p>${L("Identify what changes, what produces feedback, and what the successor inherits. Then compare the implementation and results.", "先分清改了哪里、靠什么改、什么进入下一轮，再比较实现方式与研究结果。")}</p></header><div class="guide-axis-grid">${g.axes.map((x) => `<article class="panel"><div class="eyebrow">${x.axis}</div><h3>${esc(x.title)}</h3><p><b>${esc(x.question)}</b></p><p>${esc(x.content)}</p></article>`).join("")}</div><div class="section-head"><h2>${L("Six worked examples", "六项研究的机制对照")}</h2></div><div class="guide-case-tabs">${g.cases.map((x) => `<a href="#guide&case=${x.id}" class="${x.id === c.id ? "active" : ""}">${esc(works.get(x.id).short)}</a>`).join("")}</div><article class="panel"><h2>${esc(c.headline)}</h2><dl class="case-details">${[
    ["loop", "Update loop", "运行闭环"],
    ["changed", "What changes", "实际改变"],
    ["feedback", "Feedback", "反馈"],
    ["retained", "What persists", "继承"],
    ["fixed", "What stays fixed", "固定条件"],
    ["insight", "Key idea", "核心思想"],
    ["boundary", "Result scope", "结果范围"],
    ["basis", "Source locations", "原文位置"],
  ]
    .map(([key, en, zh]) => `<dt>${L(en, zh)}</dt><dd>${esc(c[key])}</dd>`)
    .join(
      "",
    )}</dl><a class="button" href="#work=${c.id}" data-open-work="${c.id}">${L("Read complete study", "展开完整研究卡片")} →</a></article><div class="section-head"><h2>${L("Comparisons that distinguish mechanisms", "区分机制的研究对照")}</h2></div><div class="two-col">${g.comparisons.map((x) => `<article class="panel"><h3>${esc(x.title)}</h3><p>${esc(x.text)}</p><small>${esc(x.kind)}</small><div class="mini-list">${x.ids.map(workOpen).join("")}</div></article>`).join("")}</div>`;
}
const leadState = { q: "", filter: "all", page: 1 };
const leadNames = {
  catalog: ["In the reading catalog", "已在阅读目录"],
  scope_candidate: ["Method candidate", "方法候选 · 待精读"],
  enabling_or_background: ["Enabling method / background", "使能方法 / 背景"],
  evaluation_candidate: ["Evaluation / theory candidate", "评测 / 理论候选"],
  survey: ["Survey / roadmap", "综述 / 路线图"],
  outside_scope: ["Outside this scope", "本图范围外"],
  duplicate: ["Matched catalog record", "已对应目录"],
};
const leadName = (id) => (leadNames[id] ? L(...leadNames[id]) : id);
function discoveryPage() {
  return `<header class="landscape-heading"><div class="eyebrow">DISCOVERY POOL / ${A.discovery_review.entries.length}</div><h1>${L("Research discovery and scope", "文献检索与范围判断")}</h1><p>${L("Browse the original discovery pool, abstracts and recorded relevance decisions alongside the detailed catalog. The discovery pool and catalog overlap; unmatched entries have not all undergone full-paper review.", "浏览原有检索池、摘要和逐条相关性判断，并跳转到已建立的详细研究卡片。检索池与目录存在交集；尚未匹配的条目并非全部完成全文研读。")}</p></header><div class="filter-chips">${Object.entries(
    A.discovery_review.counts,
  )
    .map(
      ([k, n]) =>
        `<button data-lead-filter="${k}">${leadName(k)} · ${n}</button>`,
    )
    .join(
      "",
    )}</div><div class="filters" style="margin-top:20px"><input id="lead-query" type="search" aria-label="${L("Search discovery pool", "检索文献线索")}" placeholder="${L("Title, author or arXiv ID…", "题名、作者或 arXiv 编号……")}" value="${esc(leadState.q)}"><select id="lead-filter" aria-label="${L("Relevance decision", "范围判断")}">${options([["all", L("All entries", "全部线索")], ...Object.keys(A.discovery_review.counts).map((k) => [k, leadName(k)])], leadState.filter)}</select></div><div id="lead-results">${discoveryResults()}</div>`;
}
function discoveryResults() {
  const rows = A.discovery_review.entries.filter(
    (x) =>
      (leadState.filter === "all" || x.decision === leadState.filter) &&
      [x.title, x.arxiv_id, x.reason, x.abstract, ...(x.authors || [])]
        .join(" ")
        .toLowerCase()
        .includes(leadState.q.toLowerCase()),
  );
  const pages = Math.max(1, Math.ceil(rows.length / 12));
  leadState.page = Math.min(leadState.page, pages);
  return `<p class="quiet">${rows.length} ${L("entries", "条线索")} · ${leadState.page} / ${pages}</p>${rows
    .slice((leadState.page - 1) * 12, leadState.page * 12)
    .map(
      (x) =>
        `<details class="lead-entry"><summary><small>${esc(x.arxiv_id)} · ${leadName(x.decision)}</small>${esc(x.title)}</summary><p>${esc(x.authors.join(" · "))}</p><p>${esc(x.abstract)}</p>${lang === "zh" ? `<p>${esc(x.reason)}</p>` : `<details><summary>Original relevance note (Chinese)</summary><p lang="zh">${esc(x.reason)}</p></details>`}${x.matched_work_id && works.has(x.matched_work_id) ? `<p>${workOpen(x.matched_work_id)}</p>` : ""}${sourceLink(x.url, L("Primary source", "原始资料"))}</details>`,
    )
    .join(
      "",
    )}<div class="result-pager"><button data-lead-page="${leadState.page - 1}" ${leadState.page === 1 ? "disabled" : ""}>←</button><span>${leadState.page} / ${pages}</span><button data-lead-page="${leadState.page + 1}" ${leadState.page === pages ? "disabled" : ""}>→</button></div>`;
}
function showWork(id) {
  const box = document.getElementById("paper-dialog");
  box.querySelector("[data-dialog-language]").textContent = L(
    "中文",
    "English",
  );
  document.getElementById("paper-content").innerHTML = workPage(id);
  if (!box.open) box.showModal();
  box.scrollTop = 0;
  box.dataset.work = id;
}
function redrawRouteWorks() {
  const s = routeState(),
    el = document.getElementById("route-work-list");
  if (el) el.innerHTML = routeWorkList(selectedRoute(), s.node);
  else render();
}
function redrawPaper() {
  const view = document.getElementById("paper-viewport"),
    scroll = view && [view.scrollLeft, view.scrollTop];
  render();
  const next = document.getElementById("paper-viewport");
  if (scroll && next) {
    next.scrollLeft = scroll[0];
    next.scrollTop = scroll[1];
  }
}
document.getElementById("search-form").addEventListener("submit", (e) => {
  e.preventDefault();
  filters.q = document.getElementById("global-query").value;
  filters.route = "all";
  filters.scope = "all";
  filters.scale = "all";
  if (location.hash === "#works") render();
  else location.hash = "works";
});
document.addEventListener("click", (e) => {
  const open = e.target.closest("[data-open-work]");
  if (open) {
    e.preventDefault();
    showWork(open.dataset.openWork);
    return;
  }
  if (e.target.closest("[data-close-dialog]"))
    document.getElementById("paper-dialog").close();
  if (e.target.closest("[data-expand-map]")) {
    mapState.expanded = !mapState.expanded;
    render();
  }
  if (e.target.closest("[data-method-wires]")) {
    mapState.methods = !mapState.methods;
    redrawPaper();
  }
  if (e.target.closest("[data-reset-paper]")) {
    Object.assign(mapState, {
      group: "all",
      org: "all",
      status: "all",
      small: false,
      zoom: 0.9,
      methods: true,
    });
    location.hash = "route=" + selectedRoute().id + "&mode=papers";
    render();
  }
  const zoom = e.target.closest("[data-zoom]");
  if (zoom) {
    mapState.zoom =
      zoom.dataset.zoom === "reset"
        ? 0.9
        : Math.max(
            0.35,
            Math.min(
              1.8,
              mapState.zoom + (zoom.dataset.zoom === "in" ? 0.15 : -0.15),
            ),
          );
    redrawPaper();
  }
  const kind = e.target.closest("[data-route-kind]");
  if (kind) {
    mapState.kind = kind.dataset.routeKind;
    mapState.page = 1;
    redrawRouteWorks();
  }
  const page = e.target.closest("[data-route-page]");
  if (page) {
    mapState.page = Number(page.dataset.routePage);
    redrawRouteWorks();
    document
      .getElementById("route-work-list")
      .scrollIntoView({ block: "start" });
  }
  const mode = e.target.closest("[data-participant-mode]");
  if (mode) {
    participantState.mode = mode.dataset.participantMode;
    participantState.page = 1;
    render();
  }
  const pp = e.target.closest("[data-participant-page]");
  if (pp) {
    participantState.page = Number(pp.dataset.participantPage);
    document.getElementById("participant-results").innerHTML =
      participantResults();
  }
  const lf = e.target.closest("[data-lead-filter]");
  if (lf) {
    leadState.filter = lf.dataset.leadFilter;
    leadState.page = 1;
    render();
  }
  const lp = e.target.closest("[data-lead-page]");
  if (lp) {
    leadState.page = Number(lp.dataset.leadPage);
    document.getElementById("lead-results").innerHTML = discoveryResults();
  }
  if (e.target.closest("#language, [data-dialog-language]")) {
    const box = document.getElementById("paper-dialog");
    if (box.open) showWork(box.dataset.work);
  }
});
document.addEventListener("input", (e) => {
  if (e.target.id === "participant-query") {
    participantState.q = e.target.value;
    participantState.page = 1;
    document.getElementById("participant-results").innerHTML =
      participantResults();
  }
  if (e.target.id === "lead-query") {
    leadState.q = e.target.value;
    leadState.page = 1;
    document.getElementById("lead-results").innerHTML = discoveryResults();
  }
});
document.addEventListener("change", (e) => {
  const key = {
    "map-org": "org",
    "map-status": "status",
    "paper-group": "group",
  }[e.target.id];
  if (key) {
    mapState[key] = e.target.value;
    mapState.page = 1;
    redrawRouteWorks();
  }
  if (e.target.id === "map-small") {
    mapState.small = e.target.checked;
    mapState.page = 1;
    redrawRouteWorks();
  }
  const pk = {
    "participant-kind": "kind",
    "participant-route": "route",
    "participant-coop": "coop",
  }[e.target.id];
  if (pk) {
    participantState[pk] = e.target.value;
    participantState.page = 1;
    document.getElementById("participant-results").innerHTML =
      participantResults();
  }
  if (e.target.id === "lead-filter") {
    leadState.filter = e.target.value;
    leadState.page = 1;
    document.getElementById("lead-results").innerHTML = discoveryResults();
  }
});
window.addEventListener("hashchange", () => {
  const box = document.getElementById("paper-dialog");
  if (box.open) box.close();
});
document.getElementById("paper-dialog").addEventListener("close", () => {
  document.getElementById("paper-content").replaceChildren();
});
render();
document.fonts.ready.then(render);
