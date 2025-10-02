---
type: plan
team: global
created: 2025-10-02T00:00:00Z
updated: 2025-10-02T00:00:00Z
tags: [planning, rollout, phase-03]
status: draft
---

# Phase 03 — Standard Migration (Renames + Link Updates)

Purpose: Execute the Standard migration to normalize session NOTE filenames and references, with safe, auditable steps.
Rules:
- Filename HHMM uses CREATED timestamp rounded down to 15 minutes (00, 15, 30, 45)
- Filenames are immutable after creation; only frontmatter `updated:` changes

## Outcomes

- All `SN_*` files follow `SN_YYYYMMDD-HHMM_slug-with-dashes.md`
- Internal links updated; no broken links
- Rename index created and committed

## Prerequisites

- Phase 01 merged
- Phase 02 docs and rules merged
- Rename candidates index present: `docs/indexes/renames-YYYY-MM-DD.md`

## Step-by-step Tasks

1. Finalize Rename Mapping (Owner: Human)

   - Review `docs/indexes/renames-YYYY-MM-DD.md` and confirm each mapping
   - Determine `HHMM` by rounding created time to nearest 15 minutes; if unknown, accept `0000`

2. Create Migration Branch (Owner: Agent)

   - `git checkout -b chore/phase-03-standard-migration`

3. Apply Renames (Owner: Agent)

   - For each mapping, execute `git mv` old → new path
   - Commit in batches (e.g., 10-20 files) with descriptive messages

4. Update Internal Links (Owner: Agent)

   - Search references in `docs/**`, `00-key-docs/**`, `.cursor/**`
   - Replace old paths with new; avoid over-matching
   - Commit link updates with clear messages

5. Link Integrity Check (Owner: Agent)

   - Run `python3 scripts/check_markdown_links.py`
   - Fix any reported issues; re-run until zero errors

6. Timestamp Validation (Owner: Agent)

   - Run `python3 scripts/validate_iso_timestamps.py docs`
   - Fix missing or malformed timestamps in frontmatter if reported

7. Migration Report (Owner: Agent)

   - Update rename index with any deviations encountered
   - Add `docs/indexes/migration-report-YYYY-MM-DD.md` summarizing scope, batches, and residuals

8. Open PR (Owner: Agent)
   - Title: `chore: Phase 03 Standard migration — session NOTE renames & link updates`
   - Include rename index and migration report in the PR body

## Checks (Background Agent Verification)

### Check 1: Batch Rename Verification

**Ask**: Verify each batch commit contains only expected `git mv` renames.
**Output**: `docs/agents/session-notes/SN_YYYYMMDD-HHMM_phase-03-batch-rename-check.md` with commit SHAs and file lists.

### Check 2: Link Integrity

**Ask**: Run link checker; report results.
**Output**: Append checker output summary to the check NOTE; list any fixed links.

### Check 3: Timestamp Validation

**Ask**: Run timestamp validator and record any fixes.
**Output**: Append validator results to the check NOTE.

## Success Criteria

- All targeted files renamed to the new standard
- Zero broken markdown links
- Migration report and updated rename index committed
