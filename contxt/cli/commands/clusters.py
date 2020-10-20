from contxt.services import ContxtDeploymentService
from contxt.models.contxt import Cluster
from contxt.utils.serializer import Serializer
from contxt.auth.cli import ClusterAuth
import jwt
import json

from .common import BaseParser, get_org_id


class Clusters(BaseParser):
    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("clusters", help="Contxt Clusters")
        parser.add_argument("-n", "--org-name", help="Organization name", required=True)
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Get Cluster
        cluster_parser = _subparsers.add_parser("get", help="Get a cluster")
        cluster_parser.add_argument("cluster_slug", help="Cluster Slug")
        cluster_parser.set_defaults(func=self._get_cluster)

        # Create Cluster
        create_parser = _subparsers.add_parser("register", help="Register a new cluster")
        create_parser.add_argument("--description", required=True)
        create_parser.add_argument("--infrastructure_id", required=True)
        create_parser.add_argument("--region", required=True)
        create_parser.add_argument("--slug", required=True)
        create_parser.add_argument("--host")
        create_parser.add_argument("--type", required=True)
        create_parser.add_argument("--token", required=True)
        create_parser.set_defaults(func=self._register_cluster)

        # Login to Cluster
        login_parser = _subparsers.add_parser("login", help="Login to a cluster")
        login_parser.add_argument("cluster_slug", help="Cluster Slug")
        login_parser.set_defaults(func=self._login_to_cluster)

        return parser

    def _get_cluster(self, args):
        org_id = get_org_id(args.org_name, args.auth)
        contxt_service = ContxtDeploymentService(args.auth)
        cluster = contxt_service.get_cluster(org_id, args.cluster_slug)
        print(Serializer.to_pretty_cli(cluster))

    def _register_cluster(self, args):
        org_id = get_org_id(args.org_name, args.auth)
        contxt_service = ContxtDeploymentService(args.auth)
        cluster = Cluster(description=args.description,
                          infrastructure_id=args.infrastructure_id,
                          region=args.region,
                          slug=args.slug,
                          host=args.host,
                          type=args.type,
                          organization_id=org_id)

        contxt_service.register_cluster(organization_id=org_id,
                                        cluster=cluster,
                                        secret_bearer_token=args.token)

    def _login_to_cluster(self, args):
        CLUSTER_HARDCODE = {
            'cluster-1': 'LLYTn1WB9E7wg2US5gdppvfXZHI60GFX'
        }
        if args.cluster_slug not in CLUSTER_HARDCODE:
            print(f'Invalid cluster ID. Should be one of: {CLUSTER_HARDCODE.keys()}')
            return

        cluster_client_id = CLUSTER_HARDCODE[args.cluster_slug]

        auth = ClusterAuth(cluster_client_id)
        prov = auth.login()
        id_token = prov.token_info['id_token']

        print(id_token)
        decoded_id_token = jwt.decode(id_token, verify=False)
        print(json.dumps(decoded_id_token, indent=4))



