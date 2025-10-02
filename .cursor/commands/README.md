# Cursor Commands

This directory contains custom Cursor commands for the withco-general repository.

## Available Commands

### `/sync-help`

Automated git synchronization command that handles the complete process of reviewing changes, managing merges, and syncing with remote repositories.

**Usage:**

```bash
/sync-help
```

**What it does:**

1. **Repository Assessment** - Checks current git status and branch divergence
2. **Change Review** - Reviews all modified and untracked files
3. **Safety Checks** - Verifies no unauthorized operations
4. **Merge Process** - Handles remote pulls and conflict resolution
5. **Commit & Push** - Commits changes and pushes to remote
6. **Cleanup** - Removes temporary files and shows final status

**Features:**

- ✅ Automatic conflict resolution for simple cases
- ✅ Safety boundary enforcement
- ✅ Comprehensive status reporting
- ✅ Emergency stops for unauthorized operations
- ✅ Cleanup of backup files

**Example Output:**

```
🔄 Starting /sync-help command...
[INFO] 🔍 Assessing repository state...
[INFO] 📋 Reviewing changes...
[SUCCESS] Safety checks passed
[INFO] 🚀 Starting sync process...
[SUCCESS] Successfully committed changes
[SUCCESS] Successfully pushed to remote
[SUCCESS] 🎉 Sync process completed successfully!
```

## Command Files

- `sync-help.md` - Command documentation and specification
- `sync-help.sh` - Executable script implementation
- `sync-help-impl.md` - Implementation details and usage examples

## Safety Features

The `/sync-help` command includes multiple safety mechanisms:

- **Automatic Resolution**: Handles simple conflicts (capitalization, whitespace)
- **User Intervention**: Flags complex conflicts requiring manual review
- **Emergency Stops**: Prevents unauthorized Linear operations
- **Audit Trail**: Logs all operations for compliance

## Integration

- Works with existing git workflow
- Integrates with Cursor IDE
- Maintains compatibility with background agents
- Preserves audit trail for compliance

## Maintenance

Commands are maintained alongside the repository and updated as needed for:

- Git workflow changes
- Enhanced conflict resolution
- Improved safety checks
- Better user communication
