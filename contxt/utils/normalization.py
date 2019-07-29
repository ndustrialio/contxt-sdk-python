"""
This stuff feels super custom/broken
"""

from csv import DictWriter
from datetime import datetime
from typing import Dict

from tqdm import tqdm

from contxt.cli.parsers import ContxtArgParser, _get_organization_id
from contxt.services import (
    AssetsService,
    ContxtService,
    EmsService,
    FacilitiesService,
    IotService,
)
from contxt.utils import make_logger

logger = make_logger(__name__)


class NormalizationParser(ContxtArgParser):
    def _init_parser(self, subparsers):
        from contxt.models.ems import ResourceType
        from contxt.models import Parsers

        parser = subparsers.add_parser("norm-metrics", help="Normalized Metrics")
        parser.set_defaults(func=self._help)
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Spend Metric Normalization
        spend_metrics_parser = _subparsers.add_parser(
            "util-spend-metrics", help="Utility spend metrics"
        )
        spend_metrics_parser.add_argument(
            "metric", help="Provide the metric you want to normalize against"
        )
        spend_metrics_parser.add_argument(
            "interval", choices=["daily", "monthly"], help="Time interval"
        )
        spend_metrics_parser.add_argument(
            "resource_type", type=ResourceType, help="Type of resource"
        )
        spend_metrics_parser.add_argument(
            "start_date", type=Parsers.date, help="Start date"
        )
        spend_metrics_parser.add_argument(
            "end_date", type=Parsers.date, help="End date"
        )
        spend_metrics_group = spend_metrics_parser.add_mutually_exclusive_group(
            required=True
        )
        spend_metrics_group.add_argument(
            "-f", "--facility-id", type=int, help="Facility id"
        )
        spend_metrics_group.add_argument("-g", "--org-id", help="Organization id")
        spend_metrics_group.add_argument("-n", "--org-name", help="Organization name")

        spend_metrics_parser.add_argument(
            "-o", "--output", help="Filename to save data (csv)"
        )
        spend_metrics_parser.add_argument(
            "-p",
            "--pro-forma",
            action="store_true",
            help="Include pro forma calculations",
        )
        spend_metrics_parser.add_argument(
            "--metric-scalar",
            type=float,
            help="Optionally scale the normalized metric by a float",
        )
        spend_metrics_parser.set_defaults(func=self._utility_spend_metrics)

        # Usage Metric Normalization
        usage_metrics_parser = _subparsers.add_parser(
            "util-usage-metrics", help="Utility usage metrics"
        )

        usage_metrics_parser.add_argument(
            "metric", help="Provide the metric you want to normalize against"
        )
        usage_metrics_parser.add_argument(
            "interval", choices=["daily", "monthly"], help="Time interval"
        )
        usage_metrics_parser.add_argument(
            "resource_type", type=ResourceType, help="Type of resource"
        )
        usage_metrics_parser.add_argument(
            "start_date", type=Parsers.date, help="Start date"
        )
        usage_metrics_parser.add_argument(
            "end_date", type=Parsers.date, help="End date"
        )

        usage_metrics_group = usage_metrics_parser.add_mutually_exclusive_group(
            required=True
        )
        usage_metrics_group.add_argument(
            "-f", "--facility-id", type=int, help="Facility id"
        )
        usage_metrics_group.add_argument("-g", "--org-id", help="Organization id")
        usage_metrics_group.add_argument("-n", "--org-name", help="Organization name")

        usage_metrics_parser.add_argument(
            "-o", "--output", help="Filename to save data (csv)"
        )
        usage_metrics_parser.add_argument(
            "-p",
            "--pro-forma",
            action="store_true",
            help="Include pro forma calculations",
        )
        usage_metrics_parser.add_argument(
            "--metric-scalar",
            type=float,
            help="Optionally scale the normalized metric by a float",
        )
        usage_metrics_parser.set_defaults(func=self._utility_usage_metrics)

        return parser

    def _utility_spend_metrics(self, args, auth):
        helper = NormalizationHelper(auth, None)

        if args.facility_id:
            normalized_spend = helper.get_facility_spend_vs_monthly_metric(
                facility_id=args.facility_id,
                interval=args.interval,
                start_date=args.start_date,
                end_date=args.end_date,
                metric_label=args.metric,
                resource_type=args.resource_type,
                pro_forma=args.pro_forma,
                metric_scalar=args.metric_scalar or 1,
            )
            helper._print_facility_normalized_metrics(normalized_spend, "spend")
        else:
            assert args.output, "--output required"
            organization_id = args.org_id or _get_organization_id(args.org_name, auth)
            normalized_spend = helper.get_organization_spend_vs_monthly_metric(
                organization_id=organization_id,
                metric_label=args.metric,
                start_date=args.start_date,
                end_date=args.end_date,
                resource_type=args.resource_type,
                pro_forma=args.pro_forma,
                interval=args.interval,
                metric_scalar=args.metric_scalar or 1,
            )
            helper.to_csv_organization_normalized_metric(args.output, normalized_spend)

    def _utility_usage_metrics(self, args, auth):
        helper = NormalizationHelper(auth, None)

        if args.facility_id:
            normalized_usage = helper.get_facility_usage_vs_monthly_metric(
                facility_id=args.facility_id,
                interval=args.interval,
                start_date=args.start_date,
                end_date=args.end_date,
                metric=args.metric,
                resource_type=args.resource_type,
                pro_forma=args.pro_forma,
                metric_scalar=args.metric_scalar or 1,
            )
            helper._print_facility_normalized_metrics(normalized_usage, "usage")
        else:
            assert args.output, "--output required"
            organization_id = args.org_id or _get_organization_id(args.org_name, auth)
            normalized_usage = helper.get_organization_usage_vs_monthly_metric(
                organization_id=organization_id,
                metric_label=args.metric,
                start_date=args.start_date,
                end_date=args.end_date,
                resource_type=args.resource_type,
                pro_forma=args.pro_forma,
                interval=args.interval,
                metric_scalar=args.metric_scalar or 1,
            )
            helper.to_csv_organization_normalized_metric(args.output, normalized_usage)


