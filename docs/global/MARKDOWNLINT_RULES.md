# Markdownlint Custom Rules Documentation

## Overview

This document explains the custom markdownlint rules and disable comment usage patterns for the withco-general repository.

## Configuration

The repository uses `.markdownlint.json` with the following key rules:

### Core Rules

- **MD013**: Line length limit of 120 characters (relaxed from default 80)

  - `code_blocks: false` - Don't wrap code blocks
  - `tables: false` - Don't wrap tables
  - `headings: false` - Don't wrap headings
  - `strict: false` - Allow some flexibility

- **MD003**: ATX heading style (`# ## ###`) - consistent across repository
- **MD029**: Ordered list style (1/2/3) - sequential numbering
- **MD046**: Fenced code blocks with language specification
- **MD040**: Require language tags on fenced code blocks
- **MD024**: Duplicate headings (siblings only) - prevent confusion
- **MD033**: No inline HTML - security and consistency
- **MD041**: First line heading requirement (respects front matter titles)

## Disable Comment Patterns

### Template Files

Template files use comprehensive disable comments due to front matter conflicts:

```markdown
<!-- markdownlint-disable MD003 MD022 -->
<!-- markdownlint-disable MD041 -->
<!-- markdownlint-disable MD025 -->
```

**Reasoning**: Templates have both front matter titles AND H1 headings, which violates MD025. Front matter fields are incorrectly parsed as headings, triggering MD003/MD022.

### File-Level Disables

For files with specific needs:

```markdown
<!-- markdownlint-disable MD013 -->
```

**Use when**: File contains long URLs, code examples, or other content that shouldn't be wrapped.

### Line-Level Disables

For specific problematic lines:

```markdown
<!-- markdownlint-disable-next-line MD013 -->

This is a very long line that contains important information that shouldn't be wrapped for readability reasons.
```

**Use when**: Single line exceeds 120 characters but breaking it would harm readability.

### Inline Disables

For specific rules within a section:

```markdown
<!-- markdownlint-disable MD033 -->
<table>
  <tr><td>Complex table</td></tr>
</table>
<!-- markdownlint-enable MD033 -->
```

**Use when**: HTML is necessary for complex formatting that Markdown can't handle.

## Common Scenarios

### Front Matter Documents

Documents with YAML front matter may need:

```markdown
## <!-- markdownlint-disable MD041 -->

## title: Document Title

# Document Title
```

### Code Examples

Long code examples or URLs:

```markdown
<!-- markdownlint-disable-next-line MD013 -->

https://very-long-url-that-exceeds-120-characters.com/path/to/resource?param=value&other=param
```

### Historical Documents

Session notes and historical documents:

```markdown
<!-- markdownlint-disable MD013 MD049 -->

_This section uses underscores for emphasis due to historical formatting_
```

## Best Practices

1. **Prefer content fixes over disables** - Fix the underlying issue when possible
2. **Use specific rule disables** - Don't disable all rules unless necessary
3. **Document reasoning** - Add comments explaining why rules are disabled
4. **Review periodically** - Check if disables are still needed
5. **Template consistency** - Use consistent disable patterns across templates

## Rule Violations Guide

### MD013 (Line Length)

- **Fix**: Break long lines at natural word boundaries
- **Disable**: Only for URLs, code, or when breaking harms readability

### MD025 (Multiple H1)

- **Fix**: Use front matter title OR H1, not both
- **Disable**: For templates that need both (with explanation)

### MD033 (Inline HTML)

- **Fix**: Convert to Markdown equivalents
- **Disable**: For complex tables or when Markdown is insufficient

### MD040 (Code Language)

- **Fix**: Add language tags to code blocks
- **Disable**: Rarely needed - usually indicates missing language

### MD024 (Duplicate Headings)

- **Fix**: Make headings unique or use hierarchical structure
- **Disable**: Only for intentional duplicates (like template examples)

## Integration

- **Pre-commit**: Auto-fixes enabled for local development
- **CI/CD**: Validation only (no auto-fix) for pull requests
- **VS Code**: Real-time linting with extension
- **Scripts**: `scripts/fix-markdown.sh` for comprehensive fixes

## Maintenance

- Review disable comments quarterly
- Update rules based on team feedback
- Monitor CI/CD performance impact
- Document new patterns as they emerge
