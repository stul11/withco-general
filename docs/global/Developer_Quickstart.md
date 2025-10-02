# Developer Quickstart (uv)

Follow this quickstart to set up a local development environment using [`uv`](https://docs.astral.sh/uv/) as the sole Python package manager for the repository.

## 1. Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- The installer adds `uv` to `~/.local/bin`. Ensure that directory is on your `PATH` before continuing.
- If you already have `uv` installed, update it with `uv self update`.

## 2. Create an isolated environment

```bash
uv venv
source .venv/bin/activate  # optional when you prefer an activated shell
```

- `uv venv` creates a project-local virtual environment in `.venv/`. Re-run the command whenever you want a clean environment.
- Activation is optional when you rely on `uv run` or target the env explicitly with `uv pip --python .venv`.
- On Windows, activate with `.\.venv\Scripts\activate`.

## 3. Install repository dependencies

```bash
uv pip install --python .venv pyyaml ruamel.yaml toml pytest pre-commit
```

- This installs the current tooling set (YAML + TOML helpers, pytest, pre-commit) into the `.venv/` created above.
- Avoid `pip install`; the repository expects all contributors and automation to rely on `uv`.

## 4. Bootstrap repo tooling

```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

- `uv run ...` executes commands inside the managed environment without needing to manually activate it.
- Running the full pre-commit suite once ensures your workspace is formatted and validated against current rules.

## 5. Verify the setup

```bash
uv run pytest
uv run python scripts/sync_agents_rules.py --check
```

- `pytest` confirms the Python tooling is installed correctly.
- The sync script check verifies that generated `AGENTS.md` files are in sync with rule definitions.

## 6. Daily workflow tips

- Use `uv run <command>` for all Python-based tooling instead of activating the virtual environment explicitly.
- When adding a new dependency, prefer `uv pip install --python .venv <package>` (or future `uv add` once `pyproject.toml` lands) and update repository documentation as needed.
- If dependencies drift, rebuild with `uv venv --recreate` followed by the installation steps above.

Sticking to these `uv` commands keeps local development aligned with the repository's dependency-management policy and avoids `pip` or `poetry` drift.
