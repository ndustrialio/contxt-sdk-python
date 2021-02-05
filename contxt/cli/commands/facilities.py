from csv import DictReader
from typing import IO, List

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import fields_option, print_table, sort_option
from contxt.models.facilities import Facility


@click.group()
def facilities() -> None:
    """Facilities."""


@facilities.command()
@fields_option(default=["id", "name", "organization_id"], obj=Facility)
@sort_option(default="id")
@click.pass_obj
def get(clients: Clients, fields: List[str], sort: str) -> None:
    """Get facilities"""
    items = clients.facilities.get_facilities()
    print_table(items=items, keys=fields, sort_by=sort)


@facilities.command()
@click.argument("org_id")
@click.option("--input", required=True, type=click.File(), help="CSV of facilities to create")
@click.pass_obj
def create(clients: Clients, org_id: str, input: IO[str]) -> None:
    """Create facilities"""
    # Parse file
    try:
        facilities = [
            dict(name=r["name"], timezone=r["timezone"], organization_id=org_id)
            for r in DictReader(input)
        ]
    except KeyError:
        raise click.ClickException("The following columns are required: name, timezone")

    # Create facilities
    with click.progressbar(
        facilities,
        label="Creating facilities",
        item_show_func=lambda f: f"Facility {f['name']}" if f else "",
    ) as facilities_:
        for f in facilities_:
            clients.facilities.post("facilities", data=f)
