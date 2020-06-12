from contxt.models.contxt import Organization
from contxt.services import ContxtService
from contxt.utils.serializer import Serializer

from .common import BaseParser, get_org_id


class Contxt(BaseParser):
    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("contxt", help="Contxt service")
        parser.set_defaults(func=self._help)
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Organizations
        orgs_parser = _subparsers.add_parser("orgs", help="Get organizations")
        orgs_parser.set_defaults(func=self._orgs)

        # Make organization
        create_org_parser = _subparsers.add_parser("mk-org", help="Create organization")
        create_org_parser.add_argument("org_name", help="Organization name")
        create_org_parser.set_defaults(func=self._mk_org)

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

    def _orgs(self, args):
        contxt_service = ContxtService(args.auth)
        orgs = contxt_service.get_organizations()
        print(Serializer.to_table(orgs))

    def _mk_org(self, args):
        contxt_service = ContxtService(args.auth)
        org = contxt_service.create_organization(Organization(args.org_name))
        contxt_service.add_user_to_organization(user_id=args.auth.user_id, organization_id=org.id)
        print(org)

    def _users(self, args):
        contxt_service = ContxtService(args.auth)
        organization_id = args.org_id or get_org_id(args.org_name, args.auth)
        users = contxt_service.get_users_for_organization(organization_id)
        print(users)

    def _add_user(self, args):
        contxt_service = ContxtService(args.auth)
        contxt_service.add_user_to_organization(user_id=args.user_id, organization_id=args.org_id)
