from contxt.services.control.control import ControlService

import click

SANDBOX_CLIENT_ID = "XZnouDOjhmb65Fp954myAedX6wxVNbXc"
SANDBOX_CLIENT_SECRET = "DbDJOdTQA_1dO-hkQyeUyDGfuJcJy4WL1s6j_sytNt9BSeKqtXh_p0lwsHEQ5X-4"


@click.group()
def control() -> None:
    """Facility Control Functions"""


@control.command()
@click.option('--facility-id', type=int)
@click.option('--project-id', type=str)
def get_events(facility_id: int, project_id: str):
    control = ControlService(client_id=SANDBOX_CLIENT_ID,
                             client_secret=SANDBOX_CLIENT_SECRET,
                             env="staging")
    events = control.get_control_events(facility_id=facility_id, project_id=project_id)
    for event in events:
        print(event)


@control.command()
def get_token():
    control = ControlService(client_id=SANDBOX_CLIENT_ID,
                             client_secret=SANDBOX_CLIENT_SECRET,
                             env="staging")
    print(control.get_auth_token())


@click.group(context_settings=dict(help_option_names=["-h", "--help"], show_default=True))
def cli() -> None:
    pass
