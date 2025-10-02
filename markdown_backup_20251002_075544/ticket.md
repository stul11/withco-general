# /ticket commands

Minimal, low‑argument commands for ticket drafting, promotion, validation, review, and implementation. Defaults and interactive prompts minimize flags.

## Commands

See individual command docs:

- `./ticket-new.md`
- `./ticket-wizard.md`
- `./ticket-simplify.md`
- `./ticket-promote.md`
- `./ticket-validate.md`
- `./ticket-draft.md`
- `./ticket-review.md`
- `./ticket-approve.md`
- `./ticket-implement.md`
- `./ticket-archive.md`

### /ticket-new "Title"

- Start a best‑practices draft in chat; prompt for missing team and basic metadata.
- Does not write files without confirmation.

### /ticket-wizard

- Run the 5‑phase conversation per `.cursor/rules/ticket-wizard.mdc`.
- No writes without confirmation.

### /ticket-simplify

- Prune verbosity, normalize headings, dedupe bullets.
- Interactive prompts (keep/drop). Operates on current draft by default.

### /ticket-promote

- Transform best‑practices → minimal `ticket-template.md` shape.
- Default DoD tier: Standard (override during triage if needed).
- Auto‑set `created` (once) and refresh `updated` (ISO 8601 UTC).

### /ticket-validate

- Verify headings and order match `linear/docs/templates/ticket-template.md`.
- Validate front matter and timestamps; offer auto‑fixes.

### /ticket-draft

- Save under `linear/tickets/drafts/{TEAM}-{slug}-draft.md` after confirmation.
- Operates on current draft by default.

### /ticket-review

- Mark `status: In Review`; generate Reviewer Pack (TL;DR + checks).

### /ticket-approve

- Mark `status: Approved`; freeze DoD and link next steps.

### /ticket-implement

- With explicit approval only: create issue in Global To‑Do project and back‑link.

### /ticket-archive

- Mark deprecated and move to archive when finished.

## Aliases

`/t new | wizard | simplify | promote | validate | draft | review | approve | implement | archive`

## Philosophy

- Zero/one‑arg defaults: act on the current draft; prompt for essentials.
- Never write to Linear automatically; Global To‑Do writes only with explicit approval.
- Use `GLB-TKT_Best_Practices.md` as drafting space; final tickets must match `ticket-template.md`.

## Related

- `docs/agents/workflows/Ticket_Workflow_README.md`
- `.cursor/rules/ticket-wizard.mdc`
- `linear/docs/templates/ticket-template.md`
