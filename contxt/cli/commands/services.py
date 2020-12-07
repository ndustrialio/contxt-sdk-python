from typing import List, Optional

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import fields_option, print_table, sort_option
from contxt.models.contxt import Service, ServiceGrant, ServiceScope
from contxt.utils.serializer import Serializer


@click.group()
def services() -> None:
    """Contxt Services"""


@services.group()
def scopes() -> None:
    """Service Scopes"""


@services.group()
def dependencies() -> None:
    """Service Dependencies"""


def _get_dependency_info_for_scopes(clients: Clients, from_service_id: int, to_service_id: int):

    # retrieve the origin service
    from_service = clients.contxt.get_service(from_service_id)
    to_service = clients.contxt.get_service(to_service_id)

    # retrieve the dependencies of that service
    deps = clients.contxt.get_service_dependencies(from_service.id)

    print(deps)
    # find the dependency for this "to service"
    to_dependency = next((g for g in deps if int(g.to_service_id) == int(to_service.id)), None)
    if to_dependency is None:
        print(
            f"Service ID {from_service.id} ({from_service.name}) does not currently have a "
            f"dependency on Service ID {to_service.id} ({to_service.name}). You can add it via "
            f'the "contxt services dependencies add" CLI command'
        )
        return None, None, None

    to_service_scopes = {s.label: s for s in clients.contxt.get_service_scopes(to_service.id)}
    existing_dep_scopes = [e.label for e in to_dependency.ServiceScopes]

    return to_service_scopes, existing_dep_scopes, to_dependency


"""
Services Commands
"""


@services.command("get")
@click.argument("id", default="")  # HACK: make an optional argument
@fields_option(default=["id", "name", "service_type", "description"], obj=Service)
@sort_option(default="id")
@click.pass_obj
def get_services(clients: Clients, id: Optional[str], fields: List[str], sort: str) -> None:
    """Get service(s)"""
    items = [clients.contxt.get_service(id)] if id else clients.contxt.get_services()
    if id:
        print(Serializer.to_pretty_cli(items[0]))
    else:
        print_table(items=items, keys=fields, sort_by=sort)


"""
Scopes Commands
"""


@scopes.command("get")
@click.argument("service_id")
@fields_option(default=["label", "description"], obj=ServiceScope)
@sort_option(default="label")
@click.pass_obj
def get_scopes(clients: Clients, service_id: str, fields: List[str], sort: str) -> None:
    scopes = clients.contxt.get_service_scopes(service_id)
    print_table(items=scopes, keys=fields, sort_by=sort)


"""
Dependency Commands
"""


@dependencies.command("get")
@click.argument("service_id")
@click.pass_obj
def get_dependencies(clients: Clients, service_id: str) -> None:
    dependencies = clients.contxt.get_service_dependencies(service_id)
    objs = []
    for dep in dependencies:
        to_service = clients.contxt.get_service(dep.to_service_id)
        if len(dep.ServiceScopes):
            for row in dep.ServiceScopes:
                objs.append(
                    {
                        "to_service_id": dep.to_service_id,
                        "to_service_name": to_service.name,
                        "scope": row.label,
                        "description": row.description,
                    }
                )
        else:
            objs.append(
                {
                    "to_service_id": dep.to_service_id,
                    "to_service_name": to_service.name,
                    "scope": "<No Scopes>",
                    "description": "<No Scopes>",
                }
            )
    print(Serializer.to_table(objs))


@dependencies.command()
@click.option("--from-service-id", help="From Service ID", required=True)
@click.option("--to-service-id", help="To Service ID", required=True)
@click.pass_obj
def add(clients: Clients, from_service_id: int, to_service_id: int) -> None:
    from_service = clients.contxt.get_service(from_service_id)
    to_service = clients.contxt.get_service(to_service_id)

    print(f"Creating dependency between {from_service.name} -> {to_service.name}")
    grant = ServiceGrant(from_service_id=from_service.id, to_service_id=to_service.id)
    dep = clients.contxt.create_service_dependency(grant)
    print(Serializer.to_pretty_cli(dep))


@dependencies.command()
@click.option("--from-service-id", help="From Service ID", required=True)
@click.option("--to-service-id", help="To Service ID", required=True)
@click.pass_obj
def remove(clients: Clients, from_service_id: int, to_service_id: int) -> None:

    # fetch the services
    from_service = clients.contxt.get_service(from_service_id)
    to_service = clients.contxt.get_service(to_service_id)

    # fetch the org of the from service since we'll need it to call DELETE
    project = clients.contxt.get_project(from_service.stack_id)

    (_, _, existing_grant) = _get_dependency_info_for_scopes(clients, from_service_id, to_service_id)
    if not existing_grant:
        print("Dependency does not exist between specified services")
        return

    print(f"Removing dependency between {from_service.name} -> {to_service.name}")
    clients.deployments.remove_service_dependency(
        organization_id=project.organization_id, service_grant=existing_grant
    )
    print("Success!")


@dependencies.command()
@click.option("--from-service-id", help="From Service ID", required=True)
@click.option("--to-service-id", help="To Service ID", required=True)
@click.option("--scopes", help="Command-delimited list of scope labels to add", required=True)
@click.pass_obj
def add_scope(clients: Clients, from_service_id: int, to_service_id: int, scopes: str) -> None:

    (to_service_scopes, existing_dep_scopes, to_dep) = _get_dependency_info_for_scopes(
        clients, from_service_id, to_service_id
    )
    if to_dep is None:
        return

    intended_scopes = scopes.split(",")
    to_add = []
    for scope in intended_scopes:
        # check to make sure the scope is value
        if scope not in to_service_scopes:
            print(f'Invalid scope "{scope}" -- does not exist in to_service')
            continue
        if scope not in existing_dep_scopes:
            print(f"Adding scope {scope}")
            to_add.append(to_service_scopes[scope])
        else:
            print(f"{scope} already exists for dependency")

    for scope in to_add:
        r = clients.contxt.add_service_scope(to_dep, scope)
        print(r)


@dependencies.command()
@click.option("--from-service-id", help="From Service ID", required=True)
@click.option("--to-service-id", help="To Service ID", required=True)
@click.option("--scopes", help="Command-delimited list of scope labels to add", required=True)
@click.pass_obj
def remove_scope(clients: Clients, from_service_id: int, to_service_id: int, scopes: str) -> None:

    (to_service_scopes, existing_dep_scopes, to_dep) = _get_dependency_info_for_scopes(
        clients, from_service_id, to_service_id
    )

    if to_dep is None:
        return

    scopes_to_remove = scopes.split(",")
    to_remove = []
    for scope in scopes_to_remove:
        # check to make sure the scope actually exists
        if scope not in to_service_scopes:
            print(f'Invalid scope "{scope}" -- does not exist in to_service')
            continue
        if scope not in existing_dep_scopes:
            print(f"Scope {scope} is not currently granted in dependency -- doing nothing")
        else:
            to_remove.append(to_service_scopes[scope])

    for scope in to_remove:
        clients.contxt.remove_service_scope(to_dep, scope)
        print(f"Removed {scope}")
