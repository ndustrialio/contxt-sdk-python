import click

from contxt.cli.clients import Clients


@click.group()
def auth() -> None:
    """Authenticate with Contxt."""


@auth.command()
@click.pass_obj
def login(client: Clients) -> None:
    """Login to Contxt."""
    client.auth.login()


@auth.command()
@click.pass_obj
def logout(client: Clients) -> None:
    """Logout of Contxt."""
    client.auth.logout()


@auth.command()
@click.argument("audience")
@click.pass_obj
def token(client: Clients, audience: str) -> None:
    """Fetch an access token for an API."""
    token = client.auth.get_token_provider(audience).access_token
    print(token)
