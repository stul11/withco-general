# Sync Help Command Implementation

## Command Definition

```bash
/sync-help
```

## Description

Automated git synchronization command that handles the complete process of reviewing changes, managing merges, and syncing with remote repositories. Based on the successful background agent branch management workflow.

## Implementation

The command executes the script located at `.cursor/commands/sync-help.sh` which performs:

1. **Repository Assessment**

   - Check current git status
   - Analyze branch divergence
   - Review recent commit history

2. **Change Review**

   - Count and list modified files
   - Identify untracked files
   - Assess scope of changes

3. **Safety Checks**

   - Verify no unauthorized Linear operations
   - Check for template modifications
   - Validate scope boundaries

4. **Merge Process**

   - Stash uncommitted changes
   - Pull from remote with merge strategy
   - Resolve conflicts automatically when possible

5. **Commit and Push**

   - Add all changes
   - Commit with descriptive message
   - Push to remote repository

6. **Cleanup**
   - Remove backup files
   - Clean temporary files
   - Show final status

## Safety Features

- **Automatic Resolution**: Handles simple conflicts (capitalization, whitespace)
- **User Intervention**: Flags complex conflicts requiring manual review
- **Emergency Stops**: Prevents unauthorized operations
- **Audit Trail**: Logs all operations for compliance

## Usage Examples

```bash
# Basic usage
/sync-help

# The command will automatically:
# - Review all changes
# - Handle merge conflicts
# - Commit and push changes
# - Provide status updates
```

## Expected Output

```
🔄 Starting /sync-help command...
==================================
[INFO] 🔍 Assessing repository state...
[INFO] 📋 Reviewing changes...
[INFO] 🛡️ Performing safety checks...
[SUCCESS] Safety checks passed
[INFO] 🚀 Starting sync process...
[SUCCESS] Successfully pulled from remote
[INFO] 📝 Committing changes...
[SUCCESS] Successfully committed changes
[INFO] 📤 Pushing to remote repository...
[SUCCESS] Successfully pushed to remote
[INFO] 🧹 Cleaning up...
[SUCCESS] Cleanup completed
[SUCCESS] ✅ Repository is clean and up to date with origin/master
[SUCCESS] 🎉 Sync process completed successfully!
```

## Error Handling

- **Safety Violations**: Immediate stop with error message
- **Complex Conflicts**: Manual intervention required
- **Network Issues**: Graceful failure with retry options
- **Permission Problems**: Clear error messages with solutions

## Integration

- Works with existing git workflow
- Integrates with Cursor IDE
- Maintains compatibility with background agents
- Preserves audit trail for compliance

## Maintenance

- Regular updates for git workflow changes
- Enhanced conflict resolution patterns
- Improved safety checks
- Better user communication
