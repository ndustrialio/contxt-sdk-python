from typing import List

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import fields_option, print_table, sort_option
from contxt.models.facilities import Organization


@click.group()
def orgs() -> None:
    """Organizations."""


@orgs.command()
@fields_option(default=["id", "name", "slug"], obj=Organization)
@sort_option(default="id")
@click.pass_obj
def get(clients: Clients, fields: List[str], sort: str) -> None:
    """Get organizations"""
    items = clients.contxt.get_organizations()
    print_table(items=items, keys=fields, sort_by=sort)
