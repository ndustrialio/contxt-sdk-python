from contxt.services.facilities import FacilitiesService
from contxt.workers import BaseWorker


class ExampleWorker(BaseWorker):
    def __init__(self):
        super().__init__()
        facilities_config = self.env.get_config_for_service_name('facilities')
        self.facilities_service = FacilitiesService(facilities_config)

    def do_work(self):
        facilities = self.facilities_service.get_facilities()
        for facility in facilities:
            print(facility.name)


if __name__ == "__main__":
    worker = ExampleWorker()
    worker.do_work()
