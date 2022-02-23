from contxt.services.facilities import FacilitiesService
from contxt.utils.serializer import Serializer
from contxt.workers import BaseWorker


class ExampleWorker(BaseWorker):
    def __init__(self):
        super().__init__()
        facilities_config = self.env.get_config_for_service_name('facilities')
        self.facilities_service = FacilitiesService(facilities_config)

    def do_work(self):
        facilities = self.facilities_service.get_facilities()
        print(Serializer.to_table(facilities, exclude_keys=['organization','tags','info'], sort_by='id'))


if __name__ == "__main__":
    worker = ExampleWorker()
    worker.do_work()
