#!/bin/bash
# fix-markdown-staged.sh - Staged markdown fixing by directory

set -e

echo "🔧 Starting staged markdown fixing process..."

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

# Function to fix markdown in a specific directory
fix_directory() {
    local dir="$1"
    local description="$2"
    
    if [ ! -d "$dir" ]; then
        print_warning "Directory $dir does not exist, skipping..."
        return 0
    fi
    
    print_status "Fixing markdown in $description ($dir)..."
    
    # Count files before
    local file_count=$(find "$dir" -name "*.md" -type f | wc -l)
    if [ "$file_count" -eq 0 ]; then
        print_warning "No markdown files found in $dir"
        return 0
    fi
    
    print_status "Found $file_count markdown files in $dir"
    
    # Run markdownlint with auto-fix
    if markdownlint --fix "$dir"; then
        print_success "Auto-fix completed for $description"
    else
        print_warning "Some issues in $description couldn't be auto-fixed"
    fi
    
    # Show remaining issues for this directory
    local remaining=$(markdownlint "$dir" 2>&1 | wc -l)
    if [ "$remaining" -gt 0 ]; then
        print_warning "Found $remaining remaining issues in $description:"
        echo ""
        markdownlint "$dir" | head -10
        if [ "$remaining" -gt 10 ]; then
            echo "... and $((remaining - 10)) more issues"
        fi
        echo ""
    else
        print_success "No remaining issues in $description!"
    fi
    
    echo ""
}

# Function to show usage
show_usage() {
    echo "Usage: $0 [OPTIONS] [DIRECTORY]"
    echo ""
    echo "Options:"
    echo "  --all              Fix all directories in sequence"
    echo "  --docs             Fix docs/ directory"
    echo "  --linear           Fix linear/ directory"
    echo "  --scripts          Fix scripts/ directory"
    echo "  --root             Fix root directory files"
    echo "  --help             Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 --all                    # Fix all directories"
    echo "  $0 --docs                   # Fix only docs/ directory"
    echo "  $0 docs/agents/             # Fix specific subdirectory"
    echo "  $0 README.md                # Fix specific file"
    echo ""
}

# Parse command line arguments
if [ $# -eq 0 ]; then
    show_usage
    exit 1
fi

case "$1" in
    --help|-h)
        show_usage
        exit 0
        ;;
    --all)
        print_status "Running staged fix for all directories..."
        echo ""
        
        # Fix in order of priority/importance
        fix_directory "docs/" "Documentation"
        fix_directory "linear/" "Linear Documentation"
        fix_directory "scripts/" "Scripts"
        fix_directory "." "Root Directory Files"
        
        print_success "Staged fixing completed for all directories!"
        ;;
    --docs)
        fix_directory "docs/" "Documentation"
        ;;
    --linear)
        fix_directory "linear/" "Linear Documentation"
        ;;
    --scripts)
        fix_directory "scripts/" "Scripts"
        ;;
    --root)
        fix_directory "." "Root Directory Files"
        ;;
    *)
        # Treat as directory or file path
        if [ -d "$1" ]; then
            fix_directory "$1" "Custom Directory ($1)"
        elif [ -f "$1" ] && [[ "$1" == *.md ]]; then
            print_status "Fixing specific file: $1"
            if markdownlint --fix "$1"; then
                print_success "Auto-fix completed for $1"
            else
                print_warning "Some issues in $1 couldn't be auto-fixed"
            fi
        else
            print_error "Invalid argument: $1"
            show_usage
            exit 1
        fi
        ;;
esac

# Run custom validations after fixing
print_status "Running custom validations..."
echo ""

print_status "Running markdown link validation..."
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

# Summary
echo ""
print_status "📋 Summary:"
echo "  ✅ Staged markdown fixing completed"
echo "  ✅ Custom validations completed"
echo "  📊 Check output above for any warnings or errors"
echo ""
print_status "Next steps:"
echo "  1. Review any warnings above"
echo "  2. Use 'markdownlint <directory>' to check specific areas"
echo "  3. Use 'markdownlint --fix <directory>' to fix specific areas"
echo "  4. Run './scripts/fix-markdown-staged.sh --all' to fix all directories"
echo ""
print_success "Staged markdown fixing process completed!"