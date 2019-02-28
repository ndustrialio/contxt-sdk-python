class ArgParser:

    def __init__(self, subparsers):
        self.parser = self._init_parser(subparsers)

    def _init_parser(self, subparsers):
        raise NotImplementedError

    def parse(self, args, auth):
        if 'func' in args:
            args.func(args, auth)


class AuthParser(ArgParser):

    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("auth", help="Authentication")
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Login
        login_parser = _subparsers.add_parser("login", help="Login to contxt")
        login_parser.set_defaults(func=self._login)

        # Logout
        logout_parser = _subparsers.add_parser("logout", help="Logout of contxt")
        logout_parser.set_defaults(func=self._logout)

        return parser

    def _login(self, args, auth):
        # TODO: create separate auth class
        auth.login()

    def _logout(self, args, auth):
        auth.reset()


class IotParser(ArgParser):

    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("iot", help="IOT service")
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

        # Field data
        field_data_parser = _subparsers.add_parser("field-data", help="Get field data")
        field_data_parser.add_argument("grouping_id", help="Grouping id")
        field_data_parser.add_argument("start_date", help="Data start date")
        field_data_parser.add_argument("window", type=int, choices=[0, 60, 900, 3600], help="Data windowing period")
        field_data_parser.add_argument("-e", "--end-date", help="Data end date")
        field_data_parser.add_argument("-p", "--plot", action="store_true", help="Plot data")
        field_data_parser.set_defaults(func=self._field_data)

        return parser

    def _groupings(self, args, auth):
        from contxt.functions.iot import IOT
        iot = IOT(auth)
        groupings = iot.iot_service.get_all_groupings(args.facility_id)
        print(groupings)

    def _feeds(self, args, auth):
        from contxt.functions.iot import IOT
        iot = IOT(auth)
        feeds = iot.iot_service.get_all_feeds(args.facility_id)
        print(feeds)

    def _fields(self, args, auth):
        from contxt.functions.iot import IOT
        iot = IOT(auth)
        if args.facility_id:
            # Get fields for facility
            fields = iot.iot_service.get_all_fields(args.facility_id)
            print(fields)
        else:
            # Get fields for grouping
            fields = iot.get_fields_for_grouping(args.grouping_id)
            print(fields)

    def _field_data(self, args, auth):
        from contxt.functions.iot import IOT
        iot = IOT(auth)
        field_data = iot.get_field_data_for_grouping(
            grouping_id=args.grouping_id,
            start_date=args.start_date,
            window=args.window,
            end_date=args.end_date,
            plot=args.plot)


