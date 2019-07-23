from contxt.auth.cli import CliAuth
from contxt.models.contxt import Organization, User
from contxt.services import ContxtService
from tests.static.data import TestOrganization, TestWorker


class TestContxtService:
    service = ContxtService(CliAuth())

    def test_get_organizations(self):
        organizations = self.service.get_organizations()
        assert all([isinstance(o, Organization) for o in organizations])

    def test_get_organization_with_name(self):
        organization = self.service.get_organization_with_name(TestOrganization.name)
        assert organization.name.lower() == TestOrganization.name.lower()
        assert organization.id == TestOrganization.id

    def test_create_organization(self):
        pass
        # created_organization = self.service.create_organization(new_organization)
        # assert created_organization

    def test_add_user_to_organization(self):
        pass
        # organization_user = self.service.add_user_to_organization(
        #     user_id, organization_id
        # )
        # assert organization_user.user_id == user_id
        # assert organization_user.organization_id == organization_id

    def test_get_users_for_organization(self):
        users = self.service.get_users_for_organization(TestOrganization.id)
        assert all([isinstance(u, User) for u in users])

    def test_get_config(self):
        config = self.service.get_config(TestWorker.config_id)
        assert config.id == TestWorker.config_id

    # TODO: figure out valid values (these fails with "Access denied for scopes
    # init:clients")
    def test_get_config_for_client(self):
        pass
        # config = self.service.get_config_for_client(client_id, env_id)
        # assert config

    # TODO: this endpoint fail (cannot GET)
    def test_get_config_values(self):
        values = self.service.get_config_values(TestWorker.config_id, TestWorker.env_id)
        assert values

    # TODO: figure out valid value for worker_id
    def test_get_config_values_for_worker(self):
        pass
        # values = self.service.get_config_values_for_worker(worker_id)
        # assert values

    def test_start_worker_run(self):
        pass
        # response = self.service.start_worker_run(client_id)
        # assert response

    def test_end_worker_run(self):
        pass
        # self.service.end_worker_run(client_id, run_id)

    def test_create_worker_run_metric(self):
        pass
        # response = self.service.create_worker_run_metric()
        # assert response
