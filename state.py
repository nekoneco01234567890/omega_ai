# state.py

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AIState:
    goal: str = ""
    world_state: dict[str, Any] = field(default_factory=dict)
    facts: list[Any] = field(default_factory=list)
    hypotheses: list[Any] = field(default_factory=list)
    results: list[Any] = field(default_factory=list)
    unknowns: list[Any] = field(default_factory=list)
    history: list[Any] = field(default_factory=list)
