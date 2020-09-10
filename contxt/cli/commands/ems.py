from csv import DictWriter
from datetime import datetime
from pathlib import Path
from typing import List

import click
import requests

from contxt.cli.utils import ClickPath, Clients, fields_option, print_table, sort_option
from contxt.models.ems import MainService, ResourceType
from contxt.models.iot import Window
from contxt.utils.serializer import Serializer


@click.group()
def ems() -> None:
    """Energy Management System."""


@ems.command()
@click.argument("facility_id")
@click.option("--resource-type", type=ResourceType, default="electric", help="Resource type")
@fields_option(default=["id", "name", "resource_type"], obj=MainService)
@sort_option(default="id")
@click.pass_obj
def mains(
    obj: Clients, facility_id: int, resource_type: ResourceType, fields: List[str], sort: str
) -> None:
    """Get main services"""
    items = obj.ems.get_main_services(facility_id=facility_id, resource_type=resource_type)
    print_table(items=items, keys=fields, sort_by=sort)


@ems.command()
@click.argument("facility_ids", nargs=-1)
@click.option("--resource-type", type=ResourceType, default="electric", help="Resource type")
@click.option("--start", type=click.DateTime(), help="Start time")
@click.option("--end", type=click.DateTime(), help="End time")
@click.option("--output", type=ClickPath(file_okay=False, dir_okay=True), help="Path for output")
@click.pass_obj
def main_data(
    obj: Clients,
    facility_ids: List[int],
    resource_type: ResourceType,
    start: datetime,
    end: datetime,
    output: Path,
) -> None:
    """Get main service data"""
    for i, id in enumerate(facility_ids):
        print(f"Fetching for facility {id} ({i + 1} of {len(facility_ids)})")

        # Get facility
        try:
            facility = obj.facilities.get_facility_with_id(id)
        except requests.exceptions.HTTPError:
            print(f"Skipping facility {id} (not found)")
            continue

        print(f"Getting interval data for {facility.id} -> {facility.name}")
        try:
            services = obj.ems.get_main_services(facility_id=id, resource_type=resource_type)
        except requests.exceptions.HTTPError:
            print("Facility not found in EMS service")
            continue

        data = {
            service.name: obj.iot.get_time_series_for_field(
                service.usage_field,
                start_time=start,
                end_time=end,
                window=Window.MINUTELY,
                per_page=5000,
            )
            for service in services
        }

        blended_data = {}
        for service_name, data in data.items():
            print(f"Getting data for {service_name}")
            data_counter = 0
            for ts in data:
                data_counter += 1
                if ts[0] not in blended_data:
                    blended_data[ts[0]] = [ts[1]]
                else:
                    blended_data[ts[0]].append(ts[1])
            print(f"Total points for service: {data_counter}")

        summed_data = []
        skipped_count = 0
        for time, values in blended_data.items():
            if len(values) == len(services):
                try:
                    summed_data.append({"time": time, "value": sum(values)})
                except Exception as e:
                    print(e)
            else:
                skipped_count += 1

        # Dump
        if not output:
            print(Serializer.to_table(summed_data))
        else:
            Serializer.to_csv(summed_data, Path(output) / facility.slug / "ems" / "minute_intervals.csv")


@ems.command()
@click.argument("facility_id")
@click.option("--resource-type", type=ResourceType, default="electric", help="Resource type")
@click.option("--start", type=click.DateTime(), help="Start time")
@click.option("--end", type=click.DateTime(), help="End time")
@click.option(
    "--interval", type=click.Choice(["daily", "monthly"]), default="monthly", help="Time interval"
)
@click.option("--output", type=ClickPath(file_okay=False, dir_okay=True), help="Path for output")
@click.pass_obj
def spend(
    obj: Clients,
    facility_id: int,
    resource_type: ResourceType,
    start: datetime,
    end: datetime,
    interval: str,
    output: Path,
) -> None:
    """Utility spend"""
    items = obj.ems.get_monthly_utility_spend(
        facility_id=facility_id, resource_type=resource_type, start_date=start, end_date=end
    )
    print_table(items=items)


