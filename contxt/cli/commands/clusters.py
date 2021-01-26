from typing import List, Optional

import click
import yaml
from requests.exceptions import HTTPError

from contxt.cli.clients import Clients
from contxt.cli.utils import fields_option, print_table, sort_option
from contxt.models.contxt import Cluster


def _get_org(clients: Clients, name: str):
    organization = clients.contxt.get_organization_with_name(name)
    if not organization:
        raise click.ClickException(f"Organization {name!r} does not exist.")
    return organization


@click.group()
def clusters() -> None:
    """Clusters"""


@clusters.command()
@click.argument("cluster_slug", required=False)
@click.option("--org", required=True, help="Org slug")
@fields_option(default=["id", "host", "slug"], obj=Cluster)
@sort_option(default="id")
@click.pass_obj
def get(clients: Clients, org: str, fields: List[str], sort: str, cluster_slug: Optional[str]) -> None:
    """Get clusters"""
    organization = _get_org(clients, org)
    items = (
        [clients.contxt_deployments.get_cluster(organization.id, cluster_slug)]
        if cluster_slug
        else clients.contxt_deployments.get_clusters(organization.id)
    )
    print_table(items=items, keys=fields, sort_by=sort)


@clusters.command()
@click.argument("host")
@click.option("--org", required=True, help="Org slug")
@click.pass_obj
def login(clients: Clients, host: str, org: str) -> None:
    """Get clusters"""
    try:
        token = clients.auth.get_token_provider(audience=host).access_token
        organization = _get_org(clients, org)
        clusters = clients.contxt_deployments.get_clusters(organization.id)
        cluster = next((cluster.slug for cluster in clusters if cluster.host == host), None)
        kubeconfig = {
            "kind": "Config",
            "apiVersion": "v1",
            "preferences": {},
            "current-context": cluster,
            "users": [{"name": cluster, "user": {"token": token}}],
            "clusters": [{"name": cluster, "cluster": {"server": host}}],
            "contexts": [
                {
                    "name": cluster,
                    "context": {"cluster": cluster, "namespace": "default", "user": cluster},
                }
            ],
        }
        print(yaml.safe_dump(kubeconfig))
    except HTTPError:
        pass


@clusters.command()
@click.argument("host")
@click.option("--org", required=True, help="Org slug")
@click.option(
    "--description",
    required=True,
    help="Information about what this cluster is for and " "what environment it belongs to",
)
@click.option(
    "--infrastructure-id",
    required=True,
    help="The ID of the infrastructure registered in "
    "our system. Ask ndustrial.io DevOps "
    "what this value should be",
)
@click.option("--region", required=True, help="The AWS region where this cluster is deployed")
@click.option(
    "--slug",
    required=True,
    help="The slugified name you would like to use for this cluster."
    " You will need to reference this in other commands so it's "
    "ideal to make this value easy to remember",
)
@click.option("--token", help="Used for legacy DC/OS clusters. Leave blank for K8S Clusters")
@click.pass_obj
def register(
    clients: Clients,
    org: str,
    description: str,
    infrastructure_id: int,
    region: str,
    slug: str,
    host: str,
    token: Optional[str],
):
    organization = _get_org(clients, org)

    cluster = Cluster(
        description=description,
        infrastructure_id=infrastructure_id,
        region=region,
        slug=slug,
        host=host,
        type="kubernetes",  # only supporting creation of new k8s clusters
        organization_id=organization.id,
    )

    clients.contxt_deployments.register_cluster(
        organization_id=organization.id, cluster=cluster, secret_bearer_token=token
    )
