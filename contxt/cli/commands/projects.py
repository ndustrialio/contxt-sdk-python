from typing import Optional

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import OPTIONAL_PROMPT_KWARGS, print_item, print_table, sort_option


@click.group()
def projects() -> None:
    """Projects."""


@projects.command()
@click.argument("slug", default="")
@sort_option(default="slug")
@click.pass_obj
def get(clients: Clients, slug: Optional[str], sort: str) -> None:
    """Get project(s)"""
    items = (
        [clients.contxt_deployments.get(f"{clients.org_id}/projects/{slug}")]
        if slug
        else clients.contxt_deployments.get(f"{clients.org_id}/projects")
    )
    print_table(items=items, keys=["slug", "name", "type", "description"], sort_by=sort)


@projects.command()
@click.option("--name", prompt=True)
@click.option("--slug", **OPTIONAL_PROMPT_KWARGS)
@click.option("--type", type=click.Choice(["Core", "Custom"]), default="Custom", prompt=True)
@click.option("--description", **OPTIONAL_PROMPT_KWARGS)
@click.option("--owner-role-id", **OPTIONAL_PROMPT_KWARGS)
@click.pass_obj
def create(
    clients: Clients,
    name: str,
    description: str,
    type: str,
    slug: Optional[str],
    owner_role_id: Optional[str],
) -> None:
    """Create a project"""
    result = clients.contxt_deployments.post(
        f"{clients.org_id}/projects",
        {
            "name": name,
            "slug": slug,
            "description": description,
            "type": type,
            "owner_role_id": owner_role_id,
        },
    )
    print_item(result)


@projects.command()
@click.argument("curr_slug", metavar="SLUG")
@click.option("--name")
@click.option("--slug")
@click.option("--type")
@click.option("--description")
@click.pass_obj
def update(
    clients: Clients,
    curr_slug: str,
    name: Optional[str],
    slug: Optional[str],
    type: Optional[str],
    description: Optional[str],
) -> None:
    """Update a project"""
    clients.contxt_deployments.put(
        f"{clients.org_id}/projects/{curr_slug}",
        {"name": name, "slug": slug, "type": type, "description": description},
    )


@projects.command()
@click.argument("slug", default="")
@click.pass_obj
def delete(clients: Clients, slug: str) -> None:
    """Delete a project"""
    clients.contxt_deployments.delete(f"{clients.org_id}/projects/{slug}")
