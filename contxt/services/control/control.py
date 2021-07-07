import requests
from sgqlc.types import list_of
from sgqlc.operation import Operation
from sgqlc.endpoint.http import HTTPEndpoint
from datetime import datetime
import pytz
from typing import List

from contxt.services.api import ApiEnvironment
from contxt.services.control.control_schema import control_schema as schema

ENVS = {
    'staging': ApiEnvironment(
        name="staging",
        base_url="https://poc.staging.ndustrial.io/control/graphql",
        client_id="https://wms-poc.staging.ndustrial.io"
    ),
    'dev': ApiEnvironment(
        name="dev",
        base_url="https://facilitycontrol.staging.opencontxt.com/graphql",
        client_id="https://ndustrial-pocs.opencontxt.com"
    )
}


class EnvironmentException(Exception):
    pass


class ControlService:

    def __init__(self, client_id: str, client_secret: str, env='staging'):
        self.token = None
        self.endpoint = None
        if not ENVS.get(env):
            raise EnvironmentException('Environment not found')
        self.env = ENVS.get(env)
        self.url = self.env.base_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.audience = self.env.client_id

    def get_auth_token(self):

        if self.token is None:
            resp = requests.post('https://contxt.auth0.com/oauth/token', json={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "audience": self.audience,
                "grant_type": "client_credentials",
            })

            if resp.status_code != 200:
                print('ERROR!')
                print(resp.text)
                return

            resp = resp.json()
            self.token = resp["access_token"]

        return self.token

    def _get_endpoint(self):
        if not self.endpoint:
            self.endpoint = HTTPEndpoint(self.url, {'Authorization': f'Bearer {self.get_auth_token()}'})
        return self.endpoint

    def get_control_events(self, facility_id: int, project_id: str = None):
        op = Operation(schema.Query)

        filters = {}
        if facility_id:
            filters['facility_id'] = facility_id

        if project_id:
            filters['project_id'] = project_id

        if len(filters) > 0:
            events = op.control_events(condition=filters)
        else:
            events = op.control_events()

        events.nodes.id()
        events.nodes.start_time()
        events.nodes.end_time()
        events.nodes.project.id()
        events.nodes.project.name()

        print(op)

        data = self._get_endpoint()(op)

        events = (op + data).control_events

        return events.nodes

    def propose_control_event(self, facility_id: int, project_id: str, start_time: datetime,
                              end_time: datetime, components: List[schema.ControllableComponent]):

        op = Operation(schema.Mutation)

        proposal = schema.ProposeControlEventInput()
        event_proposal = schema.ControlEventProposalInputRecordInput()
        event_proposal.facilityid = facility_id
        event_proposal.projectid = project_id
        event_proposal.starttime = str(start_time.astimezone(pytz.utc))
        event_proposal.endtime = str(end_time.astimezone(pytz.utc))
        proposal.proposed_event = event_proposal
        proposal.components_to_control = components

        print(proposal)
        propose = op.propose_control_event(input=proposal)

        propose.control_event.id()

        print(op)

        data = self._get_endpoint()(op)
        if 'errors' in data:
            print(data)
            raise Exception(data['errors'][0]['message'])

        event = (op + data).propose_control_event.control_event
        return event

    def add_savings_for_component_control_event(self, component: schema.ControllableComponent,
                                                control_event: schema.ControlEvent, success_metric_id: str,
                                                projected_savings_amount: float):
        op = Operation(schema.Mutation)

        input = schema.CreateControlEventMetricInput()
        metric = schema.ControlEventMetricInput()
        metric.control_event_id = control_event.id
        metric.controllable_component_id = component.id
        metric.project_success_metric_id = success_metric_id
        metric.projected_impact_amount = projected_savings_amount

        input.control_event_metric = metric

        new_metric = op.create_control_event_metric(input=input)

        new_metric.control_event_metric.project_success_metric_id()

        print(op)

        data = self._get_endpoint()(op)

        if 'errors' in data:
            print(data)
            raise Exception(data['errors'][0]['message'])

        metric = (op + data).create_control_event_metric
        return metric

    def get_controllables_for_facility(self, facility_id: int):
        op = Operation(schema.Query)

        filters = {}
        if facility_id:
            filters['facility_id'] = facility_id

        if len(filters) > 0:
            components = op.controllable_components(condition=filters)
        else:
            components = op.controllable_components()

        components.nodes.id()
        components.nodes.slug()
        components.nodes.label()

        print(op)

        data = self._get_endpoint()(op)

        components = (op + data).controllable_components

        return components.nodes

    def get_project_definition(self, project_id: str, metric_name: str = None):
        op = Operation(schema.Query)

        project = op.project(id=project_id)

        project.id()
        project.description()
        project.name()

        if metric_name:
            metrics = project.project_success_metrics(condition={'name': metric_name}).nodes()
        else:
            metrics = project.project_success_metrics().nodes()

        metrics.id()
        metrics.name()
        metrics.units()
        metrics.description()

        print(op)

        data = self._get_endpoint()(op)

        project = (op + data).project

        return project
