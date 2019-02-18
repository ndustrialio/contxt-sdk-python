from datetime import datetime

from contxt.services.ems import EMSService
from contxt.services.contxt import ContxtService
from contxt.services.facilities import FacilitiesService

from contxt.utils import make_logger

logger = make_logger(__name__)


class EMS:

    def __init__(self, auth_module):

        self.auth = auth_module

        self.ems_service = EMSService(self.auth)
        self.contxt_service = ContxtService(self.auth)
        self.facilities_service = FacilitiesService(self.auth)

    def get_facility_spend(self, facility_id, interval, resource_type, start_date, end_date, proforma=False):

        start_date = datetime.strptime(start_date, "%Y-%m")
        end_date = datetime.strptime(end_date, "%Y-%m")

        if resource_type not in ['electric', 'gas', 'combined']:
            logger.critical("--resource_type must be one of 'electrical','gas','combined'")
            return

        if interval == 'monthly':

            print(proforma)

            print(self.ems_service.get_monthly_utility_spend(facility_id=facility_id,
                                                             type=resource_type,
                                                             date_start=start_date,
                                                             date_end=end_date,
                                                             proforma=proforma))

        elif interval == 'daily':
            pass

        else:
            print("Invalid interval provided: {}. Must be 'monthly' or 'daily'")
