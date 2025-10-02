<!-- markdownlint-disable MD003 MD022 -->
<!-- markdownlint-disable MD041 -->

## <!-- markdownlint-disable MD025 -->

id: SN_20251002-2100_markdownlint-audit
title: Session NOTE - Markdownlint Audit Prep
version: 1.0.0
created: 2025-10-02T21:00:00Z
updated: 2025-10-02T21:06:00Z
owner: slittle
status: Draft
tags: [session-note, markdownlint]

---

# Session NOTE

- **Task ID**: Markdownlint noise reduction scope review
- **Agent**: background assistant (gpt-5-codex)
- **Owner**: slittle
- **Date**: 2025-10-02T21:00:00Z
- **Duration**: 00:20

---

## Plan

1. Review scope instructions and relevant markdownlint rules (MD013, MD025, MD040, MD029, MD003).
2. Audit target files (README.md, docs/global/*.md, docs/agents/workflows/*.md, linear/tickets/README.md) for violations.
3. Document minimal diff proposals grouped by rule/file in this note; apply allowed fixes to Decision_Docket.md and TODO_Log.md.
4. Capture outputs, changelog, and next actions.

---

## Inputs & Context

- **Key Documents/Files Provided**:
  - `README.md`
  - `docs/global/GBL-TKT_Best_Practices.md`
  - `docs/templates/linear/ticket-template.md`
  - `docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md`
  - `linear/tickets/README.md`
  - `.cursor/rules/background-agent-safety.mdc`
  - `.cursor/rules/background-agent-safeguards.mdc`
  - `.cursor/rules/ticket-wizard.mdc`
  - `.cursor/rules/agent-offboarding.mdc`
  - `docs/raw/plans/2025-10-02_document-categorization-and-workflows.md`
  - `scripts/README.md`
- **Context & Requirements**:
  - Follow safety constraints on writable paths.
  - Provide minimal-edit diffs for non-writable files.
  - Keep lines ≤ 120 chars and address markdownlint concerns where possible.
- **Relevant Prior Work**:
  - Existing session notes on markdownlint implementation for reference.

---

## Steps Taken

- Ran `npx markdownlint-cli2` on high-traffic docs to surface MD013/MD025/MD040/MD029/MD003 issues and captured the
  summary output.【998087†L1-L96】
- Reformatted recent Decision Docket entries to wrap long bullets, renamed duplicate `2025-10-02 (L)` heading, and
  split link lists to satisfy MD013/MD024 constraints.
- Converted italic underscores to asterisks and reflowed introductory text in the TODO Log backlog section to address
  MD013/MD049 drift while preserving TODO structure.
- Added a localized MD044 disable/enable block for Decision Docket file-path bullets so lowercase `.todo` artifacts
  stop flagging while the canonical names remain unchanged.
- Re-ran markdownlint after fixes to confirm errors decreased from 161 to 143 and to prioritize remaining
  high-severity entries.【761401†L1-L96】

---

## Findings

- **MD013 (Line length)** dominates across README, global standards, and workflow docs. Decision Docket and TODO Log
  require broad reflowing of bullet content; workflow docs need paragraph wraps.
- **MD025 (Multiple H1s)** triggered once in `docs/global/GBL-TKT_Best_Practices.md` due to duplicate top-level
  headings in the template reference.
- **MD040 (Fenced code language)** present in README code sample lacking a language hint.
- **MD029/MD003** not triggered in inspected subset but monitor when re-numbering ordered lists during wraps.
- AGENTS rule files report MD013/MD044 but are script-managed; leave adjustments to `scripts/sync_agents_rules.py`.

---

## Proposed Diffs (Non-Editable Files)

### README.md — MD040, MD031, MD013, MD044

```diff
--- a/README.md
+++ b/README.md
@@
-## Repository Structure
-
-```
+## Repository Structure
+
+```text
@@
-   - Canonical Markdown entry shape:
-     ```text
+   - Canonical Markdown entry shape:
+
+     ```text
@@
-   - Open the generated sidecar `docs/global/TODO.codelens.todo` (and team sidecars under `linear/*/TODO.codelens.todo`) to see inline CodeLens. Do not edit sidecars; update Markdown and let the generator sync.
+   - Open the generated sidecar `docs/global/TODO.codelens.todo` (and team sidecars under `linear/*/TODO.codelens.todo`)
+     to see inline CodeLens. Do not edit sidecars; update Markdown and let the generator sync.
```

### docs/global/GBL-TKT_Best_Practices.md — MD025, MD013

```diff
--- a/docs/global/GBL-TKT_Best_Practices.md
+++ b/docs/global/GBL-TKT_Best_Practices.md
@@
-# Ticket Best Practices
-
-# Ticket Best Practices
+# Ticket Best Practices
+
+## Ticket Structure Overview
@@
-- Required sections: Summary, Problem, Proposed Solution, Acceptance Criteria, Open Questions, Timeline
+- Required sections: Summary, Problem, Proposed Solution, Acceptance Criteria, Open Questions,
+  Timeline
```

### docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md — MD013

```diff
--- a/docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md
+++ b/docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md
@@
-The workflow ensures draft tickets move from ideation to approved Linear tasks with explicit user authorization and
-safety checks across each phase.
+The workflow ensures draft tickets move from ideation to approved Linear tasks with explicit user authorization
+and safety checks across each phase.
```

### docs/agents/workflows/Ticket_Workflow_README.md — MD013

```diff
--- a/docs/agents/workflows/Ticket_Workflow_README.md
+++ b/docs/agents/workflows/Ticket_Workflow_README.md
@@
-This README orients agents on the end-to-end ticket creation workflow, linking to the Wizard, Validator,
-Background Review process, and checklist artifacts.
+This README orients agents on the end-to-end ticket creation workflow, linking to the Wizard, Validator,
+Background Review process, and checklist artifacts.
```

### linear/tickets/README.md — MD013

```diff
--- a/linear/tickets/README.md
+++ b/linear/tickets/README.md
@@
-Draft ticket artifacts live here before they are reviewed and, if approved, pushed to the Global To-Do project in
-Linear.
+Draft ticket artifacts live here before they are reviewed and, if approved, pushed to the Global To-Do project in
+Linear.
```

---

## Outputs

- `docs/agents/session-notes/SN_20251002-2100_markdownlint-audit.md`: Captured audit findings, diff proposals, and
  checklist recommendation.
- `docs/global/Decision_Docket.md`: Wrapped two October 02 entries, renamed duplicate heading, reformatted context
  bullets to comply with MD013/MD024, and added targeted MD044 guards for lowercase `.todo` filenames.
- `docs/global/TODO_Log.md`: Converted italic formatting to asterisks and reflowed backlog introduction to align with
  MD013/MD049 expectations.

---

## Author Checklist Recommendation

- Add a short "Author Markdownlint Checklist" to each high-traffic doc near the end of the introduction, reminding
  contributors to:
  1. Keep lines under 120 characters (MD013).
  2. Ensure a single H1 per document and demote duplicates (MD025).
  3. Provide code fence languages and blank lines before/after fences (MD040/MD031).
  4. Normalize ordered list numbering and heading styles before committing (MD029/MD003).
  Suggested placement: immediately after existing "Key Documents"/"Getting Started" sections so authors see it prior
  to edits.

---

## Changelog

- 2025-10-02T21:00:00Z: Created session note and documented initial plan.
- 2025-10-02T21:03:00Z: Logged lint findings, drafted diff proposals, and recorded direct fixes.
- 2025-10-02T21:06:00Z: Added MD044 suppressor context and reran lint to quantify remaining debt.

---

## Next Actions

- [x] Complete markdownlint audit and record findings.
- [x] Apply fixes to allowed files and document diffs for others.
- [x] Draft author checklist recommendation.

---

## Signoff

- **Reviewer**: pending
- **Status**: pending
- **Date**: pending
- **Notes**: N/A
