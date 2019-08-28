from contxt.utils import make_logger

logger = make_logger(__name__)


def _get_organization_id(name, auth):
    from contxt.services import ContxtService

    contxt_service = ContxtService(auth)
    return contxt_service.get_organization_with_name(name).id


def _to_csv(self, filename, items):
    from csv import DictWriter
    from pathlib import Path

    with Path(filename).open("w") as f:
        writer = DictWriter(f, fieldnames=vars(items[0]))
        writer.writeheader()
        for item in items:
            writer.writerow(vars(item))


class ContxtArgParser:
    def __init__(self, subparsers):
        self.parser = self._init_parser(subparsers)

    def _init_parser(self, subparsers):
        raise NotImplementedError

    def _help(self, args, auth):
        self.parser.print_help()

    def parse(self, args, auth):
        if "func" in args:
            args.func(args, auth)


class AuthParser(ContxtArgParser):
    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("auth", help="Authentication")
        parser.set_defaults(func=self._help)
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Login
        login_parser = _subparsers.add_parser("login", help="Login to contxt")
        login_parser.set_defaults(func=self._login)

        # Logout
        logout_parser = _subparsers.add_parser("logout", help="Logout of contxt")
        logout_parser.set_defaults(func=self._logout)

        return parser

    def _login(self, args, auth):
        auth.login()

    def _logout(self, args, auth):
        auth.logout()


class IotParser(ContxtArgParser):
    def _init_parser(self, subparsers):
        from contxt.models.iot import Window
        from contxt.models import Parsers
        from pathlib import Path

        parser = subparsers.add_parser("iot", help="IOT service")
        parser.set_defaults(func=self._help)
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Groupings
        groupings_parser = _subparsers.add_parser("groupings", help="Get groupings")
        groupings_parser.add_argument("facility_id", type=int, help="Facility id")
        groupings_parser.set_defaults(func=self._groupings)

        # Feeds
        feeds_parser = _subparsers.add_parser("feeds", help="Get feeds")
        feeds_parser.add_argument("-f", "--facility-id", type=int, help="Facility id")
        feeds_parser.set_defaults(func=self._feeds)

        # Fields
        fields_parser = _subparsers.add_parser("fields", help="Get fields")
        fields_group = fields_parser.add_mutually_exclusive_group(required=True)
        fields_group.add_argument("-f", "--facility-id", type=int, help="Facility id")
        fields_group.add_argument("-g", "--grouping-id", help="Grouping id")
        fields_parser.set_defaults(func=self._fields)

        # Unprovisioned Fields
        unprovisioned_fields_parser = _subparsers.add_parser(
            "unprovisioned", help="Unprovisioned fields"
        )

        feeds_group = unprovisioned_fields_parser.add_mutually_exclusive_group(
            required=True
        )
        feeds_group.add_argument("--feed_key", help="Provide feed key")
        feeds_group.add_argument("--feed_id", type=int, help="Provide feed id")

        unprovisioned_fields_parser.add_argument(
            "--output", help="Dump results to csv if desired"
        )
        unprovisioned_fields_parser.set_defaults(func=self._unprovisioned_fields)

        # Field data
        field_data_parser = _subparsers.add_parser("field-data", help="Get field data")
        field_data_parser.add_argument("grouping_id", help="Grouping id")
        field_data_parser.add_argument(
            "start_time", type=Parsers.datetime, help="Data start time"
        )
        field_data_parser.add_argument(
            "window", type=lambda x: Window(int(x)), help="Data windowing period"
        )
        field_data_parser.add_argument(
            "-e", "--end-time", type=Parsers.datetime, help="Data end time"
        )
        field_data_parser.add_argument(
            "-o", "--output", type=Path, help="File for output"
        )
        field_data_parser.set_defaults(func=self._field_data)

        return parser

    def _groupings(self, args, auth):
        from contxt.services import IotService

        iot_service = IotService(auth)
        groupings = iot_service.get_field_groupings_for_facility(args.facility_id)
        print(groupings)

    def _feeds(self, args, auth):
        from contxt.services import IotService

        iot_service = IotService(auth)
        feeds = iot_service.get_feeds(args.facility_id)
        print(feeds)

    def _fields(self, args, auth):
        from contxt.services import IotService

        iot_service = IotService(auth)
        if args.facility_id:
            # Get fields for facility
            fields = iot_service.get_fields_for_facility(args.facility_id)
        else:
            # Get fields for grouping
            fields = iot_service.get_field_grouping(args.grouping_id).fields
        print(fields)

    def _unprovisioned_fields(self, args, auth):
        from contxt.services import IotService

        iot_service = IotService(auth)
        fields = (
            iot_service.get_unprovisioned_fields_for_feed_id(args.feed_id)
            if args.feed_id
            else iot_service.get_unprovisioned_fields_for_feed_key(args.feed_key)
        )

        if args.output:
            _to_csv(args.output, fields)
        else:
            print(fields)

    def _field_data(self, args, auth):
        from contxt.services import IotService
        from contxt.utils.serializer import Serializer
        from tqdm import tqdm

        iot_service = IotService(auth)
        fields = iot_service.get_field_grouping(args.grouping_id).fields
        print(
            f"Fetching iot data for {len(fields)} tags for {args.start_time}"
            f" - {args.end_time}..."
        )
        try:
            field_data = {}
            for field in tqdm(fields):
                for d in iot_service.get_time_series_for_field(
                    field=field,
                    start_time=args.start_time,
                    end_time=args.end_time,
                    window=args.window,
                ):
                    field_data.setdefault(d[0], {})[field.field_human_name] = d[1]
        except MemoryError:
            print("ERROR: Ran out of memory. Trying fetching a smaller date range.")

        # Output to csv
        print(f"Writing field data to {args.output}...")
        data = [{"timestamp": k, **v} for k, v in field_data.items()]
        Serializer.to_csv(data, args.output)


