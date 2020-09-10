from collections import defaultdict
from typing import List

import click

from contxt.cli.utils import Clients, fields_option, print_table, sort_option
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
def get(obj: Clients, type: str, fields: List[str], sort: str) -> None:
    """Get assets"""
    types = defaultdict(list)
    for t in obj.assets.get_asset_types():
        types[t.label].append(t)
    items = []
    for t in types[type]:
        items += obj.assets.get_assets(t.id)
    print_table(items=items, keys=fields, sort_by=sort)
