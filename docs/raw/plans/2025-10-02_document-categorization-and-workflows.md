---
type: plan
team: global
created: 2025-10-02T00:00:00Z
updated: 2025-10-02T00:00:00Z
tags: [planning, taxonomy, naming, todos]
status: draft
source: docs/agents/session-notes/SN_20251002-0630_session-note-template-analysis.md
---

## Plan: Document Categorization and Workflow System

### Executive Summary

Establish a clear, consistent document taxonomy, naming scheme, and lightweight workflows for session notes, meetings/granola, research, raw capture, and planning artifacts. Define TODO/TOPLAN schemas with required linking, add human-in-the-loop prompts for naming, and provide a safe migration plan (Standard and Gold). This document is a proposal only—no changes will be implemented until approved.

### Decisions Confirmed (from discussion)

- Naming prefix for session notes: `SN_` (uppercase)
- Timestamp separator: `YYYYMMDD-HHMM` (e.g., `20251002-0930`)
- Slugs: kebab-case (lowercase, `-`), with `_` used only after the prefix
- Apply same pattern to `MN_` (meeting), `RN_` (raw), and `GR_` (granola kept distinct)
- All creation flows prompt for final name/slug confirmation
- TODO/TOPLAN item format: Alternative B (multi-line)
- Labels available: `(POTENTIAL) (AGENT) (RESEARCH) (DECISION) (BLOCKED)`
- Linking back to source is required for automated/template workflows
- Granola lives under `docs/` (not team-scoped by default) as paired prompt+response
- Raw capture uses `RN_YYYYMMDD-HHMM_slug.md`; two-step raw→organized flow; team-scoped if known, else global
- Separate business lists (by team) under `linear/` alongside global `00-key-docs`

---

## 1) Naming Conventions

### 1.1 Filenames

- Session notes (agents): `SN_YYYYMMDD-HHMM_slug-with-dashes.md` (HHMM = CREATED rounded down to 15 min; immutable)
- Meeting notes: `MN_YYYYMMDD-HHMM_slug-with-dashes.md`
- Granola notes: `GR_YYYYMMDD-HHMM_slug-with-dashes.md`
- Raw capture: `RN_YYYYMMDD-HHMM_slug-with-dashes.md`

Examples:

```text
docs/agents/session-notes/SN_20251002-0930_session-NOTE-template-analysis.md
docs/meeting-notes/MN_20251002-1100_customer-interview-acme.md
docs/granola/GR_20251002-1015_pricing-page-rewrite-research.md
docs/raw/RN_20251002-0845_prompt-ideas-for-markdownlint.md
```

Rationale:

- The hyphen between date and time (`YYYYMMDD-HHMM`) preserves lexicographic sort while improving readability.
- Use kebab-case slugs for cross-platform friendliness and conventional readability.

### 1.2 Tags vs Types

- Frontmatter includes a `type` and optional `tags` list.
- For granola: keep `GR_` prefix and include `tags: [granola]` for filtering.

---

## 2) Directory Taxonomy (Option A, refined)

Maintain a clear separation between business/team planning under `linear/` and shared knowledge/agent outputs under `docs/`.

### 2.1 Global operational docs

```text
00-key-docs/
  TODO.md              # global operational TODOs (rename from TODO_Log.md at migration)
  TOPLAN.md            # global operational planning backlog (new)
```

### 2.2 Business/team-scoped planning (when team known)

```text
linear/
  PROD/
    TODO.md
    TOPLAN.md
    docs/
    raw/
    tickets/
      draft/
    projects/
      draft/
    plans/
      draft/
  ANA/
    TODO.md
    TOPLAN.md
    docs/
    raw/
    tickets/
      draft/
    projects/
      draft/
    plans/
      draft/
  DATA/
    TODO.md
    TOPLAN.md
    docs/
    raw/
    tickets/
      draft/
    projects/
      draft/
    plans/
      draft/
  LEG/
    TODO.md
    TOPLAN.md
    docs/
    raw/
    tickets/
      draft/
    projects/
      draft/
    plans/
      draft/
  AM/
    TODO.md
    TOPLAN.md
    docs/
    raw/
    tickets/
      draft/
    projects/
      draft/
    plans/
      draft/
  global/
    TODO.md
    TOPLAN.md
    docs/
    raw/
    tickets/
      draft/
    projects/
      draft/
    plans/
      draft/
```

