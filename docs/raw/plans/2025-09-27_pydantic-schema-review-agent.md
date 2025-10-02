# Plan: Pydantic Schema Review Agent

- Date: 2025-09-27
- Status: Draft

## Objective

Design options for an agent that reviews a Pydantic schema repo (class-by-class, including Enums), identifies classes relevant to a set of user requirements, and recommends whether to include each as precedent in schema design requirements.

## Assumptions & constraints

- Input: a root `schema/` directory or list of files; user provides short natural-language requirements.
- Output: a recommendation table (class/enum → relevance rationale → include? → notes), citations to file paths and line ranges, and an optional summary.
- Human-in-the-loop: No changes to code; agent emits suggestions only.
- Planning-only: No repo mutations; outputs are Markdown.

## Option A — Minimal in-chat agent (no file writes)

- Flow:
  1. User provides requirements text and optionally a subset of paths.
  2. Agent scans file list and summarizes classes/enums, filtering by keyword/semantic relevance.
  3. Agent returns a Markdown table with rationale and citations; user copies results.
- Pros: Zero setup; fastest iteration.
- Cons: No durable output; easy to lose context; weaker reproducibility.
- When to use: Quick one-off assessments.

## Option B — Session NOTE + Recommendation Log (recommended start)

- Flow:
  1. Prepare a Context Pack pointing at `schema/**` and requirements.
  2. Run agent; for each file, extract class/enum signatures and docstrings, compute semantic match to requirements.
  3. Emit: `docs/agents/session-notes/SN_<date>_schema-review.md` with a recommendation table and citations like `path.py:Lx-Ly`.
  4. Update `docs/global/Decision_Docket.md` with a short entry and link to the session NOTE.
- Pros: Lightweight, reproducible, auditable via Session Notes.
- Cons: Manual copy to PRDs later; requires discipline on notes.
- Enhancements: Add a small rule to require citations and the table shape.

## Option C — Structured extraction + scoring

- Flow:
  1. Parse Python files to AST to extract Pydantic BaseModel/Enum nodes, their fields, types, validators.
  2. Build a relevance score per class using: term overlap, embedding similarity of names/docstrings, and field-type matches to requirement keywords (e.g., money, date, identifiers).
  3. Emit two artifacts: a JSONL of scored candidates and a Markdown summary.
- Pros: Higher precision/recall; enables later automation.
- Cons: Requires local tools/runner; more engineering.
- When to use: Medium-long term; when quality must be higher.

## Option D — PRD-aligned outputs

- Flow:
  1. Agent produces a `PRD Appendix` style Markdown file with: Recommended Precedents, Rejected Candidates (with reasons), Open Questions.
  2. Human pastes this into the active PRD.
- Pros: Output is immediately PRD-friendly.
- Cons: Still manual integration.

## Common deliverables (any option)

- Recommendation Table:

| Symbol        | Kind  | File            | Lines | Relevance                  | Include? | Notes                  |
| ------------- | ----- | --------------- | ----- | -------------------------- | -------- | ---------------------- |
| `UserAccount` | Model | schema/user.py  | 10-98 | Strong (fields: email, id) | Yes      | Precedent for identity |
| `Currency`    | Enum  | schema/money.py | 3-12  | Medium                     | Maybe    | Align with FX needs    |

- Citations format: ``start:end:path`
- Summary paragraph noting coverage and gaps.

## Contracts (strict, Option B baseline)

- Inputs:
  - Requirements text (<= 20 lines), optional focus paths.
- Outputs:
  - Session NOTE file path, recommendation table, citations for each row.
  - No code edits, no mass summaries without citations.
- Review:
  - Human owner sign-off required before logging to Decision Docket or PRD appendix.

## Cursor rules to back this agent

- `agent-session-notes.mdc`: require Session NOTE with table and citations before accepting results.
- `agent-artifacts-standard.mdc`: ensure Context Pack references exact files/dirs; ARC defines constraints (read-only).

## Lightweight commands (scaffolding only; not executed)

- Create Context Pack for this task:

```bash
mkdir -p withco-general/docs/agents/context-packs && cat > withco-general/docs/agents/context-packs/CP_pydantic-schema-review.md <<'MD'
# Context Pack: Pydantic Schema Review
Objective: Identify relevant Pydantic models/enums for <project> requirements
## Required Docs
- schema/**
- docs/prds/<active-prd>.md
## Allowed Data
- Allowed: repo files under schema/
- Excluded: secrets, binaries
## Session Boundaries
- Time-box: 45m
- Token scope: minimal
MD
```

- Session NOTE filename suggestion:

```
docs/agents/session-notes/SN_20250927_pydantic-schema-review.md
```

## Recommendation

Start with Option B (Session NOTE + Recommendation Log). If quality or scale demands, evolve toward Option C for structured scoring; keep PRD-friendly appendix output as an optional D.

## Next Steps

- Approve Option B as the initial operating mode.
- Approve creating the two rules above if not already present.
- If approved, I’ll scaffold the Context Pack and a Session NOTE stub and run a dry-run on a small subset of `schema/`.
