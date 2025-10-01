# Onboarding Brief: agent-offboarding

## TL;DR

- Commands added: /offboard, /end-session, /onboard-next-agent; safety + read-only company doc separation enforced.
- Repo cleanup: normalized filenames, moved non-draft data, added link/timestamp validation and pre-commit.
- Offboarding note created; changes staged; broken links remain to fix next.

## Required Reading (in order)

1. docs/agents/session-notes/SN_20251001_agent-offboarding.md
2. docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md
3. docs/global/GLB-TKT_Best_Practices.md

## Current State

We implemented clear separation between company Linear documentation and personal drafting best practices. New chat commands are documented and discoverable. Offboarding for this session is documented and staged, and validations surfaced several broken links to resolve. No commits have been made yet; next agent should fix links, validate, and commit.

## Next Agent First Tasks

- [ ] Run pre-commit: `pre-commit run --all-files` and capture failures
- [ ] Fix broken links flagged by checker (README offboarding link; SLF-78 references to try-shortcut; workflow rule/template links)
- [ ] Verify all `.cursor/rules/*` and `docs/agents/workflows/*` links resolve after fixes
- [ ] Review staged changes and commit: `git commit -m "feat: offboard agent - Session: agent-offboarding"`
- [ ] Test `/offboard --dry-run` and `/end-session --dry-run` end-to-end
- [ ] Generate a dry-run `/onboard-next-agent` to verify handoff format

## Open Decisions and Risks

- Broken links list is non-trivial; decide whether to fix now or defer selectively
- Consider adding CI to run link/timestamp checks on PRs

## Related Files

- docs/agents/session-notes/SN_20251001_agent-offboarding.md
- docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md
- docs/global/README.md
