from typing import List

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import fields_option, print_table, sort_option
from contxt.models.assets import Asset, AssetType


@click.group()
def assets() -> None:
    """Assets."""


@assets.command()
@fields_option(default=["id", "label", "description"], obj=AssetType)
@sort_option(default="id")
@click.pass_obj
def types(clients: Clients, fields: List[str], sort: str) -> None:
    """Get asset types"""
    items = clients.assets.get_asset_types()
    print_table(items=items, keys=fields, sort_by=sort)


@assets.command()
@click.argument("type")
@fields_option(default=["id", "label", "description"], obj=Asset)
@sort_option(default="id")
@click.pass_obj
def get(clients: Clients, type: str, fields: List[str], sort: str) -> None:
    """Get assets"""
    types = [t for t in clients.assets.get_asset_types() if t.label == type]
    items = [a for t in types for a in clients.assets.get_assets(t.id)]
    print_table(items=items, keys=fields, sort_by=sort)
