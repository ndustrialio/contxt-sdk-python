DIRS := contxt tests
RUNNER := poetry run
VERSION := $$(poetry version | sed -n 's/contxt-sdk //p')

help: ## Show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z -]+:.*?## / {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

lint: ## Report format and lint violations
	$(RUNNER) isort --check --quiet $(DIRS)
	$(RUNNER) black --check --quiet $(DIRS)
	$(RUNNER) flake8 $(DIRS)
	# $(RUNNER) mypy $(DIRS)

fmt: ## Format code
	$(RUNNER) isort --quiet $(DIRS)
	$(RUNNER) black --quiet $(DIRS)

test: ## Run unit tests
	$(RUNNER) pytest tests/unit

clean: ## Remove build artifacts
	@rm -rf .mypy_cache/ .pytest_cache/ build/ dist/ *.egg-info
	@find $(DIRS) -name "*.pyc" -delete 

release: ## Release new version [usage: release v=major|minor|patch]
ifndef v
	$(error v is undefined)
endif
	@poetry version $(v)
	@git commit pyproject.toml -m "chore(release): v$(VERSION)"
	@git tag -am "chore(release): v$(VERSION)" "v$(VERSION)"
	@git push --follow-tags
