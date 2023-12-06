from datetime import datetime

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
    "--facility-id",
    required=True,
    help="Facility ID",
)
@click.option("--label", required=True, help="Facility ID")
@click.option("--start", required=True, type=click.DateTime())
@click.pass_obj
def data(clients: Clients, facility_id: int, label: str, start: datetime) -> None:
    """Get metric data"""
    results = clients.nionic.get_metric_data(label, facility_id, start.astimezone().isoformat())
    print(Serializer.to_table(results))