class NormalizationHelper:
    def __init__(self, auth, organization_id):
        self.auth = auth
        self.organization_id = organization_id
        self.ems_service = EmsService(self.auth)
        self.contxt_service = ContxtService(self.auth)
        self.iot_service = IotService(self.auth)
        self.facilities_service = FacilitiesService(self.auth)
        self.assets_service = AssetsService(self.auth, organization_id)

    def get_facility_spend_vs_monthly_metric(
        self,
        facility_id: int,
        metric_label: str,
        interval: str,
        resource_type,
        start_date: datetime,
        end_date: datetime,
        pro_forma: bool = False,
        metric_scalar: int = 1,
    ) -> Dict:
        facility = self.facilities_service.get_facility_with_id(facility_id)
        asset = self.assets_service.get_complete_asset(facility.asset_id)
        metric = asset.asset_type.metric_with_label(metric_label)
        assert (
            metric.time_interval == "monthly"
        ), f"Time interval {metric.time_interval} must be monthly"

        # Get monthly utility spend
        facility_spend = self.ems_service.get_monthly_utility_spend(
            facility_id=facility_id,
            resource_type=resource_type,
            start_date=start_date,
            end_date=end_date,
            pro_forma=pro_forma,
        )

        # Get metric values
        metric_values = asset.metrics[metric_label]

        # Do something super ugly
        data = {
            mv.effective_start_date: {"metric_value": mv.value} for mv in metric_values
        }
        for spend in facility_spend.spend_periods:
            if spend.date in data:
                data[spend.date].update(
                    {
                        "spend": spend.value,
                        "pro_forma_date": spend.pro_forma_date,
                        "normalized": (spend.value / data[spend.date]["metric_value"])
                        * metric_scalar
                        if spend.value
                        else None,
                    }
                )
            else:
                data[spend.date] = {
                    "spend": None,
                    "normalized": "Metric Data Unavailable",
                    "pro_forma_date": None,
                }
        return data

    def get_facility_usage_vs_monthly_metric(
        self,
        facility_id: int,
        metric_label: str,
        interval: str,
        resource_type,
        start_date: datetime,
        end_date: datetime,
        pro_forma: bool = False,
        metric_scalar: int = 1,
    ) -> Dict:
        facility = self.facilities_service.get_facility_with_id(facility_id)
        asset = self.assets_service.get_complete_asset(facility.asset_id)
        metric = asset.asset_type.metric_with_label(metric_label)
        assert (
            metric.time_interval == "monthly"
        ), f"Time interval {metric.time_interval} must be monthly"

        # Get monthly utility spend
        facility_usage = self.ems_service.get_monthly_utility_usage(
            facility_id=facility_id,
            resource_type=resource_type,
            start_date=start_date,
            end_date=end_date,
            pro_forma=pro_forma,
        )

        # Get metric values
        metric_values = asset.metrics[metric_label]

        # Do something super ugly
        data = {
            mv.effective_start_date: {"metric_value": mv.value} for mv in metric_values
        }
        for usage in facility_usage.usage_periods:
            if usage.date in data:
                data[usage.date].update(
                    {
                        "usage": usage.value,
                        "pro_forma_date": usage.pro_forma_date,
                        "normalized": (usage.value / data[usage.date]["metric_value"])
                        * metric_scalar
                        if usage.value
                        else None,
                    }
                )
            else:
                data[usage.date] = {
                    "usage": None,
                    "normalized": "Metric Data Unavailable",
                    "pro_forma_date": None,
                }
        return data

    def get_organization_usage_vs_monthly_metric(
        self,
        metric_label: str,
        interval: str,
        resource_type,
        start_date: datetime,
        end_date: datetime,
        pro_forma: bool = False,
        metric_scalar: int = 1,
    ) -> Dict:
        facilities = self.facilities_service.get_facilities(self.organization_id)
        return {
            f.name: self.get_facility_usage_vs_monthly_metric(
                facility_id=f.id,
                metric_label=metric_label,
                interval=interval,
                resource_type=resource_type,
                start_date=start_date,
                end_date=end_date,
                pro_forma=pro_forma,
                metric_scalar=metric_scalar,
            )
            for f in tqdm(facilities)
        }

    def get_organization_spend_vs_monthly_metric(
        self,
        metric_label: str,
        interval: str,
        resource_type,
        start_date: datetime,
        end_date: datetime,
        pro_forma: bool = False,
        metric_scalar: int = 1,
    ) -> Dict:
        facilities = self.facilities_service.get_facilities(self.organization_id)
        return {
            f.name: self.get_facility_spend_vs_monthly_metric(
                facility_id=f.id,
                metric_label=metric_label,
                interval=interval,
                resource_type=resource_type,
                start_date=start_date,
                end_date=end_date,
                pro_forma=pro_forma,
                metric_scalar=metric_scalar,
            )
            for f in tqdm(facilities)
        }

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
            csv_writer = DictWriter(f, fieldnames=field_names)
            csv_writer.writeheader()
            for facility_name in sorted(organization_spend_or_usage.keys()):
                row = organization_spend_or_usage[facility_name]
                row["facility"] = facility_name
                csv_writer.writerow(row)

    def print_facility_normalized_metrics(normalized_data_by_date, normalization_key):
        from tabulate import tabulate

        normalized_to_print = []
        for date, data in normalized_data_by_date.items():
            # TODO clean this up when we can properly filter metric value data
            # by start->end date
            if normalization_key in data:
                normalized_to_print.append(
                    [
                        date.strftime("%Y-%m"),
                        data[normalization_key],
                        data["metric_value"] if "metric_value" in data else None,
                        data["normalized"],
                        data["pro_forma_date"],
                    ]
                )
        print(
            tabulate(
                normalized_to_print,
                headers=[
                    "date",
                    normalization_key,
                    "metric-value",
                    "normalized",
                    "pro_forma_date",
                ],
            )
        )

    def to_csv_organization_normalized_metric(filename, normalized_data_by_facility):
        from csv import DictWriter

        to_csv_data = []
        unique_dates = []
        by_facility = {}
        # gotta organize by date so that all the dates match across facilities
        for facility_name in sorted(normalized_data_by_facility.keys()):
            data = normalized_data_by_facility[facility_name]
            by_facility[facility_name] = {}
            for date, spend in data.items():
                if date not in unique_dates:
                    unique_dates.append(date)
                by_facility[facility_name][date] = spend.get("normalized", "N/A")
        facility_data = {}
        for date in reversed(sorted(unique_dates)):
            for facility_name, date_data in by_facility.items():
                if facility_name not in facility_data:
                    facility_data[facility_name] = {}
                facility_data[facility_name][date] = date_data.get(date)
        for facility, date_dict in facility_data.items():
            date_dict["facility_name"] = facility
            to_csv_data.append(date_dict)
        with open(filename, "w") as f:
            fields = ["facility_name"]
            fields.extend(unique_dates)
            writer = DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for row in to_csv_data:
                writer.writerow(row)
