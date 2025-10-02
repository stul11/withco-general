#!/usr/bin/env python3
"""Fail fast when legacy package managers are referenced in tracked files."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".cursor",
    "docs",
    "linear",
}
ALLOWLIST = {
    Path("requirements.txt"),
}
PATTERNS = [
    (
        re.compile(r"(?<!uv\\s)pip\\s+install", re.IGNORECASE),
        "Replace bare `pip install` with `uv pip install` or `uv sync`.",
    ),
    (
        re.compile(r"python\\s+-m\\s+pip\\s+install", re.IGNORECASE),
        "Use `uv pip` or `uv run` instead of `python -m pip`.",
    ),
    (
        re.compile(r"\\bpoetry\\b", re.IGNORECASE),
        "Swap Poetry commands for `uv` equivalents (e.g. `uv run`, `uvx`).",
    ),
]

def should_skip(path: Path) -> bool:
    return any(part in IGNORE_DIRS for part in path.parts)


def main() -> int:
    violations: list[str] = []
    for path in ROOT.rglob("*"):
        if path.is_dir() or should_skip(path):
            continue
        relative_path = path.relative_to(ROOT)
        if relative_path in ALLOWLIST:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern, guidance in PATTERNS:
            for match in pattern.finditer(text):
                line_number = text.count("\n", 0, match.start()) + 1
                snippet = text.splitlines()[line_number - 1].strip()
                violations.append(
                    f"{relative_path}:{line_number} → `{snippet}`. {guidance}"
                )
    if violations:
        print("Legacy package manager usage detected. Switch to `uv` workflows:\n")
        for violation in violations:
            print(f"- {violation}")
        print("\nDocs and templates should steer contributors toward `uv`.")
        return 1
    print("All checked files comply with the `uv`-first policy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
