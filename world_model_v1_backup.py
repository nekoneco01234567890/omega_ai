from dataclasses import dataclass, field
from copy import deepcopy


@dataclass(frozen=True)
class Knowledge:
    observation: object
    results: set = field(default_factory=set)
    history_count: int = 0

    @property
    def stable(self):
        return len(self.results) == 1

    @property
    def conflict(self):
        return len(self.results) >= 2

    @property
    def unknown(self):
        return self.history_count == 0


class WorldModel:
    def __init__(self):
        self._history = {}

    def observe(self, experience):
        if isinstance(experience, dict):
            observation = experience["observation"]
            actual_result = experience["actual_result"]
        else:
            observation = experience.observation
            actual_result = experience.actual_result

        key = repr(observation)

        entry = self._history.setdefault(
            key,
            {
                "observation": deepcopy(observation),
                "results": set(),
                "count": 0,
            },
        )

        entry["results"].add(actual_result)
        entry["count"] += 1

    def lookup(self, observation):
        key = repr(observation)

        if key not in self._history:
            return Knowledge(observation=deepcopy(observation))

        entry = self._history[key]

        return Knowledge(
            observation=deepcopy(entry["observation"]),
            results=set(entry["results"]),
            history_count=entry["count"],
        )

    def has_conflict(self, observation):
        return self.lookup(observation).conflict

    def history_size(self):
        return len(self._history)
