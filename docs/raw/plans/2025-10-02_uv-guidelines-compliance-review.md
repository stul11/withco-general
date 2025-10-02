<!-- Generative Planning Mode activated per docs/raw/plans/AGENTS.md -->

## Title: Repository-wide uv Compliance Review Plan

### Goals

- Ensure the entire repository complies with the rule to use `uv` exclusively for Python dependency management
- Eliminate `pip`, `pip-tools`, and `poetry` usage in code, scripts, CI, and docs
- Preserve developer ergonomics and backward compatibility for existing scripts and workflows

### Scope

- File types: `.py`, `.sh`, `.md`, `.yml`/`.yaml` (CI), `Makefile`, `Dockerfile*`
- Key locations: `scripts/`, `.cursor/`, `docs/`, `.github/workflows/`, top-level files (e.g., `requirements.txt`, `pyproject.toml`)

### Inventory & Current State (to be validated)

- `scripts/requirements.txt` exists (added previously for contributors)
- No known `pyproject.toml` or `uv.lock` tracked yet
- Inline script metadata may be applicable for lightweight scripts

### Compliance Definition

- All Python dependency operations use `uv` commands
- If project-level deps are needed: prefer `pyproject.toml` + `uv.lock`
- If script-scoped deps are sufficient: use uv script metadata blocks or `uv add --script`
- CI and docs reference `uv` (not `pip`, `poetry`, `pip-tools`)

### Detection Plan (searches)

Run these repo scans and catalog results (paths + line refs):

```bash
# 1) Anti-pattern detection
rg -n "\b(pip|pip3)\b" --glob '!**/.venv/**' --glob '!**/.git/**'
rg -n "pip(-)?tools|poetry" --glob '!**/.venv/**' --glob '!**/.git/**'
rg -n "pip install|pip3 install" --glob '!**/.venv/**' --glob '!**/.git/**'

# 2) Dependency files and workflow references
rg -n "requirements\.txt|requirements/|constraints\.txt" \
  --glob '!**/.venv/**' --glob '!**/.git/**'
rg -n "pyproject\.toml|uv\.lock|uv add|uv remove|uv sync|uv run" \
  --glob '!**/.venv/**' --glob '!**/.git/**'

# 3) Subprocess usage that shells out to pip/poetry
rg -n "subprocess\.run\(.*(pip|poetry)" --type py
```

For each hit, classify as: code, docs, CI, or legacy artifact. Create a remediation entry.

### Migration Strategy Options

- Option A (Recommended): Project-level uv

  - Introduce `pyproject.toml` and `uv.lock` in repo root
  - Manage shared tools via `uv add` (e.g., `pyyaml` for scripts)
  - Update scripts/docs/CI to use `uv run` and `uv sync`

- Option B (Transitional): Script-scoped uv only

  - Keep `requirements.txt` temporarily (read-only) for reference
  - Add per-script metadata blocks and use `uv add --script`
  - Later promote to project-level `pyproject.toml`

- Option C (Minimal): Docs-only enforcement
  - Update docs/CI references to `uv` but do not add `pyproject.toml`
  - Rely solely on `uv run` with ephemeral environments

### Recommendation

- Adopt Option A (Project-level uv) for consistency and reproducibility
- Allow Option B for utility scripts that are intentionally isolated

### Backward Compatibility Considerations

- Preserve developer workflows by documenting `uv sync` equivalents for `pip install -r requirements.txt`
- Keep `requirements.txt` (if present) as a generated artifact or deprecate with a clear notice
- Ensure CI caches `uv` appropriately to maintain build performance

### Remediation Steps (Phased)

1. Analysis

   - Run searches above; produce a hit list with categories and priorities

2. Core Setup

   - Create `pyproject.toml` with minimal metadata and required tools
   - Run `uv add` to record first-party tool deps; commit `uv.lock`

3. Code & Script Updates

   - Replace `pip`/`poetry` shells with `uv` in Python and shell scripts
   - Add script metadata blocks where appropriate; otherwise use `uv run`

4. Docs & CI Updates

   - Update all `.md` and workflow `.yml` references to `uv`
   - Add a CI job to verify exclusive `uv` usage (regex scan)

5. Transitional Policy

   - If `requirements.txt` remains, mark as generated and point to `uv export`
   - Document migration in `docs/global/` and link from Decision Docket

6. Validation
   - Re-run scans; zero remaining `pip`/`poetry` usages outside historical notes
   - Execute link and timestamp validators; fix any issues

### CI Enhancements

- Add a job to fail if `pip install`/`poetry` appears in modified files
- Cache uv downloads and `~/.cache/uv` for speed

### Risk & Mitigation

- Risk: Contributors unfamiliar with `uv` → Mitigation: concise README section + examples
- Risk: Hidden `pip` calls in legacy scripts → Mitigation: regex scan in CI + code review checklist
- Risk: Environment mismatch → Mitigation: pin via `uv.lock` or script metadata

### Deliverables

- `.cursor/rules/uv-guidelines.mdc` (done)
- `docs/raw/plans/2025-10-02_uv-guidelines-compliance-review.md` (this doc)
- Proposed `pyproject.toml` + `uv.lock` (future PR)
- Updated CI config and developer docs (future PR)

### Timeline (Draft)

- Day 0–1: Analysis and proposal
- Day 2–3: PR with `pyproject.toml`, initial script/docs updates
- Day 4–5: CI policy, final sweep, approve and merge

### Ownership

- Owner: `slittle`
- Implementation support: Agent sessions as needed

### Backout Plan

- If issues arise, revert to pre-uv state via git; maintain `requirements.txt` reference for emergency install
