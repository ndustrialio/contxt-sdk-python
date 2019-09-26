from contxt.services.facilities import FacilitiesService
from contxt.workers import BaseWorker


class ExampleWorker(BaseWorker):
    def __init__(self):
        super().__init__()
        self.facilities_service = FacilitiesService(self.auth)

    def do_work(self):
        facilities = self.facilities_service.get_facilities()
        print(facilities)


if __name__ == "__main__":
    worker = ExampleWorker()
    worker.do_work()
