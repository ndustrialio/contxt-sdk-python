.PHONY: lint fix test version publish

lint:
	poetry run isort --check-only
	poetry run black --check .
	poetry run flake8

fix:
	poetry run isort --apply
	poetry run black .

test:
	poetry run pytest tests/unit

version:
	# Usage: make version v=[major|minor|patch|release|build]
	bump2version $(v) --commit --tag && git push && git push --tags

publish:
	poetry publish --build --username ndustrial.io
	rm -rf dist/