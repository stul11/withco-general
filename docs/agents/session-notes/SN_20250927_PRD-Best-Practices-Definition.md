# Session Note

- **Task ID**: PRD-Best-Practices-Definition
- **Agent**: GPT-5-Pro
- **Owner**: slittle
- **Date**: 2025-09-27
- **Duration**: ~2 hours

## Inputs

- withco-general/linear/docs/How to use Linear.md
- .cursor/rules/planning-mode.mdc
- .cursor/rules/todo-cursor.mdc
- .cursor/rules/datetime-format.mdc
- User requirements for PRD templates and offboarding process

## Steps Taken

- Analyzed Linear workflow structure and vocabulary
- Collaboratively defined V3 front matter schema with team-based naming
- Created two distinct PRD templates (Linear-aligned vs Repo-only)
- Designed lightweight offboarding process with Session Notes and Decision Docket
- Created Cursor rules for offboarding workflow
- Generated planning documents for agent artifacts and Pydantic schema review

## Outputs

- withco-general/docs/global/GBL-PRD_Best_Practices.md (comprehensive PRD best practices)
- withco-general/docs/global/TODO_Log.md (persistent TODO tracking)
- withco-general/docs/global/Decision_Docket.md (decision history)
- .cursor/rules/agent-offboarding.mdc (offboarding workflow rule)
- withco-general/docs/agents/templates/ (Session Note, TODO Log, Decision Docket templates)
- withco-general/docs/raw/plans/2025-09-27_agent-artifacts-and-workflows.md
- withco-general/docs/raw/plans/2025-09-27_pydantic-schema-review-agent.md
- Directory structure: /docs/global/, /docs/prds/, /docs/agents/

## Citations

- withco-general/linear/docs/How to use Linear.md:1-160
- .cursor/rules/planning-mode.mdc:1-143
- .cursor/rules/todo-cursor.mdc:1-34
- .cursor/rules/datetime-format.mdc:1-33

## Risks Identified

- None significant identified
- TODO list continuity between sessions requires discipline
- Manual mirroring to Linear requires process adherence

## Next Actions

- Create remaining PRDs from finalized templates
- Implement agent artifacts framework (Role Cards, Context Packs, Playbooks)
- Define ADR and Research Request templates
- Test offboarding process in next session

## Signoff

- **Reviewer**: slittle
- **Status**: approved
- **Date**: 2025-09-27
- **Notes**: Process ready for implementation
