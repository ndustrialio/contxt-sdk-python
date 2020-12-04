import click
from typing import Optional

from contxt.cli.clients import Clients
from contxt.models.contxt import Cluster
from contxt.utils.serializer import Serializer


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
def get(clients: Clients, org: str, cluster_slug: str):
    organization = fetch_organization_from_name(clients, org)
    cluster = clients.deployments.get_cluster(organization.id, cluster_slug)
    print(Serializer.to_pretty_cli(cluster))


@clusters.command()
@click.option("--description", required=True)
@click.option("--infrastructure_id", required=True)
@click.option("--region", required=True)
@click.option("--slug", required=True)
@click.option("--host")
@click.option("--token")
def register(clients: Clients, org: str, description: str, infrastructure_id: int, region: str,
             slug: str, host: Optional[str], token: Optional[str]):
    organization = fetch_organization_from_name(clients, org)

    cluster = Cluster(description=description,
                      infrastructure_id=infrastructure_id,
                      region=region,
                      slug=slug,
                      host=host,
                      type='kubernetes',    # only supporting creation of new k8s clusters
                      organization_id=organization.id)

    clients.deployments.register_cluster(organization_id=organization.id,
                                         cluster=cluster,
                                         secret_bearer_token=token)
