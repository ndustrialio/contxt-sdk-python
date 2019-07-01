.PHONY: lint fix test

lint:
	isort --check-only
	black . --check
	flake8

fix:
	isort --apply
	black .

test:
	pytest tests/unit
