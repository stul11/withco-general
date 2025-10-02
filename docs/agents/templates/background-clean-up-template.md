Goal: Audit the entire @withco-general/ workspace and produce an updated, prioritized section for @TODO_Log.md. Do NOT implement code changes.

Scope & rules:

- Only read the repo; do not commit code except for:
  - Edits to @TODO_Log.md
  - Creation/update of a session NOTE in docs/agents/session-notes/
  - Any other required artifacts or trackers specified in @offboard.md (e.g., Decision Docket updates)
- Load and follow all instructions in @offboard.md at the end, including validations, artifact creation, and PR preparation.
- Build a prioritized (easy/obvious first) action list focused on:
  (1) uncertainties/conflicts in docs,
  (2) duplicated/overlapping docs & folder structure,
  (3) finished TODOs that can be marked done,
  (4) stranded TODOs in files not reflected in @TODO_Log.md,
  (5) quick cleanups & dead files.
- Produce all required outputs:
  A) Append a new, ISO-8601 dated section to @TODO_Log.md (bulleted, high→low priority)
  B) Write a session NOTE with full findings, file paths, and reasoning in docs/agents/session-notes/
  C) Update any other global trackers or artifacts as required by @offboard.md (e.g., Decision Docket)
  D) Ensure all outputs have correct front matter and timestamps per repo standards

Operating checklist (read-only unless writing the allowed markdown outputs):

- Use ripgrep to inventory markers: TODO|FIXME|TBD|XXX|\?\?\? across all languages.
- Compare findings to current @TODO_Log.md and highlight deltas.
- Identify near-duplicate docs via headings overlap and summary diffs.
- Call out conflicts (e.g., “Use X” vs “Use Y”) with file paths and quotes.
- Propose simple, safe next steps only; label each with a 5–30 min estimate.
- When finished: follow all @offboard.md instructions, including:
  - Validating markdown links and ISO timestamps
  - Staging only the required markdown changes for review
  - Proposing a commit message per repo conventions
  - Preparing a PR with only the allowed changes and a summary of findings and next actions
