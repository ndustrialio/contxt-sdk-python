from contxt.services import ContxtService
from contxt.utils.serializer import Serializer

from .common import BaseParser, get_org_id


class Projects(BaseParser):
    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("projects", help="Contxt Projects")
        parser.set_defaults(func=self._get_projects)
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Get Project
        project_parser = _subparsers.add_parser("get", help="Get a project")
        project_parser.add_argument("project_id", help="Project ID")
        project_parser.set_defaults(func=self._get_project)

        # Services
        services_parser = _subparsers.add_parser("get-services", help="Get services for a project")
        services_parser.add_argument("project_id", help="Project ID")
        services_parser.set_defaults(func=self._get_services)

        # Edge Nodes
        edge_nodes_parser = _subparsers.add_parser("get-edge-nodes", help="Get edge nodes for a project")
        edge_nodes_parser.add_argument("project_id", help="Project ID")
        org_group = edge_nodes_parser.add_mutually_exclusive_group(required=True)
        org_group.add_argument("-i", "--org-id", help="Organization id")
        org_group.add_argument("-n", "--org-name", help="Organization name")
        edge_nodes_parser.set_defaults(func=self._get_edge_nodes)

        return parser

    def _get_project(self, args):
        contxt_service = ContxtService(args.auth)
        project = contxt_service.get_project(args.project_id)
        print(Serializer.to_pretty_cli(project))

    def _get_projects(self, args):
        contxt_service = ContxtService(args.auth)
        projects = contxt_service.get_projects()
        print(Serializer.to_table(projects, sort_by="created_at"))

    def _get_services(self, args):
        contxt_service = ContxtService(args.auth)
        services = contxt_service.get_services(args.project_id)
        print(Serializer.to_table(services))

    def _get_edge_nodes(self, args):
        org_id = args.org_id or get_org_id(args.org_name, args.auth)
        contxt_service = ContxtService(args.auth)
        nodes = contxt_service.get_edge_nodes(organization_id=org_id, project_id=args.project_id)
        print(Serializer.to_table(nodes))