Notes:

- Place business-context planning and raw capture by team here; mirror later into Linear manually as needed.
- Additional teams (e.g., `OPS`, `ENG`) can be added incrementally.

### 2.3 Knowledge, research, and agent outputs

```text
docs/
  agents/
    session-notes/      # all SN_ files (agents)
  granola/              # GR_ files, paired prompt+response
    outputs/            # optional finalized outputs copied from paired files
  research/             # (optional) RS_ files if distinct from granola
  meeting-notes/        # (optional) MN_ if preferred outside granola
  raw/                  # RN_ default when team not known
  plans/                # this planning area (YYYY-MM-DD_topic.md)
```

NOTE (2025-10-02): Option D (Guidance + Templates split) adopted.

- Canonical guidance: `docs/company/linear/How_to_use_Linear.md`
- Canonical template: `docs/templates/linear/ticket-template.md`
- `linear/` remains for drafts and archives; legacy files carry MOVED/DEPRECATED notices.

---

## 3) TODO and TOPLAN Schema

### 3.1 Item format (Alternative B: multi-line)

```text
- [ ] (LABELS) [PRIORITY] Title
  source: <relative-path>#<anchor>
  tags: <comma-or-list>
  notes: <optional 1-2 lines>
```

Where:

- `(LABELS)`: any of `(POTENTIAL) (AGENT) (RESEARCH) (DECISION) (BLOCKED)` (multiple allowed)
- `[PRIORITY]`: one of `[LOW] [MED] [HIGH]`
- `source:`: required for automated/template workflows; should point to the originating NOTE/section
- `tags:`: optional, free-form; use for topical filters (`granola, session-notes, pricing`)
- `notes:`: optional, keeps the first line clean and terse

Examples (global vs team):

```text
# 00-key-docs/TODO.md
- [ ] (AGENT) [MED] Align `/offboard` required sections across commands
  source: docs/agents/session-notes/SN_20251002-0630_session-NOTE-template-analysis.md#immediate-actions
  tags: session-notes, templates

# linear/PROD/TOPLAN.md
- [ ] (POTENTIAL) (DECISION) [HIGH] Evaluate pricing granola study scope
  source: docs/granola/GR_20251002-1015_pricing-page-rewrite-research.md#recommendations
  tags: granola, pricing
  notes: Prepare 2 scenario options before exec review
```

### 3.2 Lists and placement

- Global operational lists: `00-key-docs/TODO.md`, `00-key-docs/TOPLAN.md`
- Team business lists: `linear/{TEAM}/TODO.md`, `linear/{TEAM}/TOPLAN.md`
- All creation commands prompt for: target (global/team), labels, priority, and source path

---

## 4) Minimal Frontmatter Standard

Apply a minimal, consistent header across new docs (including linear business docs where applicable):

```yaml
---
type: session-NOTE | meeting-NOTE | granola | research | raw | plan | TODO
team: PROD | ANA | DATA | LEG | global
created: 2025-10-02T09:30:00Z
updated: 2025-10-02T09:30:00Z # update on edits; filename remains based on created
source: docs/agents/session-notes/SN_20251002-0930_slug.md#context
tags: [session-notes, template]
---
```

Notes:

- Keep fields minimal; expand only where they add value.
- Ensure `created/updated` use ISO 8601; update `updated` when substantial edits occur.

---

## 5) Commands and Prompts (spec, non-executable)

All creation flows prompt you to confirm/edit: `prefix`, `YYYYMMDD-HHMM`, and `slug`. Agents may propose a default, but human confirms.

### 5.1 `/capture-raw`

- Behavior: Create a raw capture NOTE at `RN_YYYYMMDD-HHMM_slug.md` in `linear/{TEAM}/raw/` if team known, else `docs/raw/`
- Required prompt inputs: `team?`, `slug`, `context` (short)
- Output includes frontmatter with `type: raw`, `team`, and timestamps

