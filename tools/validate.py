#!/usr/bin/env python3
"""Validate every handbook entry against the framework.

Run from the repository root:

    python tools/validate.py

Exits non-zero if anything fails. CI runs this on every pull request.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install -r tools/requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
ENTRIES = ROOT / "entries"

WORD_CEILING = 250
STATUSES = ("stub", "draft", "reviewed", "ratified")
DIMENSIONS = ("property-type", "deal-type", "leverage", "period-type")
BODY_HEADINGS = ("Purpose", "Inputs", "Output", "Method", "Rules")
REQUIRED_KEYS = ("id", "name", "section", "status")

ID_RE = re.compile(r"^[123]\.\d+\.\d+$")
SECTION_RE = re.compile(r"^[123]\.\d+$")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.DOTALL)

problems: list[str] = []


def fail(path: Path, message: str) -> None:
    problems.append(f"{path.relative_to(ROOT).as_posix()}: {message}")


def slug(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[&/]", " ", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def body_word_count(body: str) -> int:
    """Words from the Purpose heading through the end of Rules."""
    lines = body.splitlines()
    start = end = None
    for i, line in enumerate(lines):
        m = re.match(r"^##\s+(.*?)\s*$", line)
        if not m:
            continue
        heading = m.group(1)
        if heading == "Purpose" and start is None:
            start = i
        elif start is not None and heading not in BODY_HEADINGS:
            end = i
            break
    if start is None:
        return 0
    return len(" ".join(lines[start:end]).split())


def body_headings(body: str) -> list[str]:
    found = re.findall(r"^##\s+(.*?)\s*$", body, re.MULTILINE)
    return [h for h in found if h in BODY_HEADINGS]


def load_entries() -> dict[str, dict]:
    entries: dict[str, dict] = {}
    for path in sorted(ENTRIES.rglob("*.md")):
        if path.name == "TEMPLATE.md" or path.name == "SECTION.md":
            continue
        text = path.read_text(encoding="utf-8")
        match = FRONTMATTER_RE.match(text)
        if not match:
            fail(path, "missing or malformed YAML frontmatter")
            continue
        try:
            meta = yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError as exc:
            fail(path, f"frontmatter is not valid YAML: {exc}")
            continue
        if not isinstance(meta, dict):
            fail(path, "frontmatter must be a mapping")
            continue

        missing = [k for k in REQUIRED_KEYS if k not in meta]
        if missing:
            fail(path, f"missing required key(s): {', '.join(missing)}")
            continue

        entry_id = str(meta["id"])
        if not ID_RE.match(entry_id):
            fail(path, f"id {entry_id!r} is not region.section.item")
            continue
        if entry_id in entries:
            other = entries[entry_id]["path"].relative_to(ROOT).as_posix()
            fail(path, f"duplicate id {entry_id} (also in {other})")
            continue

        entries[entry_id] = {"meta": meta, "body": match.group(2), "path": path}
    return entries


def check_entry(entry_id: str, record: dict, entries: dict[str, dict]) -> None:
    meta, body, path = record["meta"], record["body"], record["path"]

    section = str(meta["section"])
    if not SECTION_RE.match(section):
        fail(path, f"section {section!r} is not region.section")
    elif not entry_id.startswith(section + "."):
        fail(path, f"id {entry_id} does not sit in section {section}")

    expected_name = f"{entry_id}-{slug(str(meta['name']))}.md"
    if path.name != expected_name:
        fail(path, f"filename should be {expected_name}")

    status = str(meta.get("status", ""))
    if status not in STATUSES:
        fail(path, f"status {status!r} is not one of {', '.join(STATUSES)}")

    for dim in meta.get("varies_on") or []:
        if dim not in DIMENSIONS:
            fail(path, f"varies_on {dim!r} is not a known dimension")

    for key in ("draws_from", "feeds"):
        for ref in meta.get(key) or []:
            if str(ref) not in entries:
                fail(path, f"{key} references unknown entry {ref}")

    if status == "stub":
        return

    headings = body_headings(body)
    if headings != list(BODY_HEADINGS):
        fail(path, f"body headings are {headings or 'none'}, expected {list(BODY_HEADINGS)} in order")

    words = body_word_count(body)
    if words > WORD_CEILING:
        fail(path, f"body is {words} words, ceiling is {WORD_CEILING}")

    if status == "ratified":
        has_example = re.search(r"^##\s+Worked example\s*$", body, re.MULTILINE)
        if not (str(meta.get("evidence") or "").strip() or has_example):
            fail(path, "ratified entries need a citation in `evidence` or a Worked example section")


def check_graph(entries: dict[str, dict]) -> None:
    for entry_id, record in entries.items():
        meta, path = record["meta"], record["path"]
        for target in meta.get("feeds") or []:
            other = entries.get(str(target))
            if other and entry_id not in [str(x) for x in (other["meta"].get("draws_from") or [])]:
                fail(path, f"feeds {target}, but {target} does not draw from {entry_id}")
        for source in meta.get("draws_from") or []:
            other = entries.get(str(source))
            if other and entry_id not in [str(x) for x in (other["meta"].get("feeds") or [])]:
                fail(path, f"draws from {source}, but {source} does not feed {entry_id}")


def main() -> int:
    if not ENTRIES.is_dir():
        sys.exit(f"no entries directory at {ENTRIES}")

    entries = load_entries()
    for entry_id, record in entries.items():
        check_entry(entry_id, record, entries)
    check_graph(entries)

    if problems:
        print(f"{len(problems)} problem(s) found:\n")
        for p in problems:
            print(f"  {p}")
        return 1

    print(f"{len(entries)} entries validated, no problems found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
