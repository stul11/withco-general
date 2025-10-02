---
id: CHECK-AGENT-OFFBOARDING
title: Agent Offboarding Checklist
version: 1.0.0
created: 2025-01-28T00:00:00Z
updated: 2025-01-28T00:00:00Z
owner: Agent Operations
tags: [agent, offboarding, checklist]
status: Active
---

# Agent Offboarding Checklist

Follow this checklist to safely conclude an agent session and prepare the next handoff.

## 1. Pre-Offboarding Review

- [ ] Verify all work-in-progress files are saved and staged in the repository workspace.
- [ ] Ensure the current Session NOTE in `docs/agents/session-notes/` reflects the latest work, blockers, and outstanding items.
- [ ] Confirm the Decision Docket (`docs/global/Decision_Docket.md`) captures every decision taken during the session.
- [ ] Update the TODO Log (`docs/global/TODO_Log.md`) with remaining tasks, owners, and statuses.
- [ ] Capture any risks, mitigations, or follow-ups discovered during the session.

## 2. Offboarding Actions

- [ ] Revoke or expire any temporary credentials or access tokens issued for the session.
- [ ] Remove or reset environment variables, API keys, and other secrets from local shells or configuration files.
- [ ] Clean up temporary assets (scratch pads, cache directories, generated artifacts) that should not persist.
- [ ] Stage or commit final code/documentation changes with a descriptive message.
- [ ] Attach artifacts, logs, or validation outputs to the Session NOTE or repository as appropriate.

## 3. Handoff Preparation

- [ ] Summarize current status, remaining scope, and next priority steps in the Session NOTE.
- [ ] Link relevant artifacts (Role Card, Context Pack, Playbooks, ADRs) for the incoming agent.
- [ ] Record validation results (tests, `pre-commit`, manual checks) and list any failures needing follow-up.
- [ ] Provide contact information or escalation paths if clarifications are required.

## 4. Finalization

- [ ] Commit and push (or stage) final changes and document the git status in the Session NOTE.
- [ ] Verify repository hygiene: no stray files, secrets, or temporary notes remain.
- [ ] Archive the completed checklist alongside the Session NOTE.
- [ ] Notify stakeholders that the agent has been offboarded and identify the next owner.

## Related Assets

- `docs/agents/templates/Offboarding_Checklist_Template.md`
- `.cursor/rules/agent-offboarding.mdc`
- `docs/global/Decision_Docket.md`
- `docs/global/TODO_Log.md`
- `docs/agents/templates/Session_Note_Template.md`