### 5.2 `/organize-raw`

- Flags: `--source <path>` `--as [session|meeting|granola|research]` `--team <TEAM|global>`
- Behavior: Scaffold target file (SN*/MN*/GR*/RS*) with back-links to raw source; carry over key context

### 5.3 `/toplan-add`

- Flags: `--title` `--priority [LOW|MED|HIGH]` `--labels` `--team <TEAM|global>` `--source <path#anchor>` `--tags` `--notes`
- Behavior: Append a multi-line item (schema §3.1) to the chosen TOPLAN list; prompt for name confirmation

### 5.4 `/TODO-add` (deferred)

- Same interface as `/toplan-add`; targets TODO lists instead. Specification to be finalized later.

### 5.5 Session/meeting/granola NOTE creators

- Ensure each creator prompts for final name; emits correct prefix per §1.1; inserts frontmatter per §4.

---

## 6) Granola and Research

- Location: `docs/granola/` (not team-scoped by default)
- File: `GR_YYYYMMDD-HHMM_slug.md` with paired sections:
  - Prompt/initial context
  - Response(s)/analysis
  - Recommendations (optional)
- Finalization: when a single clean output is preferred, copy finalized content to `docs/granola/outputs/` as a standalone file, adding `source:` back-reference to the paired file.
- Research that is not granola can use `docs/research/RS_YYYYMMDD-HHMM_slug.md` (optional category) with `type: research`.

---

## 7) Raw → Organized Workflow

1. Capture: `/capture-raw` creates `RN_YYYYMMDD-HHMM_slug.md` under team `raw/` when known; else under `docs/raw/`.
2. Organize: `/organize-raw` scaffolds target (SN/MN/GR/RS) and back-links to raw; moves or references content as appropriate.
3. Propagate TODOs/TOPLAN:
   - [ ] Prompt creators to add related items with labels/priorities
   - [ ] Include a `source:` link to the originating section

---

## 8) Linear Mirroring (Team Structure)

- Mirror company structure under `linear/{PROD,ANA,DATA,LEG,global}/` for business-scoped planning and raw capture.
- Keep agent/knowledge artifacts in `docs/` and link when moving context into Linear.
- Avoid automated writes to company Linear projects; keep manual mirroring consistent with safety rules.

---

## 9) Session NOTE Sections (Full vs Lite)

To standardize completeness while keeping authoring lightweight:

- Full (for substantial sessions): Inputs & Context; Full Findings; Steps Taken; Outputs; Citations; Risks & Issues Identified; Reasoning & Rationale; Next Actions; Signoff
- Lite (for short sessions): Inputs & Context; Steps Taken; Outputs; Next Actions; Signoff

Commands can prompt for Full vs Lite and insert the correct skeleton.

---

## 10) Migration Plan (Standard and Gold)

### 10.1 Standard (recommended)

Scope:

- Rename legacy `SN_*` files to `SN_YYYYMMDD-HHMM_*`.
- Update in-repo references pointing to renamed files (within `docs/` and `00-key-docs/`).
- Rename `00-key-docs/TODO_Log.md` → `00-key-docs/TODO.md` and update references.

Steps:

1. Inventory current files (dry run; no changes): list of `SN_*`, `MN_*?`, `GR_*?`, `RN_*?`
2. Compute new names based on extraction of date/time from filename or frontmatter/content
3. `git mv` each file to the new name (batched by directory)
4. Update Markdown links referencing moved files (search/replace with review)
5. Verify links via a local Markdown link check
6. Commit with descriptive messages (by batch)

Pros/Cons:

- Pros: Repository feels consistent quickly; modest effort
- Cons: Requires careful link updates; temporary churn in history

### 10.2 Gold (optional, on top of Standard)

Add:

- `docs/indexes/renames-YYYYMMDD.md` mapping `old_name → new_name`
- Add/update `updated:` in frontmatter of each renamed file
- Optional: lightweight stubs (or symlinks if desired) for historically referenced paths, with a NOTE pointing to the new location

Pros/Cons:

- Pros: Strong auditability and discoverability; smoother consumer transition
- Cons: Slight additional maintenance overhead

