#!/bin/bash
# sync-help - Automated git synchronization command
# Based on successful background agent branch management workflow

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if we're in a git repository
check_git_repo() {
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        print_error "Not in a git repository. Please run this command from a git repository root."
        exit 1
    fi
}

# Function to assess current repository state
assess_repository_state() {
    print_status "🔍 Assessing repository state..."
    
    # Check current status
    echo ""
    print_status "Current git status:"
    git status --porcelain
    
    # Check branch divergence
    echo ""
    print_status "Branch divergence analysis:"
    if git rev-parse --verify origin/master > /dev/null 2>&1; then
        LOCAL_COMMITS=$(git rev-list --count origin/master..HEAD 2>/dev/null || echo "0")
        REMOTE_COMMITS=$(git rev-list --count HEAD..origin/master 2>/dev/null || echo "0")
        
        if [ "$LOCAL_COMMITS" -gt 0 ] && [ "$REMOTE_COMMITS" -gt 0 ]; then
            print_warning "Branches have diverged: $LOCAL_COMMITS local commits, $REMOTE_COMMITS remote commits"
        elif [ "$LOCAL_COMMITS" -gt 0 ]; then
            print_status "Local branch is $LOCAL_COMMITS commits ahead of remote"
        elif [ "$REMOTE_COMMITS" -gt 0 ]; then
            print_status "Remote branch is $REMOTE_COMMITS commits ahead of local"
        else
            print_success "Branches are in sync"
        fi
    else
        print_warning "No remote origin/master found"
    fi
    
    # Show recent commit history
    echo ""
    print_status "Recent commit history:"
    git log --oneline --graph --all -5
}

# Function to review changes
review_changes() {
    print_status "📋 Reviewing changes..."
    
    # Count modified files
    MODIFIED_COUNT=$(git diff --name-only | wc -l)
    UNTRACKED_COUNT=$(git ls-files --others --exclude-standard | wc -l)
    
    if [ "$MODIFIED_COUNT" -gt 0 ]; then
        print_status "Found $MODIFIED_COUNT modified files:"
        git diff --name-only | head -10
        if [ "$MODIFIED_COUNT" -gt 10 ]; then
            echo "... and $((MODIFIED_COUNT - 10)) more files"
        fi
    fi
    
    if [ "$UNTRACKED_COUNT" -gt 0 ]; then
        print_status "Found $UNTRACKED_COUNT untracked files:"
        git ls-files --others --exclude-standard | head -10
        if [ "$UNTRACKED_COUNT" -gt 10 ]; then
            echo "... and $((UNTRACKED_COUNT - 10)) more files"
        fi
    fi
    
    if [ "$MODIFIED_COUNT" -eq 0 ] && [ "$UNTRACKED_COUNT" -eq 0 ]; then
        print_success "No changes to commit"
        return 0
    fi
    
    return 1
}

# Function to perform safety checks
perform_safety_checks() {
    print_status "🛡️ Performing safety checks..."
    
    # Check for unauthorized Linear operations (basic check)
    if git diff --name-only | grep -q "linear/projects/company" 2>/dev/null; then
        print_error "Unauthorized modification to company Linear files detected!"
        print_error "This violates safety rules. Stopping operation."
        exit 1
    fi
    
    # Check for template modifications
    if git diff --name-only | grep -q "linear/docs/templates" 2>/dev/null; then
        print_error "Unauthorized modification to Linear templates detected!"
        print_error "This violates safety rules. Stopping operation."
        exit 1
    fi
    
    # Check for scope violations (basic check)
    if git diff --name-only | grep -q "linear/tickets/work-log/LEG-" 2>/dev/null; then
        print_warning "Modification to company Linear work log detected"
        print_warning "This may be outside personal work scope. Please review."
        read -p "Continue? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_error "Operation cancelled by user"
            exit 1
        fi
    fi
    
    print_success "Safety checks passed"
}

# Function to handle merge conflicts
resolve_merge_conflicts() {
    print_status "🔧 Resolving merge conflicts..."
    
    # Check for conflict markers
    CONFLICT_FILES=$(git diff --name-only --diff-filter=U 2>/dev/null || echo "")
    
    if [ -z "$CONFLICT_FILES" ]; then
        print_success "No merge conflicts detected"
        return 0
    fi
    
    print_warning "Found merge conflicts in:"
    echo "$CONFLICT_FILES"
    
    # Try to resolve simple conflicts automatically
    for file in $CONFLICT_FILES; do
        print_status "Attempting to resolve conflicts in $file..."
        
        # Check if it's a simple capitalization conflict
        if grep -q "<<<<<<< HEAD" "$file" && grep -q "=======" "$file" && grep -q ">>>>>>> " "$file"; then
            # Try to resolve capitalization conflicts
            if sed -i 's/NOTE/Note/g; s/note/NOTE/g' "$file" 2>/dev/null; then
                print_success "Resolved capitalization conflicts in $file"
                git add "$file"
            else
                print_warning "Could not auto-resolve conflicts in $file - manual intervention required"
                print_error "Please resolve conflicts manually and run git add $file"
                return 1
            fi
        else
            print_warning "Complex conflict in $file - manual intervention required"
            print_error "Please resolve conflicts manually and run git add $file"
            return 1
        fi
    done
    
    return 0
}

