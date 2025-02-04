.DEFAULT_GOAL := help

.PHONY: help
help: ## Display this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: install
install: pyproject.toml requirements.lock ## Synchronize dependencies
	rye sync

.PHONY: init
init: pyproject.toml .pre-commit-config.yaml install ## Initialize project (first installation)
	rye run pre-commit install
	cp .env.example .env || true

.PHONY: format
format: ## Format code
	-rye fmt
	rye lint --fix

.PHONY: lint
lint: ## Run linting checks
	rye lint

.PHONY: test
test: ## Run tests with coverage
	rye test

.PHONY: precommit
precommit: ## Run pre-commit on all files
	rye run pre-commit run --all-files

.PHONY: check
check: ## Run all checks (precommit + test)
	-make precommit
	make test

.PHONY: build
build: ## Build package
	rye build
