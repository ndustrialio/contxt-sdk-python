from dataclasses import dataclass
from datetime import datetime

from typing import Optional, List, Dict, AnyStr, Any

from contxt.utils.serializer import Serializer


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
    start_control_upon_approval: Optional[bool] = None
    approval_deadline_time: Optional[datetime] = None
    control_start_deadline_time: Optional[datetime] = None
    metadata: Optional[Dict[AnyStr, Any]] = None

    def __str__(self):
        return Serializer.to_pretty_cli(self)