class EmsParser(ContxtArgParser):
    def _init_parser(self, subparsers):
        from contxt.models.ems import ResourceType
        from contxt.models import Parsers

        parser = subparsers.add_parser("ems", help="EMS service")
        parser.set_defaults(func=self._help)
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Main Services
        mains_parser = _subparsers.add_parser("mains", help="Get Main Services")
        mains_parser.add_argument(
            "facility_id", type=int, help="Facility to get main services for"
        )
        mains_parser.add_argument(
            "--resource_type", type=ResourceType, help="Filter by type of resource"
        )
        mains_parser.set_defaults(func=self._get_mains)

        # Get Main Service Data
        md_parser = _subparsers.add_parser(
            "main-data", help="Get main service data for a facility"
        )
        md_parser.add_argument("facility_id", type=int, help="Facility ID")
        md_parser.add_argument("resource_type", type=ResourceType)
        md_parser.add_argument("start_time", type=Parsers.datetime, help="Start time")
        md_parser.add_argument("end_time", type=Parsers.datetime, help="End time")
        md_parser.set_defaults(func=self._get_main_data)

        # Spend
        spend_parser = _subparsers.add_parser("util-spend", help="Utility spend")
        spend_parser.add_argument(
            "interval", choices=["daily", "monthly"], help="Time interval"
        )
        spend_parser.add_argument(
            "resource_type", type=ResourceType, help="Type of resource"
        )
        spend_parser.add_argument("start_date", type=Parsers.date, help="Start date")
        spend_parser.add_argument("end_date", type=Parsers.date, help="End date")

        spend_group = spend_parser.add_mutually_exclusive_group(required=True)
        spend_group.add_argument("-f", "--facility-id", type=int, help="Facility id")
        spend_group.add_argument("-g", "--org-id", help="Organization id")
        spend_group.add_argument("-n", "--org-name", help="Organization name")

        spend_parser.add_argument("-o", "--output", help="Filename to save data (csv)")
        spend_parser.add_argument(
            "-p",
            "--pro-forma",
            action="store_true",
            help="Include pro forma calculations",
        )
        spend_parser.set_defaults(func=self._utility_spend)

        # Usage
        usage_parser = _subparsers.add_parser("util-usage", help="Utility usage")
        usage_parser.add_argument(
            "interval", choices=["daily", "monthly"], help="Time interval"
        )
        usage_parser.add_argument(
            "resource_type", type=ResourceType, help="Type of resource"
        )
        usage_parser.add_argument("start_date", type=Parsers.date, help="Start date")
        usage_parser.add_argument("end_date", type=Parsers.date, help="End date")

        usage_group = usage_parser.add_mutually_exclusive_group(required=True)
        usage_group.add_argument("-f", "--facility-id", type=int, help="Facility id")
        usage_group.add_argument("-g", "--org-id", help="Organization id")
        usage_group.add_argument("-n", "--org-name", help="Organization name")

        usage_parser.add_argument("-o", "--output", help="Filename to save data (csv)")
        usage_parser.add_argument(
            "-p",
            "--pro-forma",
            action="store_true",
            help="Include pro forma calculations",
        )
        usage_parser.set_defaults(func=self._utility_usage)

        return parser

    def _get_mains(self, args, auth):
        from contxt.services import EmsService

        ems_service = EmsService(auth)

        main_services = ems_service.get_main_services(
            facility_id=args.facility_id, resource_type=args.resource_type
        )
        print(main_services)

    def _get_main_data(self, args, auth):
        from contxt.services import EmsService, IotService

        ems_service = EmsService(auth)
        iot_service = IotService(auth)
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

    def _utility_spend(self, args, auth):
        from contxt.services import EmsService

        ems_service = EmsService(auth)

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
            from contxt.services import FacilitiesService

            organization_id = args.org_id or _get_organization_id(args.org_name, auth)
            facilities_service = FacilitiesService(auth)
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

    def _utility_usage(self, args, auth):
        from contxt.services import EmsService

        ems_service = EmsService(auth)

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
            from contxt.services import FacilitiesService

            organization_id = args.org_id or _get_organization_id(args.org_name, auth)
            facilities_service = FacilitiesService(auth)
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


