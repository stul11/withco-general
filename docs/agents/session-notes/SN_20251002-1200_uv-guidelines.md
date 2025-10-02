---
type: session-NOTE
created: 2025-10-02T12:00:00Z
updated: 2025-10-02T12:00:00Z
owner: slittle
tags: [uv, dependencies, python]
---

# Session NOTE

- **Task ID**: uv-guidelines
- **Agent**: GPT-5
- **Owner**: slittle
- **Date**: 2025-10-02T12:00:00Z
- **Duration**: ~45 minutes

---

## Inputs & Context

- **Key Documents/Files Provided**:
  - `.cursor/commands/offboard.md`
  - `.cursor/rules/agent-session-notes.mdc`
  - `.cursor/rules/agent-chat-commands.mdc`
  - `docs/global/Decision_Docket.md`
  - `docs/global/TODO_Log.md`
  - `docs/raw/plans/2025-10-02_uv-guidelines-compliance-review.md`
  - `scripts/hhmm_round.py`
- **Context & Requirements**:
  - Add a Cursor rule enforcing `uv` as the exclusive Python dependency manager
  - Produce a repository-wide compliance review plan with backward compatibility
  - Offboard the session per `/offboard` checklist
- **Relevant Prior Work**:
  - Session notes and rules around agent offboarding and session note requirements

---

## Full Findings

- **Summary of Findings**:
  - No `pyproject.toml` or `uv.lock` currently in the repo
  - Existing pip references found in contributor documentation and a `requirements.txt`
  - No existing `uv` usage in docs/CI detected yet
- **Detailed Findings**:
  - **Description**: PIP install instructions present in contributor docs
    - **File(s) Involved**: `scripts/README.md`
    - **Line Numbers/Sections**: L31-L36, L60-L61
    - **Reasoning**: Instructs users to install via `pip`, conflicting with `uv`-only rule
    - **Supporting Evidence**: `pip install pyyaml`; `pip install -r requirements.txt`
  - **Description**: PIP instructions found inside `requirements.txt`
    - **File(s) Involved**: `requirements.txt`
    - **Line Numbers/Sections**: L31-L36
    - **Reasoning**: Encourages `pip install`, should be replaced or marked generated with `uv` guidance
    - **Supporting Evidence**: Inline examples referencing `pip`
  - **Description**: No `pyproject.toml`/`uv.lock`
    - **File(s) Involved**: N/A (missing files)
    - **Reasoning**: Indicates project-level dependency management not yet set up for `uv`

---

## Steps Taken

- **Major Actions**:
  - Added rule: `.cursor/rules/uv-guidelines.mdc`
  - Authored plan: `docs/raw/plans/2025-10-02_uv-guidelines-compliance-review.md`
  - Searched repo for `pip`/`poetry` occurrences and inventoried hits
  - Prepared updates to Decision Docket and TODO Log
  - Created this Session NOTE and ran validations
- **Key Decisions**:
  - Recommend project-level `uv` adoption with `pyproject.toml` + `uv.lock` (allow script-scoped as transitional)
- **Tools/Methods Used**:
  - Semantic and regex searches; repository documentation review

---

## Outputs

- **Files Created/Modified**:
  - `.cursor/rules/uv-guidelines.mdc` (new): Added `uv` dependency management rule
  - `docs/raw/plans/2025-10-02_uv-guidelines-compliance-review.md` (new): Compliance review plan
  - `docs/agents/session-notes/SN_20251002-1200_uv-guidelines.md` (new): This note
  - `docs/global/Decision_Docket.md` (modified): Added `uv` adoption decision
  - `docs/global/TODO_Log.md` (modified): Logged completed tasks and follow-ups
- **Key Deliverables**:
  - Codified `uv` usage policy and review plan
- **Documented Decisions**:
  - Decision Docket updated with `uv` adoption rationale and links

---

## Citations

- `scripts/README.md:L31-L36`
- `scripts/README.md:L60-L61`
- `requirements.txt:L31-L36`
- `.cursor/commands/offboard.md`
- `.cursor/rules/agent-session-notes.mdc`

---

## Risks & Issues Identified

- Potential confusion for contributors accustomed to `pip`
- Hidden `pip` usage in scripts or CI could be missed initially
- CI performance considerations for first-time `uv` setup

---

## Reasoning & Rationale

- `uv` provides a unified, reproducible workflow for dependency management
- A staged migration minimizes disruption: plan first, introduce `pyproject.toml`, then update docs/CI
- CI guardrails ensure long-term compliance

---

## Next Actions

- Create `pyproject.toml` and initialize `uv.lock` with core tools (`pyyaml`, `pre-commit`, test deps as needed)
- Replace `pip` references in `scripts/README.md` and clarify `requirements.txt` status (generated/deprecated)
- Add CI checks to prevent `pip`/`poetry` usage and to encourage `uv`
- Document developer quickstart with `uv` equivalents

---

## Signoff

- **Reviewer**: slittle
- **Status**: pending
- **Date**: 2025-10-02T12:00:00Z
- **Notes**: Please approve the policy and plan; implementation PRs to follow
