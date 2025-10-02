# Sync Help Command

## Overview

Automated git synchronization command that handles the complete process of reviewing changes, managing merges, and syncing with remote repositories. Based on the successful background agent branch management workflow.

## Usage

```
/sync-help
```

## Process Flow

### 1. Pre-Operation Assessment

- Check current repository status
- View all branches (local and remote)
- Visualize divergence with git log
- Check what commits are ahead/behind

### 2. Change Review

- Review all modified files
- Identify untracked files
- Assess scope of changes
- Flag any potentially problematic changes

### 3. Safety Checks

- Verify no unauthorized Linear operations
- Confirm changes are within allowed scope
- Check for template modifications
- Validate file paths are allowed

### 4. Merge Strategy Execution

- Stash uncommitted changes with descriptive message
- Pull with merge strategy (--no-rebase)
- Handle merge conflicts automatically when possible
- Restore stashed changes

### 5. Conflict Resolution

- Resolve simple conflicts (capitalization, whitespace)
- Flag complex conflicts for user review
- Add resolved files to staging
- Complete merge commit

### 6. Final Commit and Push

- Commit all changes with descriptive message
- Push to remote repository
- Verify final sync status
- Clean up temporary files

## Safety Mechanisms

### Automatic Resolution

- Capitalization conflicts (NOTE vs NOTE)
- Whitespace differences
- Simple formatting conflicts
- Backup file cleanup

### User Intervention Required

- Complex merge conflicts requiring manual review
- Unauthorized file modifications
- Template changes to company Linear files
- Scope violations outside personal work

### Emergency Stops

- Unauthorized Linear writes detected
- Company Linear template modifications
- Safety rule violations
- Critical file conflicts

## Output Format

### Status Updates

- Current git status
- Branch divergence analysis
- Change summary
- Conflict resolution progress

### Success Indicators

- ✅ Repository is clean
- ✅ Branch is up to date with origin/master
- ✅ All conflicts resolved and committed
- ✅ Changes pushed successfully

### Warning Conditions

- ⚠️ Complex conflicts requiring review
- ⚠️ Scope boundary approached
- ⚠️ Multiple safety check failures

### Error Conditions

- ❌ Safety violation detected
- ❌ Unauthorized operations attempted
- ❌ Critical conflicts unresolved

## Implementation Guidelines

### Defensive Programming

- Always verify safety before operations
- Default to safe operations when in doubt
- Maintain complete audit trail
- Get explicit approval for risky operations

### Error Prevention

- Pre-operation safety checks
- Post-operation verification
- Continuous monitoring
- Immediate response to violations

### User Communication

- Clear progress updates
- Transparent operation explanations
- Risk assessment communication
- Recovery options provided

## Expected Behavior

### Normal Operation

1. **Assessment**: "Checking repository status and branch divergence..."
2. **Review**: "Reviewing X modified files and Y untracked files..."
3. **Safety**: "Performing safety checks... ✅ All checks passed"
4. **Merge**: "Stashing changes and pulling from remote..."
5. **Resolve**: "Resolving merge conflicts... ✅ X conflicts resolved"
6. **Commit**: "Committing changes with message: [descriptive]"
7. **Push**: "Pushing to remote repository... ✅ Success"
8. **Cleanup**: "Cleaning up temporary files... ✅ Complete"

### Warning Scenarios

- "⚠️ Complex conflict detected in [file] - requires manual review"
- "⚠️ Scope boundary approached - changes outside personal work detected"
- "⚠️ Multiple safety check failures - proceeding with caution"

### Error Scenarios

- "❌ Safety violation detected - stopping all operations"
- "❌ Unauthorized Linear write attempted - immediate stop"
- "❌ Critical conflict unresolved - manual intervention required"

## Recovery Procedures

### If Process Fails

1. **Immediate Stop**: Halt all operations
2. **Error Logging**: Record failure details
3. **User Notification**: Alert user of issues
4. **Recovery Plan**: Develop plan to restore state

### Rollback Options

1. **Git Reset**: Return to previous commit
2. **Stash Recovery**: Restore from stash
3. **Manual Resolution**: Guide user through conflicts
4. **Fresh Start**: Clean slate approach

## Integration Points

### Background Agent Workflow

- Follows established branch management procedures
- Maintains compatibility with existing workflows
- Preserves audit trail for compliance
- Integrates with safety monitoring

### File System Operations

- Respects .gitignore rules
- Handles symlinks appropriately
- Manages backup files correctly
- Preserves file permissions

### IDE Integration

- Works with Cursor environment
- Maintains workspace state
- Preserves open file context
- Integrates with VS Code settings

## Testing and Validation

### Positive Test Cases

- Clean repository sync
- Simple merge conflicts
- Standard file modifications
- Normal workflow completion

### Edge Cases

- Empty repository state
- No remote changes
- All-local changes
- Complex branch structures

### Error Conditions

- Network failures
- Permission issues
- Corrupted repository state
- Conflicting operations

## Maintenance

### Regular Updates

- Monitor git workflow changes
- Update conflict resolution patterns
- Enhance safety checks
- Improve user communication

### Performance Optimization

- Minimize git operations
- Optimize conflict detection
- Streamline resolution process
- Reduce user wait time

## Documentation Requirements

### User Documentation

- Clear usage instructions
- Expected behavior description
- Troubleshooting guide
- Recovery procedures

### Technical Documentation

- Implementation details
- Safety mechanisms
- Error handling
- Integration points

## Compliance

### Safety Rules

- Follow background agent safety rules
- Maintain Linear operation boundaries
- Preserve file system access controls
- Respect operational scope limits

### Audit Requirements

- Log all operations
- Record safety check results
- Document conflict resolutions
- Maintain change history

## Success Metrics

### Performance Indicators

- Successful sync completion rate
- Conflict resolution success rate
- User intervention frequency
- Process completion time

### Quality Metrics

- Safety violation frequency
- Error recovery success rate
- User satisfaction scores
- Process reliability measures

---

**NOTE**: This command automates the git synchronization process while maintaining safety boundaries and providing clear feedback to users. It follows the established background agent branch management workflow and integrates with existing safety mechanisms.
