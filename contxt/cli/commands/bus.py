from contxt.services import MessageBusService
from contxt.utils.serializer import Serializer

from .common import BaseParser, get_org_id


class Bus(BaseParser):
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
        stats_parser = _subparsers.add_parser("stats", help="View Message Bus Channel statistics")
        stats_organization_group = stats_parser.add_mutually_exclusive_group(required=True)
        stats_organization_group.add_argument("-I", "--org-id", help="Organization id")
        stats_organization_group.add_argument("-N", "--org-name", help="Organization name")
        stats_channel_group = stats_parser.add_mutually_exclusive_group(required=True)
        stats_channel_group.add_argument("-i", "--channel-id", help="Channel id")
        stats_channel_group.add_argument("-n", "--channel-name", help="Channel name")
        stats_parser.add_argument("service_id", help="Service id")
        stats_parser.set_defaults(func=self._stats)

        return parser

    def _channels(self, args):
        organization_id = args.org_id or get_org_id(args.org_name, args.auth)
        bus_service = MessageBusService(args.auth, organization_id)
        channels = bus_service.get_channels_for_service(args.service_id)
        print(Serializer.to_table(channels))

    def _stats(self, args):
        organization_id = args.org_id or get_org_id(args.org_name, args.auth)
        bus_service = MessageBusService(args.auth, organization_id)
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
