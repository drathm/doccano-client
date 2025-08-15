# Repository Guidelines

## Project Structure & Module Organization
- Source: `doccano_client/` (API client, CLI in `doccano_client/cli/`, beta client under `doccano_client/beta/`).
- Tests: `doccano_client/beta/tests/` and `tests/` (unit/integration fixtures under `tests/fixtures`).
- Docs: `docs/` (MkDocs), CI and templates in `.github/`.

## Build, Test, and Development Commands
- Install: `poetry install` (uses `pyproject.toml`).
- Lint all: `make lint` (runs flake8, black --check, isort --check, mypy).
- Test: `make test` or `poetry run task test` (pytest).
- Individual linters: `poetry run task flake8 | black | isort | mypy`.
- CLI help: `poetry run docli --help`.
- Build package: `poetry build`.

## Coding Style & Naming Conventions
- Language: Python 3.8+.
- Formatting: Black (line length 120) and isort (profile=black).
- Linting: Flake8 (ignore: E203, E266, W503; max-complexity=18).
- Typing: mypy enabled (errors on project code; some imports ignored).
- Conventions: PEP 8 — modules/functions `snake_case`, classes `CapWords`, constants `UPPER_CASE`.
- Pre-commit: `pre-commit install` recommended (see `.pre-commit-config.yaml`).

## Testing Guidelines
- Frameworks: pytest, responses (HTTP mocking), vcrpy (cassettes in `tests/fixtures/cassettes`).
- Location: place unit tests alongside beta client in `doccano_client/beta/tests/` or general tests in `tests/`.
- Naming: files `test_*.py`, tests use clear Arrange–Act–Assert.
- Running: `poetry run pytest -q` or `make test`.
- Integration: prefer vcrpy cassettes; keep fixtures small and anonymized.

## Commit & Pull Request Guidelines
- Commits: concise, imperative subject (e.g., "Fix login retry logic"). Group related changes; keep noise (e.g., "Run black") separate.
- PRs: include description, motivation, and link issues (use "Fixes #123"). Follow template in `.github/PULL_REQUEST_TEMPLATE.md`.
- Checks: ensure `make lint` and tests pass locally; include screenshots or CLI output when behavior changes.

## Security & Configuration Tips
- Do not commit credentials or real tokens; scrub test recordings.
- Prefer environment variables in examples and tests; pin external URLs to non-sensitive demos.
