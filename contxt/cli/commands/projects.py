from typing import List, Optional

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import fields_option, print_table, sort_option
from contxt.models.contxt import EdgeNode, Project, Service


@click.group()
def projects() -> None:
    """Projects."""


@projects.command()
@click.argument("id", default="")
@fields_option(default=["id", "name", "type", "description"], obj=Project)
@sort_option(default="id")
@click.pass_obj
def get(clients: Clients, id: Optional[str], fields: List[str], sort: str) -> None:
    """Get project(s)"""
    items = [clients.contxt.get_project(id)] if id else clients.contxt.get_projects()
    print_table(items=items, keys=fields, sort_by=sort)


@projects.command()
@click.argument("id")
@fields_option(default=["id", "name", "service_type", "description"], obj=Service)
@sort_option(default="id")
@click.pass_obj
def get_services(clients: Clients, id: str, fields: List[str], sort: str) -> None:
    """Get services for a project"""
    items = clients.contxt.get_services(id)
    print_table(items=items, keys=fields, sort_by=sort)


@projects.command()
@click.argument("org_id")
@click.argument("project_id")
@fields_option(default=["id", "name", "stack_id", "description"], obj=EdgeNode)
@sort_option(default="id")
@click.pass_obj
def get_edge_nodes(clients: Clients, org_id: str, project_id: int, fields: List[str], sort: str) -> None:
    """Get edge nodes for a project"""
    items = clients.contxt.get_edge_nodes(organization_id=org_id, project_id=project_id)
    print_table(items=items, keys=fields, sort_by=sort)
