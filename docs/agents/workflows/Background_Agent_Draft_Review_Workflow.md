# Background Agent Draft Review Workflow

**Created**: 2025-10-01T00:00:00Z  
**Status**: Final  
**Purpose**: Define practical workflow for background agent draft ticket creation, review, and Linear implementation

---

## Overview

This workflow establishes a clear process for background agents to create draft tickets and documentation, get user approval, and then implement changes in Linear. This ensures safety, quality control, and user oversight while maintaining efficiency.

---

## Workflow Phases

### Phase 1: Draft Creation (Background Agent)

**Location**: `/home/slittle/dev/withco-general/linear/tickets/drafts/`

**Process** (follows `.cursor/rules/ticket-wizard.mdc` + `docs/agents/workflows/Ticket_Workflow_README.md`):

1. **Agent runs Ticket Wizard conversation** with user (5 phases):

   - **Phase 0 - Boot**: Locate `TKT_Best_Practices.md`
   - **Phase 1 - Triage**: Working title, deliverable format, DoD tier (Fast/Standard/Gold)
   - **Phase 2 - Context**: Links, docs, precedents, prior work
   - **Phase 3 - DoD + Plan**: 3-tier DoD with binary checks, 20-60 min task plan
   - **Phase 4 - Risks/OOS**: Guardrails, out-of-scope, reviewers, dates
   - **Phase 5 - Output**: "Beautiful Ticket" + Reviewer Pack (TL;DR, review checklist)
   - **Promote & Validate Gate**: Run `/ticket-promote` (collapse DoD to one tier, default Standard) then `/ticket-validate` (template headings, front matter, ISO timestamps)

2. **Agent produces complete ticket** with all required sections (best‑practices draft), then promotes to minimal template:

   - Goal/Purpose, Assumptions, Inputs/Dependencies, Deliverable
   - DoD (3 tiers: Fast/Standard/Gold with 5-8 binary checks each)
   - Feedback & Reviews, OOS, Open Questions, Plan
   - Appendix (Links/Precedents/Prior Work/Data/People/Decision Log/Context Digest)

3. **Agent asks before writing** and offers to save draft in `linear/tickets/drafts/`
4. **Agent saves draft** with naming convention: `{TEAM}-{title-slug}-draft.md`
5. **Agent notifies user** that draft is ready for review

**Critical Rule**: Agent operates in chat; **does NOT push to Linear automatically** per ticket-wizard rule.

**Example**:

```bash
Ticket Wizard Complete ✅

Created: linear/tickets/drafts/SLF-75-cost-model-improvements-draft.md

Includes:
- Promoted minimal template (single DoD list: Standard tier)
- Template validation passed (headings order + ISO timestamps)
- Reviewer Pack: 3-bullet TL;DR + review checklist
- Appendix with links and precedents

Ready for your review. Please review and approve before Linear creation.
```

---

### Phase 2: User Review (Human)

**Location**: Review draft in IDE or Linear tickets/drafts directory

**Process**:

1. **User opens draft file** in editor
2. **User reviews content**:
   - Technical accuracy
   - Completeness
   - Appropriate scope
   - Correct Linear hierarchy
   - Safety compliance
3. **User makes edits** directly in draft file if needed
4. **User provides authorization** via one of:
   - **Explicit approval**: "Approved, create in Linear"
   - **Conditional approval**: "Approved with changes: [changes]"
   - **Rejection**: "Not approved, [reason]"

**Review Checklist**:

- [ ] Title is clear and descriptive
- [ ] Goal/Purpose is well-defined
- [ ] Assumptions are reasonable
- [ ] DoD is achievable
- [ ] Scope is appropriate
- [ ] Out of scope is clearly defined
- [ ] Linear hierarchy is correct
- [ ] Safety rules are followed

**Ticket Wizard Quality Checks** (from `.cursor/rules/ticket-wizard.mdc`):

