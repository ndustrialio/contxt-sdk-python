from typing import List

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import fields_option, print_item, print_table, sort_option
from contxt.models.contxt import EdgeNode, EdgeNodeGrant


@click.group("edge-nodes")
def edge_nodes() -> None:
    """Edge Nodes."""


@edge_nodes.command()
@click.argument("project_slug")
@fields_option(default="id, name, project_id, description", obj=EdgeNode)
@sort_option(default="id")
@click.pass_obj
def get(clients: Clients, project_slug: int, fields: List[str], sort: str) -> None:
    """Get edge nodes for a project"""
    items = clients.contxt_deployments.get_edge_nodes(
        organization_id=clients.org_id, project_slug=project_slug
    )
    print_table(items=items, keys=fields, sort_by=sort)


@edge_nodes.command()
@click.option("--project-slug", prompt=True)
@click.option("--name", prompt=True)
@click.option("--description", prompt=True)
@click.pass_obj
def create(
    clients: Clients,
    project_slug: str,
    name: str,
    description: str,
) -> None:
    """Create an edge node"""
    result = clients.contxt_deployments.post(
        f"{clients.org_id}/projects/{project_slug}/edgenodes",
        {
            "name": name,
            "description": description,
        },
    )
    print_item(result)


@edge_nodes.command()
@click.argument("edge_node_id")
@click.argument("target")
@click.pass_obj
def add_grant(clients: Clients, edge_node_id: str, target: int) -> None:
    """Add grant to edge node"""
    result = clients.contxt.create_edge_node_grant(
        edge_node_id=edge_node_id, to_service_instance_id=target
    )
    print_item(result)


@edge_nodes.command()
@click.argument("edge_node_id")
@fields_option(default="id, from_edge_node_id, to_service_instance_id", obj=EdgeNodeGrant)
@sort_option(default="id")
@click.pass_obj
def get_grants(clients: Clients, edge_node_id: str, fields: List[str], sort: str) -> None:
    """Get all edge node grants"""
    items = clients.contxt_deployments.get_edge_node_grants(clients.org_id, edge_node_id=edge_node_id)

    print_table(items=items, keys=fields, sort_by=sort)
