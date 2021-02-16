# Quickstart

## Install

If you only want to use the CLI, we recommend installing with [pipx](https://github.com/pipxproject/pipx#install-pipx):

```sh
# Setup pipx (once only)
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Install
pipx install contxt-sdk

# Upgrade
pipx upgrade contxt-sdk
```

## Login

To access any Contxt API, first login with your Contxt credentials:

```sh
contxt auth login
```

This will open a browser window and ask you to login.
