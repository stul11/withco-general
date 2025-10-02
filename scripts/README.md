# Scripts

This directory contains utility scripts for repository maintenance and automation.

## sync_agents_rules.py

Synchronizes AGENTS.md files from Cursor rule definitions.

### Purpose

This script inspects `.cursor/rules/*.mdc` files, reads the YAML-style front matter to discover the globs that each rule applies to, and renders standardized Markdown guidance snippets into `AGENTS.md` files within the matching directories.

### Usage

```bash
# Generate/update AGENTS.md files
python scripts/sync_agents_rules.py

# Check if workspace is up to date without writing files
python scripts/sync_agents_rules.py --check
```

### Dependencies

- Python 3.6+
- `pyyaml` - for parsing YAML front matter in rule files

### Installation

```bash
# Using uv (preferred)
uv pip install pyyaml

# Need a temporary requirements.txt for legacy tooling?
uv export --format requirements-txt > requirements.txt
pip install -r requirements.txt
rm requirements.txt
```

### How it works

1. Scans `.cursor/rules/` for `.mdc` files
2. Parses YAML front matter to extract `globs` patterns
3. Expands glob patterns to find target directories
4. Generates `AGENTS.md` files with rule-specific guidance
5. Includes manual directory mappings from rule templates

### Generated files

The script generates `AGENTS.md` files in directories matching the glob patterns defined in rule front matter. These files contain:

- A generator header (do not edit manually)
- Agent guidelines organized by rule template
- Standardized guidance for each applicable rule

### Pre-commit integration

This script is integrated into the pre-commit hooks to ensure AGENTS.md files stay synchronized with rule definitions.

### Troubleshooting

- **Missing pyyaml**: Install with `uv pip install pyyaml`
- **Permission errors**: Ensure you have write access to target directories
- **Glob pattern issues**: Check that glob patterns in rule front matter are valid
- **Manual directories**: Some rules include hardcoded directory mappings in addition to glob patterns
