from typing import Optional

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import print_item, print_table


@click.group()
def service_instances() -> None:
    """Service Instances."""


@service_instances.command()
@click.option("--service-id")
@click.pass_obj
def get(clients: Clients, service_id: Optional[str]) -> None:
    """Get service instance(s)"""
    items = (
        clients.contxt_deployments.get(f"{clients.org_id}/services/{service_id}/service_instances")
        if service_id
        else clients.contxt_deployments.get(f"{clients.org_id}/service_instances")
    )
    print_table(items, keys=["id", "slug", "service_id", "description"])


@service_instances.command()
@click.option("--service-id", prompt=True)
@click.option("--project-environment-id", prompt=True)  # optional?
@click.option("--name", prompt=True)
@click.option("--slug", prompt=True)
@click.option("--descriptor", prompt=True)
@click.option("--service-type", type=click.Choice(["API", "Application", "Worker"]), prompt=True)
@click.pass_obj
def create(
    clients: Clients,
    service_id: str,
    project_environment_id: str,
    name: str,
    slug: str,
    descriptor: str,
    service_type: str,
) -> None:
    """Create service instances"""
    result = clients.contxt_deployments.post(
        f"{clients.org_id}/services/{service_id}/service_instances",
        json={
            "project_environment_id": project_environment_id,
            "name": name,
            "slug": slug,
            "descriptor": descriptor,
            "service_type": service_type,
        },
    )
    print_item(result)


@service_instances.command()
@click.argument("id")
@click.pass_obj
def delete(clients: Clients, id: str) -> None:
    """Delete service instance"""
    clients.contxt_deployments.delete(f"{clients.org_id}/service_instances/{id}")
