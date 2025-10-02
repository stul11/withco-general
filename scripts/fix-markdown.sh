#!/bin/bash

# Fix markdown linting issues using markdownlint-cli
# This script runs markdownlint with --fix flag to automatically fix issues

set -e

echo "🔧 Starting markdown linting fixes..."

# Check if markdownlint is installed
if ! command -v markdownlint &> /dev/null; then
    echo "❌ markdownlint-cli is not installed. Please install it first:"
    echo "   npm install -g markdownlint-cli"
    exit 1
fi

# Create backup directory
BACKUP_DIR="markdown_backup_$(date +%Y%m%d_%H%M%S)"
echo "📁 Creating backup in $BACKUP_DIR"
mkdir -p "$BACKUP_DIR"

# Backup all markdown files
find . -name "*.md" -not -path "./node_modules/*" -not -path "./$BACKUP_DIR/*" | while read -r file; do
    cp "$file" "$BACKUP_DIR/"
done

echo "🔍 Running markdownlint to identify issues..."
markdownlint "**/*.md" --config .markdownlint.json || true

echo "🔧 Running markdownlint --fix to automatically fix issues..."
markdownlint "**/*.md" --config .markdownlint.json --fix

echo "✅ Markdown linting fixes completed!"
echo "📁 Original files backed up to: $BACKUP_DIR"
echo ""
echo "🔍 Running final check..."
markdownlint "**/*.md" --config .markdownlint.json || echo "⚠️  Some issues may require manual fixing"

echo ""
echo "📊 Summary:"
echo "   - Backup created: $BACKUP_DIR"
echo "   - Configuration: .markdownlint.json"
echo "   - To restore: cp $BACKUP_DIR/* ."
echo "   - To check remaining issues: markdownlint **/*.md"