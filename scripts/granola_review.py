"""Utilities for the paste-based Granola review workflow.

The helpers here normalize user-provided content, enforce write targets, and
split pasted content into the expected logical blocks (actions template plus an
optional summary block).
"""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import PurePosixPath
from typing import Iterable, Optional, Tuple

__all__ = [
    "SUMMARY_SPLIT_PATTERNS",
    "split_paste_blocks",
    "normalize_date",
    "normalize_priority",
    "generate_meeting_slug",
    "ensure_safe_output_path",
]

# Regexes that mark the beginning of the optional summary block. The patterns
# intentionally allow heading markers so both plain-text and Markdown summaries
# are detected.
SUMMARY_SPLIT_PATTERNS: Tuple[re.Pattern[str], ...] = (
    re.compile(r"^\s*(?:#+\s*)?auto[-\s]?generated summary\b", re.IGNORECASE | re.MULTILINE),
    re.compile(r"^\s*(?:#+\s*)?executive summary\b", re.IGNORECASE | re.MULTILINE),
    re.compile(r"^\s*(?:#+\s*)?summary[:\s]", re.IGNORECASE | re.MULTILINE),
)

# Allowed output targets defined by workflow safety rules.
_ALLOWED_DIRECTORIES = (
    PurePosixPath("docs/agents/session-notes"),
    PurePosixPath("linear/tickets/drafts"),
)
_ALLOWED_FILES = {
    PurePosixPath("docs/global/Decision_Docket.md"),
    PurePosixPath("docs/global/TODO_Log.md"),
}

# Date parsing helpers recognise a handful of common human formats.
_DATE_FORMATS = (
    "%Y-%m-%d",
    "%Y/%m/%d",
    "%m/%d/%Y",
    "%m-%d-%Y",
    "%d/%m/%Y",
    "%d-%m-%Y",
    "%b %d %Y",
    "%B %d %Y",
    "%d %b %Y",
    "%d %B %Y",
)
_ORDINAL_SUFFIX_RE = re.compile(r"(\d{1,2})(st|nd|rd|th)\b", flags=re.IGNORECASE)
_SLUG_TOKEN_RE = re.compile(r"[a-z0-9]+", flags=re.IGNORECASE)

_PRIORITY_ALIASES = {
    "critical": "P0",
    "blocker": "P0",
    "urgent": "P0",
    "highest": "P0",
    "high": "P1",
    "medium": "P2",
    "med": "P2",
    "normal": "P2",
    "standard": "P2",
    "low": "P3",
    "lowest": "P3",
    "minor": "P3",
    "none": "P3",
}


def split_paste_blocks(raw_text: str) -> Tuple[str, Optional[str]]:
    """Split pasted chat content into actions and optional summary blocks.

    Returns a tuple ``(actions_block, summary_block)`` where ``summary_block`` is
    ``None`` when the paste does not include a recognised summary section.
    Leading/trailing whitespace is trimmed from both blocks.
    """

    if raw_text is None:
        raise ValueError("raw_text must not be None")

    content = raw_text.strip()
    if not content:
        raise ValueError("raw_text must contain content")

    for pattern in SUMMARY_SPLIT_PATTERNS:
        match = pattern.search(content)
        if match:
            start = match.start()
            actions = content[:start].rstrip()
            summary = content[start:].lstrip()
            if not actions:
                # If the paste begins with a recognised summary heading, treat the
                # entire paste as actions-less summary to avoid returning an empty block.
                return content, None
            return actions, summary or None
    return content, None


def normalize_date(value: str) -> str:
    """Normalise assorted human-readable dates into YYYY-MM-DD."""

    if value is None:
        raise ValueError("value must not be None")

    text = value.strip()
    if not text:
        raise ValueError("value must contain a date")

    cleaned = _ORDINAL_SUFFIX_RE.sub(r"\\1", text)
    cleaned = cleaned.replace(",", "")
    iso_candidate = cleaned

    # Fast path for already-normalised dates.
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", iso_candidate):
        return iso_candidate

    # Handle full ISO timestamps with optional timezone or trailing Z.
    if iso_candidate.upper().endswith("Z"):
        iso_candidate = iso_candidate[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(iso_candidate)
        return dt.date().isoformat()
    except ValueError:
        pass

    for fmt in _DATE_FORMATS:
        try:
            dt = datetime.strptime(cleaned, fmt)
            return dt.date().isoformat()
        except ValueError:
            continue

    raise ValueError(f"Unrecognised date format: {value!r}")


def normalize_priority(value: str) -> str:
    """Coerce priority labels into the canonical P0–P3 scale."""

    if value is None:
        raise ValueError("value must not be None")

    text = value.strip()
    if not text:
        raise ValueError("value must contain a priority")

    canonical = text.upper()
    if re.fullmatch(r"P[0-3]", canonical):
        return canonical

    alias = _PRIORITY_ALIASES.get(text.lower())
    if alias:
        return alias

    raise ValueError(f"Unsupported priority: {value!r}")


def generate_meeting_slug(title: str, meeting_date: str) -> str:
    """Create the `<YYYY-MM-DD>-<kebab-title>` slug used for filenames."""

    if title is None:
        raise ValueError("title must not be None")

    date_iso = normalize_date(meeting_date)

    tokens = _SLUG_TOKEN_RE.findall(title.lower())
    slug_tail = "-".join(tokens)
    slug_tail = re.sub(r"-+", "-", slug_tail).strip("-")

    if not slug_tail:
        slug_tail = "meeting"

    # Trim runaway slugs while keeping them meaningful.
    if len(slug_tail) > 60:
        slug_tail = slug_tail[:60].rstrip("-")

    return f"{date_iso}-{slug_tail}"


def ensure_safe_output_path(path: str) -> PurePosixPath:
    """Validate that a proposed output path complies with safety rules."""

    if path is None:
        raise ValueError("path must not be None")

    candidate = PurePosixPath(path)
    if candidate.is_absolute() or candidate.root:
        raise ValueError(f"Absolute paths are not allowed: {path!r}")

    if not candidate.parts:
        raise ValueError("path must not be empty")

    if any(part == ".." for part in candidate.parts):
        raise ValueError(f"Parent directory references are not allowed: {path!r}")

    if candidate in _ALLOWED_FILES:
        return candidate

    for allowed_dir in _ALLOWED_DIRECTORIES:
        try:
            candidate.relative_to(allowed_dir)
        except ValueError:
            continue
        else:
            return candidate

    raise ValueError(f"Disallowed output target: {path!r}")


def ensure_safe_output_paths(paths: Iterable[str]) -> None:
    """Validate an iterable of paths, raising on the first invalid entry."""

    for path in paths:
        ensure_safe_output_path(path)

