#!/usr/bin/env python3
"""
Generate and validate CodeLens sidecar files from Markdown TODO logs.

Inputs: One or more Markdown files (global or team TODO logs).
Outputs: For each input `<path>/TODO_Log.md` or `TODO.md`, emit a sibling sidecar:
  - `<path>/TODO.codelens.todo`

Rules:
  - Parse actionable checklist lines beginning with "- [ ]" or "- [x]"
  - Extract a stable id from trailing HTML comment: <!-- id: <identifier> -->
  - If id missing, synthesize deterministic ids based on file stem and running counter
  - Sidecar lines use comment-style tokens that editors recognize as TODO/FIXME
  - Completed items mapped to FIXME? Keep as TODO with [x] marker for simplicity

Example sidecar line:
  # TODO [In Progress] id=todo-20251002-003 text=Align /offboard required sections — docs/...

Validation:
  - Fail with non-zero exit if duplicate ids detected within a file
  - Optionally verify that every sidecar line can be traced back to a Markdown item
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Tuple


CHECKBOX_RE = re.compile(r"^\s*- \[(?P<state>[ xX])\] (?P<text>.*?)(?:\s*<!--\s*id:\s*(?P<id>[^\s>]+)\s*-->)?\s*$")


@dataclass
class TodoItem:
    state: str  # "x" or " "
    text: str
    identifier: str


def read_markdown_todos(markdown_path: Path) -> List[TodoItem]:
    items: List[TodoItem] = []
    seen_ids: set[str] = set()
    synthesized_counter = 1
    file_tag = markdown_path.stem.replace("_", "-")
    for line in markdown_path.read_text(encoding="utf-8").splitlines():
        m = CHECKBOX_RE.match(line)
        if not m:
            continue
        state = m.group("state").lower()
        text = m.group("text").strip()
        identifier = (m.group("id") or f"{file_tag}-{synthesized_counter:03d}").strip()
        if identifier in seen_ids:
            raise SystemExit(f"Duplicate id '{identifier}' in {markdown_path}")
        seen_ids.add(identifier)
        if not m.group("id"):
            synthesized_counter += 1
        items.append(TodoItem(state=state, text=text, identifier=identifier))
    return items


def sidecar_lines(items: Iterable[TodoItem]) -> List[str]:
    lines: List[str] = []
    for item in items:
        status = "Done" if item.state == "x" else "Open"
        # Use hash-comment to be universally recognized in many modes; token TODO is key for CodeLens
        line = f"# TODO [{status}] id={item.identifier} {item.text}"
        lines.append(line)
    return lines


def target_sidecar_path(md_path: Path) -> Path:
    parent = md_path.parent
    return parent / "TODO.codelens.todo"


def process_file(md_path: Path, write: bool = True, check_only: bool = False) -> Tuple[Path, int]:
    items = read_markdown_todos(md_path)
    sc_path = target_sidecar_path(md_path)
    lines = sidecar_lines(items)
    content = "\n".join(lines) + ("\n" if lines else "")
    if check_only:
        # Compare existing content
        if sc_path.exists():
            existing = sc_path.read_text(encoding="utf-8")
            if existing != content:
                raise SystemExit(f"Drift detected for {md_path}: sidecar out of sync at {sc_path}")
        else:
            raise SystemExit(f"Missing sidecar for {md_path}: expected {sc_path}")
    elif write:
        sc_path.write_text(content, encoding="utf-8")
    return sc_path, len(lines)


def discover_default_targets() -> List[Path]:
    candidates: List[Path] = []
    # Global
    for name in ("TODO_Log.md", "TODO.md"):
        p = Path("docs/global") / name
        if p.exists():
            candidates.append(p)
    # Teams
    for p in Path("linear").glob("**/TODO.md"):
        candidates.append(p)
    return candidates


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync CodeLens sidecars for TODO logs")
    parser.add_argument("paths", nargs="*", help="Markdown TODO paths; defaults to global and team logs")
    parser.add_argument("--check", action="store_true", help="Only check for drift; exit non-zero on mismatch")
    args = parser.parse_args()

    md_paths = [Path(p) for p in args.paths] if args.paths else discover_default_targets()
    if not md_paths:
        raise SystemExit("No TODO logs found to process")

    total = 0
    for md in md_paths:
        sc_path, count = process_file(md, write=not args.check, check_only=args.check)
        print(f"Synced {count} items -> {sc_path}")
        total += count
    print(f"Done. {total} TODO items processed across {len(md_paths)} file(s).")


if __name__ == "__main__":
    main()

