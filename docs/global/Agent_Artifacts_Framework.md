# Agent Artifacts Framework

- **Last Updated**: 2025-10-02T21:37:16Z
- **Owner**: Agents Working Group

## Purpose

The agent artifacts framework keeps every background agent predictable, auditable, and easy to hand off. Each artifact answers a specific set of questions and together they describe:

- *Who* the agent is (`Role Card`)
- *What* context it may use (`Context Pack`)
- *How* it should execute tasks (`Playbook`)
- *Why* the guardrails exist (`ADRs`)

All artifacts live under `docs/agents/` and must reference the canonical templates in `docs/agents/templates/`.

## Artifact Overview

| Artifact | Primary Question | Key Contents | Canonical Template |
| --- | --- | --- | --- |
| Agent Role Card | What work is this agent allowed to do? | Purpose & Scope, Inputs/Outputs, Constraints & Safety, Success Criteria, Owners & Escalations | `docs/agents/templates/Agent_Role_Card_Template.md` |
| Context Pack | What curated context is required? | Objective, Required Docs with commit pins, Allowed/Excluded data, Session boundaries, Quality checks | `docs/agents/templates/Context_Pack_Template.md` |
| Playbook | How do we run this work safely? | Preconditions, Phased steps with STOP_FOR_APPROVAL gates, Error handling, Variations, Quality checks | `docs/agents/templates/Playbook_Template.md` |
| ADR | Why did we choose these policies? | Context, Decision drivers, Considered options, Outcome, Links | `docs/agents/templates/ADR_Template.md` |

## Agent Role Card

`docs/agents/templates/Agent_Role_Card_Template.md`

- **Purpose**: Define the agent's mandate, success bar, and safety boundaries. The Role Card is the top-level source of truth for the agent.
- **Minimum required sections**: Purpose & Scope (including in/out of scope lists), Inputs & Outputs with allowed tools, Constraints & Safety (data boundaries, prohibited actions, safety checks), Success Criteria, Ownership & Escalation, Context Packs, Playbooks, Version History, and Related Documents.
- **Lifecycle**:
  - Draft a Role Card before a new agent is onboarded.
  - Transition to `Active` only after human review and a baseline session NOTE confirm the guardrails.
  - Update the Version History and `Last Updated` stamp whenever scope, constraints, or ownership changes.
- **Linkage**: Must name the approved Context Packs and Playbooks the agent may use. Significant policy or scope changes require an ADR reference.

## Context Pack

`docs/agents/templates/Context_Pack_Template.md`

- **Purpose**: Provide the minimum, curated inputs an agent needs for a task while enforcing data boundaries.
- **Minimum required sections**: Objective, Required Docs (with path and pinned commit when applicable), Allowed Data vs Excluded Data, Session Boundaries (time-box and token budgets), Context Summary, Usage Guidelines, Quality Checks, Related Context Packs, Version History, Notes.
- **Lifecycle**:
  - Create or refresh Context Packs whenever the underlying source docs move or materially change.
  - Pin exact revisions (using `path@sha`) when the agent must stay on a particular snapshot.
  - Archive or mark as Deprecated when superseded; update referencing Role Cards and Playbooks.
- **Linkage**: Listed in the Role Card under Context Packs; referenced in Playbooks for steps that depend on specific datasets.

## Playbook

`docs/agents/templates/Playbook_Template.md`

- **Purpose**: Describe the deterministic procedure an agent (or human) follows to complete recurring work with safety checks.
- **Minimum required sections**: Overview, Preconditions (state/access/resources), Phase-based Steps with explicit inputs/outputs/validation, STOP_FOR_APPROVAL gates, Postconditions, Error Handling (including rollback/abort), Quality Checks, Variations, Related Documents, Version History.
- **Lifecycle**:
  - Draft alongside the Role Card for any process-heavy work.
  - Validate the Playbook during the first supervised runs; capture feedback in ADRs or updated steps.
  - Keep approval gates aligned with risk level; record revisions in Version History.
- **Linkage**: Referenced by the Role Card under Playbooks and by Context Packs when a step consumes a specific dataset.

## Architecture Decision Records (ADRs)

`docs/agents/templates/ADR_Template.md`

- **Purpose**: Capture the rationale behind agent policies, major scope decisions, and safety trade-offs.
- **Minimum required sections**: Status, Context, Decision Drivers, Considered Options, Decision Outcome (positive/negative consequences), Pros & Cons per option, Links.
- **Lifecycle**:
  - Create an ADR whenever a change alters the Role Card, Context Packs, or Playbooks in a non-trivial way (new permissions, new data boundaries, escalation changes, etc.).
  - Update the `status` to `Accepted` only after the change is live and reviewed.
  - Supersede or link ADRs when later decisions revise earlier ones.
- **Linkage**: Role Cards and Playbooks should link to the governing ADRs in their Related Documents section.

## Governance & Workflow

1. **Propose**: Draft Role Card, Context Pack(s), Playbook(s), and supporting ADR for new work. Capture open questions in the TODO Log if unresolved.
2. **Review**: Obtain human review, ensuring the Role Card aligns with business goals, Context Packs are scoped correctly, and Playbooks include approvals and rollback paths.
3. **Activate**: Mark artifacts `Active`, distribute to the agent, and log the decision in `docs/global/Decision_Docket.md` if it changes policy.
4. **Operate**: During sessions, reference the Context Pack and Playbook. Capture deviations or gaps in Session NOTES and update artifacts as needed.
5. **Maintain**: When any artifact changes, update linked documents and the Version History, and ensure ADRs remain the authoritative explanation.

## Storage & Naming

- Store working artifacts in `docs/agents/` — create dedicated subdirectories as needed:
  - `docs/agents/role-cards/` for active Role Cards
  - `docs/agents/context-packs/` for Context Packs
  - `docs/agents/playbooks/` for Playbooks
  - `docs/agents/adrs/` for agent-focused ADRs (if split from global ADRs)
- Use predictable filenames: `ARC_<Agent>.md`, `CP_<Topic>.md`, `PB_<Process>.md`, `[TEAM]-ADR_<Title>.md`.
- Keep repository-wide guidance synchronized via `scripts/sync_agents_rules.py` so generated `AGENTS.md` guardrails stay accurate.

## Related Resources

- Templates: `docs/agents/templates/`
- Workflows: `docs/agents/workflows/`
- Session Notes: `docs/agents/session-notes/`
- Global governance: `docs/global/Decision_Docket.md`, `docs/global/TODO_Log.md`
