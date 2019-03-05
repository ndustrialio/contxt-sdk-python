import csv
from datetime import datetime

import pandas as pd
from plotly import graph_objects as go
from tqdm import tqdm

from contxt.functions.organizations import find_organization_by_name
from contxt.services import UnauthorizedException
from contxt.services.asset_framework import datetime_zulu_parse
from contxt.services.contxt import ContxtService
from contxt.services.ems import EMSService
from contxt.services.facilities import FacilitiesService
from contxt.utils import make_logger
from contxt.utils.vis import DataVisualizer

logger = make_logger(__name__)


class EMS:

    def __init__(self, auth_module):

        self.auth = auth_module

        self.ems_service = EMSService(self.auth)
        self.contxt_service = ContxtService(self.auth)
        self.facilities_service = FacilitiesService(self.auth)

    def get_facility_spend(self, facility_id, interval, resource_type, start_date, end_date, pro_forma=False):

        start_date = datetime.strptime(start_date, "%Y-%m")
        end_date = datetime.strptime(end_date, "%Y-%m")

        if resource_type not in ['electric', 'gas', 'combined']:
            logger.critical("--resource_type must be one of 'electrical','gas','combined'")
            return

        if interval == 'monthly':

            return self.ems_service.get_monthly_utility_spend(facility_id=facility_id,
                                                              type=resource_type,
                                                              date_start=start_date,
                                                              date_end=end_date,
                                                              pro_forma=pro_forma)

        elif interval == 'daily':
            pass

        else:
            print("Invalid interval provided: {}. Must be 'monthly' or 'daily'")

    def get_organization_spend(self, resource_type, interval, start_date, end_date, filename, pro_forma=False,
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
        facility_name_to_spends = {}
        logger.info("Loading data for facilities")
        for facility in tqdm(facilities):
            try:
                spend = self.ems_service.get_monthly_utility_spend(facility_id=facility.id,
                                                                   type=resource_type,
                                                                   date_start=start_date,
                                                                   date_end=end_date,
                                                                   pro_forma=pro_forma)
            except UnauthorizedException as e:
                logger.warning(f"Unauthorized for facility {facility.id}")
                continue

            organization_spend[facility.name] = {}
            facility_name_to_spends[facility.name] = spend
            for period in spend.spend_periods:
                organization_spend[facility.name][period.date] = period.spend

        # Plot or dump to csv
        # TODO: add plot flag
        # TODO: normalize spend format
        if False:
            self.plot_monthly_utility_spend(facility_name_to_spends)
        else:
            self.write_monthly_utility_spend_to_file(organization_spend, filename)

    def plot_monthly_utility_spend(self, facility_name_to_spends):
        data_vis = DataVisualizer(multi_plots=False)

        # Create graphs
        labeled_graphs = {
            f'Facility {f}': data_vis._create_scatter_plot(
                df=s.spend_periods.get_df(),
                x_label='date',
                y_label='value',
                name=f"{f}'s monthly utility spend",
                line=dict(shape='spline'))
            for f, s in facility_name_to_spends.items()
        }

        # Plot
        data_vis.run(labeled_graphs, title='Monthly Utility Spend')

    def write_monthly_utility_spend_to_file(self, organization_spend, filename):
        # write this to the CSV file
        field_names = ['facility']
        field_names.extend(organization_spend[list(organization_spend.keys())[0]].keys())
        with open(filename, 'w') as f:
            csv_writer = csv.DictWriter(f, fieldnames=field_names)

            csv_writer.writeheader()

            for facility_name, spend_dict in organization_spend.items():
                row = spend_dict
                row['facility'] = facility_name
                csv_writer.writerow(row)
