from contxt.workers import BaseWorker

from contxt.functions.facilities import Facilities


class TestWorker(BaseWorker):

    def __init__(self):

        super().__init__()

        self.facilities = Facilities(auth_module=self.auth_module)

    def doWork(self):

        facilities = self.facilities.get_all_facilities()
        print(facilities)


if __name__ == '__main__':

    worker = TestWorker()
    worker.doWork()
