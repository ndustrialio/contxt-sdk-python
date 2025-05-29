from typing import List

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import fields_option, print_item, print_table, sort_option
from contxt.models.contxt import Role


@click.group("roles")
def roles() -> None:
    """Roles."""


@roles.command()
@fields_option(default="id, name, description", obj=Role)
@sort_option(default="id")
@click.pass_obj
def get(clients: Clients, fields: List[str], sort: str) -> None:
    """Get roles for a project"""
    items = clients.contxt_access.get_roles(organization_id=clients.org_id)
    print_table(items=items, keys=fields, sort_by=sort)


@roles.command()
@click.option("--name", prompt=True)
@click.option("--description", prompt=True)
@click.pass_obj
def create(
    clients: Clients,
    name: str,
    description: str,
) -> None:
    """Create a role"""
    result = clients.contxt_access.post(
        f"{clients.org_id}/roles",
        {
            "name": name,
            "description": description,
        },
    )
    print_item(result)


@roles.command()
@click.argument("target_role")
@click.argument("application_id")
@click.pass_obj
def add_application(clients: Clients, target_role: int, application_id: str) -> None:
    """Add application to role"""
    result = clients.contxt_access.add_role_application(
        organization_id=clients.org_id, target_role_id=target_role, application_id=application_id
    )
    print_item(result)