- [ ] **DoD checks are binary** and evidence-backed (file/link + named reviewer)
- [ ] **Every Open Question** has a suggested path to answer
- [ ] **No repeated bullets** - content is concise and unique
- [ ] **Section headings normalized** to template structure
- [ ] **3-tier DoD** with 5-8 checks per tier (Fast/Standard/Gold)
- [ ] **20-60 minute task plan** with validation front-loaded
- [ ] **Early review checkpoint** included in plan
- [ ] **Reviewer Pack included**: TL;DR (3 bullets) + review checklist
- [ ] **All required sections present**: Goal, Assumptions, Inputs, Deliverable, DoD, Feedback, OOS, Questions, Plan, Appendix
- [ ] **Reviewers/owners not invented** - real names or marked TBD
- [ ] **Front matter complete** - all required fields populated (id, title, status, team, etc.)

---

### Phase 3: Authorization (Human → Agent)

**Location**: Chat/session with background agent

**Authorization Options**:

#### Option A: Direct Approval

```text
"Approved. Create ticket in Linear for draft: SLF-75-cost-model-improvements-draft.md"
```

#### Option B: Approval with Changes

```text
"Approved with changes:
- Change priority to High
- Add tag 'urgent'
- Update team to 'Product'
Then create in Linear."
```

#### Option C: Rejection

```text
"Not approved. Issues:
- Scope too broad, split into multiple tickets
- Missing key dependencies
Please revise and resubmit."
```

---

### Phase 4: Linear Implementation (Background Agent)

**Safety Checks** (Automatic):

- [ ] Verify target project is Global To-Do (`to-do-and-planning-e2ce95344374`)
- [ ] Confirm user authorization received
- [ ] Validate all required fields present
- [ ] Check compliance with safety rules

**Implementation Process**:

1. **Agent verifies authorization**
2. **Agent performs safety checks**
3. **Agent creates Linear issue** in Global To-Do project
4. **Agent updates draft** with Linear issue link
5. **Agent moves draft** to archive or deletes if requested
6. **Agent confirms completion** with Linear link

**Example**:

```text
✅ Safety checks passed
✅ Created Linear issue: SLF-75
✅ Updated draft with Linear link
✅ Draft archived to: linear/tickets/archive/SLF-75-cost-model-improvements.md

Linear issue: https://linear.app/withco/issue/SLF-75
```

---

## File Organization

### Draft Directory Structure

```text
linear/tickets/drafts/
├── {ticket-id}-draft.md           # Active drafts pending review
├── {ticket-id}-wip.md             # Work-in-progress drafts
└── README.md                       # Directory guide

linear/tickets/archive/
├── {ticket-id}-{title}.md         # Completed tickets (created in Linear)
└── {ticket-id}-rejected.md        # Rejected drafts (with reason)
```

### Naming Conventions

**Draft Tickets**:

- Format: `{TEAM-ID}-{title-slug}-draft.md`
- Example: `SLF-75-cost-model-improvements-draft.md`

**WIP Tickets**:

- Format: `{descriptive-name}-wip.md`
- Example: `cost-model-improvements-wip.md`

**Archived Tickets**:

- Format: `{TEAM-ID}-{title-slug}.md`
- Example: `SLF-75-cost-model-improvements.md`

---

## Integration with Global Work Log and To-Do Project

### Content Placement Rules

**SLF-73 (Global Work Log)**:

- Meeting notes and context
- Key decisions and rationale
- Background information
- Reference materials
- Historical documentation

**To-Do & Planning Project** (Linear):

- Active work items from approved drafts
- Task execution and tracking
- Progress updates
- Action items
- Work item status

**Drafts Directory** (Pre-Linear):

- Draft tickets pending review
- Work-in-progress documentation
- Ticket wizard outputs
- Pre-approval content

### Cross-Reference Pattern

When creating Linear issue from draft:

1. **Add context reference** to SLF-73 in Linear issue description using proper Linear formatting (e.g., `SLF-73`)
2. **Update SLF-73** with link to new Linear issue using proper Linear formatting
3. **Archive draft** with Linear issue link in front matter
4. **Cross-link** related work items using proper Linear formatting

### Document Management Process

For detailed meeting notes and context:

