# Overview

This software development kit (SDK) gives you quick access to the set of Contxt API's from <https://ndustrial.io>, both programatically and on the command line.

## Install

Before proceeding, you must have [Python](https://www.python.org/) 3.7+ installed.

### Library

To install and use this SDK as a library, just use [pip](https://pip.pypa.io/en/stable/quickstart/):

```sh
python3 -m pip install --upgrade contxt-sdk
```

### CLI

If you only need the CLI, the above method will work fine. However, we recommend using [pipx](https://pipxproject.github.io/pipx/installation/#install-pipx)[^1]:

```sh
# Setup pipx (once only)
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Install
pipx install contxt-sdk

# Upgrade
pipx upgrade contxt-sdk
```

Run the following to ensure the installation was successful:

```sh
$ contxt --version
contxt, version 2.1.4
```

[^1]: Why pipx? See [here](https://pipxproject.github.io/pipx/#how-is-it-different-from-pip)
