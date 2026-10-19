#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
WORKS_PATH = ROOT / "data" / "works.json"
GRAPH_PATH = ROOT / "data" / "knowledge-graph.json"
HYPOTHESES_PATH = ROOT / "data" / "hypotheses.json"

ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SNAKE_RE = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")
EVIDENCE = {"reported", "reproduced", "replicated", "contradicted", "open"}
AUDIT = {"pending", "in_progress", "complete"}
SOURCE_TYPES = {"paper", "repository", "project_page", "proceedings"}


def fail(message: str) -> None:
    raise ValueError(message)


def load(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_url(value: object, context: str) -> None:
    if not isinstance(value, str):
        fail(f"{context}: URL must be a string")
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc:
        fail(f"{context}: URL must use HTTPS: {value!r}")


def validate_works(data: object) -> set[str]:
    if not isinstance(data, dict):
        fail("works catalog root must be an object")
    required = {"schema_version", "updated", "depth_definitions", "evidence_definitions", "works"}
    if set(data) != required:
        fail(f"works catalog keys must be exactly {sorted(required)}")
    if not re.fullmatch(r"\d+\.\d+\.\d+", data["schema_version"]):
        fail("works schema_version must use MAJOR.MINOR.PATCH")
    if set(data["evidence_definitions"]) != EVIDENCE:
        fail("evidence_definitions must contain the five evidence labels")

    ids: set[str] = set()
    for index, work in enumerate(data["works"]):
        context = f"works[{index}]"
        required_work = {
            "id", "name", "year", "role", "reported_depth", "changed_objects",
            "evidence_status", "audit_status", "central_limit", "sources",
        }
        if not isinstance(work, dict) or set(work) != required_work:
            fail(f"{context}: invalid keys")
        work_id = work["id"]
        if not isinstance(work_id, str) or not ID_RE.fullmatch(work_id):
            fail(f"{context}: invalid id {work_id!r}")
        if work_id in ids:
            fail(f"duplicate work id: {work_id}")
        ids.add(work_id)
        if not isinstance(work["name"], str) or not work["name"].strip():
            fail(f"{work_id}: empty name")
        if not isinstance(work["year"], int) or not 1900 <= work["year"] <= 2100:
            fail(f"{work_id}: invalid year")
        if not isinstance(work["role"], str) or not SNAKE_RE.fullmatch(work["role"]):
            fail(f"{work_id}: role must use lowercase snake_case")
        if work["reported_depth"] not in data["depth_definitions"]:
            fail(f"{work_id}: undefined reported_depth {work['reported_depth']!r}")
        changed = work["changed_objects"]
        if not isinstance(changed, list) or len(changed) != len(set(changed)):
            fail(f"{work_id}: changed_objects must be a unique list")
        for item in changed:
            if not isinstance(item, str) or not SNAKE_RE.fullmatch(item):
                fail(f"{work_id}: invalid changed object {item!r}")
        if work["evidence_status"] not in EVIDENCE:
            fail(f"{work_id}: invalid evidence status")
        if work["audit_status"] not in AUDIT:
            fail(f"{work_id}: invalid audit status")
        if not isinstance(work["central_limit"], str) or len(work["central_limit"].strip()) < 20:
            fail(f"{work_id}: central_limit is too short")
        sources = work["sources"]
        if not isinstance(sources, list) or not sources:
            fail(f"{work_id}: sources must be non-empty")
        seen_urls: set[str] = set()
        for source in sources:
            if not isinstance(source, dict) or set(source) != {"type", "url"}:
                fail(f"{work_id}: each source must contain exactly type and url")
            if source["type"] not in SOURCE_TYPES:
                fail(f"{work_id}: invalid source type")
            validate_url(source["url"], work_id)
            if source["url"] in seen_urls:
                fail(f"{work_id}: duplicate source URL")
            seen_urls.add(source["url"])
    return ids


def validate_graph(data: object, work_ids: set[str]) -> None:
    if not isinstance(data, dict):
        fail("knowledge graph root must be an object")
    if data.get("schema_version") in {"4.0.0", "5.0.0"}:
        from check_literature_graphs import check
        check()
        return
    required = {"schema_version", "updated", "nodes", "edges", "work_bindings"}
    if set(data) != required:
        fail(f"knowledge graph keys must be exactly {sorted(required)}")

    node_ids: set[str] = set()
    for node in data["nodes"]:
        if not isinstance(node, dict) or set(node) != {"id", "type", "label"}:
            fail("invalid graph node")
        if not ID_RE.fullmatch(node["id"]):
            fail(f"invalid node id {node['id']!r}")
        if node["id"] in node_ids:
            fail(f"duplicate node id {node['id']}")
        node_ids.add(node["id"])

    for edge in data["edges"]:
        if not isinstance(edge, dict) or set(edge) != {"source", "target", "relation"}:
            fail("invalid graph edge")
        if edge["source"] not in node_ids or edge["target"] not in node_ids:
            fail(f"edge references unknown node: {edge}")
        if not SNAKE_RE.fullmatch(edge["relation"]):
            fail(f"invalid edge relation {edge['relation']!r}")

    bound: set[str] = set()
    for binding in data["work_bindings"]:
        if not isinstance(binding, dict) or set(binding) != {"work_id", "node_ids"}:
            fail("invalid work binding")
        if binding["work_id"] not in work_ids:
            fail(f"binding references unknown work {binding['work_id']!r}")
        if binding["work_id"] in bound:
            fail(f"duplicate binding for {binding['work_id']}")
        bound.add(binding["work_id"])
        if not binding["node_ids"]:
            fail(f"{binding['work_id']}: empty node binding")
        for node_id in binding["node_ids"]:
            if node_id not in node_ids:
                fail(f"{binding['work_id']}: unknown node {node_id!r}")



def validate_hypotheses(data: object) -> None:
    if not isinstance(data, dict):
        fail("hypothesis registry root must be an object")
    required = {"schema_version", "updated", "status_definitions", "hypotheses"}
    if set(data) != required:
        fail(f"hypothesis registry keys must be exactly {sorted(required)}")
    statuses = {"open", "supported", "weakened", "falsified", "superseded"}
    if set(data["status_definitions"]) != statuses:
        fail("hypothesis status_definitions are invalid")

    seen: set[str] = set()
    for index, item in enumerate(data["hypotheses"]):
        context = f"hypotheses[{index}]"
        required_item = {"id", "status", "statement", "decisive_test", "files"}
        if not isinstance(item, dict) or set(item) != required_item:
            fail(f"{context}: invalid keys")
        hypothesis_id = item["id"]
        if not isinstance(hypothesis_id, str) or not ID_RE.fullmatch(hypothesis_id):
            fail(f"{context}: invalid id")
        if hypothesis_id in seen:
            fail(f"duplicate hypothesis id: {hypothesis_id}")
        seen.add(hypothesis_id)
        if item["status"] not in statuses:
            fail(f"{hypothesis_id}: invalid status")
        if not isinstance(item["statement"], str) or len(item["statement"].strip()) < 20:
            fail(f"{hypothesis_id}: statement is too short")
        if not isinstance(item["decisive_test"], str) or len(item["decisive_test"].strip()) < 20:
            fail(f"{hypothesis_id}: decisive_test is too short")
        if not isinstance(item["files"], list) or not item["files"]:
            fail(f"{hypothesis_id}: files must be non-empty")


def validate_scope_catalog(work_ids: set[str]) -> None:
    scopes = load(ROOT / "data/scope-review.json")
    rows = scopes["works"]
    ids = [r["id"] for r in rows]
    if len(ids) != len(set(ids)) or set(ids) != work_ids:
        fail("scope catalog must classify every work exactly once")
    if dict(Counter(r["scope"] for r in rows)) != scopes["counts"]:
        fail("scope counts do not match classified works")
    for r in rows:
        if r["scope"] not in scopes["definitions"] or not r["reading_scope"]:
            fail(f"{r['id']}: undefined scope or missing reading boundary")
        validate_url(r["primary_source"], r["id"])
    expanded = load(ROOT / "data/expansion-reviews.json")["works"]
    expanded_ids = [r["id"] for r in expanded]
    if len(expanded_ids) != len(set(expanded_ids)) or not set(expanded_ids) <= work_ids:
        fail("expansion contains duplicate or unregistered work IDs")
    for r in expanded:
        if r["review_level"] not in {"abstract_screen", "selected_sections"}:
            fail(f"{r['id']}: unsupported review level")
        for field in ["reported_operation", "limit", "separating_intervention", "tasks_and_resources", "reading_scope"]:
            if not r[field].strip():
                fail(f"{r['id']}: missing {field}")
    pool = load(ROOT / "data/discovery-pool.json")["entries"]
    arxiv_ids = [r["arxiv_id"] for r in pool]
    if len(arxiv_ids) != len(set(arxiv_ids)):
        fail("discovery pool contains duplicate arXiv IDs")


def validate_curated_atlas(work_ids: set[str]) -> None:
    review = load(ROOT / "data/quality-review.json")
    decisions = review["decisions"]
    decision_ids = [r["id"] for r in decisions]
    if len(decision_ids) != len(set(decision_ids)) or set(decision_ids) != work_ids:
        fail("quality decisions must cover the complete catalog exactly once")
    states = {"core", "pending", "historical", "background", "low_value"}
    for row in decisions:
        if row["admission"] not in states or not row["reason"].strip():
            fail(f"{row['id']}: missing or invalid admission decision")
    core = {r["id"] for r in decisions if r["admission"] == "core"}
    cards = review["core_cards"]
    if len(cards) != len(core) or {r["id"] for r in cards} != core:
        fail("core cards and admission decisions disagree")
    families = {r["id"] for r in review["families"]}
    for card in cards:
        if card["family"] not in families:
            fail(f"{card['id']}: unknown mechanism family")
        for field in ["principle", "distinct_contribution", "evidence", "scale", "limit", "insight", "source_location"]:
            if not card[field].strip():
                fail(f"{card['id']}: incomplete claim review ({field})")
        validate_url(card["source_url"], card["id"])
    for relation in review["relations"]:
        if relation["source"] not in core or relation["target"] not in core:
            fail("non-admitted work leaked into the core relationship graph")
        if relation["type"].startswith("explicit"):
            validate_url(relation.get("source_url"), "explicit relation")
            if not relation.get("location"):
                fail("explicit relationship lacks a primary-source locator")
    layer = load(ROOT / "data/layer-review.json")
    layers = layer["works"]
    if len(layers) != len(work_ids) or {r["id"] for r in layers} != work_ids:
        fail("layer decisions must cover every work exactly once")
    route_ids = {r["id"] for r in layer["routes"]}
    if route_ids != {"harness", "model", "hybrid"}:
        fail("the primary atlas must have exactly three routes")
    main = {r["id"] for r in layers if r["placement"] == "main"}
    for r in layers:
        if r["placement"] not in layer["placement_labels"] or not r["why"].strip():
            fail(f"{r['id']}: missing placement decision")
        if r["route"] not in route_ids | {"unresolved", "crosscut"}:
            fail(f"{r['id']}: invalid route")
        if any(k not in layer["contribution_axes"] for k in r["focus"]) or len(r["focus"]) > 3:
            fail(f"{r['id']}: invalid contribution tags")
        if r["audit"] == "selected_sections":
            validate_url(r["source_url"], r["id"])
            if not r["source_location"] or not r["return_path"] or not r["changed"]:
                fail(f"{r['id']}: missing update/return-path locator")
        if r["placement"] == "main":
            if r["id"] not in core or r["route"] not in route_ids or r["audit"] != "selected_sections":
                fail(f"{r['id']}: unreviewed or invalid main-view work")
            if r["route"] in {"model", "hybrid"}:
                eligible = [m for m in r["models"] if max(m["total_b"] or 0, m.get("total_lower_bound_b",0)) >= layer["minimum_total_parameters_b"] and m["role"] == "实际训练对象"]
                if not eligible or r["scale_status"] != "eligible":
                    fail(f"{r['id']}: no verified >=27B trained target")
                for m in eligible:
                    if m.get("total_lower_bound_b") and not r.get("parameter_check"):
                        fail(f"{r['id']}: parameter lower bound needs a derivation")
            provenance = r.get("provenance", {})
            if provenance.get("sector") not in {"industry", "academic", "joint"} or not provenance.get("institutions"):
                fail(f"{r['id']}: main-view institutional provenance missing")
            validate_url(provenance.get("source_url"), r["id"])
        if r["scale_status"] == "below" and any(m["total_b"] is None or m["total_b"] >= layer["minimum_total_parameters_b"] for m in r["models"]):
            fail(f"{r['id']}: invalid below-threshold label")
    for slot in layer["spaces"]:
        if slot["route"] not in route_ids or not set(slot["evidence_ids"]) <= work_ids:
            fail("invalid research-space association")
    graph = load(GRAPH_PATH)
    if graph.get("schema_version") not in {"4.0.0", "5.0.0"}:
        if {r["work_id"] for r in graph["work_bindings"]} != main:
            fail("canonical graph must bind exactly the main-view works")
        if {r["id"] for r in graph["nodes"] if r["type"] == "work"} != main:
            fail("out-of-scope work leaked into main graph")
        if {r["id"] for r in graph["nodes"] if r["type"] == "concept"} != {"route-"+k for k in route_ids}:
            fail("main graph must use three route concepts")
    atlas = load(ROOT / "data/research-atlas.json")
    counts = dict(Counter(r["admission"] for r in decisions))
    counts.setdefault("low_value", 0)
    if atlas["counts"] != counts or {r["id"] for r in atlas["works"]} != work_ids:
        fail("generated atlas is stale or incomplete")
    if {r["id"] for r in atlas["works"] if r["main_view"]} != main:
        fail("atlas main-view membership is stale")
    if atlas["main_count"] != len(main) or atlas["reviewed_count"] != len(core):
        fail("atlas headline counts disagree")
    if atlas["placement_counts"] != dict(Counter(r["placement"] for r in layers)):
        fail("placement counts disagree")
    if atlas["route_counts"] != {k: sum(r["route"] == k and r["placement"] == "main" for r in layers) for k in route_ids}:
        fail("route counts disagree")
    expected_sectors = {k:dict(Counter(r['provenance']['sector'] for r in layers if r['placement']=='main' and r['route']==k)) for k in route_ids}
    if atlas.get("sector_counts") != expected_sectors:
        fail("mutually exclusive institutional counts disagree")
    brief = load(ROOT / "data/research-brief.json")
    if atlas.get("brief") != brief or set(brief['claim_labels']) != main:
        fail("brief or per-case evidence labels disagree")
    source_layers = {r["id"]:r for r in layers}
    if any(r["layer"] != source_layers[r["id"]] for r in atlas["works"]):
        fail("generated layer record differs from reviewed source")
    if graph.get("schema_version") not in {"4.0.0", "5.0.0"}:
        page = (ROOT / "research/atlas/index.html").read_text(encoding="utf-8")
        embedded = re.search(r'<script id="atlas-data" type="application/json">(.*?)</script>', page, re.S)
        if not embedded or json.loads(embedded.group(1)) != atlas:
            fail("offline atlas does not contain the current complete dataset")


def main() -> int:
    try:
        work_ids = validate_works(load(WORKS_PATH))
        validate_graph(load(GRAPH_PATH), work_ids)
        validate_hypotheses(load(HYPOTHESES_PATH))
        validate_scope_catalog(work_ids)
        validate_curated_atlas(work_ids)
    except (OSError, json.JSONDecodeError, ValueError, AssertionError) as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        return 1

    print(f"validation passed: {len(work_ids)} works")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