@ems.command()
@click.argument("facility_ids", nargs=-1)
@click.option("--resource-type", type=ResourceType, default="electric", help="Resource type")
@click.option("--start", type=click.DateTime(), help="Start time")
@click.option("--end", type=click.DateTime(), help="End time")
@click.option(
    "--interval", type=click.Choice(["daily", "monthly"]), default="monthly", help="Time interval"
)
@click.option(
    "--output", type=ClickPath(file_okay=False, dir_okay=True), default=".", help="Path for output"
)
@click.pass_obj
def usage(
    obj: Clients,
    facility_ids: List[int],
    resource_type: ResourceType,
    start: datetime,
    end: datetime,
    interval: str,
    output: Path,
) -> None:
    """Utility usage"""
    with click.progressbar(
        facility_ids, label="Downloading usage", item_show_func=lambda f: f"Facility {f}" if f else "",
    ) as facility_ids_:
        for id in facility_ids_:
            # Get facility
            try:
                facility = obj.facilities.get_facility_with_id(id)
            except requests.exceptions.HTTPError:
                print(f"Skipping facility {id} (not found)")
                continue

            # Get usage
            usage = obj.ems.get_usage(
                facility_id=facility.id,
                interval=interval,
                resource_type=resource_type,
                start=start,
                end=end,
            )

            # Output
            if output:
                Serializer.to_csv(usage.values, output / facility.slug / "ems" / "usage.csv")
            else:
                print_table(items=usage.values)


@ems.command()
@click.option("--start", type=click.DateTime(), help="Start time")
@click.option("--end", type=click.DateTime(), help="End time")
@click.option("--interval", type=click.Choice(["daily", "monthly"]), help="Time interval")
@click.option("--output", type=ClickPath(file_okay=False, dir_okay=True), help="Path for output")
@click.pass_obj
def bills(
    obj: Clients,
    facility_ids: List[int],
    resource_type: ResourceType,
    start: datetime,
    end: datetime,
    interval: str,
    output: Path,
) -> None:
    """Get utility bills"""
    print(f"Exporting bills for {len(facility_ids)} facilities")
    for facility_id in facility_ids:
        print(f"Exporting bills for facility {facility_id}")
        try:
            facility = obj.assets.get_facility_with_id(facility_id)
        except requests.exceptions.HTTPError:
            print(f"Skipping facility {facility_id} (not found)")
            continue

        bills = obj.sis.get_statements(facility_id=facility.id, start=start, end=end)

        # Output
        if output:
            _download_pdf(obj.sis, facility, output, bills)
        else:
            print(Serializer.to_table(bills, sort_by="interval_start"))


def _download_pdf(sis_api, facility, output, bills):
    print(f"Getting information for {facility.name}")
    # Build directory structure
    utility_dir = output / facility.slug / "utilities"
    bill_dir = utility_dir / "bill-pdfs"
    bill_dir.mkdir(parents=True, exist_ok=True)

    # Build csv
    data = []
    accounts = {a.id: a for a in sis_api.get_accounts(facility.id)}
    meters = {m.id: m for m in sis_api.get_meters(facility.id)}
    for i, bill in enumerate(bills):
        print(f"Fetching bill {i + 1} of {len(bills)}")

        # Build row
        row = {
            "account_number": accounts[meters[bill.utility_meter_id].utility_account_id].label,
            "meter_number": meters[bill.utility_meter_id].label,
            "service_type": meters[bill.utility_meter_id].service_type,
            "interval_start": bill.interval_start,
            "interval_end": bill.interval_end,
            "assigned_month": f"{bill.statement_year}-{bill.statement_month}-1",
            **{
                f"{row['node_label'].lower()} ({row['units']})": row["value"]
                for row in sis_api.get_statement_data(bill.id)
            },
            "pdf": "",
        }

        # Download pdf
        if bill.file_id:
            try:
                pdf = sis_api.request_read_file(bill.file_id)
                path = bill_dir / f"{bill.id}.pdf"
                pdf.download(path)
                row["pdf"] = path
            except Exception as e:
                print(e)

        data.append(row)

    # Dump to csv
    columns = data[0].keys() if data else []
    with (utility_dir / "summary.csv").open("w") as f:
        writer = DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)
