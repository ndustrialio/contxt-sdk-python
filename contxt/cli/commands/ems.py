from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import click

from contxt.cli.clients import Clients
from contxt.cli.utils import (
    LAST_WEEK,
    NOW,
    ClickPath,
    csv_callback,
    fields_option,
    print_table,
    sort_option,
)
from contxt.models.ems import MainService, ResourceType
from contxt.models.iot import Window
from contxt.utils.serializer import Serializer


@click.group()
def ems() -> None:
    """Energy Management System."""


@ems.command()
@click.argument("facility_id")
@click.option("--resource-type", type=ResourceType, default="electric", help="Resource type")
@fields_option(default="id, name, resource_type", obj=MainService)
@sort_option(default="id")
@click.pass_obj
def mains(
    clients: Clients, facility_id: int, resource_type: ResourceType, fields: List[str], sort: str
) -> None:
    """Get main services"""
    items = clients.ems.get_main_services(facility_id=facility_id, resource_type=resource_type)
    print_table(items=items, keys=fields, sort_by=sort)


@ems.command()
@click.argument("facility_id")
@click.option("--resource-type", type=ResourceType, default="electric", help="Resource type")
@click.option("--start", type=click.DateTime(), help="Start time")
@click.option("--end", type=click.DateTime(), help="End time")
@click.pass_obj
def main_data(
    clients: Clients, facility_id: int, resource_type: ResourceType, start: datetime, end: datetime
) -> None:
    """Get main service data"""
    data: Dict[datetime, Dict[str, Any]] = defaultdict(dict)
    services = clients.ems.get_main_services(facility_id=facility_id, resource_type=resource_type)
    with click.progressbar(
        services,
        label="Downloading main service data",
        item_show_func=lambda s: f"Service {s.name}" if s else "",
    ) as services_:
        for service in services_:
            for (t, v) in clients.iot.get_time_series_for_field(
                field=service.usage_field,
                start_time=start,
                end_time=end,
                window=Window.MINUTELY,
                per_page=5000,
            ):
                data[t][service.usage_field.field_human_name] = v

    # Dump
    print_table(items=data)


@ems.command()
@click.argument("facility_id")
@click.option("--resource-type", type=ResourceType, default="electric", help="Resource type")
@click.option("--start", type=click.DateTime(), default=LAST_WEEK.isoformat(), help="Start time")
@click.option("--end", type=click.DateTime(), default=NOW.isoformat(), help="End time")
@click.option(
    "--interval", type=click.Choice(["daily", "monthly"]), default="monthly", help="Time interval"
)
@click.pass_obj
def spend(
    clients: Clients,
    facility_id: int,
    resource_type: ResourceType,
    start: datetime,
    end: datetime,
    interval: str,
) -> None:
    """Get utility spend"""
    items = clients.ems.get_monthly_utility_spend(
        facility_id=facility_id, resource_type=resource_type, start_date=start, end_date=end
    )
    print_table(items=items)


@ems.command()
@click.argument("facility_id")
@click.option("--resource-type", type=ResourceType, default="electric", help="Resource type")
@click.option("--start", type=click.DateTime(), default=LAST_WEEK.isoformat(), help="Start time")
@click.option("--end", type=click.DateTime(), default=NOW.isoformat(), help="End time")
@click.option(
    "--interval", type=click.Choice(["daily", "monthly"]), default="daily", help="Time interval"
)
@click.pass_obj
def usage(
    clients: Clients,
    facility_id: int,
    resource_type: ResourceType,
    start: datetime,
    end: datetime,
    interval: str,
) -> None:
    """Get utility usage"""
    usage = clients.ems.get_usage(
        facility_id=facility_id, resource_type=resource_type, start=start, end=end, interval=interval
    )
    print_table(items=usage.values)


@ems.command()
@click.argument("facility_ids", nargs=-1)
@click.option(
    "--include",
    default="all",
    callback=csv_callback(options=["spend", "usage"]),
    help="Data to export",
)
@click.option("--start", type=click.DateTime(), default=LAST_WEEK.isoformat(), help="Start time")
@click.option("--end", type=click.DateTime(), default=NOW.isoformat(), help="End time")
@click.option("--output", type=ClickPath(file_okay=False), default=".", help="Path for output")
@click.pass_obj
def export(
    clients: Clients,
    facility_ids: List[int],
    include: List[str],
    start: datetime,
    end: datetime,
    output: Path,
) -> None:
    """Export data for facilities"""
    with click.progressbar(
        facility_ids, label="Downloading data", item_show_func=lambda f: f"Facility {f}" if f else ""
    ) as facility_ids_:
        for facility in clients.nionic.get_facilities():
            if facility.id not in facility_ids_:
                continue
            fpath = output / facility.slug

            # Utility usage
            if "usage" in include:
                usage = clients.ems.get_usage(
                    facility_id=facility.id, start=start, end=end, interval="daily"
                )
                Serializer.to_csv(usage.values, fpath / "ems" / "usage.csv")

            # Main service data
            if "mains" in include:
                data: Dict[datetime, Dict[str, Any]] = defaultdict(dict)
                services = clients.ems.get_main_services(facility_id=facility.id)
                for service in services:
                    for (t, v) in clients.iot.get_time_series_for_field(
                        field=service.usage_field,
                        start_time=start,
                        end_time=end,
                        window=Window.MINUTELY,
                        per_page=5000,
                    ):
                        data[t][service.usage_field.field_human_name] = v
                Serializer.to_csv(data, fpath / "ems" / "main_service_usage.csv")

    print(f"Wrote data to {output}")
