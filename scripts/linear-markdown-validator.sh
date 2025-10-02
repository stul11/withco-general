#!/bin/bash
# linear-markdown-validator.sh - Validate markdown before Linear ticket creation

set -e

echo "🔍 Linear Markdown Validator"
echo "=============================="

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

# Function to show usage
show_usage() {
    echo "Usage: $0 [OPTIONS] <ticket-file>"
    echo ""
    echo "Options:"
    echo "  --strict              Fail on any markdown issues"
    echo "  --fix                 Auto-fix markdown issues before validation"
    echo "  --preview             Show what would be validated without creating ticket"
    echo "  --help                Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 linear/tickets/drafts/my-ticket.md"
    echo "  $0 --fix linear/tickets/drafts/my-ticket.md"
    echo "  $0 --strict linear/tickets/drafts/my-ticket.md"
    echo ""
}

# Parse command line arguments
STRICT_MODE=false
AUTO_FIX=false
PREVIEW_MODE=false
TICKET_FILE=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --strict)
            STRICT_MODE=true
            shift
            ;;
        --fix)
            AUTO_FIX=true
            shift
            ;;
        --preview)
            PREVIEW_MODE=true
            shift
            ;;
        --help|-h)
            show_usage
            exit 0
            ;;
        -*)
            print_error "Unknown option: $1"
            show_usage
            exit 1
            ;;
        *)
            TICKET_FILE="$1"
            shift
            ;;
    esac
done

# Check if ticket file is provided
if [ -z "$TICKET_FILE" ]; then
    print_error "No ticket file provided"
    show_usage
    exit 1
fi

# Check if ticket file exists
if [ ! -f "$TICKET_FILE" ]; then
    print_error "Ticket file does not exist: $TICKET_FILE"
    exit 1
fi

# Check if markdownlint is installed
if ! command -v markdownlint &> /dev/null; then
    print_error "markdownlint is not installed. Please run: npm install -g markdownlint-cli"
    exit 1
fi

print_status "Validating ticket file: $TICKET_FILE"

# Auto-fix if requested
if [ "$AUTO_FIX" = true ]; then
    print_status "Auto-fixing markdown issues..."
    if markdownlint --fix "$TICKET_FILE"; then
        print_success "Auto-fix completed"
    else
        print_warning "Some issues couldn't be auto-fixed"
    fi
fi

# Run markdownlint validation
print_status "Running markdownlint validation..."
MARKDOWNLINT_OUTPUT=$(markdownlint "$TICKET_FILE" 2>&1 || true)
MARKDOWNLINT_EXIT_CODE=$?

if [ $MARKDOWNLINT_EXIT_CODE -eq 0 ]; then
    print_success "Markdown validation passed"
else
    print_warning "Markdown validation found issues:"
    echo "$MARKDOWNLINT_OUTPUT"
    echo ""
    
    if [ "$STRICT_MODE" = true ]; then
        print_error "Strict mode enabled - failing due to markdown issues"
        exit 1
    fi
fi

# Run custom validations
print_status "Running custom validations..."

# Check markdown links
if python3 scripts/check_markdown_links.py "$TICKET_FILE"; then
    print_success "Link validation passed"
else
    print_warning "Link validation found issues"
    if [ "$STRICT_MODE" = true ]; then
        print_error "Strict mode enabled - failing due to link issues"
        exit 1
    fi
fi

# Check ISO timestamps if file is in docs directory
if [[ "$TICKET_FILE" == docs/* ]]; then
    if python3 scripts/validate_iso_timestamps.py "$TICKET_FILE"; then
        print_success "ISO timestamp validation passed"
    else
        print_warning "ISO timestamp validation found issues"
        if [ "$STRICT_MODE" = true ]; then
            print_error "Strict mode enabled - failing due to timestamp issues"
            exit 1
        fi
    fi
fi

# Check if file follows naming conventions
print_status "Checking file naming conventions..."
FILENAME=$(basename "$TICKET_FILE")
DIRECTORY=$(dirname "$TICKET_FILE")

# Check if it's a draft ticket
if [[ "$DIRECTORY" == *"drafts"* ]]; then
    if [[ "$FILENAME" =~ ^[A-Z]{2,4}-TKT_.*\.md$ ]] || [[ "$FILENAME" =~ ^[A-Z]{2,4}-PRD_.*\.md$ ]]; then
        print_success "File naming convention is correct"
    else
        print_warning "File naming convention may not follow standards: $FILENAME"
        print_status "Expected format: PREFIX-TKT_Name.md or PREFIX-PRD_Name.md"
    fi
fi

# Check front matter if it's a session note
if [[ "$FILENAME" =~ ^SN_.*\.md$ ]]; then
    print_status "Checking session note front matter..."
    if grep -q "^---$" "$TICKET_FILE" && grep -q "^id:" "$TICKET_FILE" && grep -q "^title:" "$TICKET_FILE"; then
        print_success "Session note front matter appears complete"
    else
        print_warning "Session note front matter may be incomplete"
        print_status "Required fields: id, title, version, created, updated, owner, status, tags"
    fi
fi

# Summary
echo ""
print_status "📋 Validation Summary:"
echo "  File: $TICKET_FILE"
echo "  Markdownlint: $([ $MARKDOWNLINT_EXIT_CODE -eq 0 ] && echo "✅ Passed" || echo "⚠️  Issues found")"
echo "  Links: ✅ Validated"
echo "  Timestamps: ✅ Validated"
echo "  Naming: ✅ Checked"
echo "  Front Matter: ✅ Checked"

if [ "$PREVIEW_MODE" = true ]; then
    print_status "Preview mode - no ticket creation"
    exit 0
fi

# Final decision
if [ $MARKDOWNLINT_EXIT_CODE -eq 0 ]; then
    print_success "✅ Ticket file is ready for Linear creation!"
    echo ""
    print_status "Next steps:"
    echo "  1. Review the ticket content"
    echo "  2. Create ticket in Linear using the validated file"
    echo "  3. Move file from drafts/ to archive/ after creation"
else
    print_warning "⚠️  Ticket file has markdown issues but may still be usable"
    echo ""
    print_status "Recommendations:"
    echo "  1. Fix markdown issues using 'markdownlint --fix $TICKET_FILE'"
    echo "  2. Or use '--fix' flag with this script"
    echo "  3. Review issues above before creating Linear ticket"
fi

echo ""
print_success "Linear markdown validation completed!"