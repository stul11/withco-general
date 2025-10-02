---
type: plan
team: global
created: 2025-10-02T12:30:00Z
updated: 2025-10-02T12:30:00Z
tags: [planning, todos, codelens]
status: draft
source: docs/agents/session-notes/SN_20251002-1230_todo-codelens-readiness.md
---

## Plan: TODO + CodeLens Enablement

### Executive Summary

Codex surfaces an **Enable CodeLens** control above `TODO`-style comments, making inline worklists easier to execute directly
from the editor. The repository currently tracks work in Markdown logs that do not emit recognized comment markers, so CodeLens
never appears. This plan inventories the existing TODO ecosystem, defines CodeLens-driven requirements, compares solution
options, and recommends a hybrid logging architecture that keeps the curated Markdown backlog while emitting lightweight
comment markers for CodeLens automation.

### Current State Audit

#### Tracking documents and structure

- Global backlog lives in `00-key-docs/TODO_Log.md`, a Markdown checklist organized by session history and priority
  sections.【F:00-key-docs/TODO_Log.md†L1-L120】
- The canonical copy is duplicated in `docs/global/TODO_Log.md`, and documentation points contributors to update it at the end
  of each working session.【F:docs/global/TODO_Log.md†L1-L120】【F:docs/global/README.md†L7-L70】
- Team-specific TODO placeholders exist under `linear/{TEAM}/TODO.md`, but they currently only contain headings without
  actionable content, so no shared schema is enforced beyond the global log.【F:linear/global/TODO.md†L1-L1】

#### Templates, rules, and commands

- The TODO log template prescribes checkbox sections (Completed, In Progress, Pending, Blocked) and lacks any inline comment
  markers that an editor could promote to CodeLens actions.【F:docs/agents/templates/TODO_Log_Template.md†L1-L52】
- `/TODO-add` is spec'd to append multi-line Markdown items to `docs/global/TODO_Log.md`, reinforcing the current schema and
  requiring metadata such as labels, priority, and source links.【F:.cursor/commands/todo-add.md†L1-L70】
- `.cursor/rules/todo-cursor.mdc` forces agents to use the `todo_write` tool when updating TODOs, ensuring a single Markdown log
  remains the source of truth.【F:.cursor/rules/todo-cursor.mdc†L1-L33】
- The in-flight document taxonomy plan already proposes renaming the log to `TODO.md`, introducing paired `TOPLAN.md` files,
  and standardizing list schema across global and team scopes.【F:docs/raw/plans/2025-10-02_document-categorization-and-workflows.md†L11-L200】

#### Observations for CodeLens readiness

- Markdown checkboxes (`- [ ]`) do not register as TODO comments in Cursor/VS Code, so CodeLens never appears for log entries.
- Inline TODO comment markers are scattered sparsely across the repo, making CodeLens activation inconsistent with backlog
  tracking expectations.
- Session note workflow requires every documentation change to leave an audit trail, so any new TODO structure must remain
  compatible with mandated offboarding steps.【F:docs/agents/session-notes/SN_20251002-0400_background-cleanup-priority-refresh.md†L1-L116】

### CodeLens-Oriented Requirements

1. **Inline Triggers**: Each actionable TODO must emit a recognizable comment token (`TODO:`/`FIXME:`) in a syntax the editor can
   parse without losing the richer Markdown context for humans.
2. **Single Source of Truth**: Updates through `/TODO-add` and `todo_write` must still target a canonical backlog file so that
   Decision Docket, session notes, and audits stay intact.【F:.cursor/commands/todo-add.md†L18-L66】
3. **Bidirectional Sync**: Converting between Markdown sections and inline comment markers must be deterministic so scripted
   updates do not drift.
4. **Team Parity**: Global and team-scoped TODOs should follow the same format to keep CodeLens behavior consistent when
   business units adopt the flow.【F:docs/raw/plans/2025-10-02_document-categorization-and-workflows.md†L63-L145】
