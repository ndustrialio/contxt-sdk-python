.PHONY: help install lint fix test release

CMD := poetry run
DIRS := contxt tests
VERSION := $$(poetry version | sed -n 's/contxt-sdk //p')

help: ## List all commands
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z -]+:.*?## / {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:
	pip install poetry
	poetry install -E server

lint: ## Run formatters and linter
	$(CMD) isort --check-only --recursive $(DIRS)
	$(CMD) black --check $(DIRS)
	$(CMD) flake8 $(DIRS)

fix: ## Fix formatting
	$(CMD) isort --apply --recursive $(DIRS)
	$(CMD) black $(DIRS)

test: ## Run unit tests
	$(CMD) pytest tests/unit

release: ## Release new version [usage: v=rule]
	# Update pyproject and changelog
	poetry version $(v)
	sed -i "" "s/\[Unreleased\]/\[$(VERSION)\] - $(shell date +%F)/" CHANGELOG.md
	# Create commit and tag
	git commit pyproject.toml CHANGELOG.md -m "Bump version to $(VERSION)" && git tag "v$(VERSION)"
	git push && git push --tags
	# Publish to pypi
	poetry publish --build