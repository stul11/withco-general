# Ticket Validator Spec (Template Compliance + Timestamps)

## Purpose

Define checks the agent should run for `/ticket-validate` and during `/ticket-promote` to ensure the final ticket matches `linear/docs/templates/ticket-template.md` exactly and uses ISO 8601 UTC timestamps.

## Checks

### 1) Front matter schema (required keys)

Required keys:

```text
id, title, status, stage, owner, people[], reviewers[], approver, priority,
tags[], team, super_initiative, initiative, project, milestone, requirement,
linear_issue_link, created, updated, version, related_docs[], risk_level, repo_only
```

Rules:

- `created` and `updated` must be ISO 8601 UTC (e.g., 2025-10-01T00:00:00Z)
- `created` set once; `updated` refreshed on transitions
- Unknown values allowed as `"TBD"` but keys must exist

### 2) Heading presence and order (exact)

Order must match the template:

1. `# [Issue Title]`
2. `Goal / Purpose`
3. `Assumptions`
4. `Open Questions`
5. `Inputs / Dependencies`
6. `Feedback requirements`
7. `Explicitly out of scope`
8. `Deliverable`
9. `Definition of Done (DoD)`
10. `Appendix`

Rules:

- No extra top-level sections beyond the above
- Allow subheadings within Appendix

### 3) DoD ladder collapse

If input is from best‑practices with tiers (Fast/Standard/Gold):

- Select one tier (default: Standard) and output a single DoD checklist
- Each DoD check must be binary and evidence-backed (file/link + reviewer)

### 4) Simplification heuristics

- Trim duplicate bullets
- Cap to a reasonable bullet count per section (suggested ≤5)
- Remove empty sections only after warning; encourage concise content

### 5) Naming & paths

- Draft path: `linear/tickets/drafts/{TEAM}-{slug}-draft.md`
- Archive path: `linear/tickets/archive/{TEAM}-{slug}.md`

### 6) Safety checks (informational)

- No Linear writes without explicit approval
- Only Global To‑Do project for Linear creation

## Outputs

- Validation report with pass/fail per check and suggested fixes
- Auto‑fix options for timestamps, heading normalization, and minor field normalization

## References

- `linear/docs/templates/ticket-template.md`
- `docs/agents/workflows/Ticket_Workflow_README.md`
- `.cursor/rules/ticket-wizard.mdc`