1. **Create documents in To-Do & Planning project** for detailed content
2. **Reference documents in SLF-73** with summary and purpose
3. **Use proper Linear formatting** for all issue references (e.g., `SLF-74` not markdown links)
4. **Use markdown links for document references** (e.g., `[📞 RSM CALL NOTES - SEPTEMBER 30, 2025](https://linear.app/withco/document/...)`)
5. **Update project descriptions** to include document references with summaries

**Example**:

```markdown
# In Linear Issue SLF-75

**Context**: See SLF-73 for background

# In SLF-73

**Related Work**: SLF-75

# In Archived Draft

linear_issue_link: "SLF-75"

# For Documents

linear_issue_link: "[📞 RSM CALL NOTES - SEPTEMBER 30, 2025](https://linear.app/withco/document/...)"
```

---

## Safety Rules Integration

### Pre-Creation Safety Checks

Background agent MUST verify:

1. **Target Project**: Only `to-do-and-planning-e2ce95344374` (Global To-Do)
2. **User Authorization**: Explicit approval received
3. **Safety Compliance**: No writes to company Linear projects
4. **Scope Validation**: Work is personal work management only

### Safety Violation Response

If safety check fails:

1. **Stop immediately**: Halt all Linear operations
2. **Alert user**: Notify of safety violation
3. **Log violation**: Record details for audit
4. **Request guidance**: Ask user how to proceed

### Audit Trail

All Linear operations logged with:

- Timestamp
- Operation type
- Target project
- User authorization
- Safety check results
- Outcome

---

## Background Agent Responsibilities

### During Draft Creation

- ✅ **Follow ticket wizard rule** (`.cursor/rules/ticket-wizard.mdc`) - all 5 phases
- ✅ **Run guided conversation**: Triage → Context → DoD → Risks → Output
- ✅ **Produce "Beautiful Ticket"** matching `TKT_Best_Practices.md` structure
- ✅ **Create Reviewer Pack**: TL;DR (3 bullets) + review checklist
- ✅ **Include all required sections**: Goal, Assumptions, Inputs, Deliverable, DoD (3 tiers), Feedback, OOS, Questions, Plan, Appendix
- ✅ **Validate completeness** against ticket wizard quality checks
- ✅ **Ask before writing files** - offer to save in `linear/tickets/drafts/`
- ✅ **Do NOT invent reviewers/owners** - ask or mark TBD
- ✅ **Save to drafts directory** with proper naming convention
- ✅ **Notify user for review** with summary of ticket contents

### During Review Phase

- ✅ Wait for user authorization
- ✅ Answer clarifying questions
- ✅ Make requested changes
- ✅ Re-submit for review if needed
- ✅ Do not proceed without approval

### During Implementation (Agent)

- ✅ Perform safety checks
- ✅ Create Linear issue only in Global To-Do
- ✅ Update draft with Linear link
- ✅ Archive draft appropriately
- ✅ Confirm completion
- ✅ Update related documentation

### Never Do

- ❌ **Push to Linear automatically** - ticket wizard operates in chat only
- ❌ **Create Linear issues without user approval** - explicit authorization required
- ❌ **Invent reviewers or owners** - ask user or mark TBD
- ❌ **Write to company Linear projects** - Global To-Do only
- ❌ **Bypass safety checks** - all operations must pass safety validation
- ❌ **Modify company Linear templates** - read-only access
- ❌ **Create issues in company projects** - prohibited by safety rules
- ❌ **Skip ticket wizard phases** - all 5 phases required for quality

---

## User Responsibilities

### During Review

- Review drafts in reasonable timeframe
- Provide clear authorization or rejection
- Make any needed edits directly in draft
- Specify changes if conditional approval
- Communicate clearly with agent

### During Authorization

- Explicitly authorize Linear creation
- Confirm target project is correct
- Review safety compliance
- Provide clear instructions for changes
- Approve only when content is final

### During Implementation

- Monitor agent actions
- Verify Linear issue created correctly
- Confirm draft archived appropriately
- Validate cross-references are correct
- Provide feedback for improvements

---

## Example End-to-End Flow

### Step 1: Agent Creates Draft

```text
Agent: "I've created a draft ticket for cost model improvements:

File: linear/tickets/drafts/cost-model-improvements-wip.md

Summary:
- Title: Improve Cost of Manufacturing Model
- Goal: More accurate cost calculations
- DoD: Standard tier (2-3 days)
- Team: Shelf

Please review and let me know if you'd like any changes before I create it in Linear."
```

