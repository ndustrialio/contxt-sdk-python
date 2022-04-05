from typing import List, Optional

import click
import yaml
from requests.exceptions import HTTPError

from contxt.cli.clients import Clients
from contxt.cli.utils import fields_option, print_item, print_table, sort_option
from contxt.models.contxt import Cluster


@click.group()
def clusters() -> None:
    """Clusters"""


@clusters.command()
@click.argument("cluster_slug", required=False)
@fields_option(default="id, host, slug", obj=Cluster)
@sort_option(default="id")
@click.pass_obj
def get(clients: Clients, fields: List[str], sort: str, cluster_slug: Optional[str]) -> None:
    """Get clusters"""
    (items, fields) = (
        ([clients.contxt_deployments.get_cluster(clients.org_id, cluster_slug)], None)  # type: ignore
        if cluster_slug
        else (clients.contxt_deployments.get_clusters(clients.org_id), fields)
    )
    print_table(items=items, keys=fields, sort_by=sort)


@clusters.command()
@click.argument("slug")
@click.pass_obj
def login(clients: Clients, slug: str) -> None:
    """Get cluster config"""
    try:
        clusters = clients.contxt_deployments.get_clusters(clients.org_id)
        cluster_host = next((cluster.host for cluster in clusters if cluster.slug == slug), None)
        if cluster_host is None:
            raise click.ClickException(f"Unable to locate cluster with the slug {slug}")

        config = clients.auth.get_cluster_config(cluster_host)
        print(yaml.safe_dump(config))
    except HTTPError:
        pass


@clusters.command()
@click.option("--host", prompt=True)
@click.option(
    "--slug",
    prompt=True,
    help="The slugified name you would like to use for this cluster."
    " You will need to reference this in other commands so it's "
    "ideal to make this value easy to remember",
)
@click.option(
    "--description",
    prompt=True,
    help="Information about what this cluster is for and what environment it belongs to",
)
@click.option(
    "--environment-type",
    type=click.Choice(["production", "nonproduction", "blended"]),
    default="production",
    prompt=True,
)
@click.option(
    "--certificate-authority",
    type=str,
    prompt=True,
    help="Base64 encoded certificate authority (CA) for the cluster",
)
@click.pass_obj
def register(
    clients: Clients,
    description: str,
    slug: str,
    host: str,
    environment_type: str,
    certificate_authority: str,
) -> None:
    result = clients.contxt_deployments.post(
        f"{clients.org_id}/clusters",
        json={
            "host": host,
            "slug": slug,
            "description": description,
            "type": "kubernetes",
            "environment_type": environment_type,
            "certificate_authority": certificate_authority,
        },
    )
    print_item(result)


@clusters.command()
@click.argument("curr_slug", metavar="SLUG")
@click.option("--host")
@click.option(
    "--description",
    help="Information about what this cluster is for and what environment it belongs to",
)
@click.option("--environment-type", type=click.Choice(["production", "nonproduction", "blended"]))
@click.option("--certificate-authority", type=str)
@click.pass_obj
def update(
    clients: Clients,
    curr_slug: str,
    host: Optional[str],
    description: Optional[str],
    environment_type: Optional[str],
    certificate_authority: Optional[str],
) -> None:
    """Update a cluster"""
    params = {
        k: v
        for k, v in {
            "host": host,
            "description": description,
            "environment_type": environment_type,
            "certificate_authority": certificate_authority,
        }.items()
        if v is not None
    }
    result = clients.contxt_deployments.put(
        f"{clients.org_id}/clusters/{curr_slug}",
        json=params,
    )
    print_item(result)
