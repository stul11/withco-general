#!/usr/bin/env python3
"""
convert_todo_format.py

Guarded converter: transforms checkbox TODO entries (`- [ ] ...`) into Option 3 CodeLens triggers
(`- TODO: ... <!-- id: TODO-YYYYMMDD-### -->`) inside actionable sections only.

Usage:
  python3 scripts/todos/convert_todo_format.py --path docs/global/TODO_Log.md --dry-run
  python3 scripts/todos/convert_todo_format.py --path docs/global/TODO_Log.md --write

Rules:
  - Convert only in sections with headings matching: In Progress, Pending (case-insensitive)
  - Skip Completed/Blocked sections
  - Preserve existing IDs; synthesize if missing using date prefix
  - Preserve following metadata lines (source/tags/notes)
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


SECTION_ACTIONABLE = re.compile(r"^##\s+(In\s+Progress|Pending)\s*$", re.IGNORECASE)
SECTION_SKIP = re.compile(r"^##\s+(Completed|Blocked)\s*$", re.IGNORECASE)
LINE_CHECKBOX = re.compile(r"^(-)\s*\[ \]\s+(.*)$")
ID_HTML = re.compile(r"<!--\s*id:\s*(?P<id>[^\s]+)\s*-->")


def synth_id(counter: int) -> str:
    date = dt.datetime.utcnow().strftime("%Y%m%d")
    return f"TODO-{date}-{counter:03d}"


def convert_lines(lines: list[str]) -> list[str]:
    out: list[str] = []
    in_actionable = False
    in_skipped = False
    id_counter = 1

    for i, line in enumerate(lines):
        if SECTION_ACTIONABLE.match(line):
            in_actionable = True
            in_skipped = False
            out.append(line)
            continue
        if SECTION_SKIP.match(line):
            in_actionable = False
            in_skipped = True
            out.append(line)
            continue

        m = LINE_CHECKBOX.match(line)
        if in_actionable and m:
            prefix, rest = m.groups()
            # Check for existing ID
            id_match = ID_HTML.search(rest)
            todo_id = id_match.group("id") if id_match else synth_id(id_counter)
            if not id_match:
                id_counter += 1
            # Ensure single space before HTML comment
            rest_no_id = ID_HTML.sub("", rest).rstrip()
            converted = f"{prefix} TODO: {rest_no_id} <!-- id: {todo_id} -->\n"
            out.append(converted)
            continue

        out.append(line)

    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", required=True, help="Path to Markdown TODO log")
    ap.add_argument("--dry-run", action="store_true", help="Show diff-like preview without writing")
    ap.add_argument("--write", action="store_true", help="Write changes back to file")
    args = ap.parse_args()

    path = Path(args.path)
    text = path.read_text(encoding="utf-8")
    original_lines = text.splitlines(keepends=True)
    converted_lines = convert_lines(original_lines)

    if args.dry_run or not args.write:
        # Minimal preview
        for before, after in zip(original_lines, converted_lines):
            if before != after:
                print("-", before.rstrip("\n"))
                print("+", after.rstrip("\n"))
        return

    path.write_text("".join(converted_lines), encoding="utf-8")


if __name__ == "__main__":
    main()


