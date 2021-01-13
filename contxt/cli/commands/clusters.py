from typing import Optional

import click

from contxt.cli.clients import Clients
from contxt.models.contxt import Cluster
from contxt.utils.serializer import Serializer
from requests.exceptions import HTTPError
from os import path


def fetch_organization_from_name(clients: Clients, organization_name: str):
    organization = clients.contxt.get_organization_with_name(organization_name)
    if not organization:
        raise click.ClickException(f"Organization with name {organization_name} does not exist.")
    return organization


@click.group()
def clusters() -> None:
    """Contxt Clusters"""


@clusters.command()
@click.argument("cluster_slug")
@click.option("--org", required=True)
@click.pass_obj
def get(clients: Clients, org: str, cluster_slug: str = None):
    organization = fetch_organization_from_name(clients, org)
    try:
        cluster = clients.deployments.get_cluster(organization.id, cluster_slug)
        print(Serializer.to_pretty_cli(cluster))
    except HTTPError as e:
        if e.response.status_code == 404:
            cluster_slugs = [cluster.slug for cluster in clients.deployments.get_clusters(organization.id)]
            print(f"Provided cluster slug '{cluster_slug}' was not found, available options include {cluster_slugs}")
        else:
            raise


@clusters.command()
@click.option("--org", required=True, help="Organization Name")
@click.option("--description", required=True, help="Information about what this cluster is for and "
                                                   "what environment it belongs to")
@click.option("--infrastructure-id", required=True, help="The ID of the infrastructure registered in "
                                                         "our system. Ask ndustrial.io DevOps "
                                                         "what this value should be")
@click.option("--region", required=True, help="The AWS region where this cluster is deployed")
@click.option("--slug", required=True, help="The slugified name you would like to use for this cluster."
                                            " You will need to reference this in other commands so it's "
                                            "ideal to make this value easy to remember")
@click.option("--host", help="If a Kubernetes cluster, this value should be the OIDC Proxy addressed "
                             "used for making K8S API Commands. ndustrial.io DevOps should provide "
                             "this value")
@click.option("--token", help="Used for legacy DC/OS clusters. Leave blank for K8S Clusters")
@click.pass_obj
def register(
    clients: Clients,
    org: str,
    description: str,
    infrastructure_id: int,
    region: str,
    slug: str,
    host: Optional[str],
    token: Optional[str],
):
    organization = fetch_organization_from_name(clients, org)

    cluster = Cluster(
        description=description,
        infrastructure_id=infrastructure_id,
        region=region,
        slug=slug,
        host=host,
        type="kubernetes",  # only supporting creation of new k8s clusters
        organization_id=organization.id,
    )

    clients.deployments.register_cluster(
        organization_id=organization.id, cluster=cluster, secret_bearer_token=token
    )


@clusters.command()
@click.argument("filepath")
@click.pass_context
def register_from_file(ctx, filepath: str):
    if path.exists(filepath):
        argsdict = {}
        with open(filepath) as f:
            for line in f:
                (key, value) = line.split(" ", 1)
                argsdict[key.replace("-", "_")] = value.rstrip()
        ctx.invoke(register, **argsdict)
    else:
        print(f"Path {filepath} does not exist.")


@clusters.command()
@click.option("--org", required=True)
@click.argument("cluster_slug")
@click.pass_obj
def unregister(
    clients: Clients,
    org: str,
    cluster_slug: str,
):
    organization = fetch_organization_from_name(clients, org)

    if clients.auth.query_user(f"Are you sure you want to unregister cluster {cluster_slug}?"):
        clients.deployments.unregister_cluster(
            organization_id=organization.id, cluster=cluster_slug
        )