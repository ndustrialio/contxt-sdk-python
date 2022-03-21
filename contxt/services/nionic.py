from typing import List, Optional

from sgqlc.operation import Operation

from contxt.models.facilities import Facility, MetricData, MetricLabel, Mutation, Query
from contxt.services.base_graph_service import BaseGraphService

from ..auth import Auth


class NionicService(BaseGraphService):
    """Nionic API client"""

    _envs = BaseGraphService._envs

    def __init__(self, auth: Auth, env: str = "production", org_id: str = "ndustrial", **kwargs) -> None:
        self.default_org_id = org_id
        super().__init__(env=env, auth=auth)

    def get_facilities(self, organization_id: Optional[str] = None) -> List[Facility]:
        op = Operation(Query)
        op.facilities().nodes().__fields__(*list(Facility._ContainerTypeMeta__fields.keys()))

        data = self.run(op, organization_id or self.default_org_id)
        return (op + data).facilities.nodes

    def create_facility(self, data: dict, organization_id: Optional[str] = None) -> Facility:
        op = Operation(Mutation)
        op.create_facility(input={"facility": data}).__fields__("facility")

        data = self.run(op, organization_id or self.default_org_id)

        facility = data["data"]["createFacility"]["facility"]
        return facility

    def get_metric_labels(self, organization_id: Optional[str] = None) -> List[MetricLabel]:
        op = Operation(Query)
        op.metric_labels().__fields__(*list(MetricLabel._ContainerTypeMeta__fields.keys()))

        data = self.run(op, organization_id or self.default_org_id)

        metric_labels = data.get("data").get("metricLabels")
        return metric_labels

    def get_metric_data(
        self, label: str, source_id: str, organization_id: Optional[str] = None
    ) -> List[MetricData]:
        op = Operation(Query)
        fields = list(MetricData._ContainerTypeMeta__fields.keys())
        fields.remove("id")
        op.metric_data(source_id=source_id, label=label).nodes().__fields__(*fields)

        data = self.run(op, organization_id or self.default_org_id)

        return (op + data).metric_data.nodes