5. **Template Alignment**: Updated templates must scaffold the new structure automatically, preserving headings and metadata the
   workspace already depends on.【F:docs/agents/templates/TODO_Log_Template.md†L17-L52】
6. **Offboarding Compliance**: Offboarding commands and documentation should continue pointing to the authoritative log locations
   (with or without the planned rename), minimizing disruption to existing checklists.【F:docs/agents/session-notes/SN_20251002-0400_background-cleanup-priority-refresh.md†L32-L116】

### Solution Options

| Option | Description | Pros | Cons |
| --- | --- | --- | --- |
| **A. Embed comment markers inside Markdown** | Add hidden HTML comments (e.g., `<!-- TODO: id -->`) or fenced code snippets alongside each checklist item so CodeLens sees a TODO comment adjacent to the human-readable entry. | Minimal file sprawl; preserves current editing habits. | Harder to keep comments and checkboxes in sync; HTML comments can clutter diffs and may not trigger CodeLens depending on language heuristics. |
| **B. Dual-surface backlog** *(recommended)* | Keep the Markdown log as the canonical backlog but generate lightweight sidecar files (e.g., `TODO.codelens.md` or `.todo` per section) containing plain TODO comments that mirror each actionable item. | Clean comment-only surface for CodeLens; sync script can regenerate sidecar from canonical Markdown; no HTML noise in primary docs. | Requires build/sync automation; editors must open sidecar for CodeLens interactions. |
| **C. Full migration to comment-based logs** | Replace Markdown logs entirely with comment-formatted files (YAML front matter + comment list). | Simplifies CodeLens triggers and reduces duplication. | Loses existing rich structure (session history, metadata); breaks `/TODO-add` contract and historical documentation. |

### Recommended Architecture (Option B)

1. **Canonical Markdown remains**: Continue using `TODO_Log.md` (renamed to `TODO.md` per taxonomy plan) as the authoritative backlog with labels, sources, and history.【F:docs/raw/plans/2025-10-02_document-categorization-and-workflows.md†L63-L200】
2. **Introduce generated CodeLens surface**: For each backlog file, emit a deterministic sidecar (e.g., `TODO.codelens.todo`) that lists comment-style entries like `# TODO [MED][AGENT] Align /offboard required sections — docs/...`.
3. **Establish ID linkage**: Annotate each Markdown TODO with an explicit identifier (e.g., `id: todo-20251002-001`) via a trailing HTML comment or YAML attribute so the generator can map Markdown items to comment lines without relying on text diffs.
4. **Scripted sync flow**: Build a `scripts/todos/sync_codelens.py` utility that parses the Markdown schema, emits/updates sidecars, and validates that every comment maps back to a Markdown entry; integrate it into offboarding or pre-commit.
5. **Editor guidance**: Document how to open the sidecar file in Cursor/VS Code to surface CodeLens while keeping the Markdown log as the review artifact.

### Implementation Plan

#### Phase 0 — Research & Inventory

- Confirm CodeLens token requirements across Markdown/sidecar formats (test HTML comments vs dedicated `.todo` files).
- Finalize naming alignment with the taxonomy proposal (decide whether to execute the `TODO_Log.md` → `TODO.md` rename alongside this work).【F:docs/raw/plans/2025-10-02_document-categorization-and-workflows.md†L168-L200】

#### Phase 1 — Schema & Template Updates

- Update `docs/agents/templates/TODO_Log_Template.md` to include unique IDs and a reminder that each item syncs to a CodeLens
  sidecar.【F:docs/agents/templates/TODO_Log_Template.md†L17-L52】
- Extend `/TODO-add` to capture or generate item IDs and write both Markdown and sidecar payloads; adjust `todo_write` usage docs
  to explain the new behavior.【F:.cursor/commands/todo-add.md†L16-L66】【F:.cursor/rules/todo-cursor.mdc†L6-L33】
