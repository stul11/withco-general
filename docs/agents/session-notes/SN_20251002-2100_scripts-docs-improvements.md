---
id: SN_20251002_scripts-docs-improvements
title: Session Note - Scripts Docs Improvements
version: 1.0.0
created: 2025-10-02T21:00:00Z
updated: 2025-10-02T21:00:00Z
owner: slittle
status: In Progress
tags: [session-note, scripts, documentation]
---

# Session NOTE

- **Task ID**: scripts-docs-improvements
- **Agent**: gpt-5-codex
- **Owner**: slittle
- **Date**: 2025-10-02T21:00:00Z
- **Duration**: ~30 min

---

## Inputs & Context

- README.md
- scripts/README.md
- scripts/todos/sync_codelens.py
- scripts/granola_review.py
- requirements.txt
- docs/global/TODO_Log.md
- Background agent and safety rules in `.cursor/rules/`

---

## Plan

1. Review the current documentation and scripts to understand existing behaviours.
2. Draft suggested enhancements (flags, errors, messaging) for the scripts as unified diffs.
3. Capture a pre-commit hook snippet covering `markdownlint` and `sync_codelens`.
4. Outline a "How to" guide for non-technical collaborators in `scripts/README.md`.
5. Update the global TODO log with follow-up tasks and note any required sync actions.

---

## Findings & Notes

- Both `sync_codelens.py` and `granola_review.py` assume CLI usage without argument validation messaging.
- The scripts README currently focuses on developer setup and lacks plain-language onboarding steps.
- Markdown linting is already a repo expectation, but no automated pre-commit snippet exists for contributors.

---

## Proposed Changes (Diffs Only)

### scripts/README.md

```diff
@@
 ## Usage
 
 ### TODO CodeLens Sync
@@
   python scripts/todos/sync_codelens.py --help
 ```
 
+### How to run scripts without a development background
+
+1. Install the prerequisites listed above. If you get stuck, ask an engineer to run `python -m venv .venv` and
+   `pip install -r requirements.txt` for you.
+2. Open your terminal (macOS: Spotlight search for "Terminal"; Windows: open "Command Prompt").
+3. Change directories into the project folder, for example: `cd ~/dev/withco-general`.
+4. Copy the exact command from the script section you need. Paste it into the terminal and press **Enter**.
+5. Watch the terminal output. If you see `ERROR:` messages, capture the entire output and share it in Slack so an engineer
+   can help troubleshoot.
+6. When the script finishes successfully, note any generated files or TODO updates and log the outcome in the relevant
+   session note or Linear draft.
+
 ### Granola Review Helper
@@
-  python scripts/granola_review.py --input data/granola-input.csv --output data/granola-output.csv
+  python scripts/granola_review.py --input data/granola-input.csv --output data/granola-output.csv
+  
+Error handling:
+
+- The script now exits with code `2` and prints a clear message if either `--input` or `--output` is missing.
+- It also surfaces a warning if the output file already exists, prompting for `--force`.
```

### scripts/todos/sync_codelens.py

```diff
@@
-def main() -> None:
-    parser = build_parser()
-    args = parser.parse_args()
-    setup_logging(args.verbose)
-    try:
-        sync_todos(Path(args.todo_file), Path(args.output), dry_run=args.dry_run)
-    except SyncError as exc:
-        logging.error("Sync failed: %s", exc)
-        raise SystemExit(1) from exc
+def main() -> None:
+    parser = build_parser()
+    if len(sys.argv) == 1:
+        parser.print_help()
+        raise SystemExit(2)
+
+    args = parser.parse_args()
+    setup_logging(args.verbose)
+    try:
+        sync_todos(Path(args.todo_file), Path(args.output), dry_run=args.dry_run)
+    except FileNotFoundError as exc:
+        logging.error("Input file not found: %s", exc)
+        raise SystemExit(2) from exc
+    except SyncError as exc:
+        logging.error("Sync failed: %s", exc)
+        raise SystemExit(1) from exc
```

### scripts/granola_review.py

```diff
@@
-def parse_args() -> argparse.Namespace:
-    parser = argparse.ArgumentParser(description="Review granola data files")
-    parser.add_argument("--input", required=True, help="Path to the CSV input file")
-    parser.add_argument("--output", required=True, help="Path to save the processed CSV")
-    parser.add_argument("--force", action="store_true", help="Overwrite output if it exists")
-    return parser.parse_args()
+def build_parser() -> argparse.ArgumentParser:
+    parser = argparse.ArgumentParser(description="Review granola data files")
+    parser.add_argument("--input", required=True, help="Path to the CSV input file")
+    parser.add_argument("--output", required=True, help="Path to save the processed CSV")
+    parser.add_argument("--force", action="store_true", help="Overwrite output if it exists")
+    return parser
+
+
+def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
+    parser = build_parser()
+    args = parser.parse_args(argv)
+    output_path = Path(args.output)
+    if output_path.exists() and not args.force:
+        raise SystemExit("ERROR: output file exists. Use --force to overwrite.")
+    return args
```

### requirements.txt

```diff
@@
 markdownlint-cli==0.42.0
+pre-commit==3.8.0
```

---

## Pre-commit Hook Draft

```yaml
repos:
  - repo: https://github.com/igorshubovych/markdownlint-cli
    rev: v0.42.0
    hooks:
      - id: markdownlint
        additional_dependencies: ["markdownlint-cli@0.42.0"]
        files: "\\.(md|mdx)$"
  - repo: local
    hooks:
      - id: sync-codelens
        name: Sync TODO CodeLens
        entry: python scripts/todos/sync_codelens.py --todo-file docs/global/TODO.codelens.todo --output docs/global/TODO_Log.md
        language: system
        pass_filenames: false
```

---

## TODO Updates

- [ ] Schedule implementation of script enhancements and README updates (`Owner: slittle`, `Due: 2025-10-10`).
- [ ] Evaluate adding `pre-commit` dependency and hook integration (`Owner: slittle`, `Due: 2025-10-12`).
- [ ] Confirm CodeLens sync after updates; consider running `python scripts/todos/sync_codelens.py --dry-run` post-implementation.

---

## Changelog

- Drafted documentation diffs for script usability improvements.
- Captured pre-commit hook configuration covering markdown lint and TODO synchronization.
- Logged follow-up TODOs for adoption and verification.

---

## Approvals & Safety Checks

- No repository modifications made outside the allowed directories.
- TODO sync not executed; follow-up note included above.

