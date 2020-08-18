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

We use [poethepoet](https://github.com/nat-n/poethepoet) as a task runner. To see available tasks:

```console
$ poe --help
...
  clean          Remove build artifacts
  lint           Run linters and formatters
  test           Run tests
```

### Code Quality

To ensure code quality, we use the following tools:

- Formatting: [black](https://black.readthedocs.io/en/stable/) and [isort](https://isort.readthedocs.io/en/latest/)
- Linting: [flake8](http://flake8.pycqa.org/en/latest/) and [mypy](https://mypy.readthedocs.io/en/stable/)
- Testing: [pytest](https://docs.pytest.org/en/latest/)

Our [CI pipeline](.github/workflows/build.yaml) will run these tools on each commit. To run these locally, we recommend [pre-commit](https://pre-commit.com/):

```sh
poetry run pre-commit install
```

### Create Release

On a commit to master, our [CI pipeline](.github/workflows/release.yaml) will bump the version (determined by [conventional commits](https://www.conventionalcommits.org/)) and publish a new release to PyPI.
