from typing import Optional

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import Serializer


@click.group()
def metrics() -> None:
    """Metrics."""


@metrics.command()
@click.option("--org-id", help="Organization ID, defaults to first value in token if not specified")
@click.option("--slug", help="Organization slug, overrides org-id if both are set")
@click.pass_obj
def labels(clients: Clients, org_id: Optional[str] = None, slug: Optional[str] = None) -> None:
    """Get Metric Labels"""
    labels = clients.nionic.get_metric_labels(org_id, slug)
    print(Serializer.to_table(labels))


@metrics.command()
@click.option("--org-id", help="Organization ID, defaults to first value in token if not specified")
@click.option("--slug", help="Organization slug, overrides org-id if both are set")
@click.option(
    "--source-id",
    required=True,
    help="Organization ID, defaults to first value in token if not specified",
)
@click.option(
    "--label", required=True, help="Organization ID, defaults to first value in token if not specified"
)
@click.pass_obj
def data(clients: Clients, source_id: str, label: str, org_id: Optional[str] = None, slug: Optional[str] = None) -> None:
    """Get facilities"""
    facilities = clients.nionic.get_metric_data(label, source_id, org_id, slug).nodes
    print(Serializer.to_table(facilities))
