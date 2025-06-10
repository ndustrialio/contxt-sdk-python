from typing import List, Optional

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import fields_option, print_item, print_table, sort_option
from contxt.models.contxt import ServiceInstance, ServiceInstanceGrant, ServiceInstanceScope


@click.group()
def service_instances() -> None:
    """Service Instances."""


@service_instances.command()
@click.option("--service-id")
@click.pass_obj
@fields_option(default="id, slug, service_id, description", obj=ServiceInstance)
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
@click.option("--project-environment-id", required=False)
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


@service_instances.command()
@click.argument("from_service_instance_id")
@click.argument("to_service_instance_id")
@click.pass_obj
def add_grant(clients: Clients, from_service_instance_id: int, to_service_instance_id: int) -> None:
    """Add grant to service instance"""
    json = {"to_service_instance_id": to_service_instance_id}
    result = clients.contxt_deployments.post(
        f"{clients.org_id}/service_instances/{from_service_instance_id}/grants", json
    )
    print_item(result)


@service_instances.command()
@click.argument("service_instance_id")
@fields_option(default="id, from_service_instance_id, to_service_instance_id", obj=ServiceInstanceGrant)
@sort_option(default="id")
@click.pass_obj
def get_grants(clients: Clients, service_instance_id: str, fields: List[str], sort: str) -> None:
    """Get all service instance grants"""
    items = clients.contxt_deployments.get_service_instance_grants(
        clients.org_id, service_instance_id=service_instance_id
    )
    print_table(items=items, keys=fields, sort_by=sort)


@service_instances.command()
@click.argument("service_instance_id")
@fields_option(default="id, service_instance_id, label, description", obj=ServiceInstanceScope)
@sort_option(default="id")
@click.pass_obj
def get_scopes(clients: Clients, service_instance_id: str, fields: List[str], sort: str) -> None:
    """Get all service instance scopes"""
    items = clients.contxt_deployments.get_service_instance_scopes(
        clients.org_id, service_instance_id=service_instance_id
    )
    print_table(items=items, keys=fields, sort_by=sort)


@service_instances.command()
@click.option("--service_instance_id", prompt=True)
@click.option("--label", prompt=True)
@click.option("--description", prompt=True)
@click.pass_obj
def add_scope(clients: Clients, service_instance_id: int, label: str, description: str) -> None:
    """Create service instance scope"""
    json = {"label": label, "description": description}
    json = {k: v for k, v in json.items() if v is not None}
    result = clients.contxt_deployments.post(
        f"{clients.org_id}/service_instances/{service_instance_id}/scopes", json
    )
    print_item(result)


@service_instances.command()
@click.option("--service_instance_id", prompt=True)
@click.option(
    "--url_type",
    type=click.Choice(
        ["allowed_clients", "allowed_logout_urls", "allowed_origins", "callbacks", "web_origins"]
    ),
    prompt=True,
)
@click.option("--url", prompt=True)
@click.pass_obj
def add_url(clients: Clients, service_instance_id: int, url_type: str, url: str) -> None:
    """Add service instance url"""
    json = {"url_type": url_type, "url": url}
    json = {k: v for k, v in json.items() if v is not None}
    result = clients.contxt_deployments.post(
        f"{clients.org_id}/service_instances/{service_instance_id}/urls", json
    )
    print_item(result)
