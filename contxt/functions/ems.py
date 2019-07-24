import csv
import traceback
from datetime import datetime

import dateutil.parser
import pytz
from tqdm import tqdm

from contxt.exceptions import UnauthorizedException
from contxt.functions.assets import Assets
from contxt.functions.organizations import find_organization_by_name
from contxt.legacy.services.ems import EMSService
from contxt.legacy.services.iot import IOTService
from contxt.services.contxt import ContxtService
from contxt.services.facilities import FacilitiesService
from contxt.utils import make_logger
from contxt.utils.vis import DataVisualizer

logger = make_logger(__name__)


class EMS:
    def __init__(self, auth_module):

        self.auth = auth_module

        self.ems_service = EMSService(self.auth)
        self.contxt_service = ContxtService(self.auth)
        self.iot_service = IOTService(self.auth)
        self.facilities_service = FacilitiesService(self.auth)

        self.asset_functions = Assets(self.auth)

    def get_facility_main_data(self, facility_id, resource_type, start_date, end_date):
        if not isinstance(start_date, datetime):
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        if not isinstance(end_date, datetime):
            end_date = datetime.strptime(end_date, "%Y-%m-%d")

        if resource_type not in ["electric", "gas", "combined"]:
            logger.critical(
                "resource_type must be one of 'electrical','gas','combined'"
            )
            return

        facility_obj = self.facilities_service.get_facility_with_id(facility_id)
        if not facility_obj:
            return

        facility_timezone = pytz.timezone(facility_obj.timezone)

        main_services = self.ems_service.get_main_services(facility_id, resource_type)

        data_by_main = {}
        for service in main_services:
            print(
                f"Getting data for main service {service.name}. IOT Info ->"
                f" {service.demand_field.field_human_name} and output"
                f" {service.demand_field.output_id} from {start_date} to {end_date}"
            )
            data = self.iot_service.get_data_for_field(
                output_id=service.demand_field.output_id,
                field_human_name=service.demand_field.field_human_name,
                start_time=start_date,
                end_time=end_date,
                window=900,
                limit=5000,
            )
            data_by_main[service.name] = []
            for row in data:
                data_by_main[service.name].append(
                    {
                        "event_time": row["event_time"].astimezone(facility_timezone),
                        "value": row["value"],
                    }
                )

        return data_by_main

    def get_facility_spend(
        self,
        facility_id,
        interval,
        resource_type,
        start_date,
        end_date,
        pro_forma=False,
    ):

        if not isinstance(start_date, datetime):
            start_date = datetime.strptime(start_date, "%Y-%m")
        if not isinstance(end_date, datetime):
            end_date = datetime.strptime(end_date, "%Y-%m")

        if resource_type not in ["electric", "gas", "combined"]:
            logger.critical(
                "--resource_type must be one of 'electrical','gas','combined'"
            )
            return

        if interval == "monthly":

            return reversed(
                self.ems_service.get_monthly_utility_spend(
                    facility_id=facility_id,
                    type=resource_type,
                    date_start=start_date,
                    date_end=end_date,
                    pro_forma=pro_forma,
                )
            )

        elif interval == "daily":
            pass

        else:
            print("Invalid interval provided: {}. Must be 'monthly' or 'daily'")

    def get_facility_usage(
        self,
        facility_id,
        interval,
        resource_type,
        start_date,
        end_date,
        pro_forma=False,
    ):
        if not isinstance(start_date, datetime):
            start_date = datetime.strptime(start_date, "%Y-%m")
        if not isinstance(end_date, datetime):
            end_date = datetime.strptime(end_date, "%Y-%m")

        if resource_type not in ["electric", "gas", "combined"]:
            logger.critical(
                "--resource_type must be one of 'electrical','gas','combined'"
            )
            return

        if interval == "monthly":

            return self.ems_service.get_monthly_utility_usage(
                facility_id=facility_id,
                type=resource_type,
                date_start=start_date,
                date_end=end_date,
                pro_forma=pro_forma,
            )

        elif interval == "daily":
            pass

        else:
            print("Invalid interval provided: {}. Must be 'monthly' or 'daily'")

    def get_organization_spend(
        self,
        resource_type,
        interval,
        start_date,
        end_date,
        pro_forma=False,
        organization_id=None,
        organization_name=None,
    ):

        start_date = datetime.strptime(start_date, "%Y-%m")
        end_date = datetime.strptime(end_date, "%Y-%m")

        if organization_name:
            org = find_organization_by_name(
                self.contxt_service, organization_name=organization_name
            )
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
                spend = self.ems_service.get_monthly_utility_spend(
                    facility_id=facility.id,
                    type=resource_type,
                    date_start=start_date,
                    date_end=end_date,
                    pro_forma=pro_forma,
                )
            except UnauthorizedException:
                logger.warning(f"Unauthorized for facility {facility.id}")
                continue

            organization_spend[facility.name] = {}
            facility_name_to_spends[facility.name] = spend
            for period in spend.spend_periods:
                if period.pro_forma_date is not None:
                    organization_spend[facility.name][period.date] = f"{period.spend}*"
                else:
                    organization_spend[facility.name][period.date] = period.spend

        return organization_spend

    def get_organization_usage(
        self,
        resource_type,
        interval,
        start_date,
        end_date,
        pro_forma=False,
        organization_id=None,
        organization_name=None,
    ):

        start_date = datetime.strptime(start_date, "%Y-%m")
        end_date = datetime.strptime(end_date, "%Y-%m")

        if organization_name:
            org = find_organization_by_name(
                self.contxt_service, organization_name=organization_name
            )
            if org is None:
                logger.critical("Organization not found")
                return

            organization_id = org.id
        else:
            organization_id = organization_id

        # Get all facilities for this organization
        facilities = self.facilities_service.get_facilities(organization_id)

        organization_spend = {}
        facility_name_to_usage = {}
        logger.info("Loading data for facilities")
        for facility in tqdm(facilities):
            try:
                usage = self.ems_service.get_monthly_utility_usage(
                    facility_id=facility.id,
                    type=resource_type,
                    date_start=start_date,
                    date_end=end_date,
                    pro_forma=pro_forma,
                )
            except UnauthorizedException:
                logger.warning(f"Unauthorized for facility {facility.id}")
                continue
            except Exception as e:
                logger.error(e)
                continue

            organization_spend[facility.name] = {}
            facility_name_to_usage[facility.name] = usage
            for period in usage.usage_periods:
                if period.pro_forma_date is not None:
                    organization_spend[facility.name][period.date] = f"{period.value}*"
                else:
                    organization_spend[facility.name][period.date] = period.value

        return organization_spend

    def get_organization_usage_vs_monthly_metric(
        self,
        metric,
        interval,
        resource_type,
        start_date,
        end_date,
        organization_name=None,
        organization_id=None,
        pro_forma=False,
        metric_scalar=1,
    ):

        # initialize an instance of the asset service to use for this,
        # so we can speed things up
        asset_service, organization_id = self.asset_functions.initialize_asset_service(
            organization_id=organization_id, organization_name=organization_name
        )

        facilities = self.facilities_service.get_facilities(organization_id)

        facility_normalized_metrics = {}

        for facility in tqdm(facilities):

            try:
                normalized_usage = self.get_facility_usage_vs_monthly_metric(
                    facility_id=facility.id,
                    metric=metric,
                    interval=interval,
                    resource_type=resource_type,
                    start_date=start_date,
                    end_date=end_date,
                    pro_forma=pro_forma,
                    asset_instance=asset_service,
                    metric_scalar=metric_scalar,
                )

                facility_normalized_metrics[facility.name] = normalized_usage

            except UnauthorizedException:
                logger.warning(f"Unauthorized for facility {facility.id}")
                continue
            except Exception as e:
                logger.critical(f"Error loading data for facility {facility.id}")
                logger.error(e)
                continue

        return facility_normalized_metrics

    def get_organization_spend_vs_monthly_metric(
        self,
        metric,
        interval,
        resource_type,
        start_date,
        end_date,
        organization_name=None,
        organization_id=None,
        pro_forma=False,
        metric_scalar=1,
    ):

        # initialize an instance of the asset service to use for this,
        # so we can speed things up
        asset_service, organization_id = self.asset_functions.initialize_asset_service(
            organization_id=organization_id, organization_name=organization_name
        )

        facilities = self.facilities_service.get_facilities(organization_id)

        facility_normalized_metrics = {}

        for facility in tqdm(facilities):

            try:
                normalized_spend = self.get_facility_spend_vs_monthly_metric(
                    facility_id=facility.id,
                    metric=metric,
                    interval=interval,
                    resource_type=resource_type,
                    start_date=start_date,
                    end_date=end_date,
                    pro_forma=pro_forma,
                    asset_instance=asset_service,
                    metric_scalar=metric_scalar,
                )

                facility_normalized_metrics[facility.name] = normalized_spend

            except UnauthorizedException:
                logger.warning(f"Unauthorized for facility {facility.id}")
                continue
            except Exception as e:
                traceback.print_exc()
                logger.critical(f"Error loading data for facility {facility.id}")
                logger.error(e)
                continue

        return facility_normalized_metrics

    def get_facility_spend_vs_monthly_metric(
        self,
        facility_id,
        metric,
        interval,
        resource_type,
        start_date,
        end_date,
        pro_forma=False,
        asset_instance=None,
        metric_scalar=1,
    ):

        if not isinstance(start_date, datetime):
            start_date = datetime.strptime(start_date, "%Y-%m").replace(tzinfo=pytz.UTC)
        if not isinstance(end_date, datetime):
            end_date = datetime.strptime(end_date, "%Y-%m").replace(tzinfo=pytz.UTC)

        # get the facility so we can get its asset_id
        facility_obj = self.facilities_service.get_facility_with_id(facility_id)
        if not facility_obj:
            return

        # get its list of metrics for the asset so we can make sure the user is
        # asking for a valid metric
        asset_obj = self.asset_functions.get_asset_info(
            asset_id=facility_obj.asset_id,
            organization_id=facility_obj.organization_id,
            asset_instance=asset_instance,
        )

        if metric not in asset_obj.asset_type.metrics:
            logger.critical(f"No such metric for facility with ID {facility_id}")
            return

        # get the metric we're looking for
        metric_obj = asset_obj.asset_type.metrics[metric]

        if metric_obj.time_interval != "monthly":
            logger.critical(
                f"Invalid time interval for metric {metric_obj.time_interval}."
                f" Must be a monthly metric"
            )
            return

        # get facility monthly utility spend
        facility_spend = self.get_facility_spend(
            facility_id=facility_id,
            interval="monthly",
            resource_type=resource_type,
            start_date=start_date,
            end_date=end_date,
            pro_forma=pro_forma,
        )

        # get metric values for the metric specified for this facility
        metric, values = self.asset_functions.get_metric_values_for_asset(
            metric=metric,
            asset_id=asset_obj.id,
            organization_id=facility_obj.organization_id,
            asset_instance=asset_instance,
        )

        normalized_data_by_date = {}
        for value in values:
            date = dateutil.parser.parse(value.effective_start_date)
            if end_date < date or date < start_date:
                continue
            if value.value is not None:
                normalized_data_by_date[date] = {"metric_value": int(value.value)}

        for spend in facility_spend.spend_periods:
            date = datetime.strptime(spend.date, "%Y-%m").replace(tzinfo=pytz.UTC)

            if date in normalized_data_by_date:
                normalized_data_by_date[date]["spend"] = spend.spend
                if spend.spend is not None:
                    normalized_value = float(
                        (
                            int(spend.spend)
                            / normalized_data_by_date[date]["metric_value"]
                        )
                        * metric_scalar
                    )
                    normalized_data_by_date[date]["normalized"] = normalized_value
                else:
                    normalized_data_by_date[date]["normalized"] = "Spend Data Available"
                normalized_data_by_date[date]["pro_forma_date"] = spend.pro_forma_date
            else:
                normalized_data_by_date[date] = {
                    "spend": None,
                    "normalized": "Metric Data Unavailable",
                    "pro_forma_date": None,
                }

        return normalized_data_by_date

    def get_facility_usage_vs_monthly_metric(
        self,
        facility_id,
        metric,
        interval,
        resource_type,
        start_date,
        end_date,
        pro_forma=False,
        asset_instance=None,
        metric_scalar=1,
    ):

        if not isinstance(start_date, datetime):
            start_date = datetime.strptime(start_date, "%Y-%m").replace(tzinfo=pytz.UTC)
        if not isinstance(end_date, datetime):
            end_date = datetime.strptime(end_date, "%Y-%m").replace(tzinfo=pytz.UTC)

        # get the facility so we can get its asset_id
        facility_obj = self.facilities_service.get_facility_with_id(facility_id)
        if not facility_obj:
            return

        # get its list of metrics for the asset so we can make sure the user is
        # asking for a valid metric
        asset_obj = self.asset_functions.get_asset_info(
            asset_id=facility_obj.asset_id,
            organization_id=facility_obj.organization_id,
            asset_instance=asset_instance,
        )

        if metric not in asset_obj.asset_type.metrics:
            logger.critical("No such metric for Facility")
            return

        # get the metric we're looking for
        metric_obj = asset_obj.asset_type.metrics[metric]

        if metric_obj.time_interval != "monthly":
            logger.critical(
                f"Invalid time interval for metric {metric_obj.time_interval}."
                " Must be a monthly metric"
            )
            return

        # get facility monthly utility spend
        facility_usage = self.get_facility_usage(
            facility_id=facility_id,
            interval="monthly",
            resource_type=resource_type,
            start_date=start_date,
            end_date=end_date,
            pro_forma=pro_forma,
        )

        # get metric values for the metric specified for this facility
        metric, values = self.asset_functions.get_metric_values_for_asset(
            metric=metric,
            asset_id=asset_obj.id,
            organization_id=facility_obj.organization_id,
            asset_instance=asset_instance,
        )

        normalized_data_by_date = {}
        for value in values:
            date = dateutil.parser.parse(value.effective_start_date)

            # skip this record if it's not in the date range
            if date < start_date or date > end_date:
                continue

            if value.value is not None:
                normalized_data_by_date[date] = {"metric_value": int(value.value)}

        for usage in facility_usage.usage_periods:
            date = datetime.strptime(usage.date, "%Y-%m").replace(tzinfo=pytz.UTC)

            if date in normalized_data_by_date:
                normalized_data_by_date[date]["usage"] = usage.value
                if usage.value is not None:
                    normalized_value = float(
                        (
                            int(usage.value)
                            / normalized_data_by_date[date]["metric_value"]
                        )
                        * metric_scalar
                    )
                    normalized_data_by_date[date]["normalized"] = normalized_value
                else:
                    normalized_data_by_date[date][
                        "normalized"
                    ] = "Usage Data Unavailable"
                normalized_data_by_date[date]["pro_forma_date"] = usage.pro_forma_date
            else:
                normalized_data_by_date[date] = {
                    "usage": None,
                    "normalized": "Metric Data Unavailable",
                    "pro_forma_date": None,
                }

        return normalized_data_by_date

    def _make_plotly_title(self, facility_name):
        return f"Monthly Utility Spend for Facility {facility_name}"

    def plot_monthly_utility_spend(self, facility_name_to_spends):
        data_vis = DataVisualizer(multi_plots=False)

        # Create graphs
        labeled_graphs = {
            f"Facility {f}": data_vis._create_scatter_plot(
                df=s.spend_periods.get_df(),
                x_label="date",
                y_label="value",
                name=f"{f}'s monthly utility spend",
                line=dict(shape="spline"),
            )
            for f, s in facility_name_to_spends.items()
        }

        # Plot
        data_vis.run(labeled_graphs, title="Monthly Utility Spend")

    def write_organization_utility_data_to_file(
        self, organization_spend_or_usage, filename
    ):
        # write this to the CSV file
        field_names = ["facility"]
        field_names.extend(
            organization_spend_or_usage[
                list(organization_spend_or_usage.keys())[0]
            ].keys()
        )
        with open(filename, "w") as f:
            csv_writer = csv.DictWriter(f, fieldnames=field_names)

            csv_writer.writeheader()

            for facility_name in sorted(organization_spend_or_usage.keys()):
                row = organization_spend_or_usage[facility_name]
                row["facility"] = facility_name
                csv_writer.writerow(row)
