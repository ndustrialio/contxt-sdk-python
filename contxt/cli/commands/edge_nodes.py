from typing import List

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import fields_option, print_table, sort_option
from contxt.models.contxt import EdgeNode


@click.group("edge-nodes")
def edge_nodes() -> None:
    """Edge Nodes."""


@edge_nodes.command()
@click.argument("org_id")
@click.argument("project_id")
@fields_option(default=["id", "name", "stack_id", "description"], obj=EdgeNode)
@sort_option(default="id")
@click.pass_obj
def get(clients: Clients, org_id: str, project_id: int, fields: List[str], sort: str) -> None:
    """Get edge nodes for a project"""
    items = clients.contxt.get_edge_nodes(organization_id=org_id, project_id=project_id)
    print_table(items=items, keys=fields, sort_by=sort)
