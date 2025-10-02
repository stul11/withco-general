# Custom Markdown Rules for WithCo Project

## Project-Specific Markdown Standards

### 1. Front Matter Requirements

All markdown files in `docs/agents/session-notes/` must include:

```yaml
---
id: SN_YYYYMMDD_task-name
title: Descriptive Title
version: 1.0.0
created: YYYY-MM-DDTHH:MM:SSZ
updated: YYYY-MM-DDTHH:MM:SSZ
owner: username
status: Active|Draft|Archived
tags: [tag1, tag2, tag3]
---
```

### 2. File Naming Conventions

- **Session Notes**: `SN_YYYYMMDD_task-name.md`
- **Templates**: `Template_Name.md`
- **Workflows**: `Workflow_Name.md`
- **PRDs**: `PREFIX-PRD_Name.md`
- **Tickets**: `PREFIX-TKT_Name.md`

### 3. Heading Structure

- Use ATX headers (# ## ###)
- Only one H1 per document
- Consistent hierarchy (H1 → H2 → H3)
- Descriptive headings (not generic like "Overview")

### 4. Link Standards

- Use descriptive link text
- Prefer relative links for internal documents
- Include `.md` extension for markdown files
- Use anchor links for sections: `[text](#section-name)`

### 5. Code Block Standards

- Always specify language for fenced code blocks
- Use proper indentation (2 spaces)
- Include comments for complex code
- Use consistent formatting

### 6. List Standards

- Use consistent indentation (2 spaces)
- Use dashes (-) for unordered lists
- Use sequential numbering (1, 2, 3) for ordered lists
- Include blank lines between list items when needed

### 7. Table Standards

- Use proper alignment
- Include headers
- Keep tables narrow (consider breaking into multiple tables)
- Use consistent formatting

### 8. Special Content Types

#### Session Notes

- Must include all required sections per template
- Use consistent section ordering
- Include proper citations and references

#### Templates

- Include front matter with template metadata
- Use placeholder text in brackets: `[Placeholder]`
- Include usage instructions

#### Workflows

- Include mermaid diagrams where appropriate
- Use step-by-step instructions
- Include error handling and troubleshooting

### 9. Line Length and Formatting

- Maximum 120 characters per line
- Use soft wraps for long URLs
- Break long sentences appropriately
- Maintain readability

### 10. Project-Specific Terms

Use consistent terminology:

- "Session NOTE" (not "Session NOTE")
- "TODO Log" (not "TODO Log")
- "Decision Docket" (not "Decision Log")
- "Background Agent" (not "background agent")

### 11. Validation Requirements

All markdown files must pass:

- markdownlint validation
- Link validation (scripts/check_markdown_links.py)
- ISO timestamp validation (scripts/validate_iso_timestamps.py)
- Agent rules synchronization (scripts/sync_agents_rules.py)

### 12. Exceptions and Overrides

Some files may have intentional formatting that conflicts with rules:

- `docs/raw/docs/fee_examples.md` - Contains long data lines
- `docs/raw/economics-cost-structure-initial-context.md` - Contains long URLs
- Template files - May use placeholder formatting

Use `.markdownlintignore` for files that need exceptions.

### 13. Integration Requirements

- Pre-commit hooks must pass
- CI/CD pipeline must pass
- VS Code extension should be installed
- Team members should use consistent settings

### 14. Maintenance

- Regular review of markdown standards
- Update rules based on team feedback
- Monitor linting results and adjust rules
- Keep documentation current
