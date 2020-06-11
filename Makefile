DIRS := contxt tests
RUNNER := poetry run
VERSION := $$(poetry version | sed -n 's/contxt-sdk //p')

help: ## Show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z -]+:.*?## / {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

lint: ## Report format and lint violations
	$(RUNNER) isort --check-only --recursive $(DIRS)
	$(RUNNER) black --check --quiet $(DIRS)
	$(RUNNER) flake8 $(DIRS)
	# $(RUNNER) mypy $(DIRS)

fmt: ## Format code
	$(RUNNER) isort --apply --recursive $(DIRS)
	$(RUNNER) black $(DIRS)

clean: ## Remove all build artifacts
	@rm -rf build/ dist/  *.egg-info

test: ## Run unit tests
	$(RUNNER) pytest tests/unit

release: ## Release a new version [usage: release v=major|minor|patch]
	# Update version string
	@poetry version $(v)
	# Create commit and tag
	@git commit pyproject.toml -m "chore(release): v$(VERSION)"
	@git tag -a "v$(VERSION)" -m "chore(release): v$(VERSION)"
	@git push && git push --tags
	# Publish to pypi
	poetry publish --build