### Step 2: User Reviews

```text
User: "Let me review..."
[Opens file, makes some edits]
```

### Step 3: User Authorizes

```text
User: "Approved. Please create in Linear Global To-Do project with:
- Priority: High
- Tag: cost-modeling
- Team: Shelf"
```

### Step 4: Agent Implements

```text
Agent: "Creating Linear issue...

✅ Safety checks passed (target: Global To-Do)
✅ User authorization confirmed
✅ Creating issue in Linear...

Created: https://linear.app/withco/issue/SLF-75
Title: Improve Cost of Manufacturing Model
Project: To-Do & Planning

Draft archived to: linear/tickets/archive/SLF-75-cost-model-improvements.md
```

---

## Success Metrics

### Process Efficiency

- Time from draft creation to Linear implementation
- Number of review iterations needed
- User satisfaction with drafts

### Quality Metrics

- Accuracy of draft content
- Completeness of drafts
- Alignment with best practices
- Safety compliance rate

### Safety Metrics

- Zero unauthorized Linear writes
- 100% safety check pass rate
- All operations logged and auditable
- No company Linear modifications

---

## Troubleshooting

### Common Issues

**Issue**: Agent created draft but user didn't receive notification
**Solution**: Check draft directory, review recent agent messages

**Issue**: Draft missing required sections
**Solution**: Use ticket wizard template, ensure all sections included

**Issue**: User authorization unclear
**Solution**: Use explicit authorization format from Phase 3

**Issue**: Safety check failed during implementation
**Solution**: Review target project, verify user authorization, check safety rules

**Issue**: Linear issue created in wrong project
**Solution**: **CRITICAL SAFETY VIOLATION** - Immediately alert user, follow rollback procedures

---

## Continuous Improvement

### Feedback Loop

1. **Collect feedback** after each ticket creation
2. **Identify improvements** to process or templates
3. **Update documentation** with lessons learned
4. **Share best practices** with future agents
5. **Refine workflow** based on usage patterns

### Process Refinement

- Weekly review of workflow effectiveness
- Monthly update of documentation
- Quarterly assessment of safety compliance
- Ongoing optimization of agent prompts

---

## Related Documentation

### Core Rules & Templates

- [Ticket Wizard Rule](/workspace/.cursor/rules/ticket-wizard.mdc) - **MUST FOLLOW** for draft creation
- [Ticket Template](/workspace/linear/docs/templates/ticket-template.md) - Structure for all tickets
- [Ticket Best Practices](/workspace/docs/global/GBL-TKT_Best_Practices.md) - Quality standards

### Safety & Process

- [Background Agent Safety Rules](/workspace/.cursor/rules/background-agent-safety.mdc) - **CRITICAL** safety boundaries
- [Background Agent Safeguards](/workspace/.cursor/rules/background-agent-safeguards.mdc) - Operational safeguards
- [Agent Offboarding Checklist](/workspace/.cursor/rules/agent-offboarding.mdc) - Session transitions

### Workflow Integration

- [Global Work Log Process](/workspace/docs/global/Global_Work_Log_vs_To_Do_Process.md) - Content placement rules
- [How to use Linear](/workspace/linear/docs/How_to_use_Linear.md) - Company documentation (READ-ONLY). Do not modify; use personal best practices instead.

---

## Chat Command Shortcuts

Use these during or after a session:

- `/offboard <task-id>` — Run full offboarding per `.cursor/rules/agent-offboarding.mdc` (create Session NOTE, update Decision Docket/TODO Log, validate links and timestamps, prep commit).
- `/end-session <task-id>` — End session with minimal closure; prompts for Session NOTE if docs were modified per `.cursor/rules/agent-session-notes.mdc`.
- `/onboard-next-agent <task-id>` — Generate a copy‑paste onboarding brief and save a handoff NOTE so the next agent starts where we left off.

See `.cursor/rules/agent-chat-commands.mdc` for details.

## Version History

- **v1.0** (2025-10-01): Initial workflow definition
