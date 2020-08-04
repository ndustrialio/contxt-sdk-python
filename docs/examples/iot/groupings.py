from contxt.services.facilities import FacilitiesService
from contxt.services.iot import IotService, IotDataService
from contxt.workers import BaseWorker
from contxt.utils.serializer import Serializer

import argparse
import os, sys


class IOTServiceFetcher(BaseWorker):

    def __init__(self, facility_id):
        super().__init__()
        self.facilities_service = FacilitiesService(self.auth)
        self.facility_id = facility_id
        self.iot_service = IotService(self.auth)
        #self.data_service = IotDataService(self.auth)

    # Required do_work method if using BaseWorker class
    def do_work(self):

        facility = self.facilities_service.get_facility_with_id(self.facility_id)

        # Get the facility
        print(f"Fetching groupings for {facility.name}")

        # Get groupings
        groupings = self.iot_service.get_field_groupings_for_facility(facility.id)

        pretty_groupings = []
        for group in groupings:
            pretty_groupings.append({
                'ID': group.id,
                'Label': group.label,
                'Category': group.field_category.name if group.field_category else 'N/A',
                'Field Count': len(group.fields)
            })
        print(Serializer.to_table(pretty_groupings))


if __name__ == "__main__":

    if 'CLIENT_ID' not in os.environ:
        print('Must have CLIENT_ID set in the environment')
    if 'CLIENT_SECRET' not in os.environ:
        print('Must have CLIENT_SECRET set in the environment')

    if not (os.environ.get("CLIENT_ID") and os.environ.get("CLIENT_SECRET")):
        sys.exit()

    parser = argparse.ArgumentParser(description='IOT Example')

    parser.add_argument("facility_id", type=int, help="Facility ID to fetch groupings")

    args = parser.parse_args()

    worker = IOTServiceFetcher(args.facility_id)
    worker.do_work()
