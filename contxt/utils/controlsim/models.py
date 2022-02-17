from dataclasses import dataclass

from typing import Optional, List, Dict


@dataclass
class SimulatedStateConfig:
    controllable: bool
    delay: Optional[int]
    workMessage: Optional[str]
    onSuccess: Optional[str]
    onFail: Optional[str]


@dataclass
class DefinitionConfig:
    definitionSlug: str
    appliesTo: str
    simulatedStateConfigs: Dict[str, SimulatedStateConfig]

    def get_state_config(self, state: str):
        return self.simulatedStateConfigs.get(state)


@dataclass
class SimulationConfigs:
    simulationConfigs: List[DefinitionConfig]

    def get_definition_config_for_slug(self, slug: str):
        for sim in self.simulationConfigs:
            if sim.definitionSlug == slug:
                return sim
