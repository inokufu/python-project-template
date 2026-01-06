# Contributing

Thank you for considering contributing to this project! This document provides
guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to abide by
the [Code of Conduct](CODE_OF_CONDUCT.md).

## How to Contribute

### Reporting Issues

- Check existing issues to avoid duplicates
- Use the issue templates when reporting bugs or requesting features
- Provide as much detail as possible to help reproduce and resolve issues

## Development Setup

### Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) for dependency management
- Git for version control

### Editor Configuration

This project uses EditorConfig to maintain consistent coding styles.
Find plugin for your editor at [editorconfig.org](https://editorconfig.org/#download)

### Pre-commit Hooks
This project uses pre-commit to enforce code quality checks before each commit.

### Pre-commit hooks installed
- Code formatting with Ruff
- Type checking with Ty
- Python syntax checking
- Security vulnerability scanning
- Trailing whitespace removal
- Merge conflict detection
- Large file detection
- And more (see .pre-commit-config.yaml)

### Development Workflow

1. **Fork and clone the repository**

2. **Set up your development environment**
   ```sh
   # Initialize the project (install dependencies and pre-commit hooks)
   make init
   ```

3. **Create a branch for your changes**
   ```sh
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**

- Write tests for new functionality
- Update documentation as needed
- Ensure your code follows the project's style guidelines

5. **Run checks and tests**
   ```sh
   # Format code
   make format
   
   # Run linters
   make lint
   
   # Run tests
   make test
   
   # Run pre-commit hooks on all files
   make precommit
   
   # Run all checks (precommit + test)
   make check
   ```

6. **Commit your changes**

   Use clear and descriptive commit messages
   following [Gitmoji](https://gitmoji.dev/) conventions:

   ```
   ✨ Add new feature X
   🐛 Fix issue with Y
   📝 Update installation instructions
   ✅ Add tests for feature Z
   ⬆️ Update dependencies
   ```

7. **Push to your fork**
   ```sh
   git push origin feature/your-feature-name
   ```

8. **Submit a Pull Request**

- Fill out the PR template
- Reference any related issues
- Wait for review and address any feedback

## Available Make Commands

This project includes a Makefile with useful commands for development:

```sh
# Display all available commands
make help
```

| Command     | Description                             |
|-------------|-----------------------------------------|
| install     | Synchronize dependencies                |
| init        | Initialize project (first installation) |
| format      | Format code                             |
| lint        | Run linting checks                      |
| test        | Run tests with coverage                 |
| precommit   | Run pre-commit on all files             |
| check       | Run all checks (precommit + test)       |
| build       | Build package                           | 
| docs        | Build documentation                     |
| docs-serve  | Serve documentation locally             |
| docs-deploy | Deploy documentation to GitHub Pages    |

## Style Guidelines

This project follows these conventions:

- Code formatting with [ruff](https://docs.astral.sh/ruff/)
- Type checking with [ty](https://docs.astral.sh/ty/)
- Type annotations for all functions
- Documentation
  using [Google style docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- Tests written with pytest

## Documentation

This project uses [MkDocs](https://www.mkdocs.org/) for documentation.
The documentation source files are in the `docs/` directory in Markdown format.

When adding or changing features, please update the documentation accordingly:

- Update docstrings for public functions, classes, and modules
- Update the README.md if needed
- Add examples for new features

## Testing

- All new features should include tests
- Bug fixes should include tests that demonstrate the issue is fixed
- Run the full test suite before submitting a PR

## Review Process

- Maintainers will review PRs as they are submitted
- Address review comments and update your PR as needed
- Once approved, maintainers will merge your PR

## Release Process

- This project follows [Semantic Versioning](https://semver.org/)
- Changes are documented in the [CHANGELOG.md](CHANGELOG.md)

Thank you for contributing!
