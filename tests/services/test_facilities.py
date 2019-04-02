import requests_mock
from contxt.services.facilities import FacilitiesService

@pytest.fixture
def create_facilities_service():
    return FacilitiesService('')

@requests_mock.Mocker()
def test_function(m):
    mock_service = create_facilities_service()
    m.get(mock_service.base_url, text='resp')
    return mock_service.get_facilities()