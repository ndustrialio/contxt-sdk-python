from typing import List

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import fields_option, print_table, sort_option
from contxt.models.contxt import Service


@click.group()
def services() -> None:
    """Services."""


@services.command()
@click.argument("id", default="")  # HACK: make an optional argument
@fields_option(default=["id", "name", "service_type", "description"], obj=Service)
@sort_option(default="id")
@click.pass_obj
def get(clients: Clients, id: str, fields: List[str], sort: str) -> None:
    """Get service(s)"""
    items = [clients.contxt.get_service(id)] if id else clients.contxt.get_services()
    print_table(items=items, keys=fields, sort_by=sort)