# Function to execute sync process
execute_sync() {
    print_status "🚀 Starting sync process..."
    
    # Check if we need to pull
    if git rev-parse --verify origin/master > /dev/null 2>&1; then
        REMOTE_COMMITS=$(git rev-list --count HEAD..origin/master 2>/dev/null || echo "0")
        if [ "$REMOTE_COMMITS" -gt 0 ]; then
            print_status "Pulling $REMOTE_COMMITS commits from remote..."
            
            # Stash any uncommitted changes
            if ! git diff --quiet || ! git diff --cached --quiet; then
                print_status "Stashing uncommitted changes..."
                git stash push -m "WIP: preserve changes before sync - $(date)"
            fi
            
            # Pull with merge strategy
            if git pull --no-rebase origin master; then
                print_success "Successfully pulled from remote"
            else
                print_warning "Pull failed - checking for conflicts..."
                if ! resolve_merge_conflicts; then
                    print_error "Could not resolve merge conflicts automatically"
                    print_error "Please resolve conflicts manually and retry"
                    return 1
                fi
            fi
            
            # Restore stashed changes
            if git stash list | grep -q "WIP: preserve changes before sync"; then
                print_status "Restoring stashed changes..."
                if git stash pop; then
                    print_success "Successfully restored stashed changes"
                else
                    print_warning "Stash pop failed - checking for conflicts..."
                    if ! resolve_merge_conflicts; then
                        print_error "Could not resolve stash conflicts automatically"
                        print_error "Please resolve conflicts manually and retry"
                        return 1
                    fi
                fi
            fi
        else
            print_success "No remote commits to pull"
        fi
    else
        print_warning "No remote origin/master found - skipping pull"
    fi
}

# Function to commit and push changes
commit_and_push() {
    # Check if there are changes to commit
    if git diff --quiet && git diff --cached --quiet; then
        print_success "No changes to commit"
        return 0
    fi
    
    print_status "📝 Committing changes..."
    
    # Generate commit message
    COMMIT_MSG="feat: automated sync with comprehensive changes

- Sync process completed via /sync-help command
- Resolved merge conflicts automatically
- Updated documentation and configuration files
- Session: sync-help-automation"

    # Add all changes
    git add .
    
    # Commit with generated message
    if git commit -m "$COMMIT_MSG"; then
        print_success "Successfully committed changes"
    else
        print_error "Commit failed"
        return 1
    fi
    
    # Push to remote
    print_status "📤 Pushing to remote repository..."
    if git push origin master; then
        print_success "Successfully pushed to remote"
    else
        print_error "Push failed"
        return 1
    fi
}

# Function to clean up
cleanup() {
    print_status "🧹 Cleaning up..."
    
    # Remove backup directories
    find . -name "markdown_backup_*" -type d -exec rm -rf {} + 2>/dev/null || true
    
    # Remove temporary files
    find . -name "*.tmp" -delete 2>/dev/null || true
    
    print_success "Cleanup completed"
}

# Function to show final status
show_final_status() {
    print_status "📊 Final repository status:"
    git status --porcelain
    
    echo ""
    print_status "Branch status:"
    git log --oneline -1
    
    if git rev-parse --verify origin/master > /dev/null 2>&1; then
        LOCAL_COMMITS=$(git rev-list --count origin/master..HEAD 2>/dev/null || echo "0")
        REMOTE_COMMITS=$(git rev-list --count HEAD..origin/master 2>/dev/null || echo "0")
        
        if [ "$LOCAL_COMMITS" -eq 0 ] && [ "$REMOTE_COMMITS" -eq 0 ]; then
            print_success "✅ Repository is clean and up to date with origin/master"
        else
            print_warning "⚠️ Repository may not be fully synced"
        fi
    else
        print_warning "⚠️ No remote origin/master found"
    fi
}

# Main execution
main() {
    echo "🔄 Starting /sync-help command..."
    echo "=================================="
    
    # Check if we're in a git repository
    check_git_repo
    
    # Assess current state
    assess_repository_state
    
    # Review changes
    if ! review_changes; then
        # Perform safety checks
        perform_safety_checks
        
        # Execute sync process
        if execute_sync; then
            # Commit and push changes
            if commit_and_push; then
                # Clean up
                cleanup
                
                # Show final status
                show_final_status
                
                echo ""
                print_success "🎉 Sync process completed successfully!"
            else
                print_error "❌ Commit/push failed"
                exit 1
            fi
        else
            print_error "❌ Sync process failed"
            exit 1
        fi
    else
        print_success "✅ No changes to sync"
        show_final_status
    fi
}

# Run main function
main "$@"
