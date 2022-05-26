from typing import List, Optional

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import OPTIONAL_PROMPT_KWARGS, fields_option, print_item, print_table, sort_option
from contxt.models.contxt import ProjectEnvironment


@click.group()
def project_envs() -> None:
    """Projects Environments."""


@project_envs.command()
@click.argument("project_slug")
@click.pass_obj
@fields_option(default="id, slug, name, type, description", obj=ProjectEnvironment)
@sort_option(default="id")
def get(clients: Clients, project_slug: str, fields: List[str], sort: str) -> None:
    """Get project environment(s)"""
    result = clients.contxt_deployments.get(f"{clients.org_id}/projects/{project_slug}/environments")

    if "cluster_slug" in fields:
        clusters = clients.contxt_deployments.get_clusters(clients.org_id)
        for r in result:
            r["cluster_slug"] = next(c.slug for c in clusters if c.id == r["cluster_id"])

    print_table(result, keys=fields, sort_by=sort)


@project_envs.command()
@click.option("--project-slug", prompt=True)
@click.option("--name", prompt=True)
@click.option("--slug", prompt=True)
@click.option("--description", **OPTIONAL_PROMPT_KWARGS)
@click.option(
    "--type", type=click.Choice(["production", "nonproduction"]), default="nonproduction", prompt=True
)
@click.option("--cluster-id", prompt=True)
@click.option(
    "--deployment-strategy",
    type=click.Choice(["contxt-managed", "self-managed"]),
    default="self-managed",
    prompt=True,
)
@click.pass_obj
def create(
    clients: Clients,
    project_slug: str,
    name: str,
    slug: str,
    description: Optional[str],
    type: str,
    cluster_id: str,
    deployment_strategy: str,
) -> None:
    """Create a project environment"""
    result = clients.contxt_deployments.post(
        f"{clients.org_id}/projects/{project_slug}/environments",
        {
            "cluster_id": cluster_id,
            "slug": slug,
            "name": name,
            "type": type,
            "deployment_strategy": deployment_strategy,
            "description": description,
        },
    )
    print_item(result)


@project_envs.command()
@click.argument("project_slug")
@click.argument("curr_slug", metavar="SLUG")
@click.option("--name")
@click.option("--slug")
@click.option("--type")
@click.option("--cluster-id")
@click.option("--deployment-strategy")
@click.option("--description")
@click.pass_obj
def update(
    clients: Clients,
    project_slug: str,
    curr_slug: str,
    cluster_id: Optional[str],
    slug: Optional[str],
    name: Optional[str],
    type: Optional[str],
    deployment_strategy: Optional[str],
    description: Optional[str],
) -> None:
    """Update a project environment"""
    clients.contxt_deployments.put(
        f"{clients.org_id}/projects/{project_slug}/environments/{curr_slug}",
        {
            "name": name,
            "slug": slug,
            "type": type,
            "cluster_id": cluster_id,
            "deployment_strategy": deployment_strategy,
            "description": description,
        },
    )


@project_envs.command()
@click.argument("project_slug")
@click.argument("slug")
@click.pass_obj
def delete(clients: Clients, project_slug: str, slug: str) -> None:
    """Delete a project environment"""
    clients.contxt_deployments.delete(f"{clients.org_id}/projects/{project_slug}/environments/{slug}")
