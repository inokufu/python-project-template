# Python Project Template with Copier

[![Python](https://img.shields.io/badge/Python-FFD43B?logo=python)](https://www.python.org/)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/copier-org/copier)
[![uv](https://img.shields.io/badge/uv-261230?logo=astral)](https://docs.astral.sh/uv/)
[![ty](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
![License](https://img.shields.io/badge/GPL--3.0-red?logo=gnu)
[![EditorConfig](https://img.shields.io/badge/EditorConfig-333333?logo=editorconfig)](https://editorconfig.org/)
[![Pre-commit](https://img.shields.io/badge/pre--commit-40332E?logo=pre-commit)](https://pre-commit.com/)
[![Makefile](https://img.shields.io/badge/Makefile-427819?logo=gnu)](https://www.gnu.org/software/make/manual/make.html)

A modern Copier template for creating standardized Python packages and
applications with best practices.

## ✨ Features

- 🛠️ **Modern tooling** with [uv](https://docs.astral.sh/uv/) for dependency
  management and virtual environments
- 📦 **Standardized project structure** following best practices for Python
  packages
- 💅 **Code quality** with pre-commit, well configured Ruff (formatter & linter) and Ty (type checker)
- 🧪 **Testing** setup with pytest and coverage reports
- 📝 **Documentation** with MkDocs and Material theme, including well-structured
  README and CHANGELOG
- 🚀 **CI/CD** with GitHub Actions
- 🐙 **GitHub integration** with PR templates, issue templates (bugs, features,
  questions)
- 🔧 **Development standards** with EditorConfig for consistent code style across
  editors
- 🚫 **Comprehensive .gitignore** tailored for Python development
- 🧩 **Multiple license options** (GPL-3.0, MIT, Apache-2.0, BSD-3-Clause,
  Proprietary)
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

# Initialize the project
make init
```

That's it! Feel free to focus on the coding within `src` and `tests` folders !

### Update an existing project

One of the advantages of Copier is the ability to update existing projects when
the template is improved:

```bash
# Update your project with the latest template version
cd path/to/your/project
copier update
```

This will update your project files while preserving your source code and tests.

## 📋 Template Variables

| Feature               | Description                                                       | Default               |
|-----------------------|-------------------------------------------------------------------|-----------------------|
| `project_name`        | Name of your project (can include spaces and hyphens)             | "Python project"      |
| `package_name`        | Python import name (must be a valid Python identifier)            | Based on project name |
| `project_description` | Brief summary of your project (used in README and pyproject.toml) | "A Python project"    |
| `author_name`         | Name of the author or organization (for credits and licensing)    |                       |
| `author_email`        | Contact email (for documentation and package metadata)            |                       |
| `min_python_version`  | Minimum Python version required                                   | 3.13                  |

## 🧑‍💻 Development

### Common Commands

```bash
# Install dependencies
make install

# Format code
make format

# Lint code
make lint

# Run tests
make test

# Run all checks (pre-commit, tests)
make check

# Build package
make build

# Generate documentation
make docs
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
