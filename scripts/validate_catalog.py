#!/usr/bin/env python3
"""Validate the machine-readable BeforeRSI public-system catalog."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "systems.json"

REQUIRED_TOP = {
    "schema_version", "updated", "status_definitions",
    "relation_definitions", "systems",
}
REQUIRED_SYSTEM = {
    "id", "name", "track", "relation_to_rsi", "claimed_changed_objects",
    "evidence_status", "before_rsi_audit", "central_question", "sources",
}
ALLOWED_STATUS = {"reported", "reproduced", "replicated", "contradicted", "open"}
ALLOWED_RELATION = {"direct_candidate", "precursor", "adjacent", "evaluation"}
ALLOWED_AUDIT = {"pending", "in_progress", "complete"}
ALLOWED_SOURCE_TYPES = {"repository", "paper", "project_page", "proceedings", "survey"}
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
OBJECT_RE = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")


def fail(message: str) -> None:
    raise ValueError(message)


def validate_url(value: object, system_id: str) -> None:
    if not isinstance(value, str):
        fail(f"{system_id}: source URL must be a string")
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc:
        fail(f"{system_id}: source URL must be HTTPS: {value!r}")


def validate_system(item: object, index: int) -> str:
    if not isinstance(item, dict):
        fail(f"systems[{index}] must be an object")

    keys = set(item)
    missing = REQUIRED_SYSTEM - keys
    extra = keys - REQUIRED_SYSTEM
    if missing:
        fail(f"systems[{index}] missing keys: {sorted(missing)}")
    if extra:
        fail(f"systems[{index}] has unknown keys: {sorted(extra)}")

    system_id = item["id"]
    if not isinstance(system_id, str) or not ID_RE.fullmatch(system_id):
        fail(f"systems[{index}].id is invalid: {system_id!r}")

    if not isinstance(item["name"], str) or not item["name"].strip():
        fail(f"{system_id}: name must be non-empty")

    if not isinstance(item["track"], str) or not OBJECT_RE.fullmatch(item["track"]):
        fail(f"{system_id}: track must use lowercase snake_case")

    if item["relation_to_rsi"] not in ALLOWED_RELATION:
        fail(f"{system_id}: invalid relation_to_rsi")

    changed = item["claimed_changed_objects"]
    if not isinstance(changed, list) or not changed or len(changed) != len(set(changed)):
        fail(f"{system_id}: claimed_changed_objects must be a unique non-empty list")
    for obj in changed:
        if not isinstance(obj, str) or not OBJECT_RE.fullmatch(obj):
            fail(f"{system_id}: invalid changed object {obj!r}")

    if item["evidence_status"] not in ALLOWED_STATUS:
        fail(f"{system_id}: invalid evidence_status")
    if item["before_rsi_audit"] not in ALLOWED_AUDIT:
        fail(f"{system_id}: invalid before_rsi_audit")

    q = item["central_question"]
    if not isinstance(q, str) or len(q.strip()) < 10 or not q.rstrip().endswith("?"):
        fail(f"{system_id}: central_question must be a substantive question")

    sources = item["sources"]
    if not isinstance(sources, list) or not sources:
        fail(f"{system_id}: sources must be a non-empty list")
    seen_urls = set()
    for src in sources:
        if not isinstance(src, dict) or set(src) != {"type", "url"}:
            fail(f"{system_id}: every source must contain exactly type and url")
        if src["type"] not in ALLOWED_SOURCE_TYPES:
            fail(f"{system_id}: invalid source type {src['type']!r}")
        validate_url(src["url"], system_id)
        if src["url"] in seen_urls:
            fail(f"{system_id}: duplicate source URL {src['url']}")
        seen_urls.add(src["url"])

    return system_id


def main() -> int:
    try:
        data = json.loads(CATALOG.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            fail("catalog root must be an object")

        keys = set(data)
        missing = REQUIRED_TOP - keys
        extra = keys - REQUIRED_TOP
        if missing:
            fail(f"catalog missing keys: {sorted(missing)}")
        if extra:
            fail(f"catalog has unknown keys: {sorted(extra)}")

        if not isinstance(data["schema_version"], str) or not re.fullmatch(
            r"[0-9]+\.[0-9]+\.[0-9]+", data["schema_version"]
        ):
            fail("schema_version must use MAJOR.MINOR.PATCH")

        if not isinstance(data["status_definitions"], dict) or set(data["status_definitions"]) != ALLOWED_STATUS:
            fail("status_definitions must define exactly the five allowed statuses")
        if not isinstance(data["relation_definitions"], dict) or set(data["relation_definitions"]) != ALLOWED_RELATION:
            fail("relation_definitions must define exactly the four relation classes")

        systems = data["systems"]
        if not isinstance(systems, list) or not systems:
            fail("systems must be a non-empty list")

        ids = set()
        for index, item in enumerate(systems):
            system_id = validate_system(item, index)
            if system_id in ids:
                fail(f"duplicate system id: {system_id}")
            ids.add(system_id)

    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"catalog validation failed: {exc}", file=sys.stderr)
        return 1

    counts = {}
    for item in systems:
        relation = item["relation_to_rsi"]
        counts[relation] = counts.get(relation, 0) + 1

    breakdown = ", ".join(f"{key}={counts[key]}" for key in sorted(counts))
    print(f"catalog valid: {len(systems)} systems ({breakdown})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
