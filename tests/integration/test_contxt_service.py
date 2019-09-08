import pytest

from contxt.auth.cli import CliAuth
from contxt.models.contxt import Organization, User
from contxt.services import ContxtService
from tests.static.data import TestOrganization, TestUser, TestWorker


class TestContxtService:
    service = ContxtService(CliAuth())

    def test_get_organizations(self):
        organizations = self.service.get_organizations()
        assert all([isinstance(o, Organization) for o in organizations])

    def test_get_organization_with_name(self):
        organization = self.service.get_organization_with_name(TestOrganization.name)
        assert organization.name.lower() == TestOrganization.name.lower()
        assert organization.id == TestOrganization.id

    @pytest.mark.skip(reason="Non-GET endpoint")
    def test_create_organization(self):
        created_organization = self.service.create_organization(
            Organization.make(name="test-org")
        )
        assert created_organization.name == "test-org"

    @pytest.mark.skip(reason="Non-GET endpoint")
    def test_create_organization_user(self):
        organization_user = self.service.create_organization_user(
            TestUser.id, TestOrganization.id
        )
        assert organization_user.user_id == TestUser.id
        assert organization_user.organization_id == TestOrganization.id

    def test_get_users_for_organization(self):
        users = self.service.get_users_for_organization(TestOrganization.id)
        assert all([isinstance(u, User) for u in users])

    def test_get_config(self):
        config = self.service.get_config(TestWorker.config_id)
        assert config.id == TestWorker.config_id

    def test_get_config_for_client(self):
        config = self.service.get_config_for_client(
            TestWorker.client_id, TestWorker.env_id
        )
        assert config
