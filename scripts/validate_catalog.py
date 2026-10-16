#!/usr/bin/env python3
"""Validate the machine-readable BeforeRSI system catalog.

The validator uses only the Python standard library so it can run in a clean
checkout and in GitHub Actions without installing dependencies.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "systems.json"

REQUIRED_TOP = {"schema_version", "updated", "status_definitions", "systems"}
REQUIRED_SYSTEM = {
    "id",
    "name",
    "repo",
    "track",
    "claimed_changed_objects",
    "evidence_status",
    "before_rsi_audit",
    "central_question",
}
ALLOWED_STATUS = {"reported", "reproduced", "replicated", "contradicted", "open"}
ALLOWED_AUDIT = {"pending", "in_progress", "complete"}
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
OBJECT_RE = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")


def fail(message: str) -> None:
    raise ValueError(message)


def validate_repo_url(value: object, system_id: str) -> None:
    if not isinstance(value, str):
        fail(f"{system_id}: repo must be a string")
    parsed = urlparse(value)
    parts = [part for part in parsed.path.split("/") if part]
    if parsed.scheme != "https" or parsed.netloc != "github.com" or len(parts) != 2:
        fail(f"{system_id}: repo must be an https://github.com/OWNER/REPO URL")


def validate_system(item: object, index: int) -> tuple[str, str]:
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

    name = item["name"]
    if not isinstance(name, str) or not name.strip():
        fail(f"{system_id}: name must be a non-empty string")

    validate_repo_url(item["repo"], system_id)

    track = item["track"]
    if not isinstance(track, str) or not OBJECT_RE.fullmatch(track):
        fail(f"{system_id}: track must use lowercase snake_case")

    changed = item["claimed_changed_objects"]
    if not isinstance(changed, list) or not changed:
        fail(f"{system_id}: claimed_changed_objects must be a non-empty list")
    if len(changed) != len(set(changed)):
        fail(f"{system_id}: claimed_changed_objects contains duplicates")
    for obj in changed:
        if not isinstance(obj, str) or not OBJECT_RE.fullmatch(obj):
            fail(f"{system_id}: invalid changed object {obj!r}")

    if item["evidence_status"] not in ALLOWED_STATUS:
        fail(f"{system_id}: invalid evidence_status {item['evidence_status']!r}")
    if item["before_rsi_audit"] not in ALLOWED_AUDIT:
        fail(f"{system_id}: invalid before_rsi_audit {item['before_rsi_audit']!r}")

    question = item["central_question"]
    if not isinstance(question, str) or len(question.strip()) < 10:
        fail(f"{system_id}: central_question is too short")
    if not question.rstrip().endswith("?"):
        fail(f"{system_id}: central_question must end with '?' ")

    return system_id, item["repo"].rstrip("/").lower()


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

        if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", data["schema_version"]):
            fail("schema_version must use MAJOR.MINOR.PATCH")

        definitions = data["status_definitions"]
        if not isinstance(definitions, dict) or set(definitions) != ALLOWED_STATUS:
            fail("status_definitions must define exactly the five allowed statuses")

        systems = data["systems"]
        if not isinstance(systems, list) or not systems:
            fail("systems must be a non-empty list")

        ids: set[str] = set()
        repos: set[str] = set()
        for index, item in enumerate(systems):
            system_id, repo = validate_system(item, index)
            if system_id in ids:
                fail(f"duplicate system id: {system_id}")
            if repo in repos:
                fail(f"duplicate repository: {repo}")
            ids.add(system_id)
            repos.add(repo)

    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"catalog validation failed: {exc}", file=sys.stderr)
        return 1

    print(f"catalog valid: {len(systems)} systems")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
