# Note: This file applies to the Python project template itself.
# Projects generated from this template will have their own version of this file.

.DEFAULT_GOAL := help

# Check if uv is installed
UV_COMMAND := $(shell command -v uv 2> /dev/null)

.PHONY: help
help: ## Display this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: all
all: check-uv install format lint check ## Build everything

.PHONY: check-uv
check-uv: ## Check if uv is installed
ifndef UV_COMMAND
	$(error "uv is not installed. Please visit https://docs.astral.sh/uv for installation instructions.")
endif

.PHONY: install
install: check-uv pyproject.toml ## Synchronize dependencies
	uv sync

.PHONY: init
init: check-uv pyproject.toml .pre-commit-config.yaml install ## Initialize project (first installation)
	uv run -- pre-commit install

.PHONY: test
test: check-uv tests ## Run tests with coverage
	uv run -- pytest

.PHONY: precommit
precommit: check-uv install ## Run pre-commit on all files
	uv run -- pre-commit run --all-files

.PHONY: check
check: check-uv install ## Run all checks (precommit + test)
	make precommit
	make test

.PHONY: build
build: check-uv install ## Build package
	uv build

.PHONY: gitignore
gitignore: ## Generate .gitignore file for this project
	curl -L https://www.gitignore.io/api/windows,macos,linux,git,pycharm,visualstudiocode,python > .gitignore

.PHONY: clean
clean: ## Remove temporary files and build artifacts
	rm -rf .pytest_cache/ .coverage htmlcov/ .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf dist/ build/
