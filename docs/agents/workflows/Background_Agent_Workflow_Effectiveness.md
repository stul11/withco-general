# Background Agent Workflow Effectiveness Tracker

**Purpose**: Provide a lightweight, repeatable way to measure how well the Background Agent Draft Review Workflow performs and capture reviewer feedback for future improvements.

---

## Weekly Metrics Snapshot

Record metrics at the end of each week after running the workflow. Keep the most recent entries at the top.

| Week of (UTC) | Drafts Run | Median Draft→Approval (hrs) | Avg Review Iterations | Safety Check Flags | Notes |
| --- | --- | --- | --- | --- | --- |
| 2025-10-03 | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |

**How to gather metrics**

1. Review session notes and Git history for ticket wizard runs during the week.
2. For each draft ticket:
   - Note the UTC timestamp when the draft was first saved.
   - Note when the user approved it for Linear.
   - Count the number of review revisions requested.
   - Record any `/ticket-validate` or safety check failures.
3. Calculate the median hours between draft creation and approval across the set.
4. Summarize any safety incidents or frictions in the Notes column.

---

## Feedback Log

Capture qualitative feedback from reviewers, users, or background agents immediately after each workflow execution.

| Date (UTC) | Feedback Source | Sentiment | Key Feedback | Follow-up Owner | Status |
| --- | --- | --- | --- | --- | --- |
| 2025-10-02 | _TBD_ | _Positive/Neutral/Concerned_ | _What went well or needs change_ | _Name_ | _Open_ |

**Collection prompts**

- "What felt smooth about the new workflow?"
- "Where did the process slow you down?"
- "Did the safety checks catch anything unexpected?"
- "Any documentation or tooling gaps we should address?"

Log feedback even if anonymous; attribute to `TBD` when the reviewer prefers anonymity.

---

## Retrospective Checklist

Run this quick checklist during weekly review:

- [ ] Metrics table updated with latest runs
- [ ] Feedback log entries triaged (owners + status)
- [ ] Action items copied to `docs/global/TODO_Log.md` if follow-up is required
- [ ] Relevant documentation updates captured in `docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md`
- [ ] Patterns or blockers summarized in session notes for the next agent

---

## Related References

- `docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md`
- `docs/global/TODO_Log.md`
- `docs/agents/session-notes/SN_20251001-0000_workflow-finalization.md`