class EmsParser(ArgParser):

    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("ems", help="EMS service")
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Spend
        spend_parser = _subparsers.add_parser("util-spend", help="Utility spend")
        spend_group = spend_parser.add_mutually_exclusive_group(required=True)
        spend_group.add_argument("-f", "--facility-id", type=int, help="Facility id")
        spend_group.add_argument("-g", "--org-id", help="Organization id")
        spend_group.add_argument("-n", "--org-name", help="Organization name")
        spend_parser.add_argument("interval", choices=["daily", "monthly"], help="Time interval")
        spend_parser.add_argument("resource_type", choices=["electric", "gas", "combined"], help="Type of resource")
        spend_parser.add_argument("start_date", help="Start month (YYYY-MM)")
        spend_parser.add_argument("end_date", help="End month (YYYY-MM)")
        spend_parser.add_argument("-o", "--output", help="Filename to save data (csv)")
        spend_parser.add_argument("-p", "--pro-forma", action="store_true", help="Include pro forma calculations")
        spend_parser.set_defaults(func=self._utility_spend)

        # TODO: Usage
        usage_parser = _subparsers.add_parser("util-usage", help="Utility usage")
        usage_group = usage_parser.add_mutually_exclusive_group(required=True)
        usage_group.add_argument("-f", "--facility-id", type=int, help="Facility id")
        usage_group.add_argument("-g", "--org-id", help="Organization id")
        usage_group.add_argument("-n", "--org-name", help="Organization name")
        usage_parser.add_argument("interval", choices=["daily", "monthly"], help="Time interval")
        usage_parser.add_argument("resource_type", choices=["electric", "gas", "combined"], help="Type of resource")
        usage_parser.add_argument("start_date", help="Start month (YYYY-MM)")
        usage_parser.add_argument("end_date", help="End month (YYYY-MM)")
        usage_parser.add_argument("-o", "--output", help="Filename to save data (csv)")
        usage_parser.add_argument("-p", "--pro-forma", action="store_true", help="Include pro forma calculations")
        usage_parser.set_defaults(func=self._utility_usage)

        # TODO: Metrics (do we want to duplicate this?)
        metrics_parser = _subparsers.add_parser("util-metrics", help="Utility metrics")
        metrics_group = metrics_parser.add_mutually_exclusive_group(required=True)
        metrics_group.add_argument("-f", "--facility-id", type=int, help="Facility id")
        metrics_group.add_argument("-g", "--org-id", help="Organization id")
        metrics_group.add_argument("-n", "--org-name", help="Organization name")
        metrics_parser.add_argument("interval", choices=["daily", "monthly"], help="Time interval")
        metrics_parser.add_argument("resource_type", choices=["electric", "gas", "combined"], help="Type of resource")
        metrics_parser.add_argument("start_date", help="Start month (YYYY-MM)")
        metrics_parser.add_argument("end_date", help="End month (YYYY-MM)")
        metrics_parser.add_argument("-o", "--output", help="Filename to save data (csv)")
        metrics_parser.add_argument("-p", "--pro-forma", action="store_true", help="Include pro forma calculations")
        metrics_parser.set_defaults(func=self._utility_metrics)

        return parser

    def _utility_spend(self, args, auth):
        from contxt.functions.ems import EMS
        ems = EMS(auth)
        if args.facility_id:
            # Facility spend
            spend = ems.get_facility_spend(
                facility_id=args.facility_id,
                interval=args.interval,
                resource_type=args.resource_type,
                start_date=args.start_date,
                end_date=args.end_date,
                pro_forma=args.pro_forma)
            print(spend)
        else:
            # Organization spend
            ems.get_organization_spend(
                resource_type=args.resource_type,
                interval=args.interval,
                start_date=args.start_date,
                end_date=args.end_date,
                filename=args.output,
                pro_forma=args.pro_forma,
                organization_id=args.org_id,
                organization_name=args.org_name)

    def _utility_usage(self, args, auth):
        raise NotImplementedError

    def _utility_metrics(self, args, auth):
        raise NotImplementedError


