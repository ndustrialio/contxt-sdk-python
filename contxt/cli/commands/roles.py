from typing import List

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import fields_option, print_item, print_table, sort_option
from contxt.models.contxt import Role, ServiceInstanceScope


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
@click.argument("target_role_id")
@click.argument("application_id")
@click.pass_obj
def add_application(clients: Clients, target_role_id: int, application_id: str) -> None:
    """Add application to role"""
    result = clients.contxt_access.add_role_application(
        organization_id=clients.org_id, target_role_id=target_role_id, application_id=application_id
    )
    print_item(result)


@roles.command()
@click.argument("role_id")
@fields_option(default="id, service_instance_id, label, description", obj=ServiceInstanceScope)
@sort_option(default="id")
@click.pass_obj
def get_role_scopes(clients: Clients, role_id: str, fields: List[str], sort: str) -> None:
    """Get scopes for a role"""
    items = clients.contxt_access.get_role_scopes(organization_id=clients.org_id, role_id=role_id)
    print_table(items=items, keys=fields, sort_by=sort)


@roles.command()
@click.argument("target_role_id")
@click.argument("service_instance_scope_id")
@click.pass_obj
def add_scope(clients: Clients, target_role_id: int, service_instance_scope_id: int) -> None:
    """Add service instance scope to role"""
    result = clients.contxt_access.add_role_service_instance_scope(
        organization_id=clients.org_id,
        target_role_id=target_role_id,
        service_instance_scope_id=service_instance_scope_id,
    )
    print_item(result)


@roles.command()
@click.argument("target_role_id")
@click.argument("service_instance_scope_id")
@click.pass_obj
def delete_scope(clients: Clients, target_role_id: int, service_instance_scope_id: int) -> None:
    """Remove service instance scope from role"""
    clients.contxt_access.delete(
        f"{clients.org_id}/roles/{target_role_id}/scopes/{service_instance_scope_id}"
    )
