# Python Project Template with Copier

[![Python](https://img.shields.io/badge/Python-FFD43B?logo=python)](https://www.python.org/)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/copier-org/copier)
[![uv](https://img.shields.io/badge/uv-261230?logo=astral)](https://docs.astral.sh/uv/)
[![ty](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
![License](https://img.shields.io/badge/GPL--3.0-red?logo=gnu)
[![EditorConfig](https://img.shields.io/badge/EditorConfig-333333?logo=editorconfig)](https://editorconfig.org/)
[![Prek](https://img.shields.io/badge/prek-F54327?logo=prek)](https://prek.j178.dev/)
[![Makefile](https://img.shields.io/badge/Makefile-427819?logo=gnu)](https://www.gnu.org/software/make/manual/make.html)
[![Ruff](https://img.shields.io/badge/Ruff-3A3A3A?logo=ruff)](https://docs.astral.sh/ruff/)
[![Pytest](https://img.shields.io/badge/pytest-E6F7FF?logo=pytest)](https://docs.pytest.org/)
[![MkDocs](https://img.shields.io/badge/MkDocs-526CFE?logo=markdown)](https://www.mkdocs.org/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-E6F0FF?logo=githubactions)](https://github.com/features/actions)
[![Dependabot](https://img.shields.io/badge/Dependabot-025E8C?logo=dependabot)](https://docs.github.com/code-security/dependabot)
[![gitleaks](https://img.shields.io/badge/gitleaks-C0392B)](https://github.com/gitleaks/gitleaks)
[![zizmor](https://img.shields.io/badge/zizmor-6E40C9)](https://docs.zizmor.sh/)

A modern Copier template for creating standardized Python packages and
applications with best practices.

## ✨ Features

- 🛠️ **Modern tooling** with [uv](https://docs.astral.sh/uv/) for dependency
  management and virtual environments
- 📦 **Standardized project structure** following best practices for Python
  packages
- 💅 **Code quality** with prek(pre-commit), well configured Ruff (formatter & linter) and Ty (type checker)
- 🔒 **Dependency security** with [`uv audit`](https://docs.astral.sh/uv/) run as a pre-commit hook to catch known vulnerabilities
- 🛡️ **Workflow security** with [zizmor](https://docs.zizmor.sh/) run as a pre-commit hook to audit GitHub Actions workflows
- 🔑 **Secret scanning** with [gitleaks](https://github.com/gitleaks/gitleaks) run as a pre-commit hook, to catch a secret before it is committed
- 🤖 **Dependency updates** with Dependabot for uv, GitHub Actions and pre-commit hooks
- 🧪 **Testing** setup with pytest, a coverage floor (90 % by default) and [diff-cover](https://github.com/Bachmann1234/diff_cover) on the changed lines
- 📝 **Documentation** with MkDocs and Material theme, including well-structured
  README and CHANGELOG
- 🚀 **CI/CD** with GitHub Actions
- 🐙 **GitHub integration** with PR templates, issue templates (bugs, features,
  questions)
- 🔧 **Development standards** with EditorConfig for consistent code style across
  editors
- 🚫 **Comprehensive .gitignore** tailored for Python development
- 🧩 **License** GPL-3.0, to replace by hand if needed
- 🤝 **Project governance** with CODE_OF_CONDUCT, CONTRIBUTING, and SECURITY
  policies
- 🔄 **Easy updates** - keep your project in sync with template improvements

## 🔧 Prerequisites

- [Python](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/) - Fast Python package installer and resolver
- [Copier](https://copier.readthedocs.io/)

## 🚀 Getting Started

### Create a new project

To create a new Python project from this template:

```bash
# Generate a new project
copier copy gh:inokufu/python-project-template path/to/destination

# Navigate to the project
cd path/to/destination

# Init GIT (if you haven't already done)
git init
git add --all
git commit -m "Initial commit"

# Initialize the project
make init
```

That's it! Feel free to focus on the coding within `src` and `tests` folders !

### Update an existing project

One of the advantages of Copier is the ability to update existing projects when
the template is improved:

Copier only updates a project that is tracked by git and has no uncommitted
changes: commit or stash your work first, including untracked files.

```bash
# Update your project with the latest template version
cd path/to/your/project
copier update
```

This will update your project files while preserving your source code and tests.

Dependabot keeps the template repository itself up to date, not the versions it ships:
it cannot read the `.jinja` files under `template/`. Those are bumped by hand at each
release.

## 📋 Template Variables

| Feature               | Description                                                       | Default               |
|-----------------------|-------------------------------------------------------------------|-----------------------|
| `project_name`        | Name of your project (can include spaces and hyphens)             | "Python project"      |
| `package_name`        | Python import name (must be a valid Python identifier)            | Based on project name |
| `project_description` | Brief summary of your project (used in README and pyproject.toml) | "A Python project"    |
| `author_name`         | Name of the author or organization (for credits and licensing)    |                       |
| `author_email`        | Contact email (for documentation and package metadata)            |                       |
| `min_python_version`  | Minimum Python version required (3.11 or higher, as major.minor)  | 3.14                  |

## 🧑‍💻 Development

### Common Commands

```bash
# Install dependencies
make install

# Initialize the template repository (first installation)
make init

# Run tests
make test

# Run pre-commit hooks on all files
make precommit

# Run all checks (pre-commit, tests)
make check

# Build package
make build
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for
guidelines.

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes and commit them (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This template is distributed under the GNU GPL v3.0 License. See the LICENSE
file for more information.
