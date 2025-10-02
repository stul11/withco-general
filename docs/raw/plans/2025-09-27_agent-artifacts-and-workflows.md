# Plan: Agent Artifacts and Workflows

- Date: 2025-09-27
- Status: Draft

## 1) Objective

Define lightweight yet effective options to implement Agent Artifacts and an agentic workflow that is safe, auditable, and productive. Scope includes: Agent Role Cards (ARC), Context Packs, Playbooks, ADRs for agent policies, Onboarding/Offboarding checklists, Session Notes, a lightweight Decision Docket (recommendation log), and TODO logs.

## 2) Background & constraints

- We use Linear as the operational system; docs live in Git (Markdown), mirrored manually to Linear for now.
- We prefer planning-first (no heavy automation) with strict, human-in-the-loop controls.
- We want Cursor rules to guide behavior and small commands to scaffold artifacts quickly.

## 3) Options (lightweight → structured)

### Option A — Minimal templates + manual review

- What: Keep simple Markdown templates for ARC, Context Pack, Playbook, Checklists, Session Notes; fill manually; reviewers sign off in Linear.
- Pros:
  - Fastest to adopt; nearly zero setup
  - Low tooling risk; easy for contributors
- Cons:
  - Inconsistency risk without guardrails
  - Harder to enforce required fields
- Kickoff:
  - Create files under `docs/agents/**` and link in Linear
  - Rely on reviewers to check completeness
- Best when: Prototyping, small team, high touch review

### Option B — Template-first + Cursor rules (recommended to start)

- What: Same templates, plus Cursor rules that remind the assistant to:
  - Use `todo_write` for tracking (TODO-cursor)
  - Emit a Session NOTE for each agent session
  - Include mandatory sections in ARC/Context Pack/Playbook
- Pros:
  - Lightweight guardrails; improves consistency without custom infra
  - Aligns with current manual mirroring policy
- Cons:
  - Soft enforcement; relies on agent rule adherence
- Kickoff:
  - Add rules: `agent-session-notes.mdc`, `agent-artifacts-standard.mdc`
  - One-liner commands to scaffold templates
- Best when: We want quick wins and improved reliability

### Option C — Structured metadata + lint pass (upgrade path)

- What: Add light front matter to artifacts (only where valuable) and run a markdown lint pass locally/CI; keep date-time rule for PRDs/ADRs.
- Pros:
  - Improves searchability and governance (owners, scope, status)
  - Enables automated checks without heavy systems
- Cons:
  - Slight authoring overhead
- Kickoff:
  - Introduce optional front matter for ARC/Playbook, keep Context Pack mostly Markdown + a tiny YAML block
  - Add a "docs lint" command later
- Best when: Scale increases and we want stronger consistency

### Option D — Issue-first with Git mirror

- What: Create artifacts as Linear docs first; mirror snapshots into Git for versioning.
- Pros:
  - Optimized for non-technical users
  - Linear remains the operational surface
- Cons:
  - Git history may lag; requires discipline to sync
- Best when: Stakeholders prefer Linear authoring; Git is archival source

## 4) Contracts: minimal required fields per artifact

### 4.1 Agent Role Card (ARC)

- Required fields:
  - Name, Version
  - Purpose & Scope (in/out)
  - Inputs (docs, systems), Outputs (artifacts), Tools Allowed
  - Constraints & Safety (no-write areas, data limits)
  - Success Criteria & KPIs
  - Owner (human), Escalation contact
- Skeleton:

```markdown
# Agent Role Card: [Name]

Version: 0.1.0

## Purpose & Scope

- Purpose:
- In-scope:
- Out-of-scope:

## Inputs & Outputs

- Inputs:
- Outputs:
- Tools Allowed:

## Constraints & Safety

- Data boundaries:
- Prohibited actions:

## Success Criteria

- Quality gates:
- KPIs:

## Ownership

- Human Owner:
- Escalation:
```

### 4.2 Context Pack (curated minimal context)

- Required fields:
  - Objective (1-2 lines)
  - Required Docs (paths/links with commit SHAs where possible)
  - Allowed Data / Exclusions
  - Session Boundaries (time-box, tokens)
- Skeleton:

```markdown
# Context Pack: [Topic]

Objective: One line

## Required Docs

- [path/to/doc.md@<sha>]

## Allowed Data

- Allowed:
- Excluded:

## Session Boundaries

- Time-box:
- Token scope:
```

### 4.3 Playbook (deterministic steps)

- Required fields:
  - Preconditions, Steps (with STOP_FOR_APPROVAL gates), Postconditions
  - Error Handling, Rollback/Abort
- Skeleton:

