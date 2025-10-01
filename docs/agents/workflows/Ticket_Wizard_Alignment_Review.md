# Ticket Wizard Alignment Review

**Date**: 2025-10-01  
**Reviewer**: Background Agent  
**Purpose**: Ensure Background Agent Draft Review Workflow properly follows `.cursor/rules/ticket-wizard.mdc`

---

## Review Summary

✅ **Workflow is now properly aligned with Ticket Wizard rule**

All changes have been made to ensure the Background Agent Draft Review Workflow correctly references and follows the ticket wizard process as defined in `.cursor/rules/ticket-wizard.mdc`.

---

## Key Requirements from Ticket Wizard Rule

### 1. Core Principle (Line 18)

> "Operate in chat; do not push to Linear automatically."

**Status**: ✅ **Implemented**

- Added explicit note in Phase 1: "does NOT push to Linear automatically"
- Added to "Never Do" section: "Push to Linear automatically - ticket wizard operates in chat only"
- Workflow clearly separates draft creation from Linear implementation

### 2. File Writing (Line 19)

> "Ask before writing files; offer to save drafts under `withco-general/linear/tickets/drafts/`."

**Status**: ✅ **Implemented**

- Phase 1, Step 3: "Agent asks before writing and offers to save draft"
- During Draft Creation: "Ask before writing files - offer to save in `linear/tickets/drafts/`"
- File organization section specifies correct draft directory

### 3. Reviewers/Owners (Line 20)

> "Do not invent reviewers/owners — ask or mark TBD."

**Status**: ✅ **Implemented**

- Added to "Never Do" section: "Invent reviewers or owners - ask user or mark TBD"
- During Draft Creation: "Do NOT invent reviewers/owners - ask or mark TBD"
- Quality checks include: "Reviewers/owners not invented - real names or marked TBD"

### 4. Five-Phase Conversation Script (Lines 24-51)

> Phase 0: Boot, Phase 1: Triage, Phase 2: Context, Phase 3: DoD + Plan, Phase 4: Risks/OOS, Phase 5: Output

**Status**: ✅ **Implemented**

- Phase 1 of workflow now explicitly lists all 5 ticket wizard phases
- Each phase described with key activities
- Process clearly states: "Agent runs Ticket Wizard conversation with user (5 phases)"

### 5. Required Output (Line 50-51)

> "Return a 'Beautiful Ticket' block that exactly matches `TKT_Best_Practices.md` structure, fully populated. Also produce a Reviewer Pack: TL;DR (3 bullets), what to check, and direct links."

**Status**: ✅ **Implemented**

- Phase 1, Step 2: "Agent produces complete ticket with all required sections"
- Phase 1, Step 2: Lists all required sections explicitly
- Phase 5 output: "'Beautiful Ticket' + Reviewer Pack (TL;DR, review checklist)"
- Example output shows: "Reviewer Pack: 3-bullet TL;DR + review checklist"

### 6. Front Matter Requirements (Lines 53-60)

> All required fields: id, title, status, stage, owner, people[], reviewers[], approver, priority, tags[], team, super_initiative, initiative, project, milestone, requirement, linear_issue_link, created (ISO 8601), updated (ISO 8601), version, related_docs[], risk_level, repo_only

**Status**: ✅ **Implemented**

- Quality checks include: "Front matter complete - all required fields populated"
- Review checklist validates front matter completeness

### 7. Finish Conditions (Lines 72-74)

> "The ticket includes Goal/Purpose, Assumptions, Inputs/Dependencies, Deliverable, DoD (3 tiers), Feedback & Reviews, OOS, Open Questions, Plan, and an Appendix with Links/Precedents/Prior Work/Data/People/Decision Log/Context Digest."

**Status**: ✅ **Implemented**

- Phase 1, Step 2 lists all required sections explicitly
- Quality checks include: "All required sections present"
- Review checklist validates section completeness

### 8. Quality Checks (Lines 76-80)

> - Keep DoD checks binary and evidence-backed
> - Ensure every Open Question has a suggested path to answer
> - Trim repeated bullets; normalize section headings to the template

**Status**: ✅ **Implemented**

- Complete "Ticket Wizard Quality Checks" section added
- All 11 quality checks from ticket wizard rule included
- Binary DoD checks with evidence requirement specified
- Open questions with suggested paths requirement included

---

## Changes Made to Background Agent Draft Review Workflow

### Phase 1: Draft Creation - Enhanced

**Before**:

- Simple 4-step process
- Generic "using ticket wizard template"

**After**:

- Detailed 5-phase ticket wizard conversation script
- All 5 phases explicitly listed (Boot → Triage → Context → DoD → Risks → Output)
- Complete ticket requirements specified
- Reviewer Pack requirement added
- Critical rule highlighted: "does NOT push to Linear automatically"
- Enhanced example showing complete deliverable

### Quality Checks - Added

**New Section**: "Ticket Wizard Quality Checks"

- 11 specific checks from ticket wizard rule
- Binary DoD requirement
- Evidence-backed checks
- No repeated bullets
- Section heading normalization
- 3-tier DoD structure
- Task plan requirements
- Reviewer Pack inclusion
- All required sections validation
- Reviewers/owners authenticity check
- Front matter completeness

### Background Agent Responsibilities - Enhanced

**During Draft Creation** (10 items instead of 6):

