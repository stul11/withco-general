---
id: CHECK-AGENT-ONBOARDING
title: Agent Onboarding Checklist
version: 1.0.0
created: 2025-01-28T00:00:00Z
updated: 2025-01-28T00:00:00Z
owner: Agent Operations
tags: [agent, onboarding, checklist]
status: Active
---

# Agent Onboarding Checklist

Use this checklist to prepare a new agent for an engagement. Complete each checkbox before handing control to the agent.

## 1. Documentation & Context

- [ ] Assign the current Agent Role Card (ARC) and confirm the assignee acknowledged receipt.
- [ ] Provide the latest Context Pack bundle covering system constraints and domain references.
- [ ] Share all required playbooks, especially `docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md` and any task-specific SOPs.
- [ ] Confirm the agent has reviewed `.cursor/rules/*.mdc` safety and execution rules relevant to the engagement.

## 2. Access & Environment

- [ ] Issue time-boxed credentials or tokens with least-privilege scopes.
- [ ] Grant read/write access to `docs/` and other required working directories; validate access by listing expected paths.
- [ ] Verify required tooling (`uv`, `pre-commit`, formatters, test suites) is installed or available in the environment.
- [ ] Enable or confirm audit logging for commands and file edits.

## 3. Orientation Session

- [ ] Walk through project objectives, key risks, and constraints.
- [ ] Review the Decision Docket (`docs/global/Decision_Docket.md`) and TODO Log (`docs/global/TODO_Log.md`) so the agent understands historical context.
- [ ] Demonstrate how to create Session NOTES using `docs/agents/templates/Session_Note_Template.md` and expected naming conventions.
- [ ] Highlight escalation paths for blockers, safety issues, or permission requests.

## 4. Readiness Validation

- [ ] Assign a low-risk smoke-test task and review the agent's execution and documentation quality.
- [ ] Confirm the agent can run validation commands (e.g., `pre-commit run --all-files`) without unexpected failures.
- [ ] Check that the agent captures outputs, decisions, and TODO updates during the smoke test.
- [ ] Obtain human sign-off indicating the agent is production-ready.

## 5. Launch & Monitoring

- [ ] Record onboarding completion, checklist artifacts, and sign-off in the Session NOTE.
- [ ] Set initial monitoring, metrics, or check-ins for the first active session.
- [ ] Notify stakeholders that onboarding is complete and provide the next scheduled checkpoint.
- [ ] Archive the completed checklist alongside other onboarding records.

## Related Assets

- `docs/agents/templates/Onboarding_Checklist_Template.md`
- `docs/agents/templates/Session_Note_Template.md`
- `docs/global/Decision_Docket.md`
- `docs/global/TODO_Log.md`
- `.cursor/rules/agent-offboarding.mdc`
