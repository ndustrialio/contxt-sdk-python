import csv
from datetime import datetime

from tqdm import tqdm
import dateutil.parser
import pytz

from contxt.functions.organizations import find_organization_by_name, get_organization_id_from_arguments
from contxt.functions.assets import Assets

from contxt.services import UnauthorizedException
from contxt.services.contxt import ContxtService
from contxt.services.ems import EMSService
from contxt.services.facilities import FacilitiesService
from contxt.utils import make_logger
from contxt.utils.vis import run_plotly

logger = make_logger(__name__)


class EMS:

    def __init__(self, auth_module):

        self.auth = auth_module

        self.ems_service = EMSService(self.auth)
        self.contxt_service = ContxtService(self.auth)
        self.facilities_service = FacilitiesService(self.auth, environment='staging')

        self.asset_functions = Assets(self.auth)

    def get_facility_spend(self, facility_id, interval, resource_type, start_date, end_date, proforma=False):

        if not isinstance(start_date, datetime):
            start_date = datetime.strptime(start_date, "%Y-%m")
        if not isinstance(end_date, datetime):
            end_date = datetime.strptime(end_date, "%Y-%m")

        if resource_type not in ['electric', 'gas', 'combined']:
            logger.critical("--resource_type must be one of 'electrical','gas','combined'")
            return

        if interval == 'monthly':

            return self.ems_service.get_monthly_utility_spend(facility_id=facility_id,
                                                              type=resource_type,
                                                              date_start=start_date,
                                                              date_end=end_date,
                                                              proforma=proforma)

        elif interval == 'daily':
            pass

        else:
            print("Invalid interval provided: {}. Must be 'monthly' or 'daily'")

    def get_facility_usage(self, facility_id, interval, resource_type, start_date, end_date):
        start_date = datetime.strptime(start_date, "%Y-%m")
        end_date = datetime.strptime(end_date, "%Y-%m")

        if resource_type not in ['electric', 'gas', 'combined']:
            logger.critical("--resource_type must be one of 'electrical','gas','combined'")
            return

        if interval == 'monthly':

            return self.ems_service.get_monthly_utility_usage(facility_id=facility_id,
                                                              type=resource_type,
                                                              date_start=start_date,
                                                              date_end=end_date)

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
        facility_name_to_spends = {}
        logger.info("Loading data for facilities")
        for facility in tqdm(facilities):
            try:
                spend = self.ems_service.get_monthly_utility_spend(facility_id=facility.id,
                                                                   type=resource_type,
                                                                   date_start=start_date,
                                                                   date_end=end_date,
                                                                   proforma=proforma)
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
            self.write_monthly_utility_spend_to_file(organization_spend, to_csv)

    def get_organization_spend_vs_monthly_metric(self, metric, interval, resource_type, start_date, end_date,
                                                 organization_name=None, organization_id=None, proforma=False):

        # initialize an instance of the asset service to use for this, so we can speed things up
        asset_service, organization_id = self.asset_functions.initialize_asset_service(organization_id=organization_id,
                                                                                       organization_name=organization_name)

        facilities = self.facilities_service.get_facilities(organization_id)

        facility_normalized_metrics = {}

        for facility in tqdm(facilities):

            try:
                normalized_spend = self.get_facility_spend_vs_monthly_metric(facility_id=facility.id,
                                                                             metric=metric,
                                                                             interval=interval,
                                                                             resource_type=resource_type,
                                                                             start_date=start_date,
                                                                             end_date=end_date,
                                                                             proforma=proforma,
                                                                             asset_instance=asset_service)

                facility_normalized_metrics[facility.name] = normalized_spend

            except UnauthorizedException as e:
                logger.warning(f"Unauthorized for facility {facility.id}")
                continue
            except Exception as e:
                logger.critical(f"Error loading data for facility {facility.id}")
                logger.error(e)
                continue

        return facility_normalized_metrics

    def get_facility_spend_vs_monthly_metric(self, facility_id, metric, interval, resource_type, start_date, end_date,
                                             proforma=False, asset_instance=None):

        if not isinstance(start_date, datetime):
            start_date = datetime.strptime(start_date, "%Y-%m").replace(tzinfo=pytz.UTC)
        if not isinstance(end_date, datetime):
            end_date = datetime.strptime(end_date, "%Y-%m").replace(tzinfo=pytz.UTC)

        # get the facility so we can get its asset_id
        facility_obj = self.facilities_service.get_facility_by_id(facility_id)

        # get its list of metrics for the asset so we can make sure the user is asking for a valid metric
        asset_obj = self.asset_functions.get_asset_info(asset_id=facility_obj.asset_id,
                                                        organization_id=facility_obj.organization_id,
                                                        asset_instance=asset_instance)

        if metric not in asset_obj.asset_type.metrics:
            logger.critical("No such metric for Facility")
            return

        # get the metric we're looking for
        metric_obj = asset_obj.asset_type.metrics[metric]

        if metric_obj.time_interval != 'monthly':
            logger.critical("Invalid time interval for metric {metric_obj.time_interval}. Must be a monthly metric")
            return

        # get facility monthly utility spend
        facility_spend = self.get_facility_spend(facility_id=facility_id,
                                                 interval='monthly',
                                                 resource_type=resource_type,
                                                 start_date=start_date,
                                                 end_date=end_date,
                                                 proforma=proforma)

        # get metric values for the metric specified for this facility
        metric, values = self.asset_functions.get_metric_values_for_asset(metric=metric,
                                                                          asset_id=asset_obj.id,
                                                                          organization_id=facility_obj.organization_id,
                                                                          asset_instance=asset_instance)

        normalized_data_by_date = {}
        for value in values:
            date = dateutil.parser.parse(value.effective_start_date)
            if end_date < date or date < start_date:
                continue
            if value.value is not None:
                normalized_data_by_date[date] = {'metric_value': int(value.value)}

        for spend in facility_spend.spend_periods:
            date = datetime.strptime(spend.date, '%Y-%m').replace(tzinfo=pytz.UTC)

            if date in normalized_data_by_date:
                normalized_data_by_date[date]['spend'] = spend.spend
                if spend.spend is not None:
                    normalized_value = float(int(spend.spend) / normalized_data_by_date[date]['metric_value'])
                    normalized_data_by_date[date]['normalized'] = normalized_value
                else:
                    normalized_data_by_date[date]['normalized'] = None
                normalized_data_by_date[date]['spend_proforma_date'] = spend.proforma_date
            else:
                normalized_data_by_date[date] = {}
                normalized_data_by_date[date]['spend'] = None
                normalized_data_by_date[date]['normalized'] = None
                normalized_data_by_date[date]['spend_proforma_date'] = None

        return normalized_data_by_date

    def get_facility_usage_vs_monthly_metric(self, facility_id, metric, interval, resource_type, start_date, end_date):

        # get the facility so we can get its asset_id
        facility_obj = self.facilities_service.get_facility_by_id(facility_id)

        # get its list of metrics for the asset so we can make sure the user is asking for a valid metric
        asset_obj = self.asset_functions.get_asset_info(asset_id=facility_obj.asset_id,
                                                        organization_id=facility_obj.organization_id)

        if metric not in asset_obj.asset_type.metrics:
            logger.critical("No such metric for Facility")
            return

        # get the metric we're looking for
        metric_obj = asset_obj.asset_type.metrics[metric]

        if metric_obj.time_interval != 'monthly':
            logger.critical("Invalid time interval for metric {metric_obj.time_interval}. Must be a monthly metric")
            return

        # get facility monthly utility spend
        facility_spend = self.get_facility_usage(facility_id=facility_id,
                                                 interval='monthly',
                                                 resource_type=resource_type,
                                                 start_date=start_date,
                                                 end_date=end_date)

        # get metric values for the metric specified for this facility
        metric, values = self.asset_functions.get_metric_values_for_asset(metric=metric,
                                                                          asset_id=asset_obj.id,
                                                                          organization_id=facility_obj.organization_id,
                                                                          )

        normalized_data_by_date = {}
        for value in values:
            date = dateutil.parser.parse(value.effective_start_date)
            if value.value is not None:
                normalized_data_by_date[date] = {'metric_value': int(value.value)}

        for usage in facility_spend.usage_periods:
            date = datetime.strptime(usage.date, '%Y-%m').replace(tzinfo=pytz.UTC)
            if date in normalized_data_by_date:
                normalized_data_by_date[date]['usage'] = usage.value
                if usage.value is not None:
                    normalized_value = float(int(usage.value) / normalized_data_by_date[date]['metric_value'])
                    normalized_data_by_date[date]['normalized'] = normalized_value
                else:
                    normalized_data_by_date[date]['normalized'] = None

            else:
                normalized_data_by_date[date]['usage'] = None
                normalized_data_by_date[date]['normalized'] = None

        return normalized_data_by_date

    def _make_plotly_title(self, facility_name):
        return f'Monthly Utility Spend for Facility {facility_name}'

    def plot_monthly_utility_spend(self, facility_name_to_spends):
        title_to_df = {
            self._make_plotly_title(f): s.spend_periods.get_df()
            for f, s in facility_name_to_spends.items()
        }
        run_plotly(title_to_df, x_label='date', y_label='value')

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
