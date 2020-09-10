from typing import List

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
