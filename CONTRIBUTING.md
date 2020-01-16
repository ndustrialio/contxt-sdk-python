# Contributing

Before getting started, make sure you have [Poetry](https://poetry.eustace.io/docs/#installation) installed.

## Install
```bash
$ poetry install -E server
```

## Code Quality
To enforce code quality, we use the following tools:
* Formatting: [black](https://black.readthedocs.io/en/stable/) and [isort](https://isort.readthedocs.io/en/latest/)
* Linting: [flake8](http://flake8.pycqa.org/en/latest/)
* Testing: [pytest](https://docs.pytest.org/en/latest/)

Our CI pipeline will run these tools on every git push. To run these locally:
```bash
# Outputs formatting + linting issues
$ make lint

# Fixes formatting issues
$ make fix

# Runs unit tests
$ make test
```

## Release
To release a new version:
```bash
# Updates pyproject/changelog and tags/publishes
$ make release v=[bump rule]
```

This does the following:
* Updates version string in [pyproject.toml](pyproject.toml)
* Updates `Unreleased` section in [CHANGELOG.md](CHANGELOG.md) with version and date
* Commits the changes and tags the commit
* Builds and publishes to PyPI an sdist and wheel