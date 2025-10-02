<!-- markdownlint-disable MD003 MD022 -->
<!-- markdownlint-disable MD041 -->
<!-- markdownlint-disable MD025 -->
<!-- markdownlint-disable MD041 -->

# Background Clean-up Template

Goal:

- [ ] Audit the entire @withco-general/ workspace
- [ ] Produce an updated, prioritized section for @TODO_Log.md
- [ ] Do NOT implement code changes

Scope & rules:

- Only read the repo; do not commit code except for:
  - Edits to @TODO_Log.md
  - Creation/update of a session NOTE in docs/agents/session-notes/
  - Any other required artifacts or trackers specified in @offboard.md (e.g., Decision Docket updates)
- Load and follow all instructions in @offboard.md at the end, including validations, artifact creation, and PR preparation.
- Build a prioritized (easy/obvious first) action list focused on:
  - [ ] Uncertainties/conflicts in docs
  - [ ] Duplicated/overlapping docs & folder structure
  - [ ] Finished TODOs that can be marked done
  - [ ] Stranded TODOs in files not reflected in @TODO_Log.md
  - [ ] Quick cleanups & dead files
- Produce all required outputs:
  - [ ] Append a new, ISO-8601 dated section to @TODO_Log.md (bulleted, high→low priority)
  - [ ] Write a session NOTE with full findings, file paths, and reasoning in docs/agents/session-notes/
  - [ ] Update any other global trackers or artifacts as required by @offboard.md (e.g., Decision Docket)
  - [ ] Ensure all outputs have correct front matter and timestamps per repo standards

Operating checklist (read-only unless writing the allowed markdown outputs):

- [ ] Use ripgrep to inventory markers: TODO|FIXME|TBD|XXX|\?\?\? across all languages
- [ ] Compare findings to current @TODO_Log.md and highlight deltas
- [ ] Identify near-duplicate docs via headings overlap and summary diffs
- [ ] Call out conflicts (e.g., “Use X” vs “Use Y”) with file paths and quotes
- [ ] Propose simple, safe next steps only; label each with a 5–30 min estimate
- [ ] When finished: follow all @offboard.md instructions, including:
  - [ ] Validate markdown links and ISO timestamps
  - [ ] Stage only the required markdown changes for review
  - [ ] Propose a commit message per repo conventions
  - [ ] Prepare a PR with only the allowed changes and a summary of findings and next actions
