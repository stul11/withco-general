# Playbook Template

---
id: PB_[Process]
title: Playbook: [Process]
version: 0.1.0
created: YYYY-MM-DDTHH:MM:SSZ
updated: YYYY-MM-DDTHH:MM:SSZ
owner: [Owner]
status: Draft | Active | Deprecated
tags: [playbook, process, automation]
---

# Playbook: [Process]

**Version**: 0.1.0  
**Status**: [Draft | Active | Deprecated]  
**Owner**: [Owner]  
**Last Updated**: YYYY-MM-DDTHH:MM:SSZ

## Overview

[Brief description of what this playbook accomplishes and when to use it]

## Preconditions

### Required State

- [ ] [Condition 1: what must be true before starting]
- [ ] [Condition 2: what must be true before starting]
- [ ] [Condition 3: what must be true before starting]

### Required Access

- [Access 1: what permissions/tools are needed]
- [Access 2: what permissions/tools are needed]

### Required Resources

- [Resource 1: what must be available]
- [Resource 2: what must be available]

## Steps

### Phase 1: Preparation

1. **[Step 1]**: [Detailed description]
   - **Input**: [What's needed]
   - **Action**: [What to do]
   - **Output**: [What's produced]
   - **Validation**: [How to verify success]

2. **[Step 2]**: [Detailed description]
   - **Input**: [What's needed]
   - **Action**: [What to do]
   - **Output**: [What's produced]
   - **Validation**: [How to verify success]

### Phase 2: Execution

3. **STOP_FOR_APPROVAL**: [Reviewer confirms Phase 1 completion]
   - **Reviewer**: [Who approves]
   - **Criteria**: [What they check]
   - **Timeout**: [How long to wait]

4. **[Step 3]**: [Detailed description]
   - **Input**: [What's needed]
   - **Action**: [What to do]
   - **Output**: [What's produced]
   - **Validation**: [How to verify success]

5. **[Step 4]**: [Detailed description]
   - **Input**: [What's needed]
   - **Action**: [What to do]
   - **Output**: [What's produced]
   - **Validation**: [How to verify success]

### Phase 3: Completion

6. **STOP_FOR_APPROVAL**: [Reviewer confirms Phase 2 completion]
   - **Reviewer**: [Who approves]
   - **Criteria**: [What they check]
   - **Timeout**: [How long to wait]

7. **[Step 5]**: [Detailed description]
   - **Input**: [What's needed]
   - **Action**: [What to do]
   - **Output**: [What's produced]
   - **Validation**: [How to verify success]

## Postconditions

### Success Criteria

- [ ] [Criterion 1: what indicates success]
- [ ] [Criterion 2: what indicates success]
- [ ] [Criterion 3: what indicates success]

### Deliverables

- [Deliverable 1: what's produced]
- [Deliverable 2: what's produced]
- [Deliverable 3: what's produced]

### Cleanup

- [Cleanup task 1: what to clean up]
- [Cleanup task 2: what to clean up]

## Error Handling

### Common Errors

#### Error 1: [Error Description]

- **Symptoms**: [How to recognize this error]
- **Causes**: [What causes this error]
- **Resolution**: [How to fix it]
- **Prevention**: [How to avoid it]

#### Error 2: [Error Description]

- **Symptoms**: [How to recognize this error]
- **Causes**: [What causes this error]
- **Resolution**: [How to fix it]
- **Prevention**: [How to avoid it]

### Rollback Procedures

#### Partial Rollback

- [Step 1: how to undo recent changes]
- [Step 2: how to restore previous state]
- [Step 3: how to verify rollback success]

#### Full Rollback

- [Step 1: how to undo all changes]
- [Step 2: how to restore original state]
- [Step 3: how to verify full rollback]

### Abort Procedures

- [Step 1: how to safely stop the process]
- [Step 2: how to preserve any completed work]
- [Step 3: how to notify stakeholders]

## Quality Checks

### Pre-Execution

- [ ] All preconditions met
- [ ] Required access confirmed
- [ ] Resources available
- [ ] Backup/rollback plan ready

### During Execution

- [ ] Each step validated before proceeding
- [ ] Approval gates respected
- [ ] Error conditions monitored

### Post-Execution

- [ ] All success criteria met
- [ ] Deliverables produced and validated
- [ ] Cleanup completed
- [ ] Documentation updated

## Variations

### Variation 1: [Scenario]

- **When to Use**: [Specific conditions]
- **Changes**: [How steps differ]
- **Additional Considerations**: [Extra factors]

### Variation 2: [Scenario]

- **When to Use**: [Specific conditions]
- **Changes**: [How steps differ]
- **Additional Considerations**: [Extra factors]

## Related Documents

- [Related Playbook 1]
- [Related Role Card 1]
- [Related Context Pack 1]
- [Related ADR 1]

## Version History

- **v0.1.0** (YYYY-MM-DD): Initial version
- **v0.2.0** (YYYY-MM-DD): [Changes made]

## Notes

[Any additional notes about usage, limitations, or special considerations]