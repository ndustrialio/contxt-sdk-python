import csv
import os
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import LAST_WEEK, NOW, ClickPath, fields_option, print_table, sort_option
from contxt.models.iot import Feed, Field, FieldGrouping, FieldValueType, Window
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
def delete_data_point(
    clients: Clients, output_id: int, field: str, interval: Window, time: datetime
) -> None:
    """Delete data point"""
    clients.iot.delete_time_series_point(output_id, field, interval, time)
    print("Data point deleted")


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


@iot.command()
@click.argument("feed_key", type=str)
@click.argument("worksheet_file", type=click.File("r"))
@click.pass_obj
def ingest_worksheet(clients: Clients, feed_key, worksheet_file) -> None:
    """Field Worksheet Ingestor"""
    feed = clients.iot.get_feed_with_key(feed_key)
    if not feed:
        print(f"Feed with key {feed_key} does not exist")
        return
    groupings_by_label = {}
    groupings = clients.iot.get_field_groupings_for_facility(feed.facility_id)
    for grouping in groupings:
        groupings_by_label[grouping.label] = grouping

    field_objs = []
    fields_for_feed = clients.iot.get_fields_for_feed(feed_id=feed.id)
    fields_descriptors_for_feed = [f.field_descriptor for f in fields_for_feed]

    desired_groupings_by_field = {}
    with worksheet_file as f:

        headers = [
            "Field Descriptor",
            "Label",
            "Data Type",
            "Units",
            "Scalar",
            "Cumulative Value?",
            "equipment group",
            "Facility Main?",
        ]
        reader = csv.DictReader(f, fieldnames=headers)

        # skip the header
        next(reader)

        # create a bunch of field objects
        for row in reader:
            if row["Label"].replace(" ", "").startswith("-"):
                label = row["equipment group"] + row["Label"]
            else:
                label = row["Label"]

            if row["Field Descriptor"] in fields_descriptors_for_feed:
                print(f'Already provisioned field with descriptor {row["Field Descriptor"]}')
            else:
                field_objs.append(
                    Field(
                        label=label,
                        output_id=feed.id,
                        field_descriptor=row["Field Descriptor"],
                        units=row["Units"],
                        field_human_name=row["Field Descriptor"],
                        feed_key=feed_key,
                        value_type=FieldValueType("numeric"),
                        is_hidden=False,
                    )
                )

            desired_groupings_by_field[row["Field Descriptor"]] = row["equipment group"]

    # go provision the fields
    for field_obj in field_objs:
        clients.iot.provision_field_for_feed(feed.id, field_obj)
        print(f"Provisioned: {field_obj.field_descriptor}")
    print("Done provisioning the fields")

    fields_for_feed = clients.iot.get_fields_for_feed(feed_id=feed.id)

    # organize the fields by their grouping names
    grouping_fields: Dict = {}
    for field in fields_for_feed:
        if field.field_descriptor in desired_groupings_by_field:
            grouping_name = desired_groupings_by_field[field.field_descriptor]
            if grouping_name.replace(" ", "") == "":
                continue
            if grouping_name not in grouping_fields:
                grouping_fields[grouping_name] = []
            grouping_fields[grouping_name].append(field.id)

        # go through organized listing, create grouping if necessary, update fields for grouping
        for grouping_name, field_ids in grouping_fields.items():
            grouping = groupings_by_label.get(grouping_name)

            if not grouping:
                print(f"Creating new grouping: {grouping_name}")
                grouping = clients.iot.create_grouping(
                    facility_id=feed.facility_id,
                    label=grouping_name,
                    description=grouping_name,
                    is_public=True,
                    field_category_id=[],
                )
                print(grouping)

            print(f"Setting {len(field_ids)} fields to grouping {grouping_name}")
            clients.iot.set_fields_for_grouping(grouping.id, field_ids)

        print("Successful!")


@iot.command()
@click.argument("feed_key", type=str)
@click.pass_obj
def create_worksheet(clients: Clients, feed_key) -> None:
    """Create Field Worksheets"""
    fields = clients.iot.get_unprovisioned_fields_for_feed_key(feed_key=feed_key)
    filename = f"{feed_key}_unprovisioned_worksheet.csv"

    with open(os.path.join(".", filename), "w") as f:

        headers = [
            "Field Descriptor",
            "Label",
            "Data Type",
            "Units",
            "Scalar",
            "Cumulative Value?",
            "equipment group",
            "Facility Main?",
        ]
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()

        for f in fields:
            row = {
                col_name: "" if col_name != "Field Descriptor" else f.field_descriptor  # type: ignore
                for col_name in headers
            }
            writer.writerow(row)

    print(f"Wrote unprovisioned fields to {filename}")


@iot.command()
@click.argument("facility_id", type=str)
@click.argument("label", type=str)
@click.argument("description", type=str)
@click.argument("is_public", type=bool)
@click.argument("field_category_id", type=int)
@click.pass_obj
def create_grouping(clients: Clients, facility_id, label, description, is_public, field_category_id):
    """Create a new IOT Grouping"""
    grouping = clients.iot.create_grouping(
        facility_id=facility_id,
        label=label,
        description=description,
        is_public=is_public,
        field_category_id=[field_category_id],
    )
    print(grouping)


@iot.command()
@click.argument("grouping_id", type=str)
@click.argument("field_id", type=str)
@click.pass_obj
def add_field_to_grouping(clients: Clients, grouping_id, field_id):
    """Add field to grouping"""
    grouping_field = clients.iot.add_field_to_grouping(grouping_id=grouping_id, field_id=field_id)
    print(grouping_field)
