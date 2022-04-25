from typing import List

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import fields_option, print_item, print_table, sort_option
from contxt.models.contxt import Service


@click.group()
def services() -> None:
    """Services."""


@services.command()
@click.argument("id", default="")  # HACK: make an optional argument
@click.pass_obj
@fields_option(default="id, slug, project_id, description", obj=Service)
@sort_option(default="slug")
def get(clients: Clients, id: str, fields: List[str], sort: str) -> None:
    """Get service(s)"""
    items = (
        [clients.contxt_deployments.get(f"{clients.org_id}/services/{id}")]
        if id
        else clients.contxt_deployments.get(f"{clients.org_id}/services")
    )
    print_table(items=items, keys=fields, sort_by=sort)


@services.command()
@click.option("--project-id", prompt=True)
@click.option("--slug", prompt=True)
@click.option("--type", type=click.Choice(["API", "Application", "Worker"]), prompt=True)
@click.option(
    "--deployment-strategy",
    type=click.Choice(["self-managed", "contxt-managed", "unmanaged"]),
    prompt=True,
)
@click.pass_obj
def create(clients: Clients, project_id: str, slug: str, type: str, deployment_strategy: str) -> None:
    """Create service"""
    result = clients.contxt_deployments.post(
        f"{clients.org_id}/services",
        json={
            "project_id": project_id,
            "slug": slug,
            "type": type,
            "deployment_strategy": deployment_strategy,
        },
    )
    print_item(result)


@services.command()
@click.argument("id")
@click.pass_obj
def delete(clients: Clients, id: str) -> None:
    """Delete service"""
    clients.contxt_deployments.delete(f"{clients.org_id}/services/{id}")
