#!/usr/bin/env python3
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

def is_relative_link(link: str) -> bool:
    return not (link.startswith("http://") or link.startswith("https://") or link.startswith("mailto:"))

def file_exists(path: str) -> bool:
    return os.path.exists(path)

def check_file(md_path: str) -> list[tuple[str, str]]:
    errors: list[tuple[str, str]] = []
    with open(md_path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            for m in LINK_RE.finditer(line):
                link = m.group(1).strip()
                if not is_relative_link(link):
                    continue
                # Ignore in-page anchors and references
                if link.startswith("#"):
                    continue
                link_path = link
                # allow code references like with spaces (URL-encoded handled elsewhere)
                abs_path = os.path.normpath(os.path.join(os.path.dirname(md_path), link_path))
                if not file_exists(abs_path):
                    errors.append((f"{md_path}:{lineno}", link))
    return errors

def main() -> int:
    target_dirs = [ROOT]
    if len(sys.argv) > 1:
        target_dirs = [os.path.abspath(sys.argv[1])]
    failures: list[tuple[str, str]] = []
    for base in target_dirs:
        for dirpath, _, filenames in os.walk(base):
            if ".git" in dirpath:
                continue
            for name in filenames:
                if not name.lower().endswith(".md"):
                    continue
                md_path = os.path.join(dirpath, name)
                failures.extend(check_file(md_path))
    if failures:
        for loc, link in failures:
            print(f"BROKEN LINK: {loc} -> {link}")
        return 1
    print("All markdown links OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())


