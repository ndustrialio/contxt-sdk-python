from typing import List, Optional

import click
import yaml
from requests.exceptions import HTTPError

from contxt.cli.clients import Clients
from contxt.cli.utils import fields_option, print_item, print_table, sort_option
from contxt.models.contxt import Cluster

AWS_CERT = """LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUN5RENDQWJDZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQk
FRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJd01EZ3lNVEEwTVRNME1Wb1hEVE13TURneE9UQTBNVE
0wTVZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2
dnRUJBTHJBCm83STNYaDRWTHRXZnljcVF6bjJ2ZTR5MnJzQWMxaDZYai9BQnVacmxLZklXcXRUQVllLzQvL012QTh1UmJnRkQKYV
UvbForR0EyaGxqMVQ2L1N2dUc1WXRrMTNZaGxwMUxBT0R6VVNxaVpiRUhqTHQzcXMrTVRaSzRRSUdRdUROSgpLUEh6RGVQckt2dF
ZuM2lnZ2ZSRW1EdzJaUjNncXBmaEZQSUtSWnlYNDBXUitUSis4eGlHaGwxVk84a1hSSDdBCmNGR056KzlsNWtLTTltZHJva3FTRW
FROW5relBzVEpQK2JKWnQxMWlnVndneGFmQkNYeVRPLzdMSGJKTEZtdEgKQlc5QWtEQU05ODkvd3ZGN3BCcWEvbERGMWR4Z3M4TG
ZyVkE4Uk1pN1NCRVo5eUJqa20yMFYxb1R0OVNybGdhSQpuRWRpQ0RXcUJRZDhzS0ttTE9jQ0F3RUFBYU1qTUNFd0RnWURWUjBQQV
FIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFCSnlmV3pCd2diYnhOVH
JnaWx5V1pIcVlUaWEKc2JVTmV3eEdvWlZMYjJGS05wTytqMEZ6d2ZXSVFGMEVnYTNEZmZjOTB2LzBRdllPbmpZMDVGTUpoVUswTU
4xNApRUGhVdTl2YzhtTHd0ekF3NldSUGtldHBsa0FFb0VGVmxFMFMzQlR4M2lMOGFxUGZWajBkd0doZFFyMXNGTU5aCjdLQUdKaX
JMY2l1WXlnOHovWW50UkFrTjFyOU95SW95VitvSHJHbXI4Y2ZHazJjQWhWSTlMSHcwTTVnSWRiMVIKNVdKMDYzQ0FmK0xYd0drYT
RHdlFIUkhCcjZ1R0ZmVi9mdlJ1eXEwWDE1M2NMaDFRbmRwNkVocCtLWDQ1ekxhaQpHVXpkbHV2TlkwZzRad2YvTjR3clR4YXFhTG
c5WEk1TTZJVFliRGZjajhSQzIzelA0Y1RWWnZ5QmZmQT0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=
""".replace(
    "\n", ""
)


@click.group()
def clusters() -> None:
    """Clusters"""


@clusters.command()
@click.argument("cluster_slug", required=False)
@fields_option(default=["id", "host", "slug"], obj=Cluster)
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
@click.argument("host")
@click.pass_obj
def login(clients: Clients, host: str) -> None:
    """Get clusters"""
    try:
        token = clients.auth.get_token_provider(audience=host).access_token
        clusters = clients.contxt_deployments.get_clusters(clients.org_id)
        cluster = next((cluster.slug for cluster in clusters if cluster.host == host), None)
        kubeconfig = {
            "kind": "Config",
            "apiVersion": "v1",
            "preferences": {},
            "current-context": cluster,
            "users": [{"name": cluster, "user": {"token": token}}],
            "clusters": [
                {
                    "name": cluster,
                    "cluster": {
                        "server": host,
                        "certificate-authority-data": AWS_CERT,
                    },
                }
            ],
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
    "--infrastructure-id",
    prompt=True,
    help="The ID of the infrastructure registered in "
    "our system. Ask ndustrial.io DevOps "
    "what this value should be",
)
@click.option("--region", prompt=True, help="The AWS region where this cluster is deployed")
@click.option(
    "--environment-type",
    type=click.Choice(["production", "nonproduction", "blended"]),
    default="production",
    prompt=True,
)
@click.pass_obj
def register(
    clients: Clients,
    description: str,
    infrastructure_id: int,
    region: str,
    slug: str,
    host: str,
    environment_type: str,
) -> None:
    result = clients.contxt_deployments.post(
        f"{clients.org_id}/clusters",
        json={
            "host": host,
            "slug": slug,
            "description": description,
            "region": region,
            "type": "kubernetes",
            "infrastructure_id": infrastructure_id,
            "environment_type": environment_type,
        },
    )
    print_item(result)
