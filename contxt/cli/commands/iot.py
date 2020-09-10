from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import LAST_WEEK, NOW, ClickPath, fields_option, print_table, sort_option
from contxt.models.iot import Feed, Field, FieldGrouping, Window
from contxt.utils.serializer import Serializer


@click.group()
def iot() -> None:
    """Internet-of-Things."""


@iot.command()
@fields_option(default=["id", "key", "facility_id"], obj=Feed)
@sort_option(default="id")
@click.pass_obj
def feeds(clients: Clients, fields: List[str], sort: str) -> None:
    """Get feeds"""
    items = clients.iot.get_feeds()
    print_table(items=items, keys=fields, sort_by=sort)


@iot.command()
@click.argument("facility_id", type=int)
@fields_option(default=["id", "feed_key", "name", "field_human_name"], obj=Field)
@sort_option(default="id")
@click.pass_obj
def fields(clients: Clients, facility_id: int, fields: List[str], sort: str) -> None:
    """Get fields"""
    items = clients.iot.get_fields_for_facility(facility_id)
    print_table(items=items, keys=fields, sort_by=sort)


@iot.command()
@click.argument("facility_id", type=int)
@fields_option(default=["id", "label", "slug", "description"], obj=FieldGrouping)
@sort_option(default="id")
@click.pass_obj
def groupings(clients: Clients, facility_id: int, fields: List[str], sort: str) -> None:
    """Get field groupings"""
    items = clients.iot.get_field_groupings_for_facility(facility_id)
    print_table(items=items, keys=fields, sort_by=sort)


@iot.command()
@click.argument("feed_id", type=int)
@click.option("--start", type=click.DateTime(), default=LAST_WEEK.isoformat(), help="Start time")
@click.option("--end", type=click.DateTime(), default=NOW.isoformat(), help="End time")
@click.option(
    "--interval",
    type=click.Choice([str(v.value) for v in Window]),
    default="3600",
    callback=lambda ctx, param, value: Window(int(value)) if value is not None else None,
    help="Time interval",
)
@click.option(
    "--output", type=ClickPath(dir_okay=False, writable=True), default="data.csv", help="Path for output"
)
@click.pass_obj
def data(
    clients: Clients, feed_id: str, start: datetime, end: datetime, interval: Window, output: Path
) -> None:
    """Get field data"""
    fields = clients.iot.get_fields_for_feed(feed_id)
    print(f"Fetching iot data for {len(fields)} tags from {start} to {end}")

    data: Dict[datetime, Dict[str, Any]] = defaultdict(dict)
    with click.progressbar(
        fields,
        label="Downloading iot data",
        item_show_func=lambda f: f"Field {f.field_human_name}" if f else "",
    ) as fields_:
        for field in fields_:
            for (t, v) in clients.iot.get_time_series_for_field(
                field=field, start_time=start, end_time=end, window=interval
            ):
                data[t][field.field_human_name] = v

    # Output to csv
    print(f"Writing data to {output}...")
    flat_data = [{"timestamp": k, **v} for k, v in data.items()]
    Serializer.to_csv(flat_data, output)
