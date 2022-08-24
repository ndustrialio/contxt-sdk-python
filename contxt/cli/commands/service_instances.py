from typing import List, Optional

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import OPTIONAL_PROMPT_KWARGS, fields_option, print_item, print_table, sort_option
from contxt.models.contxt import ServiceInstance, ServiceInstanceGrant, ServiceInstanceScope


@click.group()
def service_instances() -> None:
    """Service Instances."""


@service_instances.command()
@click.argument("SERVICE_INSTANCE_ID", type=int, required=False)
@click.option("--service-id")
@click.pass_obj
@fields_option(default="id, slug, service_id, description", obj=ServiceInstance)
@sort_option(default="slug")
def get(
    clients: Clients, service_instance_id: int, service_id: Optional[str], fields: List[str], sort: str
) -> None:
    """Get service instance(s)"""
    if service_instance_id:
        items = [clients.contxt_deployments.get_service_instance(clients.org_id, service_instance_id)]
    else:
        items = (
            clients.contxt_deployments.get(f"{clients.org_id}/services/{service_id}/service_instances")
            if service_id
            else clients.contxt_deployments.get(f"{clients.org_id}/service_instances")
        )
    print_table(items, keys=fields, sort_by=sort)


@service_instances.command()
@click.option("--service-id", prompt=True)
@click.option("--project-environment-id", **OPTIONAL_PROMPT_KWARGS)
@click.option("--name", prompt=True)
@click.option("--slug", prompt=True)
@click.option("--descriptor", prompt=True)
@click.option("--service-type", type=click.Choice(["API", "Application", "Worker"]), prompt=True)
@click.pass_obj
def create(
    clients: Clients,
    service_id: str,
    project_environment_id: Optional[str],
    name: str,
    slug: str,
    descriptor: str,
    service_type: str,
) -> None:
    """Create service instances"""
    json = {
        "name": name,
        "project_environment_id": project_environment_id,
        "slug": slug,
        "descriptor": descriptor,
        "service_type": service_type,
    }
    json = {k: v for k, v in json.items() if v is not None}
    result = clients.contxt_deployments.post(
        f"{clients.org_id}/services/{service_id}/service_instances", json
    )
    print_item(result)


@service_instances.command()
@click.argument("id")
@click.pass_obj
def delete(clients: Clients, id: str) -> None:
    """Delete service instance"""
    clients.contxt_deployments.delete(f"{clients.org_id}/service_instances/{id}")


"""
Scopes Commands
"""


@service_instances.command("scopes")
@click.argument("SERVICE_INSTANCE_ID")
@fields_option(default="label, description", obj=ServiceInstanceScope)
@sort_option(default="label")
@click.pass_obj
def scopes(clients: Clients, service_instance_id: str, fields: List[str], sort: str) -> None:
    """Get scopes for a specific service instance"""
    scopes = clients.contxt_deployments.get_service_instance_scopes(clients.org_id, service_instance_id)
    print_table(items=scopes, keys=fields, sort_by=sort)


"""
Dependency Commands
"""


@service_instances.command("deps")
@click.argument("SERVICE_INSTANCE_ID")
@click.pass_obj
def get_dependencies(clients: Clients, service_instance_id: str) -> None:
    """Get dependencies for a specific service instance"""
    dependencies = clients.contxt_deployments.get_service_instance_dependencies(
        clients.org_id, service_instance_id
    )
    objs = []
    for dep in dependencies:
        to_service = clients.contxt_deployments.get_service_instance(
            clients.org_id, dep.to_service_instance_id
        )
        if len(dep.ServiceInstanceScopes):
            for row in dep.ServiceInstanceScopes:
                objs.append(
                    {
                        "to_service_instance_id": dep.to_service_instance_id,
                        "to_service_instance_name": to_service.name,
                        "scope": row.label,
                        "description": row.description,
                    }
                )
        else:
            objs.append(
                {
                    "to_service_instance_id": dep.to_service_instance_id,
                    "to_service_instance_name": to_service.name,
                    "scope": "<No Scopes>",
                    "description": "<No Scopes>",
                }
            )
    print_table(
        items=objs,
        keys=["to_service_instance_id", "to_service_instance_name", "scope", "description"],
        sort_by="sort",
    )


@service_instances.command("add-dep")
@click.option("--from-id", help="From Service ID", required=True)
@click.option("--to-id", help="To Service ID", required=True)
@click.pass_obj
def add(clients: Clients, from_id: int, to_id: int) -> None:

    from_service = clients.contxt_deployments.get_service_instance(clients.org_id, from_id)
    to_service = clients.contxt_deployments.get_service_instance(clients.org_id, to_id)

    print(f"Creating dependency between {from_service.name} -> {to_service.name}")
    grant = ServiceInstanceGrant(
        from_service_instance_id=from_service.id, to_service_instance_id=to_service.id
    )
    dep = clients.contxt_deployments.create_service_dependency(clients.org_id, grant)
    print(dep)
