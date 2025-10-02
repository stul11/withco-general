#!/usr/bin/env python3
"""
Compute HHMM from an ISO 8601 timestamp rounded down to the nearest 15 minutes.

Usage:
  python3 scripts/hhmm_round.py 2025-10-02T10:52:00Z
  -> 1050

If no argument provided, uses current UTC time.
"""

import sys
from datetime import datetime, timezone


def round_down_15(dt: datetime) -> str:
    minutes = (dt.minute // 15) * 15
    return f"{dt.hour:02d}{minutes:02d}"


def parse_iso8601(s: str) -> datetime:
    try:
        if s.endswith("Z"):
            s = s[:-1] + "+00:00"
        return datetime.fromisoformat(s).astimezone(timezone.utc)
    except Exception as e:
        raise SystemExit(f"Invalid ISO8601 time: {s}\n{e}")


def main():
    if len(sys.argv) > 1:
        dt = parse_iso8601(sys.argv[1])
    else:
        dt = datetime.now(timezone.utc)
    print(round_down_15(dt))


if __name__ == "__main__":
    main()


