from contxt.auth.cli import CliAuth
from contxt.services import EmsService, FacilitiesService


class TestEmsServices:
    facilities = FacilitiesService(CliAuth(), env="staging")
    service = EmsService(CliAuth(), env="staging")

    def test_get_contracts(self):
        contracts = self.service.get_utility_contracts_for_facility(66)
        for c in contracts:
            for r in c.utility_contract_reminders:
                print(r)


if __name__ == "__main__":
    TestEmsServices().test_get_contracts()
