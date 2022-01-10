from contxt.services.control.control import ControlService
from contxt.utils.serializer import Serializer
import click
from contxt.services.api import ApiEnvironment
from contxt.utils.contxt_environment import ContxtEnvironment


def get_control_service():
    # load configuration file
    contxt_env = ContxtEnvironment()
    return ControlService(contxt_env=contxt_env.get_config_for_service_name('foundry-graph'))


@click.group()
def control() -> None:
    """Facility Control Functions"""


# Schema functions
@click.group()
def schema() -> None:
    """Schema Functions"""


@schema.command()
def update():
    print('Updating schema')
    get_control_service().update_schema('control')


# Getter functions
@click.group()
def get() -> None:
    """Get Functions"""


@get.command()
def organizations():
    orgs = get_control_service().get_organizations()
    print(Serializer.to_table(orgs))


@get.command()
def facilities():
    facilities = get_control_service().get_facilities(include_events=False)
    print(Serializer.to_table(facilities))


@get.command()
@click.argument('facility-id', type=int)
def facility(facility_id: int):
    facility = get_control_service().get_facility(facility_id)
    print(Serializer.to_pretty_cli(facility))


@get.command()
@click.option('--facility-id', type=int, required=True)
@click.option('--slug', type=str)
def controllables(facility_id: int, slug: str = None):
    control = get_control_service()
    controllables = control.get_controllables_for_facility(facility_id=facility_id, component_slug=slug, include_events=True)
    for controllable in controllables:
        print(Serializer.to_pretty_cli(controllable))


@get.command()
@click.option('--facility-id', type=int)
@click.option('--project-id', type=str)
def events(facility_id: int, project_id: str):
    control = get_control_service()
    events = control.get_control_events(facility_id=facility_id, project_id=project_id)
    for event in events:
        print(event)


@get.command()
@click.argument('control-event-id', type=str)
def event(control_event_id: str):
    event = get_control_service().get_control_event_detail(control_event_id=control_event_id)
    print(Serializer.to_pretty_cli(event))


@get.command()
@click.option('--facility-id', type=int)
def projects(facility_id: int):
    control = get_control_service()
    projects = control.get_projects(facility_id)
    print(Serializer.to_table(projects))


@get.command()
@click.argument('project-id', type=str, required=True)
def project(project_id: str):
    control = get_control_service()
    project = control.get_project_definition(project_id=project_id)
    print(Serializer.to_pretty_cli(project))


@get.command()
@click.option('--facility-id', type=int)
def edge_nodes(facility_id: int = None):
    edge_nodes = get_control_service().get_edge_nodes(facility_id)
    print(Serializer.to_table(edge_nodes))


@get.command()
@click.argument('edge-node-client-id', type=str)
def edge_node(edge_node_client_id: str = None):
    edge_node = get_control_service().get_edge_node(edge_node_client_id)
    print(Serializer.to_pretty_cli(edge_node))


@get.command()
@click.argument('edge-node-client-id', type=str)
def edge_node_events(edge_node_client_id: str):
    events = get_control_service().get_edge_control_events(edge_node_client_id)
    print(Serializer.to_pretty_cli(events))


@get.command()
@click.argument('event-definition-id', type=str, required=False)
def definitions(event_definition_id: str = None):
    definitions = get_control_service().get_definitions(event_definition_id)
    if event_definition_id:
        import json
        print(json.dumps(json.loads(definitions.definition), indent=4))
    else:
        print(Serializer.to_pretty_cli(definitions))


# Transition function
@control.command()
@click.option('--event', type=str, required=True)
@click.argument('control-event-id', type=str)
def transition(control_event_id: str, event: str):
    control_event = get_control_service().transition_event(control_event_id=control_event_id,
                                                           transition_event=event)
    print(Serializer.to_pretty_cli(control_event))


# Generate functions
@click.group()
def generate() -> None:
    """Generate Functions"""


@generate.command()
def token():
    control = get_control_service()
    print(control.get_auth_token())


# Create functions
@click.group()
def create() -> None:
    """Create Functions"""


@create.command()
@click.option('--name', type=str, prompt=True)
@click.option('--id', type=int, prompt=True)
@click.option('--organization_id', type=str, prompt=True)
def facility(name: str, id: int, organization_id: str):
    facility = get_control_service().create_facility(name=name, id=id, organization_id=organization_id)
    print(Serializer.to_pretty_cli(facility))


#def controllable()


@click.group(context_settings=dict(help_option_names=["-h", "--help"], show_default=True))
def cli() -> None:
    pass


control.add_command(create)
control.add_command(get)
control.add_command(generate)
control.add_command(schema)
