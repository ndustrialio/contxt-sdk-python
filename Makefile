.PHONY: lint fix test

lint:
	poetry run isort --check-only
	poetry run black --check .
	poetry run flake8

fix:
	poetry run isort --apply
	poetry run black .

test:
	poetry run pytest tests/unit