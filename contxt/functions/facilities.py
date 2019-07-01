from contxt.functions.organizations import get_organization_id_from_arguments
from contxt.services.contxt import ContxtService
from contxt.services.facilities import FacilitiesService


class Facilities:
    def __init__(self, auth_module):
        self.auth = auth_module
        self.facilities_service = FacilitiesService(self.auth)
        self.contxt_service = ContxtService(self.auth)

    def get_all_facilities(self, organization_id=None, organization_name=None):

        if organization_id or organization_name:
            organization_id = get_organization_id_from_arguments(
                contxt_service=self.contxt_service,
                organization_id=organization_id,
                organization_name=organization_name,
            )

            return self.facilities_service.get_facilities(
                organization_id=organization_id
            )

        else:
            return self.facilities_service.get_facilities()
