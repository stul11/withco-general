---
type: plan
team: global
created: 2025-10-02T00:00:00Z
updated: 2025-10-02T00:00:00Z
tags: [planning, rollout, phase-02]
status: draft
---

# Phase 02 — Rules & Commands (Spec + Implementation)

Purpose: Define and implement minimal commands and rule updates to enforce naming, prompting, and TODO/TOPLAN flows, with checks suitable for background agents.

## Outcomes

- Command specs for `/toplan-add` and `/TODO-add` finalized
- NOTE creation flows prompt for names and apply correct prefixes/frontmatter
- Minimal rule updates to reinforce required sections and linking

## Prerequisites

- Phase 01 merged
- Main plan sections §3, §4, §5 reviewed

## Step-by-step Tasks

1. Finalize Command Specs (Owner: Human)

   - `/toplan-add` flags: `--title` `--priority [LOW|MED|HIGH]` `--labels` `--team` `--source path#anchor` `--tags` `--notes`
   - `/TODO-add` flags: same as above (targets TODO.md instead of TOPLAN.md)
   - Decision: allow multiple labels and tags (comma-separated)

2. Implement Command Docs (Owner: Agent)

   - `/.cursor/commands/toplan-add.md`: usage, examples, output format (multi-line schema)
   - `/.cursor/commands/TODO-add.md`: usage, examples, output format

3. Update Rules (Owner: Agent)

   - Ensure session NOTE creators prompt for naming and apply Full/Lite skeletons
   - Require `source:` when items are created via commands
   - Reference frontmatter minimal standard

4. Dry-run Validations (Owner: Agent)
   - Create sample items in `00-key-docs/TOPLAN.md` and `linear/PROD/TODO.md`
   - Verify labels, priorities, and `source:` formatted correctly

## Checks (Background Agent Verification)

### Check A: Command Docs Present

**Ask**: Verify `toplan-add.md` and `TODO-add.md` exist and include flags, examples, and schema.
**Output**: `docs/agents/session-notes/SN_YYYYMMDD-HHMM_phase02-command-docs-check.md`

### Check B: Sample Item Creation

**Ask**: Append one TOPLAN item and one TODO item using the specified schema; include `source:` links.
**Output**: `SN_YYYYMMDD-HHMM_phase02-sample-items.md` with file paths and snippets.

### Check C: Rule Reminders

**Ask**: Confirm rule files remind assistants to prompt for naming and required sections.
**Output**: `SN_YYYYMMDD-HHMM_phase02-rule-reminders.md` with citations.

## Success Criteria

- Commands documented with examples
- Sample items created correctly in global and team lists
- Rules reflect prompting and linking requirements
