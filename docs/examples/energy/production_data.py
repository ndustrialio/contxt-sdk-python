import argparse

from contxt.services.assets import AssetsService
from contxt.services.facilities import FacilitiesService
from contxt.utils.serializer import Serializer
from contxt.workers import BaseWorker


class ProductionDataFetcher(BaseWorker):

    def __init__(self, facility_id):
        super().__init__()
        self.facilities_config = self.env.get_config_for_service_name('facilities')
        self.facilities_service = FacilitiesService(self.facilities_config)
        self.facility_id = facility_id
        self.assets = None

    # Required do_work method if using BaseWorker class
    def do_work(self):

        facility = self.facilities_service.get_facility_with_id(self.facility_id)
        self.assets = AssetsService(self.facilities_config, facility.organization_id)

        print(f"Fetching Asset type information for Organization")

        types = self.assets.get_asset_types(facility.organization_id)
        print(Serializer.to_table(types))

        facility_type = None
        for t in types:
            if t.label == 'Facility':
                facility_type = t

        # Get the metrics available for the facility type in this organization
        metrics = self.assets.get_metrics(facility_type.id)

        print(f"Metrics available for the Facility type")
        print(Serializer.to_table(metrics))

        metric = None
        for m in metrics:
            # can look for outbound volume at `facility_daily_outbound_volume`
            if m.label == 'facility_daily_inbound_volume':
                metric = m

        values = self.assets.get_metric_values(asset_id=facility.asset_id, metric_id=metric.id)
        print(f"Data for {metric.label} in units: {metric.units if not None else 'N/A'}")
        for val in values:
            print(f"{val.effective_start_date} -> {val.value}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Production Data Example')

    parser.add_argument("facility_id", type=int, help="Facility ID to fetch production data")

    args = parser.parse_args()

    worker = ProductionDataFetcher(args.facility_id)
    worker.do_work()
