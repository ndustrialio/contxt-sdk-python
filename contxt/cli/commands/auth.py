import click

from contxt.cli.clients import Clients


@click.group()
def auth() -> None:
    """Authenticate with Contxt."""


@auth.command()
@click.pass_obj
def login(client: Clients):
    """Login to Contxt."""
    client.auth.login()


@auth.command()
@click.pass_obj
def logout(client: Clients):
    """Logout of Contxt."""
    client.auth.logout()
