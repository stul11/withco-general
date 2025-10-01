#!/usr/bin/env python3
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Matches ISO 8601 UTC like 2025-10-01T12:34:56Z
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")

FRONT_MATTER_KEYS = {"created", "updated"}

def check_front_matter(md_path: str) -> list[str]:
    errors: list[str] = []
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        return [f"{md_path}: failed to read: {e}"]

    if not lines or not lines[0].strip().startswith("---"):
        return []  # no front matter

    # gather front matter block
    fm: list[str] = []
    for line in lines[1:]:
        if line.strip().startswith("---"):
            break
        fm.append(line.rstrip("\n"))

    # scan for keys and validate
    for key in FRONT_MATTER_KEYS:
        for fm_line in fm:
            if fm_line.startswith(f"{key}:"):
                value = fm_line.split(":", 1)[1].strip()
                # strip quotes if present
                if value.startswith(('"', "'")) and value.endswith(('"', "'")):
                    value = value[1:-1]
                if not ISO_RE.match(value):
                    errors.append(f"{md_path}: {key} not ISO 8601 UTC (YYYY-MM-DDTHH:MM:SSZ): {value}")
                break
    return errors

def main() -> int:
    base = ROOT
    if len(sys.argv) > 1:
        base = os.path.abspath(sys.argv[1])
    failures: list[str] = []
    for dirpath, _, filenames in os.walk(base):
        if ".git" in dirpath:
            continue
        for name in filenames:
            if not name.lower().endswith(".md"):
                continue
            md_path = os.path.join(dirpath, name)
            failures.extend(check_front_matter(md_path))
    if failures:
        for msg in failures:
            print(msg)
        return 1
    print("All ISO timestamps valid (or not applicable)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())


