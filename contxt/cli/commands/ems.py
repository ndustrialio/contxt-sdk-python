from contxt.models import Parsers
from contxt.models.ems import ResourceType, UtilityUsage
from contxt.services import EmsService, FacilitiesService, IotService, UtilitiesService, \
    LegacyFilesService
from contxt.utils.serializer import Serializer
from contxt.models.iot import Window

import requests
import os
import csv
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
            '--download', action="store_true", help="Write main data to file in the data-exports directory"
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
        usage_parser.add_argument(
            '--download', action="store_true", help="Download all usage data"
        )
        usage_group = usage_parser.add_mutually_exclusive_group(required=True)
        usage_group.add_argument("-f" "--facility-ids", type=str, help="Facilities to get usage for")
        usage_group.add_argument("-g", "--org-id", help="Organization id")
        usage_group.add_argument("-n", "--org-name", help="Organization name")
        usage_parser.add_argument("-o", "--output", help="Filename to save data (csv)")
        usage_parser.add_argument(
            "-p", "--pro-forma", action="store_true", help="Include pro forma calculations"
        )
        usage_parser.set_defaults(func=self._utility_usage)

        # Utility Bills
        bills_parser = _subparsers.add_parser("bills", help="Get Utility Bills")
        bills_parser.add_argument("facility_ids", type=str, help="Facility to get bills for")
        bills_parser.add_argument(
            "--resource_type", type=ResourceType, help="Filter by type of resource"
        )
        bills_parser.add_argument(
            '--download', action="store_true", help="Download all PDF utility statements and their summaries"
        )
        bills_parser.set_defaults(func=self._bills)

        return parser

    def _mains(self, args):
        ems_service = EmsService(args.auth)
        main_services = ems_service.get_main_services(
            facility_id=args.facility_id, resource_type=args.resource_type
        )
        print(Serializer.to_table(main_services, exclude_keys=['usage_field', 'demand_field']))

    def _bills(self, args):
        utilities_service = UtilitiesService(args.auth)
        print(args.facility_ids)
        for facility_id in args.facility_ids.split(','):
            print(f'Exporting bills for facility {facility_id}')
            bills = utilities_service.get_statements(facility_id=facility_id)
            if args.download:
                self._download_pdf_statements(args, facility_id, bills, utilities_service)
            else:
                print(Serializer.to_table(bills, sort_by='interval_start'))

    #def _main_service_data(self, args):

    def _download_pdf_statements(self, args, facility_id, bills, utility_service):
        file_service = LegacyFilesService(args.auth)
        facilities_service = FacilitiesService(args.auth)

        # get the facility object so we can make the directory more readable
        try:
            facility_obj = facilities_service.get_facility_with_id(facility_id)
        except requests.exceptions.HTTPError:
            print('Facility not found')
            return

        print(f'Getting information for {facility_obj.name}')

        # build the directory structure
        facility_export_dir = f'./data-exports/{facility_obj.name}/'
        utilities_export_dir = os.path.join(facility_export_dir, 'utilities/')
        bill_export_dir = os.path.join(utilities_export_dir, 'bill-pdfs/')

        # ensure the exports directory is created
        os.makedirs(bill_export_dir, exist_ok=True)

        # get the account and meter information so we can map it from IDs to use in our export
        meters = {m.id: m for m in utility_service.get_meters(facility_id)}
        accounts = {a.id: a for a in utility_service.get_accounts(facility_id)}

        bill_summary_data = []
        unique_data_columns = ['account_number', 'meter_number', 'service_type', 'interval_start',
                               'interval_end', 'assigned_statement_year', 'assigned_statement_month',
                               'has_pdf_bill']

        for idx, bill in enumerate(bills):
            # go get some more information about this bill regarding charges, kw, etc.
            raw_bill_data = utility_service.get_statement_data(bill.id)
            '''
            Summary CSV:
            account_number, meter_number, service_type, interval_start, interval_end, 
            assigned_statement_year, assigned_statement_month, has_pdf_bill, <charges_and_units> ->>
            '''
            # add the general bill metadata
            bill_metadata = {
                'account_number': accounts[meters[bill.utility_meter_id].utility_account_id].label,
                'meter_number': meters[bill.utility_meter_id].label,
                'service_type': meters[bill.utility_meter_id].service_type,
                'interval_start': bill.interval_start,
                'interval_end': bill.interval_end,
                'assigned_statement_year': bill.statement_year,
                'assigned_statement_month': bill.statement_month
            }

            for row in raw_bill_data:

                row_label = f"[Total] {row['node_label']} ({row['units']})"
                # iterate over the bill data and add charge info to the metadata
                bill_metadata[row_label] = row['value']
                if row_label not in unique_data_columns:
                    unique_data_columns.append(row_label)

                for child_charge in row['children']:
                    child_label = f"[{row['node_label']}] {child_charge['node_label']} ({child_charge['units']})"
                    bill_metadata[child_label] = child_charge['value']

                    if child_label not in unique_data_columns:
                        unique_data_columns.append(child_label)

            # if a PDF of the bill is available, let's go fetch that
            if bill.file_id:
                print(f'Downloading bill {idx+1} out of {len(bills)} for '
                      f'{bill.statement_year}-{bill.statement_month}')
                bill_metadata['has_pdf_bill'] = True
                file_read = file_service.request_read_file(file_id=bill.file_id)
                try_count = 0
                while try_count < 3:
                    try:
                        r = requests.get(file_read.temporary_url)
                        file_download_path = os.path.join(bill_export_dir,
                                                          f'utility-bill-{bill.statement_year}-'
                                                          f'{bill.statement_month}.pdf')
                        with open(file_download_path, 'wb') as f:
                            f.write(r.content)
                        break
                    except Exception as e:
                        print(f'Exception raised during download {e}')
                        try_count += 1

            else:
                bill_metadata['has_pdf_bill'] = True
                print(f'No PDF for bill starting: {bill.statement_year}-{bill.statement_month}')
            bill_summary_data.append(bill_metadata)

        # Write all the metadata to a summary in a CSV file
        summary_file_path = os.path.join(utilities_export_dir, f'summary.csv')
        with open(summary_file_path, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=unique_data_columns)
            writer.writeheader()
            for row in bill_summary_data:
                for key in unique_data_columns:
                    if key not in row:
                        row[key] = ''
            writer.writerows(bill_summary_data)

    def _main_data(self, args):
        ems_service = EmsService(args.auth)
        iot_service = IotService(args.auth)
        facilities_service = FacilitiesService(args.auth)

        print(args.facility_ids)
        for facility_id in args.facility_ids.split(','):

            # get the facility object so we can make the directory more readable
            try:
                facility_obj = facilities_service.get_facility_with_id(facility_id)
            except requests.exceptions.HTTPError:
                print('Facility not found')
                continue

            print(f'Getting interval data for {facility_obj.id} -> {facility_obj.name}')
            try:
                services = ems_service.get_main_services(
                    facility_id=facility_id, resource_type=args.resource_type
                )
            except requests.exceptions.HTTPError:
                print('Facility not found in EMS service')
                continue

            data = {
                service.name: iot_service.get_time_series_for_field(
                    service.demand_field, start_time=args.start_time, end_time=args.end_time,
                    window=Window.MINUTELY, per_page=5000
                )
                for service in services
            }

            blended_data = {}
            for service_name, data in data.items():
                print(f"Getting data for {service_name}")
                for ts in data:
                    if ts[0] not in blended_data:
                        blended_data[ts[0]] = [ts[1]]
                    else:
                        blended_data[ts[0]].append(ts[1])

            summed_data = []
            skipped_count = 0
            for time, values in blended_data.items():
                if (len(values)) == len(services):
                    try:
                        summed_data.append({
                            'time': time,
                            'value': sum(values)
                        })
                    except Exception as e:
                        print(e)
                        print(values)
                else:
                    skipped_count += 1

            if args.download and len(summed_data) > 0:
                # build the directory structure
                facility_export_dir = f'./data-exports/{facility_obj.name}/'
                ems_export_dir = os.path.join(facility_export_dir, 'ems/')

                # ensure the exports directory is created
                os.makedirs(ems_export_dir, exist_ok=True)

                # Write all the metadata to a summary in a CSV file
                summary_file_path = os.path.join(ems_export_dir, f'minute_intervals.csv')
                with open(summary_file_path, 'w') as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=['time', 'value'])
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

    def _download_utility_usage(self, usage_data: UtilityUsage, args, facility_id,):
        facilities_service = FacilitiesService(args.auth)

        # get the facility object so we can make the directory more readable
        try:
            facility_obj = facilities_service.get_facility_with_id(facility_id)
        except requests.exceptions.HTTPError:
            print('Facility not found')
            return

        print(f'Writing information for {facility_obj.name}')

        # build the directory structure
        facility_export_dir = f'./data-exports/{facility_obj.name}/'
        ems_export_dir = os.path.join(facility_export_dir, 'ems/')

        # ensure the exports directory is created
        os.makedirs(ems_export_dir, exist_ok=True)

        # Write all the metadata to a summary in a CSV file
        summary_file_path = os.path.join(ems_export_dir, f'usage_summary.csv')
        with open(summary_file_path, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['time', 'value'])
            writer.writeheader()

            for data in usage_data.values:
                if data.value is not None:
                    writer.writerow({
                        'time': data.event_time,
                        'value': data.value
                    })


    def _utility_usage(self, args):
        ems_service = EmsService(args.auth)
        if args.f__facility_ids:
            print(args.f__facility_ids)
            for facility_id in args.f__facility_ids.split(','):
                print(f'Getting Utility usage for facility {facility_id}')
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
                    if (args.download):
                        self._download_utility_usage(usage, args, facility_id)
                    else:
                        print(Serializer.to_pretty_cli(usage))
                except requests.exceptions.HTTPError:
                    print('Facility not found')

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
