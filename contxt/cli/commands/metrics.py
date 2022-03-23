import click

from contxt.cli.clients import Clients
from contxt.cli.utils import Serializer


@click.group()
def metrics() -> None:
    """Metrics."""


@metrics.command()
@click.pass_obj
def labels(clients: Clients) -> None:
    """Get Metric Labels"""
    labels = clients.nionic.get_metric_labels()
    print(Serializer.to_table(labels))


@metrics.command()
@click.option(
    "--source-id",
    required=True,
    help="Organization ID, defaults to first value in token if not specified",
)
@click.option(
    "--label", required=True, help="Organization ID, defaults to first value in token if not specified"
)
@click.pass_obj
def data(clients: Clients, source_id: str, label: str) -> None:
    """Get facilities"""
    facilities = clients.nionic.get_metric_data(label, source_id)
    print(Serializer.to_table(facilities))
