from typing import List

from sgqlc.endpoint.requests import RequestsEndpoint
from sgqlc.operation import Operation

from contxt.models.facilities import Facility, MetricData, MetricLabel, Mutation, Query
from contxt.services.api import ApiEnvironment, BaseGraphService

from ..auth import Auth


class NionicService(BaseGraphService):
    """Nionic API client"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://<tenant>.api.ndustrial.io",
            client_id="vtiZlMRo4apDvThTRiH7kLifQXWUdi9j",
        ),
        ApiEnvironment(
            name="staging",
            base_url="https://<tenant>.api.staging.ndustrial.io",
            client_id="vhGxildn8hRRWZj49y18BGtbjTkFHcTG",
        ),
    )

    org_id_slugs = {
        "18d8b68e-3e59-418e-9f23-47b7cd6bdd6b": "genan",
        "02efa741-a96f-4124-a463-ae13a704b8fc": "lineage",
        "2fe29680-fc3d-4888-9e9b-44be1e59c22c": "sfnt",
        "5209751f-ea46-4b3e-a5dd-b8d03311b791": "ndustrial",
    }

    def __init__(self, auth: Auth, org_id: str, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, auth=auth, **kwargs)
        slug = self.org_id_slugs.get(org_id) or org_id
        self.base_url = self.base_url.replace("<tenant>", slug)
        self.endpoint = RequestsEndpoint(self.base_url.rstrip("/") + "/graphql", session=self.session)

    def get_facilities(self) -> List[Facility]:
        op = Operation(Query)
        op.facilities().nodes().__fields__(*list(Facility._ContainerTypeMeta__fields.keys()))
        return (op + self.run(op)).facilities.nodes

    def create_facility(self, data: dict) -> Facility:
        op = Operation(Mutation)
        op.create_facility(input={"facility": data}).__fields__("facility")
        return self.run(op)["data"]["createFacility"]["facility"]

    def get_metric_labels(self) -> List[MetricLabel]:
        op = Operation(Query)
        op.metric_labels().__fields__(*list(MetricLabel._ContainerTypeMeta__fields.keys()))
        return self.run(op).get("data").get("metricLabels")

    def get_metric_data(self, label: str, source_id: str) -> List[MetricData]:
        op = Operation(Query)
        fields = list(MetricData._ContainerTypeMeta__fields.keys())
        fields.remove("id")
        op.metric_data(source_id=source_id, label=label).nodes().__fields__(*fields)
        return (op + self.run(op)).metric_data.nodes
