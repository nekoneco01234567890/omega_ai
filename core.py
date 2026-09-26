from typing import Any

from state import AIState
from observation import observe
from engine import transition


class OmegaCore:

    def __init__(self, goal: str = ""):
        self.state = AIState(goal=goal)

    def step(self, input_data: Any) -> tuple[AIState, list[dict[str, Any]]]:

        event = observe(input_data)

        next_state, effects = transition(
            self.state,
            event,
        )

        self.state = next_state

        return self.state, effects

    def get_state(self) -> AIState:
        return self.state
