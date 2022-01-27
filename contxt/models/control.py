from dataclasses import dataclass
from datetime import datetime

from enum import Enum
from typing import Optional, List, Dict


@dataclass
class EventProposal:
    id: int
    start_time: datetime
    end_time: datetime
    current_state: str


@dataclass
class ControllableComponent:
    id: str
    state_definition_slug: Optional[str]


@dataclass
class Suggestion:
    project_id: str
    facility_id: int
    start_time: datetime
    end_time: datetime
    summary: str
    components: List[ControllableComponent]

