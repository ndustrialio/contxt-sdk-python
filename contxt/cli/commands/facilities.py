from csv import DictReader
from typing import IO, List

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import fields_option, print_table, sort_option
from contxt.models.facilities import Facility
from contxt.utils.contxt_environment import ContxtEnvironment
from contxt.services.nionic import NionicService
from contxt.utils.serializer import Serializer


def get_nionic_service():
    # load configuration file
    contxt_env = ContxtEnvironment()
    return NionicService(contxt_env=contxt_env.get_config_for_service_name('nionic'))


@click.group()
def facilities() -> None:
    """Facilities."""


@facilities.command()
def get() -> None:
    """Get facilities"""
    facilities = get_nionic_service().get_facilities().nodes
    print(Serializer.to_table(facilities))


@facilities.command()
@click.argument("org_id")
@click.option("--input", required=True, type=click.File(), help="CSV of facilities to create")
@click.pass_obj
def create(clients: Clients, org_id: str, input: IO[str]) -> None:
    """Create facilities from a CSV file, containing the columns:

    \b
    - name: string
    - timezone: IANA timezone database name (ex: America/New_York)
    """
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
