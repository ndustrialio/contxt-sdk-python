from contxt.services.facilities import FacilitiesService
from contxt.services.ems import EmsService
from contxt.workers import BaseWorker

import argparse
import os, sys


class MainServiceFetcher(BaseWorker):

    def __init__(self, facility_id):
        super().__init__()
        facilities_config = self.env.get_config_for_service_name('facilities')
        ems_config = self.env.get_config_for_service_name('ems')
        self.facilities_service = FacilitiesService(facilities_config)
        self.facility_id = facility_id
        self.ems_service = EmsService(ems_config)

    # Required do_work method if using BaseWorker class
    def do_work(self):

        facility = self.facilities_service.get_facility_with_id(self.facility_id)

        # Get the facility
        print(f"Fetching main service information for {facility.name}")

        # Get the main services
        mains = self.ems_service.get_main_services(facility.id)
        print(f"{facility.name} has the following services:")
        for main in mains:
            print(f"    {main.name} ({main.resource_type})")

        # Get the utility spend
        print("Fetching utility spend")
        spend = self.ems_service.get_monthly_utility_spend(facility.id)
        for rec in spend.values:
            print(f"{rec.date} - {rec.value}")

        # Get utility usage
        print("Fetching utility usage")
        usage = self.ems_service.get_monthly_utility_usage(facility.id)
        for rec in usage.values:
            print(rec.date, rec.value)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Energy Example')

    parser.add_argument("facility_id", type=int, help="Facility ID to fetch main service data")

    args = parser.parse_args()

    worker = MainServiceFetcher(args.facility_id)
    worker.do_work()
