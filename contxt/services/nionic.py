from typing import Any, Iterable, List, Optional

from sgqlc.endpoint.requests import RequestsEndpoint

from contxt.generated.nionic_queries import Operations as nionic_operations
from contxt.generated.nionic_schema import Facility, MainService, MetricLabel
from contxt.models.ems import ResourceType
from contxt.models.iot import Window
from contxt.services.api import ApiEnvironment, BaseGraphService

from ..auth import Auth
from .pagination import DataPoint, PagedGQLTimeSeries


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

    def __init__(self, auth: Auth, org_slug: str, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, auth=auth, **kwargs)
        self.base_url = self.base_url.format(tenant=org_slug)
        self.endpoint = RequestsEndpoint(self.base_url.rstrip("/") + "/graphql", session=self.session)

    def get_facilities(self) -> List[Facility]:
        op = nionic_operations.query.facilities
        return (op + self.run(op)).facilities.nodes

    def create_facility(self, data: dict) -> Facility:
        op = nionic_operations.mutation.create_facility
        return self.run(op, data)["data"]["createFacility"]["facility"]

    def get_metric_labels(self) -> List[MetricLabel]:
        op = nionic_operations.query.metric_labels
        return self.run(op).get("data").get("metricLabels")

    def get_metric_data(self, label: str, facility_id: int, start: str) -> List[Any]:
        query = """
        query metricData($facilityId: Int!, $label: String!, $from: String!) {
            facility(id: $facilityId) {
                metricData(label: $label, from: $from) {
                    nodes {
                        time
                        data
                    }
                }
            }
        }
        """
        resp = self.query(query, {"facilityId": int(facility_id), "label": label, "from": start})
        return resp["facility"]["metricData"]["nodes"]

    def get_main_services(
        self, facility_id: int, resource_type: Optional[ResourceType] = None
    ) -> List[MainService]:
        op = nionic_operations.query.main_services
        filterValues = {"facilityId": int(facility_id)}
        return [
            x
            for x in (op + self.run(op, variables=filterValues)).main_services.nodes
            if resource_type is None or x.type.lower() == resource_type.value
        ]

    def get_data_point_data(
        self, name: str, data_source_name: str, start: str, end: str, window: Window, per_page: int
    ) -> Iterable[DataPoint]:
        return PagedGQLTimeSeries(
            api=self,
            query="""
            query dataPointData($dataSourceName: String!, $name: String!
                , $from: String!, $to: String!, $window: String!, $samplingWindow: String!
                , $limit: Int!, $after: Cursor) {
                dataPoint(dataSourceName: $dataSourceName, name: $name) {
                    data(from: $from, to: $to, orderBy: TIME_DESC
                    , window: $window, samplingWindow: $samplingWindow
                    , first: $limit, after: $after) {
                        nodes {
                            time
                            data
                        }
                        pageInfo {
                            hasNextPage
                            endCursor
                        }
                    }
                }
            }
            """,
            params={
                "dataSourceName": data_source_name,
                "name": name,
                "from": start,
                "to": end,
                "window": f"{window.value} seconds",
                # limit to 1 day if window is greater than 1 day
                "samplingWindow": f"{min(window.value, 86400)} seconds",
            },
            per_page=per_page,
        )
