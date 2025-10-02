#!/bin/bash
# fix-markdown.sh - Comprehensive markdown fixing script

set -e

echo "🔧 Starting comprehensive markdown fixing process..."

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

# Check if markdownlint is installed
if ! command -v markdownlint &> /dev/null; then
    print_error "markdownlint is not installed. Please run: npm install -g markdownlint-cli"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f ".markdownlint.json" ]; then
    print_error "No .markdownlint.json found. Please run this script from the repository root."
    exit 1
fi

print_status "Running markdownlint with auto-fix..."
if markdownlint --fix .; then
    print_success "markdownlint auto-fix completed successfully"
else
    print_warning "markdownlint found issues that couldn't be auto-fixed"
fi

print_status "Running custom markdown link validation..."
if python3 scripts/check_markdown_links.py; then
    print_success "All markdown links are valid"
else
    print_warning "Some markdown links are broken - check output above"
fi

print_status "Running ISO timestamp validation..."
if python3 scripts/validate_iso_timestamps.py docs; then
    print_success "All ISO timestamps are valid"
else
    print_warning "Some ISO timestamps are invalid - check output above"
fi

print_status "Running agent rules synchronization check..."
if python3 scripts/sync_agents_rules.py --check; then
    print_success "Agent rules are synchronized"
else
    print_warning "Agent rules need synchronization - check output above"
fi

# Show remaining issues
print_status "Checking for remaining markdownlint issues..."
REMAINING_ISSUES=$(markdownlint . 2>&1 | wc -l)
if [ "$REMAINING_ISSUES" -gt 0 ]; then
    print_warning "Found $REMAINING_ISSUES remaining markdownlint issues:"
    echo ""
    markdownlint . | head -20
    if [ "$REMAINING_ISSUES" -gt 20 ]; then
        echo "... and $((REMAINING_ISSUES - 20)) more issues"
    fi
    echo ""
    print_status "To see all issues: markdownlint ."
    print_status "To fix manually: edit files and run 'markdownlint --fix .'"
else
    print_success "No remaining markdownlint issues found!"
fi

# Summary
echo ""
print_status "📋 Summary:"
echo "  ✅ markdownlint auto-fix completed"
echo "  ✅ Custom validations completed"
echo "  📊 Check output above for any warnings or errors"
echo ""
print_status "Next steps:"
echo "  1. Review any warnings above"
echo "  2. Fix remaining issues manually if needed"
echo "  3. Run 'pre-commit install' to enable pre-commit hooks"
echo "  4. Install markdownlint VS Code extension for real-time feedback"
echo ""
print_success "Markdown fixing process completed!"
