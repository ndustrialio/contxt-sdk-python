

class OrganizationNotFoundException(Exception):
    pass


class OrganizationArgumentException(Exception):
    pass


def find_organization_by_name(contxt_service, organization_name):

    organization = None
    for org in contxt_service.get_organizations():
        if org.name == organization_name:
            organization = org

    return organization


def get_organization_id_from_arguments(contxt_service, args):

    if args.organization_name:
        organization_object = find_organization_by_name(contxt_service=contxt_service,
                                                        organization_name=args.organization_name)
        if organization_object:
            organization_id = organization_object.id
        else:
            raise OrganizationNotFoundException("Organization not found")
    else:
        organization_id = args.organization_id

    return organization_id


def check_required_organization_args(args, org_is_required):

    if args.organization_id is not None and args.organization_name is not None:
        raise OrganizationArgumentException("Specify organization_id OR organization_name. Not both.")

    if org_is_required:
        if args.organization_id is None and args.organization_name is None:
            raise OrganizationArgumentException("Either organization_id OR organization_name is a required argument")
