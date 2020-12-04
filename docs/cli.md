# Command Line Interface (CLI)

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

## Authenticate

To access any Contxt API, first login with your Contxt credentials:

```console
contxt auth login
```

## Commands

To see all commands:

```console
Usage: contxt [OPTIONS] COMMAND [ARGS]...

  Contxt CLI

Options:
  -v, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  assets      Assets.
  auth        Authenticate with Contxt.
  ems         Energy Management System.
  facilities  Facilities.
  iot         Internet-of-Things.
  orgs        Organizations.
  projects    Projects.
  services    Services.
```

## Subcommands

To see more usage from any subcommand, just pass the `--help` flag:

```console
$ contxt auth --help
Usage: contxt auth [OPTIONS] COMMAND [ARGS]...

  Authenticate with Contxt.

Options:
  -h, --help  Show this message and exit.

Commands:
  login   Login to Contxt.
  logout  Logout of Contxt.
```
