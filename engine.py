from copy import deepcopy
from typing import Any
from uuid import uuid4

from state import AIState
from observation import Event


def transition(
    state: AIState,
    event: Event,
) -> tuple[AIState, list[dict[str, Any]]]:

    next_state = deepcopy(state)

    next_state.history.append({
        "event_id": event.event_id,
        "type": event.type,
        "data": event.data,
    })

    effects: list[dict[str, Any]] = [
        {
            "effect_id": str(uuid4()),
            "type": "test_effect_1",
            "data": event.data,
        },
        {
            "effect_id": str(uuid4()),
            "type": "test_effect_2",
            "data": event.data,
        },
    ]

    return next_state, effects
