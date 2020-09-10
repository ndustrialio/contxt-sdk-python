from contxt.services import ContxtService
from contxt.utils.serializer import Serializer

from .common import BaseParser


class Services(BaseParser):
    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("services", help="Contxt Services")
        parser.set_defaults(func=self._get_services)
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Get Service
        service_parser = _subparsers.add_parser("get", help="Get a service")
        service_parser.add_argument("service_id", help="Service ID")
        service_parser.set_defaults(func=self._get_service)

        return parser

    def _get_service(self, args):
        contxt_service = ContxtService(args.auth)
        service = contxt_service.get_service(args.service_id)
        print(Serializer.to_pretty_cli(service))

    def _get_services(self, args):
        contxt_service = ContxtService(args.auth)
        services = contxt_service.get_services()
        print(Serializer.to_table(services))
