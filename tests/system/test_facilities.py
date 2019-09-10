from contxt.auth.cli import CliAuth
from contxt.models.facilities import Facility
from contxt.services import FacilitiesService
from contxt.utils.serializer import Serializer


class TestFacilities:
    service = FacilitiesService(CliAuth())

    def test_get_facilities(self):
        print(CliAuth)
        facilities = self.service.get_facilities()
        assert facilities
        assert all([isinstance(f, Facility) for f in facilities])
        print(Serializer.to_table(facilities))
        for f in facilities:
            assert str(f), (
                f"Facility to string conversion returned None or empty string, "
                f"facility: {f.name} ({f.id})"
            )