class AssetsParser(ContxtArgParser):
    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("assets", help="Assets service")
        parser.set_defaults(func=self._help)
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Facilities
        # TODO: do we want this distinct from assets?
        fac_parser = _subparsers.add_parser("facilities", help="Get facility assets")
        fac_group = fac_parser.add_mutually_exclusive_group(required=True)
        fac_group.add_argument("-i", "--org-id", help="Organization id")
        fac_group.add_argument("-n", "--org-name", help="Organization name")
        fac_parser.set_defaults(func=self._facilities)

        # Asset types
        types_parser = _subparsers.add_parser("types", help="Get asset types")
        types_group = types_parser.add_mutually_exclusive_group(required=True)
        types_group.add_argument("-i", "--org-id", help="Organization id")
        types_group.add_argument("-n", "--org-name", help="Organization name")
        types_parser.add_argument("-t", "--type-label", help="Asset type label")
        types_parser.set_defaults(func=self._types)

        # Assets
        assets_parser = _subparsers.add_parser("assets", help="Get assets")
        assets_parser.add_argument("type_label", help="Asset type label")
        assets_group = assets_parser.add_mutually_exclusive_group(required=True)
        assets_group.add_argument("-i", "--org-id", help="Organization id")
        assets_group.add_argument("-n", "--org-name", help="Organization name")
        assets_parser.set_defaults(func=self._assets)

        # TODO: Attributes
        attr_parser = _subparsers.add_parser("attr", help="Get asset attributes")
        attr_parser.set_defaults(func=self._attributes)

        # TODO: Attribute values
        attr_vals_parser = _subparsers.add_parser(
            "attr-vals", help="Get asset attribute values"
        )
        attr_vals_parser.set_defaults(func=self._attribute_values)

        # TODO: Metrics
        metrics_parser = _subparsers.add_parser("metrics", help="Get asset metrics")
        metrics_parser.set_defaults(func=self._metrics)

        # Metric values
        metric_vals_parser = _subparsers.add_parser(
            "metric-vals", help="Get asset metric values"
        )
        metrics_group1 = metric_vals_parser.add_mutually_exclusive_group(required=True)
        metrics_group1.add_argument("-i", "--org_id", help="Organization id")
        metrics_group1.add_argument("-n", "--org_name", help="Organization name")
        metrics_group2 = metric_vals_parser.add_mutually_exclusive_group(required=True)
        metrics_group2.add_argument("-a", "--asset_id", help="Asset id")
        metrics_group2.add_argument("-t", "--type_label", help="Asset type label")
        metric_vals_parser.add_argument(
            "--metric_label", nargs="+", help="Metric label"
        )
        metric_vals_parser.add_argument(
            "-p", "--plot", action="store_true", help="Plot the values"
        )
        metric_vals_parser.set_defaults(func=self._metric_values)

        return parser

    def _facilities(self, args, auth):
        from contxt.services import FacilitiesService

        facilites_service = FacilitiesService(auth)

        organization_id = args.org_id or _get_organization_id(args.org_name, auth)
        facilities = facilites_service.get_facilities(organization_id)
        print(facilities)

    def _types(self, args, auth):
        from contxt.services import AssetsService

        organization_id = args.org_id or _get_organization_id(args.org_name, auth)
        assets_service = AssetsService(auth, organization_id)

        if not args.type_label:
            # Get all asset types
            asset_types = assets_service.types_by_id.values()
            print(asset_types)
        else:
            # Get single asset type
            asset_type = assets_service.asset_type_with_label(args.type_label)
            assets_service._cache_asset_type_full(asset_type)
            print(asset_type)

    def _assets(self, args, auth):
        from contxt.services import AssetsService

        organization_id = args.org_id or _get_organization_id(args.org_name, auth)
        assets_service = AssetsService(auth, organization_id)
        asset_type = assets_service.asset_type_with_label(args.type_label)
        assets = assets_service.get_assets(asset_type.id)
        print(assets)

    def _attributes(self, args, auth):
        raise NotImplementedError

    def _attribute_values(self, args, auth):
        raise NotImplementedError

    def _metrics(self, args, auth):
        raise NotImplementedError

    def _metric_values(self, args, auth):
        from contxt.services import AssetsService

        organization_id = args.org_id or _get_organization_id(args.org_name, auth)
        assets_service = AssetsService(auth, organization_id)

        if args.asset_id:
            # Get metric values for single asset
            asset = assets_service.get_complete_asset(args.asset_id)
            print(asset.metrics)
        else:
            # Get metric values for all assets of the specified type(s)
            asset_type = assets_service.asset_type_with_label(args.type_label)
            metrics = [
                assets_service.get_complete_asset(asset.id).metrics
                for asset in assets_service.get_assets(asset_type.id)
            ]
            if args.plot:
                raise NotImplementedError
            else:
                print(metrics)


