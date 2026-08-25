# Changelog

> Note: This document applies to the Python project template itself.
> Projects generated from this template will have their own version of this
> document.

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
