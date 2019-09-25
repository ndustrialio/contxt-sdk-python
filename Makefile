dirs = contxt tests

install:
	pip install poetry
	poetry install -E server

lint:
	poetry run isort --check-only --recursive $(dirs)
	poetry run black --check $(dirs)
	poetry run flake8 $(dirs)

fix:
	poetry run isort --apply --recursive $(dirs)
	poetry run black $(dirs)

test:
	poetry run pytest tests/unit

version:
	# Usage: make version v=[major|minor|patch|release|build]
	poetry run bump2version $(v) --commit --tag && git push && git push --tags

clean:
	rm -rf dist/ build/ *.egg-info

publish: clean
	poetry publish --build --username ndustrial.io