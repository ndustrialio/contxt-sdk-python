from contxt.exceptions import (
    OrganizationArgumentException,
    OrganizationNotFoundException,
)
from contxt.models.contxt import Organization
from contxt.services.contxt import ContxtService


def find_organization_by_name(contxt_service, organization_name):

    organization = None
    for org in contxt_service.get_organizations():
        if org.name.upper() == organization_name.upper():
            organization = org
            break

    return organization


def get_organization_id_from_arguments(
    contxt_service, organization_id=None, organization_name=None
):

    if organization_id is None and organization_name is None:
        raise OrganizationArgumentException(
            "Neither organization_id nor organization_name provided. One is required."
        )

    if organization_name:
        organization_object = find_organization_by_name(
            contxt_service=contxt_service, organization_name=organization_name
        )
        if organization_object:
            organization_id = organization_object.id
        else:
            raise OrganizationNotFoundException("Organization not found")
    else:
        organization_id = organization_id

    return organization_id


def check_required_organization_args(args, org_is_required):

    if args.organization_id is not None and args.organization_name is not None:
        raise OrganizationArgumentException(
            "Specify organization_id OR organization_name. Not both."
        )

    if org_is_required:
        if args.organization_id is None and args.organization_name is None:
            raise OrganizationArgumentException(
                "Either organization_id OR organization_name is a required argument"
            )


class Organizations:
    def __init__(self, auth_module):

        self.auth = auth_module

        self.contxt_service = ContxtService(self.auth)

    def get_organization_users(self, organization_id=None, organization_name=None):

        organization_id = get_organization_id_from_arguments(
            organization_id=organization_id,
            organization_name=organization_name,
            contxt_service=self.contxt_service,
        )

        return self.contxt_service.get_users_for_organization(organization_id)

    def create_organization(self, organization_name):
        current_user_id = self.auth.user_id

        new_organization = self.contxt_service.create_organization(
            Organization(organization_name)
        )

        print("Adding currently logged in user to list of organization users")
        print(
            self.contxt_service.add_user_to_organization(
                organization_id=new_organization.id, user_id=current_user_id
            )
        )

        return new_organization
