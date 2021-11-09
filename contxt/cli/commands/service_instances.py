from typing import List, Optional

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import OPTIONAL_PROMPT_KWARGS, fields_option, print_item, print_table, sort_option
from contxt.models.contxt import ServiceInstance


@click.group()
def service_instances() -> None:
    """Service Instances."""


@service_instances.command()
@click.option("--service-id")
@click.pass_obj
@fields_option(default=["id", "slug", "service_id", "description"], obj=ServiceInstance)
@sort_option(default="slug")
def get(clients: Clients, service_id: Optional[str], fields: List[str], sort: str) -> None:
    """Get service instance(s)"""
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
