from csv import DictReader
from typing import IO

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import Serializer


@click.group()
def facilities() -> None:
    """Facilities."""


@facilities.command()
@click.pass_obj
def get(clients: Clients) -> None:
    """Get facilities"""
    facilities = clients.nionic.get_facilities()
    print(Serializer.to_table(facilities))


@facilities.command()
@click.option("--input", required=True, type=click.File(), help="CSV of facilities to create")
@click.pass_obj
def create(clients: Clients, input: IO[str]) -> None:
    """Create facilities from a CSV file, containing the columns:

    \b
    - name: string
    - timezone_name: IANA timezone database name (ex: America/New_York)
    """
    # Parse file
    try:
        facilities = [
            dict(name=r["name"], slug=r["slug"], timezone_name=r["timezone_name"])
            for r in DictReader(input)
        ]
    except KeyError:
        raise click.ClickException("The following columns are required: name, slug, timezone_name")

    # Create facilities
    with click.progressbar(
        facilities,
        label="Creating facilities",
        item_show_func=lambda f: f"Facility {f['name']}" if f else "",
    ) as facilities_:
        for f in facilities_:
            clients.nionic.create_facility(data=f)
