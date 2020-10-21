import logging
from collections import defaultdict
from csv import DictReader, DictWriter
from datetime import datetime
from pathlib import Path
from typing import IO, Any, Dict, List, Optional, cast

import click
from requests import HTTPError

from contxt.cli.clients import Clients
from contxt.cli.utils import LAST_WEEK, NOW, ClickPath, fields_option, print_table, sort_option
from contxt.models.iot import Feed, Field, FieldGrouping, FieldValueType, Window
from contxt.utils.serializer import Serializer

NEW_FIELD_ATTRS = ["field_descriptor", "label", "value_type", "units", "grouping"]


@click.group()
def iot() -> None:
    """Internet-of-Things."""


@iot.group()
def fields() -> None:
    """IoT Fields"""


@iot.group()
def groupings() -> None:
    """IoT Field Groupings"""


@iot.group()
def data() -> None:
    """IoT Field Data"""


@iot.command()
@fields_option(default=["id", "key", "facility_id"], obj=Feed)
@sort_option(default="id")
@click.option(
    "--facility_id",
    required=False,
    type=int,
    help="Filter on Facility ID",
)
@click.pass_obj
def feeds(clients: Clients, fields: List[str], sort: str, facility_id: Optional[int]) -> None:
    """Get feeds"""
    items = clients.iot.get_feeds(facility_id=facility_id)
    print_table(items=items, keys=fields, sort_by=sort)


@fields.command()
@click.argument("feed_key", type=str)
@fields_option(default=["id", "feed_key", "name", "field_human_name"], obj=Field)
@sort_option(default="id")
@click.pass_obj
def get(clients: Clients, feed_key: str, fields: List[str], sort: str) -> None:
    """Get fields"""
    feed = clients.iot.get_feed_with_key(key=feed_key)
    if not feed:
        raise click.ClickException(f"Feed with key {feed_key} does not exist.")

    items = clients.iot.get_fields_for_feed(feed.id)
    print_table(items=items, keys=fields, sort_by=sort)


@groupings.command("get")
@click.argument("facility_id", type=int)
@fields_option(default=["id", "label", "slug", "description"], obj=FieldGrouping)
@sort_option(default="id")
@click.pass_obj
def groupings_get(clients: Clients, facility_id: int, fields: List[str], sort: str) -> None:
    """Get field groupings"""
    items = clients.iot.get_field_groupings_for_facility(facility_id)
    print_table(items=items, keys=fields, sort_by=sort)


@data.command()
@click.option("--output-id", required=True, type=int, help="Output ID to delete from")
@click.option(
    "--field-human-name", required=True, help="The field to delete from. Ex: power.demand, power.usage"
)
@click.option(
    "--interval",
    required=True,
    type=click.Choice([str(v.value) for v in Window]),
    callback=lambda ctx, param, value: Window(int(value)) if value is not None else None,
    help="Time interval",
)
@click.option(
    "--time",
    required=True,
    type=click.DateTime(),
    help="The timestamp of the datapoint. Ex: 2020-07-21T05:31:00Z",
)
@click.pass_obj
def delete(clients: Clients, output_id: int, field: str, interval: Window, time: datetime) -> None:
    """Delete a data point"""
    clients.iot.delete_time_series_point(output_id, field, interval, time)
    print("Data point deleted")


@data.command("get")
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
def data_get(
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


@fields.command()
@click.argument("feed_key")
@click.option("--input", required=True, type=click.File(), help="CSV of fields to create")
@click.pass_obj
def create(clients: Clients, feed_key: str, input: IO[str]) -> None:
    """Create (provision) fields"""
    # Get feed
    feed = clients.iot.get_feed_with_key(feed_key)
    if not feed:
        raise click.ClickException(f"Feed with key {feed_key} does not exist.")

    # Parse fields
    try:
        fields = [
            [
                Field(
                    feed_key=feed_key,
                    field_descriptor=r["field_descriptor"],
                    label=r["label"],
                    units=r["units"],
                    value_type=FieldValueType(r["value_type"].lower()),
                    is_hidden=False,
                ),
                r["grouping"],
            ]
            for r in DictReader(input)
        ]
    except KeyError:
        raise click.ClickException(f"The following columns are required: {NEW_FIELD_ATTRS}")

    # Provision fields
    curr_fields = {f.field_descriptor: f for f in clients.iot.get_fields_for_feed(feed.id)}
    with click.progressbar([t[0] for t in fields], label="Provisioning fields") as _fields:
        for i, field in enumerate(_fields):
            field = cast(Field, field)
            if field.field_descriptor not in curr_fields:
                # New field, create it
                fields[i][0] = clients.iot.provision_field_for_feed(feed.id, field)
            else:
                # Existing field, ignore it
                fields[i][0] = curr_fields[field.field_descriptor]

    # Add fields to grouping
    groupings = {g.slug: g for g in clients.iot.get_field_groupings_for_facility(feed.facility_id)}
    with click.progressbar(fields, label="Adding fields to groupings") as fields_:
        for (field, grouping_label) in fields_:
            grouping_slug = cast(str, grouping_label).lower().replace(" ", "-")
            field = cast(Field, field)
            if grouping_slug not in groupings:
                # New grouping, create it
                grouping = clients.iot.create_grouping(
                    facility_id=feed.facility_id,
                    label=grouping_label,
                    description=grouping_label,
                    is_public=True,
                    field_category_id=[],
                )
                groupings[grouping.slug] = grouping
            else:
                # Existing grouping, grab it
                grouping = groupings[grouping_slug]
            try:
                clients.iot.add_field_to_grouping(grouping.id, field.id)
            except HTTPError as e:
                logging.debug(e)


@fields.command()
@click.argument("feed_key")
@click.option("--output", type=click.File(mode="w"), help="Path for output")
@click.pass_obj
def unprovisioned(clients: Clients, feed_key: str, output: Optional[IO[str]]) -> None:
    """Get unprovisioned fields"""
    items = clients.iot.get_unprovisioned_fields_for_feed_key(feed_key)
    if not output:
        print_table(items=items or [], keys=["field_descriptor"])
    else:
        writer = DictWriter(output, fieldnames=NEW_FIELD_ATTRS)
        writer.writeheader()
        writer.writerows([{"field_descriptor": f.field_descriptor} for f in items])


@groupings.command("create")
@click.argument("facility_id")
@click.option("--label", required=True)
@click.option("--description", required=True)
@click.option("--is-public", required=True, type=bool)
@click.option("--field-category-id", required=True)
@click.pass_obj
def groupings_create(
    clients: Clients,
    facility_id: int,
    label: str,
    description: str,
    is_public: bool,
    field_category_id: str,
) -> None:
    """Create a new grouping"""
    grouping = clients.iot.create_grouping(
        facility_id=facility_id,
        label=label,
        description=description,
        is_public=is_public,
        field_category_id=[field_category_id],
    )
    print(grouping)


@groupings.command()
@click.argument("grouping_id")
@click.argument("field_id")
@click.pass_obj
def add_field(clients: Clients, grouping_id: str, field_id: str) -> None:
    """Add field to grouping"""
    grouping_field = clients.iot.add_field_to_grouping(grouping_id=grouping_id, field_id=field_id)
    print(grouping_field)


@fields.command("delete")
@click.argument("field_id", nargs=-1)
@click.pass_obj
def fields_delete(clients: Clients, field_id: List[str]):
    """Delete (unprovision) fields"""
    for id in field_id:
        clients.iot.unprovision_field(id)
