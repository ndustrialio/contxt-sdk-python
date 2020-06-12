from contxt.models import Parsers
from contxt.models.ems import ResourceType
from contxt.services import EmsService, FacilitiesService, IotService

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
        md_parser.add_argument("facility_id", type=int, help="Facility ID")
        md_parser.add_argument("resource_type", type=ResourceType)
        md_parser.add_argument("start_time", type=Parsers.datetime, help="Start time")
        md_parser.add_argument("end_time", type=Parsers.datetime, help="End time")
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
        usage_group = usage_parser.add_mutually_exclusive_group(required=True)
        usage_group.add_argument("-f", "--facility-id", type=int, help="Facility id")
        usage_group.add_argument("-g", "--org-id", help="Organization id")
        usage_group.add_argument("-n", "--org-name", help="Organization name")
        usage_parser.add_argument("-o", "--output", help="Filename to save data (csv)")
        usage_parser.add_argument(
            "-p", "--pro-forma", action="store_true", help="Include pro forma calculations"
        )
        usage_parser.set_defaults(func=self._utility_usage)

        return parser

    def _mains(self, args):
        ems_service = EmsService(args.auth)
        main_services = ems_service.get_main_services(
            facility_id=args.facility_id, resource_type=args.resource_type
        )
        print(main_services)

    def _main_data(self, args):
        ems_service = EmsService(args.auth)
        iot_service = IotService(args.auth)
        services = ems_service.get_main_services(
            facility_id=args.facility_id, resource_type=args.resource_type
        )
        data = {
            service.name: iot_service.get_time_series_for_field(
                service.demand_field, start_time=args.start_time, end_time=args.end_time
            )
            for service in services
        }
        print(data)

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

    def _utility_usage(self, args):
        ems_service = EmsService(args.auth)
        if args.facility_id:
            # Get facility usage
            usage = ems_service.get_monthly_utility_usage(
                facility_id=args.facility_id,
                resource_type=args.resource_type,
                start_date=args.start_date,
                end_date=args.end_date,
                pro_forma=args.pro_forma,
            )
            print(usage)
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
