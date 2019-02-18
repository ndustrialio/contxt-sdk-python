from datetime import datetime
from tqdm import tqdm
import csv

from contxt.services.ems import EMSService
from contxt.services.contxt import ContxtService
from contxt.services.facilities import FacilitiesService
from contxt.services import UnauthorizedException

from contxt.func.organizations import find_organization_by_name

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

    def get_organization_spend(self, resource_type, interval, start_date, end_date, to_csv, proforma=False,
                               organization_id=None, organization_name=None):

        start_date = datetime.strptime(start_date, "%Y-%m")
        end_date = datetime.strptime(end_date, "%Y-%m")

        if organization_name:
            org = find_organization_by_name(self.contxt_service,
                                            organization_name=organization_name)
            if org is None:
                logger.critical("Organization not found")
                return

            organization_id = org.id
        else:
            organization_id = organization_id

        # Get all facilities for this organization
        facilities = self.facilities_service.get_facilities(organization_id)

        organization_spend = {}
        logger.info("Loading data for facilities")
        for facility in tqdm(facilities):
            try:
                spend = self.ems_service.get_monthly_utility_spend(facility_id=facility.id,
                                                                   type=resource_type,
                                                                   date_start=start_date,
                                                                   date_end=end_date,
                                                                   proforma=proforma)
            except UnauthorizedException as e:
                logger.warning("Unauthorized for facility {}".format(facility.id))
                continue

            organization_spend[facility.name] = {}
            for period in spend.spend_periods:
                organization_spend[facility.name][period.date] = period.spend

        # write this to the CSV file
        field_names = ['facility']
        field_names.extend(organization_spend[list(organization_spend.keys())[0]].keys())
        with open(to_csv, 'w') as f:
            csv_writer = csv.DictWriter(f, fieldnames=field_names)

            csv_writer.writeheader()

            for facility_name, spend_dict in organization_spend.items():
                row = spend_dict
                row['facility'] = facility_name
                csv_writer.writerow(row)