class AssetsParser(ArgParser):

    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("assets", help="Assets service")
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
        attr_vals_parser = _subparsers.add_parser("attr-vals", help="Get asset attribute values")
        attr_vals_parser.set_defaults(func=self._attribute_values)

        # TODO: Metrics
        metrics_parser = _subparsers.add_parser("metrics", help="Get asset metrics")
        metrics_parser.set_defaults(func=self._metrics)

        # Metric values
        metric_vals_parser = _subparsers.add_parser("metric-vals", help="Get asset metric values")
        metrics_group1 = metric_vals_parser.add_mutually_exclusive_group(required=True)
        metrics_group1.add_argument("-i", "--org_id", help="Organization id")
        metrics_group1.add_argument("-n", "--org_name", help="Organization name")
        metrics_group2 = metric_vals_parser.add_mutually_exclusive_group(required=True)
        metrics_group2.add_argument("-a", "--asset_id", help="Asset id")
        metrics_group2.add_argument("-t", "--type_label", help="Asset type label")
        metric_vals_parser.add_argument("-m", "--metric_label", required=True, help="Metric label")
        metric_vals_parser.add_argument("-p", "--plot", action="store_true", help="Plot the values")
        metric_vals_parser.set_defaults(func=self._metric_values)

        return parser

    def _facilities(self, args, auth):
        from contxt.functions.facilities import Facilities
        facs = Facilities(auth)
        facilities = facs.get_all_facilities(
            organization_id=args.org_id,
            organization_name=args.org_name)
        print(facilities)

    def _types(self, args, auth):
        from contxt.functions.assets import Assets
        assets = Assets(auth)
        if not args.type_label:
            # Print meta data about all types
            types = assets.get_asset_types(
                organization_id=args.org_id,
                organization_name=args.org_name)
            print(types)
        else:
            # Print detailed data about specified type
            type_ = assets.get_asset_type_info(
                type=args.type_label,
                organization_id=args.org_id,
                organization_name=args.org_name)
            from contxt.cli.assets import Assets
            Assets.print_asset_type_handler(type_)

    def _assets(self, args, auth):
        from contxt.functions.assets import Assets
        assets = Assets(auth)
        assets_of_type = assets.get_assets_for_type(
            type=args.type_label,
            organization_id=args.org_id,
            organization_name=args.org_name)
        print(assets_of_type)

    def _attributes(self, args, auth):
        raise NotImplementedError

    def _attribute_values(self, args, auth):
        raise NotImplementedError

    def _metrics(self, args, auth):
        raise NotImplementedError

    def _metric_values(self, args, auth):
        if args.asset_id:
            from contxt.functions.assets import Assets
            assets = Assets(auth)
            metric_values = assets.get_metric_values_for_asset(
                metric=args.metric_label,
                asset_id=args.asset_id,
                organization_id=args.org_id,
                organization_name=args.org_name)
            from contxt.cli.assets import Assets
            Assets.print_asset_metric_values(metric_values)
        else:
            from contxt.functions.assets import Assets
            assets = Assets(auth)
            metric_values = assets.get_metric_values_for_asset_type(
                asset_type_label=args.type_label,
                metric_label=args.metric_label,
                organization_id=args.org_id,
                organization_name=args.org_name,
                plot=args.plot)
            print(metric_values)


class ContxtParser(ArgParser):

    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("contxt", help="Contxt service")
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
        add_user_parser = _subparsers.add_parser("add-user", help="Add user to an organization")
        add_user_parser.add_argument("org_id", help="Organization id")
        add_user_parser.add_argument("user_id", help="User id")
        add_user_parser.set_defaults(func=self._add_user)

        return parser

    def _organizations(self, args, auth):
        from contxt.services.contxt import ContxtService
        contxt_service = ContxtService(auth)
        orgs = contxt_service.get_organizations()
        print(orgs)

    def _create_organization(self, args, auth):
        from contxt.functions.organizations import Organizations
        orgs = Organizations(auth)
        orgs.create_organization(args.org_name)

    def _users(self, args, auth):
        from contxt.functions.organizations import Organizations
        orgs = Organizations(auth)
        users = orgs.get_organization_users(
            organization_id=args.org_id,
            organization_name=args.org_name)
        print(users)

    def _add_user(self, args, auth):
        from contxt.services.contxt import ContxtService
        contxt_service = ContxtService(auth)
        contxt_service.add_user_to_organization(
            user_id=args.user_id, organization_id=args.org_id)


class BusParser(ArgParser):

    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("bus", help="Message bus service")
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Channels
        channel_parser = _subparsers.add_parser("channels", help="Get channels")
        channel_group = channel_parser.add_mutually_exclusive_group(required=True)
        channel_group.add_argument("-i", "--org-id", help="Organization id")
        channel_group.add_argument("-n", "--org-name", help="Organization name")
        channel_parser.add_argument("service_id", help="Service id")
        channel_parser.set_defaults(func=self._channels)

        return parser

    def _channels(self, args, auth):
        from contxt.functions.bus import Bus
        bus = Bus(auth)
        channels = bus.get_all_channels_for_service(
            service_id=args.service_id,
            organization_id=args.org_id,
            organization_name=args.org_name)
