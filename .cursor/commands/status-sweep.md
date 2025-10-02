# /status-sweep

Run repository quality checks and summarize readiness to stage or hand off work.

## Usage

```
/status-sweep [--dry-run] [--scope <path>] [--fast]
```

- `--dry-run`: Show the plan and commands without executing them.
- `--scope`: Restrict checks to a comma-separated list of directories or files.
- `--fast`: Skip optional lint extras (fallback to `pre-commit run --from-ref HEAD --to-ref HEAD` only).

## When to use

- Right before staging or requesting a review.
- Prior to `/offboard` or `/sync-help` to ensure the tree is clean.
- After large refactors to catch formatting or lint regressions early.

## Behavior

1. Confirm repository cleanliness and note untracked/unstaged files.
2. Run `pre-commit run --all-files` (or scoped variant when `--scope`/`--fast` set).
3. Execute link and timestamp validators:
   - `python3 scripts/check_markdown_links.py`
   - `python3 scripts/validate_iso_timestamps.py docs`
4. Detect TODO/TODO.codelens drift by invoking `scripts/todos/sync_codelens.py --check`.
5. Summarize failures with actionable next steps and affected paths.
6. Suggest `git add` commands for clean directories when checks pass.

## Output

- Table of executed checks with status (pass/fail/skipped).
- Consolidated error list with file paths and line hints.
- Suggested follow-up commands (e.g., rerun with `--fast`, open file locations).
- Optional `json` diagnostics (`checks`, `errors`, `git_status`).

## Safety

- Never stages or commits automatically.
- Aborts early if commands exit non-zero and surfaces stderr snippets instead of retrying blindly.

## Related

- `.cursor/rules/cursor-workflow-enhancements.mdc`
- `.cursor/commands/prep-session.md`
- `.cursor/commands/offboard.md`
- `.cursor/commands/README.md`
