from dataclasses import dataclass
from typing import Any
from uuid import uuid4


@dataclass(frozen=True)
class Event:
    event_id: str
    type: str
    data: Any


def observe(input_data: Any) -> Event:
    return Event(
        event_id=str(uuid4()),
        type="observation",
        data=input_data,
    )