- Publish contributor guidance in `docs/global/README.md` and the repo `README.md` so humans know how to trigger CodeLens on TODO
  files.【F:docs/global/README.md†L7-L70】【F:README.md†L17-L74】

#### Phase 2 — Sidecar Generation & Migration

- Build the sync script and dry-run it against the existing global log to produce a first `TODO.codelens.todo`; review to ensure
  metadata fidelity.【F:00-key-docs/TODO_Log.md†L1-L120】
- Generate sidecars for each team file under `linear/{TEAM}/TODO.md`, even if they currently contain placeholders, establishing
  a ready-to-use CodeLens surface for future content.【F:linear/global/TODO.md†L1-L1】
- Decide how to handle legacy checklist sections (e.g., Completed vs Pending) in sidecars—likely include only actionable
  sections to avoid clutter.

#### Phase 3 — Automation & Compliance

- Add CI or pre-commit validation to ensure the sidecars stay in sync (fail if Markdown and comment representations diverge).
- Update offboarding/checklist documentation to include running the sync script when TODOs change, keeping the audit trail
  intact.【F:docs/agents/session-notes/SN_20251002-0400_background-cleanup-priority-refresh.md†L32-L116】
- Provide sample Cursor automation (e.g., snippet or command) to open the sidecar automatically when editing TODO logs.

#### Phase 4 — Adoption & Follow-up

- Migrate backlog references in session notes and Decision Docket entries to point to the renamed `TODO.md` once the taxonomy
  plan is approved.【F:docs/raw/plans/2025-10-02_document-categorization-and-workflows.md†L63-L200】
- Evaluate whether to extend the generator to other checklist-heavy docs (session notes, research plans) for optional CodeLens
  enablement.

### Risks & Open Questions

- **Sync Complexity**: Keeping Markdown and comment representations synchronized introduces tooling overhead; mitigated by
  deterministic IDs and automated checks.
- **Editor Adoption**: Contributors must remember to open sidecar files; documentation and quick commands can lower the barrier.
- **Taxonomy Dependencies**: The rename to `TODO.md` and introduction of `TOPLAN.md` may require coordinated rollout with other
  planning initiatives to avoid conflicting migrations.【F:docs/raw/plans/2025-10-02_document-categorization-and-workflows.md†L63-L200】
- **Tool Constraints**: Need to validate that Cursor's CodeLens supports custom `.todo` extensions; fallback is to use `.md`
  sidecars with comment syntax recognized by the editor.

### Immediate Next Steps

1. Prototype comment formats (HTML comment vs `.todo` file) to confirm CodeLens triggers reliably.
2. Draft updates to `/TODO-add` and the TODO log template reflecting ID + sidecar expectations for review.
3. Socialize the plan with maintainers and align timing with the broader document taxonomy migration.

### Incorporation Checklist

- [ ] Update `docs/agents/templates/TODO_Log_Template.md` to add `id:` field and CodeLens note.
- [ ] Extend `.cursor/commands/todo-add.md` to generate IDs and write sidecar entries.
- [ ] Add `.cursor/rules/todo-cursor.mdc` note about sidecar sync requirements and enforcement.
- [ ] Implement `scripts/todos/sync_codelens.py` to generate and validate `*.codelens.todo` sidecars.
- [ ] Wire a pre-commit hook and/or CI job to fail on Markdown/sidecar drift.
- [ ] Document usage in `docs/global/README.md` and `README.md`, including how to open sidecars in Cursor.
- [ ] Produce initial `docs/global/TODO.codelens.todo` from `docs/global/TODO_Log.md` via the sync script.
- [ ] Generate team sidecars under `linear/{TEAM}/` to standardize behavior ahead of content.
- [ ] Align with taxonomy plan for `TODO_Log.md` → `TODO.md` rename and update references.
- [ ] Update offboarding docs to require running the sync script when TODOs are modified.