### 10.3 Backward Compatibility

- Keep content unchanged aside from filename and frontmatter adjustments
- Defer renaming for non-session artifacts unless beneficial; schedule separate passes if needed

### 10.4 Gold+ Upgrade Path (post-Standard)

Objective: Provide a clear route from Standard to a fully reorganized, relinked, and documented state.

Steps:

1. Create rename index: `docs/indexes/renames-<date>.md` mapping `old_name → new_name` with rationale
2. Insert/update frontmatter `updated:` across all renamed files; add `source:` back-references when moved
3. Run a repository-wide link update pass with a tracked script (idempotent), commit per directory
4. Add stubs/symlinks for high-traffic legacy paths with a short NOTE pointing to the new location
5. Generate a migration report in `docs/indexes/` summarizing changes and residual issues
6. Run link integrity checks and fix any remaining broken links
7. Announce completion in a Session NOTE and update Decision Docket

Success Criteria:

- All target categories follow new naming and placement
- No broken internal links (verified by link check)
- Rename index and migration report exist and are linked from the main plan

---

## 11) Concept of Plans (General)

Purpose: Dedicated space for structured planning, options, and recommendations without implementing changes.

Location and naming:

```text
docs/raw/plans/YYYY-MM-DD_topic-name.md
```

Template (lite):

```markdown
---
type: plan
team: global | PROD | ANA | DATA | LEG
created: <ISO8601>
updated: <ISO8601>
tags: [planning]
status: draft | in-review | approved | archived
---

## Plan: <Title>

### Executive Summary

### Options (easy/standard/gold)

### Recommendation

### Rollout Plan

### Risks & Open Decisions
```

Lifecycle:

- Draft in `docs/raw/plans/`; iterate via PRs/commits
- When approved, implement in follow-up sessions; keep plan as record
- Optionally maintain an index at `docs/raw/plans/PLANS_INDEX.md`

---

## 12) Risks & Open Decisions

- Confirm whether `docs/meeting-notes/` is desired, or fold meetings into granola context
- Decide whether to introduce `RS_` category now or later (research distinct from granola)
- Confirm per-team expansions beyond `{PROD,ANA,DATA,LEG,global}`
- Finalize `/TODO-add` behavior and flags

---

## 13) Phased Rollout (post-approval only)

1. Approvals

   - Confirm naming, taxonomy, schemas, and migration mode (Standard vs Gold)

2. Scaffolding

   - Create missing top-level directories and placeholder README files
   - Add plan/lite templates if helpful

3. Rules & Commands (spec updates only; implementations follow)

   - Ensure NOTE creators prompt for names and insert correct skeletons
   - Add `/toplan-add`; defer `/TODO-add` final spec

4. Migration

   - Execute Standard (or Gold) steps
   - Run link checks; fix any broken references

5. Adoption
   - Begin using new naming in all new files
   - Monitor friction; adjust templates and prompts as needed

Links to rollout sub-plans:

- Index: `docs/raw/plans/rollout/INDEX.md`
- Phase 01 — Approvals & Scaffolding: `docs/raw/plans/rollout/phase-01_approvals-and-scaffolding.md`
- Phase 02 — Rules & Commands: `docs/raw/plans/rollout/phase-02_rules-and-commands.md`
- Phase 03 — Standard Migration: `docs/raw/plans/rollout/phase-03_standard-migration.md`
- Phase 04 — Adoption & QA: `docs/raw/plans/rollout/phase-04_adoption-and-qa.md`

---

### Appendix A: Patterns (ready-to-copy)

```text
SN_YYYYMMDD-HHMM_slug-with-dashes.md
MN_YYYYMMDD-HHMM_slug-with-dashes.md
GR_YYYYMMDD-HHMM_slug-with-dashes.md
RN_YYYYMMDD-HHMM_slug-with-dashes.md
```

```text
- [ ] (POTENTIAL) (AGENT) [MED] Short, actionable title
  source: docs/agents/session-notes/SN_20251002-0930_topic.md#findings
  tags: session-notes, taxonomy
  notes: Keep concise; link to the exact anchor
```
