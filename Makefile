install:
	pip install poetry
	poetry install -E server

lint:
	poetry run isort --check-only
	poetry run black --check .
	poetry run flake8 contxt scripts tests

fix:
	poetry run isort --apply
	poetry run black .

test:
	poetry run pytest tests/unit

version:
	# Usage: make version v=[major|minor|patch|release|build]
	poetry run bump2version $(v) --commit --tag && git push && git push --tags

clean:
	rm -rf dist/ build/ *.egg-info

publish: clean
	poetry publish --build --username ndustrial.io