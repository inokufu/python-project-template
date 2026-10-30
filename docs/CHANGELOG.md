# Changelog

> Note: This document applies to the Python project template itself.
> Projects generated from this template will have their own version of this
> document.

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.0] - 2026-10-30

### Upgrade notes

`copier update` from 2.x brings five breaking changes:

- `make test` and `make diff-cover` refuse a coverage below 90 %. Raise the coverage,
  or lower `--cov-fail-under` in the `Makefile` and `fail_under` in
  `[tool.diff_cover]`.
- CI only runs for `main`. Add any other branch back to `on:` in `ci.yml`.
- `make docs-deploy` is gone. Run `uv run mkdocs gh-deploy` instead.
- `make diff-cover` no longer runs the tests: run `make test` first.
- `min_python_version` must be 3.11 or higher: 3.10 reached its end of life, and
  current dev tools no longer support it. A project generated for 3.10 updates with
  `copier update -d min_python_version=3.11`.

### Added

- Dependabot configuration for uv, GitHub Actions and pre-commit hooks, with a
  cooldown on fresh releases
- gitleaks pre-commit hook, skipped in CI where the index is empty
- A 90 % coverage floor on `make test`, and on the changed lines with `make diff-cover`

### Changed

- `make check` also runs `diff-cover`, which reads the last `make test` instead of
  running the tests again, and is skipped until `origin/main` exists
- CI: actions pinned by commit SHA, `diff-cover` replaces the coverage artifact, the
  test job no longer waits for lint, and only `main` triggers it
- `add-bounds` is `major`, and the dev dependencies use major bounds
- Coverage report lists the missing lines (`term-missing`)
- Tests may hold dummy secrets (`S105`, `S106` ignored)
- The template's own CI, hooks and dependencies follow the same rules, with its own
  Dependabot

### Removed

- `.github/zizmor.yml`, no longer needed with SHA-pinned actions
- The `docs-deploy` target

## [2.4.0] - 2026-08-25

### Added

- Validate `min_python_version`: must be 3.10 or higher, written as major.minor
- CI workflow for the template itself (prek checks and tests)

### Changed

- Updated project dependencies to latest versions
- Ignore flake8-copyright (CPY) rules in generated projects
- Derive the pyupgrade and ruff target versions from `min_python_version`
- Document the git prerequisites of `copier update`
- Improved the test suite, which now catches invalid generated files

### Fixed

- Name the documentation site after the project instead of "My Docs"
- `make test` no longer fails on a project with no test written yet

### Security

- Audit GitHub Actions workflows with zizmor
- Restrict workflow permissions to `contents: read` and stop persisting
  credentials on checkout

## [2.3.1] - 2026-07-30

### Changed

- Simplify CI & Merge Request Template
- Updated project dependencies to latest versions

## [2.3.0] - 2026-06-19

### Added

Use uv audit to check dependencies security

## [2.2.1] - 2026-06-17

### Changed

- Updated project dependencies to latest versions

## [2.2.0] - 2026-03-30

### Changed

- Replace pre-commit by prek

## [2.1.2] - 2026-03-27

### Changed

- Updated project dependencies to latest versions
- Add "--show-severity, --ignore-unfixed, --severity=medium" to uv-secure params, to avoid CI blocking on low CVEs.


## [2.1.1] - 2026-03-04

### Changed

- Updated project dependencies to latest versions
- Add package = true to pyproject.toml file for easier development.


## [2.1.0] - 2025-12-18

### Added

Static type checking with ty type checker


## [2.0.0] - 2025-12-12

### Changed - BREAKING

- Migration from Rye to uv: The template now uses uv for dependency management
  - Replaced some configuration in pyproject.toml
  - Updated all development commands to use uv
  - New lock file: uv.lock instead of requirements.lock

### Added

- Support for uv-lock pre-commit hook to keep lockfile up to date

### Removed

- Rye dependency


## [1.0.1] - 2025-10-17

### Changed

- Updated project dependencies to latest versions
- Improved test coverage configuration: excluded TYPE_CHECKING blocks from coverage reports


## [1.0.0] - 2025-03-26

### Added

- **Initial release of the Copier template**
- Modern Python project structure with src layout
- Rye integration for dependency management and virtual environments
- Pre-configured Ruff for code formatting and linting
- Pytest setup with coverage reporting
- GitHub Actions CI workflows
- GitHub templates for issues and pull requests
- Documentation structure with MkDocs support
- EditorConfig configuration for consistent code styling
- Comprehensive .gitignore for Python projects
- Project governance files (CODE_OF_CONDUCT, CONTRIBUTING, SECURITY)
- Makefile with common development commands
- README templates for generated projects
