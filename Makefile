.DEFAULT_GOAL := help

# Check if Rye is installed
RYE_COMMAND := $(shell command -v rye 2> /dev/null)

.PHONY: help
help: ## Display this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: check-rye
check-rye: ## Check if Rye is installed
ifndef RYE_COMMAND
	$(error "Rye is not installed. Please visit https://rye.astral.sh for installation instructions.")
endif

.PHONY: install
install: check-rye pyproject.toml requirements.lock ## Synchronize dependencies
	rye sync

.PHONY: init
init: check-rye pyproject.toml .pre-commit-config.yaml install ## Initialize project (first installation)
	rye run pre-commit install
	cp .env.example .env || true

.PHONY: format
format: check-rye ## Format code
	-rye fmt
	rye lint --fix

.PHONY: lint
lint: check-rye ## Run linting checks
	rye lint

.PHONY: test
test: check-rye ## Run tests with coverage
	rye test

.PHONY: precommit
precommit: check-rye ## Run pre-commit on all files
	rye run pre-commit run --all-files

.PHONY: check
check: ## Run all checks (precommit + test)
	-make precommit
	make test

.PHONY: build
build: check-rye ## Build package
	rye build

.PHONY: docs
docs: check-rye ## Build documentation
	rye run mkdocs build

.PHONY: docs-serve
docs-serve: check-rye ## Serve documentation locally
	rye run mkdocs serve

.PHONY: docs-deploy
docs-deploy: check-rye ## Deploy documentation to GitHub Pages
	rye run mkdocs gh-deploy

.PHONY: gitignore
gitignore: ## Generate .gitignore file for this project
	curl -L https://www.gitignore.io/api/windows,macos,linux,git,pycharm,visualstudiocode,python > .gitignore
