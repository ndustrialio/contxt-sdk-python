import time
from typing import List, Dict
import threading

from contxt.utils.config import load_config_class_from_file, ContxtEnvironmentConfig
from contxt.utils.contxt_environment import ContxtEnvironment
from contxt.services.control.control import ControlService
from dataclasses import dataclass

from contxt.utils.controlsim.models import SimulationConfigs, DefinitionConfig


class SimulatorException(Exception):
    pass


def get_control_service(control_config: ContxtEnvironmentConfig = None):
    if not control_config:
        contxt_env = ContxtEnvironment()
        control_config = contxt_env.get_config_for_service_name('foundry-graph')
    if control_config.clientId is None:
        raise SimulatorException("Can't use CLI Auth for authentication in simulator. Must use the credentials of "
                                 "the Edge Node. Use `contxt env set-context foundry-graph` to select a set of Edge "
                                 "Node credentials to use")
    return ControlService(contxt_env=control_config)


@dataclass
class FrameworkState:
    is_stale: bool
    control_event_id: str
    state: str


framework_reported_current_states: Dict[str, FrameworkState] = {}


class GeneralControlEventSimulator:

    def __init__(self, config: DefinitionConfig, control: ControlService, component_slug: str):
        self.config = config
        self.control = control
        self.my_component = component_slug
        self.current_state = None
        self.timer = None

    def run(self):
        global framework_reported_current_states
        # grab out current (initial state)
        self.current_state = framework_reported_current_states.get(
            self.my_component).state

        # check on the state of things every second. if a simulated timer is running, then move on
        while True:
            time.sleep(1)
            state_config = self.config.get_state_config(self.current_state)

            if not state_config:
                print(f'Config not found for state {self.current_state}')
                return

            # if we're in a state of waiting for external input, we'll grab the state from the framework
            if not state_config.controllable:
                # can't do this since the framework state may be out of date
                framework_reported_state = framework_reported_current_states.get(
                    self.my_component)
                if framework_reported_state.is_stale:
                    print('States out of sync. Waiting for sync')
                    continue
                else:
                    self.current_state = framework_reported_state.state

                print(f'[{self.my_component}] -- current state is {self.current_state}')
                print('Waiting on external input -- not controllable by our system')

            else:
                if not self.timer:
                    self.timer = threading.Timer(state_config.delay, self.transition)
                    print(f'[{self.my_component}] -- {state_config.workMessage}')
                    print(f'[{self.my_component}] -- Setting timer to send {state_config.onSuccess} in {state_config.delay} seconds')
                    self.timer.start()

    def transition(self):
        state_config = self.config.get_state_config(self.current_state)
        event = state_config.onSuccess
        control_object = framework_reported_current_states.get(self.my_component)
        transition = self.control.transition_event(control_event_id=control_object.control_event_id,
                                                   transition_event=event)
        control_object.is_stale = True
        self.timer = None
        print(transition)
        self.current_state = transition.control_event.state_machine.current_state
        print(f'Event Transition: {event}')
        print(transition)


class Simulator:

    def __init__(self, definitions: List[str], simulator_config_filename: str):
        self.simulation_config: SimulationConfigs = load_config_class_from_file(simulator_config_filename, SimulationConfigs)
        self.control_service = get_control_service()
        self.definitions = definitions

    # Thread for querying the controls api every 5 seconds and keeping our worker threads up to date
    def run(self):
        global framework_reported_current_states
        print('Running')
        threads = {}
        framework_reported_current_states = {}
        while True:
            try:
                print('Fetching control events')
                events = self.control_service.get_edge_control_events()

                # iterate over the events and persist framework state to global config
                for event in events.nodes:
                    # if there is not a thread already for this, let's create one
                    if event.componentslug not in threads:
                        print(f'{event.componentslug}')
                        print(f'  {event.controlevent.state_machine.state_definition}')
                        print(f'  {event.controlevent.state_machine.current_state}')
                        definition_config = self.simulation_config.get_definition_config_for_slug(event.controlevent.state_machine.state_definition)
                        if not definition_config:
                            print(f'Definition config not found for '
                                  f'{event.controlevent.state_machine.state_definition}')
                            continue
                        framework_reported_current_states[event.componentslug] = \
                            FrameworkState(is_stale=False,
                                           control_event_id=event.controlevent.id,
                                           state=event.controlevent.state_machine.current_state)
                        control_sim = GeneralControlEventSimulator(config=definition_config,
                                                                   control=self.control_service,
                                                                   component_slug=event.componentslug)
                        t = threading.Thread(target=control_sim.run)
                        threads[event.componentslug] = t
                        t.start()
                    else:
                        current_framework_state = framework_reported_current_states[event.componentslug]
                        if current_framework_state.control_event_id != event.controlevent.id:
                            print('Different control event ID detected. Resetting for next cycle')
                            t = threads[event.componentslug]
                            t.join()
                            del threads[event.componentslug]
                            continue
                        framework_reported_current_states[event.componentslug] = \
                            FrameworkState(is_stale=False,
                                           control_event_id=event.controlevent.id,
                                           state=event.controlevent.state_machine.current_state)

                # sleep for 5 seconds before fetching more
                time.sleep(5)
            except KeyboardInterrupt:
                break
        print('Stopping threads')
        for component, thread in threads.items():
            thread.join()