```markdown
# Playbook: [Process]

## Preconditions

-

## Steps

1. Do X
2. STOP_FOR_APPROVAL: Reviewer confirms X
3. Do Y

## Postconditions

-

## Error Handling

-
```

### 4.4 Onboarding Checklist

```markdown
# Onboarding: [Agent/Role]

- Assign Role Card and Context Pack
- Issue scoped, time-boxed RO tokens
- Run smoke test task; capture Session NOTE; human sign-off
```

### 4.5 Offboarding Checklist

```markdown
# Offboarding: [Agent/Role]

- Revoke tokens, rotate secrets
- Wipe ephemeral caches
- Close Session Log; attach outputs to PRD/issue
- Update ADRs for new rules/risks
```

### 4.6 Session NOTE (per session)

```markdown
# Session NOTE

- Task ID:
- Agent:
- Owner:
- Inputs:
- Steps:
- Outputs:
- Citations:
- Risks:
- Next Actions:
- Signoff: pending | approved (by: )
```

### 4.7 Decision Docket / Recommendation Log

- One rolling Markdown in `docs/global/Decision_Docket.md` with short entries:

```markdown
- 2025-09-27: Decision/Recommendation, Link (PRD/commit), Owner
```

### 4.8 TODO logs

- Policy: Always use the Cursor TODO tool via `TODO-cursor` rule (no ad-hoc text TODOs).

## 5) Proposed Cursor rules (lightweight guardrails)

1. `agent-session-notes.mdc`

- Description: Require a Session NOTE for each agent session that edits PRDs/agents/BOM docs.
- Globs: `**/docs/prds/**, **/docs/agents/**, **/docs/global/**`
- Behavior: Remind to create/attach Session NOTE and obtain human signoff before merging.

2. `agent-artifacts-standard.mdc`

- Description: Remind the assistant to include required sections for ARC/Context Pack/Playbook.
- Globs: `**/docs/agents/**`

3. Reuse existing rules

- `planning-mode.mdc`: one focused recommendation in chat
- `planning-mode-md.mdc`: create generative plan docs in `/docs/raw/plans`
- `TODO-cursor.mdc`: always use `todo_write` tool for TODO updates
- `datetime-format.mdc`: enforce created/updated time in front matter (PRDs/ADRs/Research)

## 6) Commands to scaffold artifacts (one-liners; do not execute by default)

- Create ARC:

```bash
mkdir -p withco-general/docs/agents/role-cards && cat > withco-general/docs/agents/role-cards/ARC_<Name>.md <<'MD'
# Agent Role Card: <Name>
Version: 0.1.0
## Purpose & Scope
## Inputs & Outputs
## Constraints & Safety
## Success Criteria
## Ownership
MD
```

- Create Context Pack:

```bash
mkdir -p withco-general/docs/agents/context-packs && cat > withco-general/docs/agents/context-packs/CP_<Topic>.md <<'MD'
# Context Pack: <Topic>
Objective:
## Required Docs
## Allowed Data
## Session Boundaries
MD
```

- Create Playbook:

```bash
mkdir -p withco-general/docs/agents/playbooks && cat > withco-general/docs/agents/playbooks/PB_<Process>.md <<'MD'
# Playbook: <Process>
## Preconditions
## Steps
## Postconditions
## Error Handling
MD
```

- Create On/Offboarding checklists:

```bash
mkdir -p withco-general/docs/agents/checklists && printf "# Onboarding: <Role>\n- Assign Role Card and Context Pack\n- Issue scoped, time-boxed RO tokens\n- Run smoke test; capture Session NOTE; sign-off\n" > withco-general/docs/agents/checklists/ON_<Role>.md && printf "# Offboarding: <Role>\n- Revoke tokens, rotate secrets\n- Wipe ephemeral caches\n- Close Session Log; attach outputs\n- Update ADRs\n" > withco-general/docs/agents/checklists/OFF_<Role>.md
```

- Create Session NOTE:

```bash
mkdir -p withco-general/docs/agents/session-notes && cat > withco-general/docs/agents/session-notes/SN_<YYYYMMDD>_<TaskId>.md <<'MD'
# Session NOTE
- Task ID:
- Agent:
- Owner:
- Inputs:
- Steps:
- Outputs:
- Citations:
- Risks:
- Next Actions:
- Signoff:
MD
```

## 8) Recommendation

Adopt Option B now (Templates + Cursor rules). It adds minimal overhead while increasing consistency and safety. Reassess after 2–3 weeks; consider selectively adopting Option C for high-sensitivity flows.

## 9) Next steps

- Approve the required sections for ARC, Context Pack, Playbook
- Approve creation of the three proposed Cursor rules
- If approved, scaffold template files and pilot on one initiative (e.g., "Economics & Structure")