class ContxtParser(ContxtArgParser):
    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("contxt", help="Contxt service")
        parser.set_defaults(func=self._help)
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Organizations
        orgs_parser = _subparsers.add_parser("orgs", help="Get organizations")
        orgs_parser.set_defaults(func=self._organizations)

        # Make organization
        create_org_parser = _subparsers.add_parser("mk-org", help="Create organization")
        create_org_parser.add_argument("org_name", help="Organization name")
        create_org_parser.set_defaults(func=self._create_organization)

        # Users
        users_parser = _subparsers.add_parser("users", help="Get users")
        users_group = users_parser.add_mutually_exclusive_group(required=True)
        users_group.add_argument("-i", "--org-id", help="Organization id")
        users_group.add_argument("-n", "--org-name", help="Organization name")
        users_parser.set_defaults(func=self._users)

        # Add users
        add_user_parser = _subparsers.add_parser(
            "add-user", help="Add user to an organization"
        )
        add_user_parser.add_argument("org_id", help="Organization id")
        add_user_parser.add_argument("user_id", help="User id")
        add_user_parser.set_defaults(func=self._add_user)

        return parser

    def _organizations(self, args, auth):
        from contxt.services.contxt import ContxtService
        from contxt.utils.serializer import Serializer

        contxt_service = ContxtService(auth)
        orgs = contxt_service.get_organizations()
        print(Serializer.to_table(orgs))

    def _create_organization(self, args, auth):
        from contxt.services import ContxtService
        from contxt.models.contxt import Organization

        contxt_service = ContxtService(auth)
        org = contxt_service.create_organization(Organization(args.org_name))
        contxt_service.add_user_to_organization(
            user_id=auth.user_id, organization_id=org.id
        )
        print(org)

    def _users(self, args, auth):
        from contxt.services import ContxtService

        contxt_service = ContxtService(auth)
        organization_id = args.org_id or _get_organization_id(args.org_name, auth)
        users = contxt_service.get_users_for_organization(organization_id)
        print(users)

    def _add_user(self, args, auth):
        from contxt.services.contxt import ContxtService

        contxt_service = ContxtService(auth)
        contxt_service.add_user_to_organization(
            user_id=args.user_id, organization_id=args.org_id
        )


class BusParser(ContxtArgParser):
    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("bus", help="Message bus service")
        parser.set_defaults(func=self._help)
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Channels
        channel_parser = _subparsers.add_parser("channels", help="Get channels")
        channel_group = channel_parser.add_mutually_exclusive_group(required=True)
        channel_group.add_argument("-I", "--org-id", help="Organization id")
        channel_group.add_argument("-N", "--org-name", help="Organization name")
        channel_parser.add_argument("service_id", help="Service id")
        channel_parser.set_defaults(func=self._channels)

        # Stats
        stats_parser = _subparsers.add_parser(
            "stats", help="View Message Bus Channel statistics"
        )
        stats_organization_group = stats_parser.add_mutually_exclusive_group(
            required=True
        )
        stats_organization_group.add_argument("-I", "--org-id", help="Organization id")
        stats_organization_group.add_argument(
            "-N", "--org-name", help="Organization name"
        )
        stats_channel_group = stats_parser.add_mutually_exclusive_group(required=True)
        stats_channel_group.add_argument("-i", "--channel-id", help="Channel id")
        stats_channel_group.add_argument("-n", "--channel-name", help="Channel name")
        stats_parser.add_argument("service_id", help="Service id")
        stats_parser.set_defaults(func=self._stats)

        return parser

    def _channels(self, args, auth):
        from contxt.services import MessageBusService
        from contxt.utils.serializer import Serializer

        organization_id = args.org_id or _get_organization_id(args.org_name, auth)
        bus_service = MessageBusService(auth, organization_id)
        channels = bus_service.get_channels_for_service(args.service_id)
        print(Serializer.to_table(channels))

    def _stats(self, args, auth):
        from contxt.services import MessageBusService

        organization_id = args.org_id or _get_organization_id(args.org_name, auth)
        bus_service = MessageBusService(auth, organization_id)
        channel_id = (
            args.channel_id
            or bus_service.get_channel_with_name_for_service(
                channel_name=args.channel_name, service_id=args.service_id
            ).id
        )
        stats = bus_service.get_stats_for_channel_and_service(
            channel_id=channel_id, service_id=args.service_id
        )
        print(stats)
