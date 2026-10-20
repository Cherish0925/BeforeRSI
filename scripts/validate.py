#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import json
import re
import sys
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


def validate_documentation() -> None:
    html = (ROOT / "docs/index.html").read_text(encoding="utf-8")
    def embedded(script_id):
        match = re.search(r'<script id="' + script_id + r'"[^>]*>(.*?)</script>', html, re.S)
        if not match:
            fail(f"missing embedded data: {script_id}")
        return json.loads(match[1])
    guide = embedded("model-learning-data")
    source = (ROOT / "docs/model-llm.md").read_bytes()
    if guide["source_sha256"] != hashlib.sha256(source).hexdigest():
        fail("guide changed: run scripts/build_learning.py")
    if base64.b64decode(guide["pdf"]) != (ROOT / "docs/Model_LLM_Learning_Manual.pdf").read_bytes():
        fail("standalone and embedded PDFs differ")
    if embedded("literature-data") != load(ROOT / "data/atlas.json"):
        fail("atlas data changed: run scripts/build_learning.py")


def main() -> int:
    try:
        work_ids = validate_works(load(WORKS_PATH))
        validate_graph(load(GRAPH_PATH), work_ids)
        validate_hypotheses(load(HYPOTHESES_PATH))
        validate_documentation()
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        return 1

    print(f"validation passed: {len(work_ids)} works")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
