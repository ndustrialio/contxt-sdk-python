from contxt.services import ContxtService
from contxt.utils.serializer import Serializer
from contxt.models.contxt import ServiceGrant

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

        # Service scopes
        scopes_parser = _subparsers.add_parser("get-scopes", help="Get scopes for a service")
        scopes_parser.add_argument("service_id", help="Service ID")
        scopes_parser.set_defaults(func=self._get_service_scopes)

        # Dependencies
        dependencies_parser = _subparsers.add_parser("get-deps", help="Get dependencies for a service")
        dependencies_parser.add_argument("service_id", help="Service ID")
        dependencies_parser.set_defaults(func=self._get_dependencies)

        create_deps_parser = _subparsers.add_parser("add-dep", help="Create a new dependency for a service")
        create_deps_parser.add_argument("--service_id", help="From Service ID")
        create_deps_parser.add_argument("--to_service_id", help="To Service ID")
        create_deps_parser.set_defaults(func=self._create_dependency)

        add_dep_scope_parser = _subparsers.add_parser("add-dep-scope", help="Add scopes to a dependency")
        add_dep_scope_parser.add_argument("-s", "--service_id", help="The from service ID",
                                          required=True)
        add_dep_scope_parser.add_argument("-t", "--to_service_id", help="The \"to\" service ID",
                                          required=True)
        add_dep_scope_parser.add_argument("--scopes", help="Comma-delimited list of scope labels to add",
                                          required=True)
        add_dep_scope_parser.set_defaults(func=self._add_dep_scopes)

        remove_dep_scope_parser = _subparsers.add_parser("remove-dep-scope", help="Remove scopes to a "
                                                                                  "dependency")
        remove_dep_scope_parser.add_argument("-s", "--service_id", help="The from service ID",
                                          required=True)
        remove_dep_scope_parser.add_argument("-t", "--to_service_id", help="The \"to\" service ID",
                                          required=True)
        remove_dep_scope_parser.add_argument("--scopes", help="Comma-delimited list of scope labels to "
                                                              "remove", required=True)
        remove_dep_scope_parser.set_defaults(func=self._remove_dep_scopes)

        return parser

    '''
    Service CRUD
    '''
    def _get_service(self, args):
        contxt_service = ContxtService(args.auth)
        service = contxt_service.get_service(args.service_id)
        print(Serializer.to_pretty_cli(service))

    def _get_services(self, args):
        contxt_service = ContxtService(args.auth)
        services = contxt_service.get_services()
        print(Serializer.to_table(services))

    '''
    Service Scopes
    '''
    def _get_service_scopes(self, args):
        contxt_service = ContxtService(args.auth)
        scopes = contxt_service.get_service_scopes(args.service_id)
        print(Serializer.to_table(scopes, exclude_keys=['id', 'created_at', 'updated_at'], sort_by='label'))

    def _get_dependency_info_for_scopes(self, args, contxt_service):

        # retrieve the origin service
        from_service = contxt_service.get_service(args.service_id)
        to_service = contxt_service.get_service(args.to_service_id)

        # retrieve the dependencies of that service
        deps = contxt_service.get_service_dependencies(from_service.id)
        # find the dependency for this "to service"
        to_dependency = next((g for g in deps if g.to_service_id == to_service.id), None)
        if to_dependency is None:
            print(f'Service ID {from_service.id} ({from_service.name}) does not currently have a '
                  f'dependency on Service ID {to_service.id} ({to_service.name}). You can add it via '
                  f'the "add-dep" CLI command')
            return None, None, None

        to_service_scopes = {s.label: s for s in contxt_service.get_service_scopes(to_service.id)}
        existing_dep_scopes = [e.label for e in to_dependency.ServiceScopes]

        return to_service_scopes, existing_dep_scopes, to_dependency

    def _add_dep_scopes(self, args):
        contxt_service = ContxtService(args.auth)

        (to_service_scopes, existing_dep_scopes, to_dep) = self._get_dependency_info_for_scopes(args, contxt_service)
        if to_dep is None:
            return

        intended_scopes = args.scopes.split(',')
        to_add = []
        for scope in intended_scopes:
            # check to make sure the scope is value
            if scope not in to_service_scopes:
                print(f'Invalid scope "{scope}" -- does not exist in to_service')
                continue
            if scope not in existing_dep_scopes:
                print(f'Adding scope {scope}')
                to_add.append(to_service_scopes[scope])
            else:
                print(f'{scope} already exists for dependency')

        for scope in to_add:
            r = contxt_service.add_service_scope(to_dep, scope)
            print(r)

    def _remove_dep_scopes(self, args):
        contxt_service = ContxtService(args.auth)

        (to_service_scopes, existing_dep_scopes, to_dep) = self._get_dependency_info_for_scopes(args,
                                                                                                contxt_service)
        if to_dep is None:
            return

        scopes_to_remove = args.scopes.split(',')
        to_remove = []
        for scope in scopes_to_remove:
            # check to make sure the scope actually exists
            if scope not in to_service_scopes:
                print(f'Invalid scope "{scope}" -- does not exist in to_service')
                continue
            if scope not in existing_dep_scopes:
                print(f'Scope {scope} is not currently granted in dependency -- doing nothing')
            else:
                to_remove.append(to_service_scopes[scope])

        for scope in to_remove:
            contxt_service.remove_service_scope(to_dep, scope)
            print(f'Removed {scope}')

    '''
    Service Dependency Management
    '''
    def _get_dependencies(self, args):
        contxt_service = ContxtService(args.auth)
        dependencies = contxt_service.get_service_dependencies(args.service_id)

        objs = []
        for dep in dependencies:
            to_service = contxt_service.get_service(dep.to_service_id)
            if len(dep.ServiceScopes):
                for row in dep.ServiceScopes:
                    objs.append({
                        'to_service_id': dep.to_service_id,
                        'to_service_name': to_service.name,
                        'scope': row.label,
                        'description': row.description
                    })
            else:
                objs.append({
                    'to_service_id': dep.to_service_id,
                    'to_service_name': to_service.name,
                    'scope': '<No Scopes>',
                    'description': '<No Scopes>'
                })
        print(Serializer.to_table(objs))

    def _create_dependency(self, args):
        contxt_service = ContxtService(args.auth)
        from_service = contxt_service.get_service(args.service_id)
        to_service = contxt_service.get_service(args.to_service_id)

        print(f'Creating dependency between {from_service.name} -> {to_service.name}')
        grant = ServiceGrant(from_service_id=from_service.id, to_service_id=to_service.id)
        dep = contxt_service.create_service_dependency(grant)
        print(Serializer.to_pretty_cli(dep))
