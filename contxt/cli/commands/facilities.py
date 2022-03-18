from csv import DictReader
from typing import IO, Optional

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import Serializer


@click.group()
def facilities() -> None:
    """Facilities."""


@facilities.command()
@click.option("--org-id", help="Organization ID, defaults to first value in token if not specified")
@click.option("--slug", help="Organization slug, overrides org-id if both are set")
@click.pass_obj
def get(clients: Clients, org_id: Optional[str] = None, slug: Optional[str] = None) -> None:
    """Get facilities"""
    facilities = clients.nionic.get_facilities(org_id, slug).nodes
    print(Serializer.to_table(facilities))


@facilities.command()
@click.option("--org-id", help="Organization ID, defaults to first value in token if none specified")
@click.option("--slug", help="Organization slug, overrides org-id if set")
@click.option("--input", required=True, type=click.File(), help="CSV of facilities to create")
@click.pass_obj
def create(clients: Clients, input: IO[str], org_id: Optional[str] = None, slug: Optional[str] = None) -> None:
    """Create facilities from a CSV file, containing the columns:

    \b
    - name: string
    - timezone: IANA timezone database name (ex: America/New_York)
    """
    # Parse file
    try:
        facilities = [
            dict(name=r["name"], slug=r["slug"], timezone=r["timezone"]) for r in DictReader(input)
        ]
    except KeyError:
        raise click.ClickException("The following columns are required: name, slug, timezone")

    # Create facilities
    with click.progressbar(
        facilities,
        label="Creating facilities",
        item_show_func=lambda f: f"Facility {f['name']}" if f else "",
    ) as facilities_:
        for f in facilities_:
            clients.nionic.create_facility(data=f, organization_id=org_id, slug = slug)
