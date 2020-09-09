import csv
import os
from pathlib import Path

import requests

from contxt.models import Parsers
from contxt.models.ems import ResourceType, UtilityUsage
from contxt.models.iot import Window
from contxt.services import EmsService, FacilitiesService, IotService, SisService
from contxt.utils.serializer import Serializer

from .common import BaseParser, get_org_id


class Ems(BaseParser):
    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("ems", help="EMS service")
        parser.set_defaults(func=self._help)
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Main Services
        mains_parser = _subparsers.add_parser("mains", help="Get Main Services")
        mains_parser.add_argument("facility_id", type=int, help="Facility to get main services for")
        mains_parser.add_argument(
            "--resource_type", type=ResourceType, help="Filter by type of resource"
        )
        mains_parser.set_defaults(func=self._mains)

        # Get Main Service Data
        md_parser = _subparsers.add_parser("main-data", help="Get main service data for a facility")
        md_parser.add_argument("facility_ids", type=str, help="Facilities to get main service data for")
        md_parser.add_argument("resource_type", type=ResourceType)
        md_parser.add_argument("start_time", type=Parsers.datetime, help="Start time")
        md_parser.add_argument("end_time", type=Parsers.datetime, help="End time")
        md_parser.add_argument(
            "--download",
            action="store_true",
            help="Write main data to file in the data-exports directory",
        )
        md_parser.set_defaults(func=self._main_data)

        # Spend
        spend_parser = _subparsers.add_parser("util-spend", help="Utility spend")
        spend_parser.add_argument("interval", choices=["daily", "monthly"], help="Time interval")
        spend_parser.add_argument("resource_type", type=ResourceType, help="Type of resource")
        spend_parser.add_argument("start_date", type=Parsers.date, help="Start date")
        spend_parser.add_argument("end_date", type=Parsers.date, help="End date")
        spend_group = spend_parser.add_mutually_exclusive_group(required=True)
        spend_group.add_argument("-f", "--facility-id", type=int, help="Facility id")
        spend_group.add_argument("-g", "--org-id", help="Organization id")
        spend_group.add_argument("-n", "--org-name", help="Organization name")
        spend_parser.add_argument("-o", "--output", help="Filename to save data (csv)")
        spend_parser.add_argument(
            "-p", "--pro-forma", action="store_true", help="Include pro forma calculations"
        )
        spend_parser.set_defaults(func=self._util_spend)

        # Usage
        usage_parser = _subparsers.add_parser("util-usage", help="Utility usage")
        usage_parser.add_argument("interval", choices=["daily", "monthly"], help="Time interval")
        usage_parser.add_argument("resource_type", type=ResourceType, help="Type of resource")
        usage_parser.add_argument("start_date", type=Parsers.date, help="Start date")
        usage_parser.add_argument("end_date", type=Parsers.date, help="End date")
        usage_parser.add_argument("--download", action="store_true", help="Download all usage data")
        usage_group = usage_parser.add_mutually_exclusive_group(required=True)
        usage_group.add_argument("-f", "--facility-ids", type=str, help="Facilities to get usage for")
        usage_group.add_argument("-g", "--org-id", help="Organization id")
        usage_group.add_argument("-n", "--org-name", help="Organization name")
        usage_parser.add_argument("-o", "--output", help="Filename to save data (csv)")
        usage_parser.add_argument(
            "-p", "--pro-forma", action="store_true", help="Include pro forma calculations"
        )
        usage_parser.set_defaults(func=self._utility_usage)

        # Utility Bills
        bills_parser = _subparsers.add_parser("bills", help="Get utility bills")
        facility_group = bills_parser.add_mutually_exclusive_group(required=True)
        facility_group.add_argument("-f", "--facility-ids", nargs="*", type=int, help="Facility ids")
        facility_group.add_argument("-n", "--org-name", help="Organization name")

        bills_parser.add_argument(
            "--start", type=Parsers.date, help="Start date of bills (format: YYYY-MM-DD)"
        )
        bills_parser.add_argument(
            "--end", type=Parsers.date, help="End date to bills (format: YYYY-MM-DD)"
        )
        bills_parser.add_argument("--output", type=Path, help="Directory to output PDF's and summaries")
        bills_parser.set_defaults(func=self._bills)

        return parser

    def _mains(self, args):
        ems_service = EmsService(args.auth)
        main_services = ems_service.get_main_services(
            facility_id=args.facility_id, resource_type=args.resource_type
        )
        print(Serializer.to_table(main_services, exclude_keys=["usage_field", "demand_field"]))

    def _bills(self, args):
        # Determine facilities
        facility_ids = args.facility_ids
        if not facility_ids:
            org_id = get_org_id(args.org_name, args.auth)
            facility_ids = [f.id for f in FacilitiesService(args.auth).get_facilities(org_id)]

        # Download
        print(f"Exporting bills for {len(facility_ids)} facilities")
        sis_api = SisService(args.auth)
        for facility_id in facility_ids:
            print(f"Exporting bills for facility {facility_id}")
            try:
                facility = FacilitiesService(args.auth).get_facility_with_id(facility_id)
            except requests.exceptions.HTTPError:
                print(f"Skipping facility {facility_id} (not found)")
                continue
            bills = sis_api.get_statements(facility_id=facility.id, start=args.start, end=args.end)
            if args.output:
                self._download_pdf_statements(sis_api, facility, args.output, bills)
            else:
                print(Serializer.to_table(bills, sort_by="interval_start"))

    def _download_pdf_statements(self, sis_api, facility, output, bills):
        print(f"Getting information for {facility.name}")
        # Build directory structure
        facility_dir = output / facility.slug
        utility_dir = facility_dir / "utilities"
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
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            writer.writerows(data)

    def _main_data(self, args):
        ems_service = EmsService(args.auth)
        iot_service = IotService(args.auth)
        facilities_service = FacilitiesService(args.auth)

        print(args.facility_ids)
        for facility_id in args.facility_ids.split(","):

            # get the facility object so we can make the directory more readable
            try:
                facility_obj = facilities_service.get_facility_with_id(facility_id)
            except requests.exceptions.HTTPError:
                print("Facility not found")
                continue

            print(f"Getting interval data for {facility_obj.id} -> {facility_obj.name}")
            try:
                services = ems_service.get_main_services(
                    facility_id=facility_id, resource_type=args.resource_type
                )
            except requests.exceptions.HTTPError:
                print("Facility not found in EMS service")
                continue

            data = {
                service.name: iot_service.get_time_series_for_field(
                    service.usage_field,
                    start_time=args.start_time,
                    end_time=args.end_time,
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
                if (len(values)) == len(services):
                    try:
                        summed_data.append({"time": time, "value": sum(values)})
                    except Exception as e:
                        print(e)
                        print(values)
                else:
                    skipped_count += 1

            if args.download and len(summed_data) > 0:
                # build the directory structure
                facility_export_dir = f"./data-exports/{facility_obj.name}/"
                ems_export_dir = os.path.join(facility_export_dir, "ems/")

                # ensure the exports directory is created
                os.makedirs(ems_export_dir, exist_ok=True)

                # Write all the metadata to a summary in a CSV file
                summary_file_path = os.path.join(ems_export_dir, "minute_intervals.csv")
                with open(summary_file_path, "w") as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=["time", "value"])
                    writer.writeheader()

                    for data in summed_data:
                        writer.writerow(data)
            else:
                print(Serializer.to_table(summed_data))

    def _util_spend(self, args):
        ems_service = EmsService(args.auth)
        if args.facility_id:
            # Get facility spend
            spend = ems_service.get_monthly_utility_spend(
                facility_id=args.facility_id,
                resource_type=args.resource_type,
                start_date=args.start_date,
                end_date=args.end_date,
                pro_forma=args.pro_forma,
            )
            print(spend)
        else:
            # Get organization spend
            organization_id = args.org_id or get_org_id(args.org_name, args.auth)
            facilities_service = FacilitiesService(args.auth)
            spend = {
                f: ems_service.get_monthly_utility_spend(
                    facility_id=f.id,
                    resource_type=args.resource_type,
                    start_date=args.start_date,
                    end_date=args.end_date,
                    pro_forma=args.pro_forma,
                )
                for f in facilities_service.get_facilities(organization_id)
            }
            print(spend)

    def _download_utility_usage(
        self, usage_data: UtilityUsage, args, facility_id,
    ):
        facilities_service = FacilitiesService(args.auth)

        # get the facility object so we can make the directory more readable
        try:
            facility_obj = facilities_service.get_facility_with_id(facility_id)
        except requests.exceptions.HTTPError:
            print("Facility not found")
            return

        print(f"Writing information for {facility_obj.name}")

        # build the directory structure
        facility_export_dir = f"./data-exports/{facility_obj.name}/"
        ems_export_dir = os.path.join(facility_export_dir, "ems/")

        # ensure the exports directory is created
        os.makedirs(ems_export_dir, exist_ok=True)

        # Write all the metadata to a summary in a CSV file
        summary_file_path = os.path.join(ems_export_dir, "usage_summary.csv")
        with open(summary_file_path, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["time", "value"])
            writer.writeheader()

            for data in usage_data.values:
                if data.value is not None:
                    writer.writerow({"time": data.event_time, "value": data.value})

    def _utility_usage(self, args):
        ems_service = EmsService(args.auth)
        if args.f__facility_ids:
            print(args.f__facility_ids)
            for facility_id in args.f__facility_ids.split(","):
                print(f"Getting Utility usage for facility {facility_id}")
                # Get facility usage
                try:
                    usage = ems_service.get_ems_usage(
                        facility_id=facility_id,
                        interval=args.interval,
                        resource_type=args.resource_type,
                        start_date=args.start_date,
                        end_date=args.end_date,
                        pro_forma=args.pro_forma,
                    )
                    if args.download:
                        self._download_utility_usage(usage, args, facility_id)
                    else:
                        print(Serializer.to_pretty_cli(usage))
                except requests.exceptions.HTTPError:
                    print("Facility not found")

        else:
            # Get organization usage
            organization_id = args.org_id or get_org_id(args.org_name, args.auth)
            facilities_service = FacilitiesService(args.auth)
            usage = {
                f: ems_service.get_monthly_utility_usage(
                    facility_id=f.id,
                    resource_type=args.resource_type,
                    start_date=args.start_date,
                    end_date=args.end_date,
                    pro_forma=args.pro_forma,
                )
                for f in facilities_service.get_facilities(organization_id)
            }
            print(usage)
