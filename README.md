# Contxt Python SDK

[![CI](https://github.com/ndustrialio/contxt-sdk-python/workflows/CI/badge.svg)](https://github.com/ndustrialio/contxt-sdk-python/actions?query=workflow%3ACI)
[![pypi version](https://img.shields.io/pypi/v/contxt-sdk.svg)](https://pypi.org/project/contxt-sdk/)
![python](https://img.shields.io/badge/python-3.7+-blue.svg)

## Installation

Clone this repo (this version is not yet published to PyPi)
```sh
git clone https://github.com/ndustrialio/contxt-sdk-python.git
cd contxt-sdk-python
```

### Create a virtual env

Create a virtual environment for this repo:
```shell
virtualenv venv --python=python3
```

Activate your environment:
```shell
source ./venv/bin/activate
```

### Install dependencies
```shell
poetry install
```


Initialize the CLI/SDK. This command will download any dependent GraphQL schemas, create a token cache file, and create
a fresh defaults file. During this process you will likely be asked to login to your Contxt account.
```shell
contxt init --fresh-from-file ./docs/configs/basic_config.yml
```

## CLI Usage

```sh
contxt --help
```

## Documentation


## Contributing

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md).
