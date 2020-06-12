from contxt.services import AssetsService, FacilitiesService

from .common import BaseParser, get_org_id


class Assets(BaseParser):
    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("assets", help="Assets service")
        parser.set_defaults(func=self._help)
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Facilities
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

        # Metric values
        metric_vals_parser = _subparsers.add_parser("metric-vals", help="Get asset metric values")
        metrics_group1 = metric_vals_parser.add_mutually_exclusive_group(required=True)
        metrics_group1.add_argument("-i", "--org_id", help="Organization id")
        metrics_group1.add_argument("-n", "--org_name", help="Organization name")
        metrics_group2 = metric_vals_parser.add_mutually_exclusive_group(required=True)
        metrics_group2.add_argument("-a", "--asset_id", help="Asset id")
        metrics_group2.add_argument("-t", "--type_label", help="Asset type label")
        metric_vals_parser.add_argument("--metric_label", nargs="+", help="Metric label")
        metric_vals_parser.add_argument("-p", "--plot", action="store_true", help="Plot the values")
        metric_vals_parser.set_defaults(func=self._metric_vals)

        return parser

    def _facilities(self, args):
        facilites_service = FacilitiesService(args.auth)
        organization_id = args.org_id or get_org_id(args.org_name, args.auth)
        facilities = facilites_service.get_facilities(organization_id)
        print(facilities)

    def _types(self, args):
        organization_id = args.org_id or get_org_id(args.org_name, args.auth)
        assets_service = AssetsService(args.auth, organization_id)
        if not args.type_label:
            # Get all asset types
            asset_types = assets_service.types_by_id.values()
            print(asset_types)
        else:
            # Get single asset type
            asset_type = assets_service.asset_type_with_label(args.type_label)
            assets_service._cache_asset_type_full(asset_type)
            print(asset_type)

    def _assets(self, args):
        organization_id = args.org_id or get_org_id(args.org_name, args.auth)
        assets_service = AssetsService(args.auth, organization_id)
        asset_type = assets_service.asset_type_with_label(args.type_label)
        assets = assets_service.get_assets(asset_type.id)
        print(assets)

    def _metric_vals(self, args):
        organization_id = args.org_id or get_org_id(args.org_name, args.auth)
        assets_service = AssetsService(args.auth, organization_id)
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
