from typing import List

from sgqlc.endpoint.requests import RequestsEndpoint
from sgqlc.operation import Operation

from contxt.models.facilities import Facility, MetricData, MetricLabel, Mutation, Query
from contxt.services.api import ApiEnvironment, BaseGraphService

from ..auth import Auth
from ..utils.orgs import get_slug_or_org_id


class NionicService(BaseGraphService):
    """Nionic API client"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://{tenant}.api.ndustrial.io",
            client_id="vtiZlMRo4apDvThTRiH7kLifQXWUdi9j",
        ),
        ApiEnvironment(
            name="staging",
            base_url="https://{tenant}.api.staging.ndustrial.io",
            client_id="vhGxildn8hRRWZj49y18BGtbjTkFHcTG",
        ),
    )

    def __init__(self, auth: Auth, org_id: str, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, auth=auth, **kwargs)
        tenant = get_slug_or_org_id(org_id)
        self.base_url = self.base_url.format(tenant=tenant)
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
