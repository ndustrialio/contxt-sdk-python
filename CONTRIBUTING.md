# Contributing

Before getting started, make sure you have [Poetry](https://python-poetry.org/docs/#installation).

## Install

```sh
# Install project
poetry install -E crypto

# Enter poetry-managed venv
poetry shell

# Exit poetry-managed venv
exit
```

## Tasks

We use `make` as a general task runner. To see available tasks:

```console
$ make help
clean      Remove build artifacts
fmt        Format code
help       Show this help
lint       Report format and lint violations
release    Release new version [usage: release v=major|minor|patch]
test       Run unit tests
```

### Code Quality

To ensure code quality, we use the following tools:

- Formatting: [black](https://black.readthedocs.io/en/stable/) and [isort](https://isort.readthedocs.io/en/latest/)
- Linting: [flake8](http://flake8.pycqa.org/en/latest/)
- Testing: [pytest](https://docs.pytest.org/en/latest/)

Our [CI pipeline](.github/workflows/build.yaml) will run these tools on every git push. To run these locally:

```sh
# Reports format/lint violations
make lint

# Formats code
make fmt

# Runs unit tests
make test
```

### Create Release

Creating a new release is simply bumping the version and creating a corresponding git tag. For example, to create a minor release:

```sh
make release v=minor
```

Our [release action](.github/workflows/release.yaml) will then build and publish to PyPI.