- Follow ticket wizard rule explicitly
- Run guided conversation (all phases)
- Produce "Beautiful Ticket"
- Create Reviewer Pack
- Include all required sections
- Validate against quality checks
- Ask before writing files
- Do NOT invent reviewers/owners
- Save to drafts directory
- Notify user with summary

### Never Do - Enhanced

**Before**: 5 prohibitions
**After**: 8 prohibitions including:

- Push to Linear automatically (NEW)
- Invent reviewers or owners (NEW)
- Skip ticket wizard phases (NEW)
- All original safety prohibitions maintained

### Related Documentation - Reorganized

**Before**: Simple list
**After**: Categorized into:

- Core Rules & Templates (Ticket Wizard Rule **MUST FOLLOW**)
- Safety & Process
- Workflow Integration

---

## Verification Checklist

### Ticket Wizard Rule Compliance

- ✅ Operates in chat, does not push to Linear automatically
- ✅ Asks before writing files
- ✅ Offers to save drafts in correct directory
- ✅ Does not invent reviewers/owners
- ✅ Follows 5-phase conversation script
- ✅ Produces "Beautiful Ticket" matching structure
- ✅ Produces Reviewer Pack (TL;DR + checklist)
- ✅ Includes all required front matter fields
- ✅ Includes all required sections (Goal → Appendix)
- ✅ Implements all quality checks
- ✅ Binary DoD checks with evidence
- ✅ Open questions with suggested paths
- ✅ No repeated bullets, normalized headings

### Workflow Integration

- ✅ Ticket wizard process integrated into Phase 1
- ✅ Safety rules maintained alongside ticket wizard
- ✅ User review process includes quality checks
- ✅ Authorization process clear before Linear creation
- ✅ Implementation phase separate from draft creation
- ✅ Clear separation between chat operation and Linear push

### Documentation Quality

- ✅ Explicit references to ticket wizard rule
- ✅ Clear examples demonstrating requirements
- ✅ Quality checks comprehensive and actionable
- ✅ Responsibilities clearly defined
- ✅ Prohibitions clearly stated
- ✅ Related documentation properly linked

---

## Remaining Alignment Items

### ✅ All Complete

No remaining alignment items. The workflow fully complies with the ticket wizard rule while maintaining all safety requirements and user oversight.

---

## Benefits of Alignment

### For Background Agents

1. **Clear Process**: Step-by-step conversation script to follow
2. **Quality Standards**: Explicit quality checks to meet
3. **Proper Boundaries**: Clear rules about what not to do
4. **Comprehensive Output**: Know exactly what to produce

### For Users

1. **Consistent Quality**: All drafts follow same high standard
2. **Complete Information**: All required sections included
3. **Easy Review**: Reviewer Pack makes review efficient
4. **Safe Operation**: No automatic Linear pushes
5. **Proper Structure**: All tickets match template

### For Workflow

1. **Quality Assurance**: Built-in quality checks at multiple stages
2. **Safety Compliance**: Ticket wizard rules + safety rules working together
3. **Clear Handoffs**: Draft → Review → Authorization → Implementation
4. **Auditability**: Complete process documented and traceable

---

## Testing Recommendations

### Test Case 1: Simple Draft Creation

1. New agent activates ticket wizard
2. Runs through all 5 phases
3. Produces Beautiful Ticket + Reviewer Pack
4. Asks before writing file
5. Saves to drafts directory
6. User reviews against quality checks
7. User authorizes Linear creation
8. Agent implements with safety checks

**Expected Result**: Complete, high-quality draft ticket following all requirements

### Test Case 2: Quality Check Validation

1. Agent creates draft
2. User reviews using Ticket Wizard Quality Checks section
3. Identifies any missing elements
4. Agent corrects based on quality checks
5. User approves corrected version
6. Agent implements

**Expected Result**: Quality checks catch issues before Linear creation

### Test Case 3: Safety Integration

1. Agent creates draft for personal work
2. Agent attempts to implement
3. Safety checks verify target is Global To-Do
4. User authorization confirmed
5. Linear issue created in correct project
6. Draft archived with Linear link

**Expected Result**: Safety rules work seamlessly with ticket wizard process

---

## Conclusion

The Background Agent Draft Review Workflow is now **fully aligned** with the Ticket Wizard rule (`.cursor/rules/ticket-wizard.mdc`). All requirements, quality checks, and prohibitions are properly documented and integrated into the workflow.

### Key Achievements

1. ✅ **Complete Alignment**: All ticket wizard requirements implemented
2. ✅ **Quality Assurance**: 11 quality checks integrated
3. ✅ **Safety Maintained**: All safety rules preserved
4. ✅ **Clear Process**: 5-phase conversation script documented
5. ✅ **Proper Boundaries**: All prohibitions clearly stated
6. ✅ **Documentation**: Comprehensive references and examples

### Next Steps

1. User reviews aligned workflow documentation
2. Test workflow with next background agent session
3. Validate quality checks work in practice
4. Gather feedback and refine as needed
5. Document lessons learned from testing

---

## Version History

- **v1.0** (2025-10-01): Initial alignment review and implementation
  - Reviewed ticket wizard rule comprehensively
  - Updated Phase 1 with 5-phase conversation script
  - Added Ticket Wizard Quality Checks section
  - Enhanced Background Agent Responsibilities
  - Updated Never Do section with ticket wizard prohibitions
  - Reorganized Related Documentation
  - Verified complete alignment

---

**Reviewer**: Background Agent  
**Status**: Complete ✅  
**Date**: 2025-10-01  
**Next Review**: After first test with new agent
