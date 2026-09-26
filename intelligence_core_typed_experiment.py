from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
from typing import Any, Sequence


class CycleStatus(Enum):
    UPDATED = "UPDATED"
    CONFLICT = "CONFLICT"


class HypothesisStatus(Enum):
    CONFIRMED = "CONFIRMED"
    REFUTED = "REFUTED"


@dataclass(frozen=True)
class Hypothesis:
    id: str
    prediction: Any


@dataclass(frozen=True)
class Experience:
    cycle: int
    observation: Any
    hypothesis_id: str
    prediction: Any
    actual_result: Any
    matched: bool


@dataclass(frozen=True)
class CycleResult:
    status: CycleStatus
    cycle: int
    prediction: Any
    actual_result: Any
    used_experience: bool
    prediction_correct: bool
    conflict: bool
    hypothesis_status: dict[str, HypothesisStatus]


class IntelligenceCoreTyped:
    def __init__(self) -> None:
        self.experiences: list[Experience] = []
        self.cycle_count: int = 0

    def _find_related_experiences(
        self,
        observation: Any,
    ) -> list[Experience]:
        return [
            experience
            for experience in self.experiences
            if experience.observation == observation
        ]

    def _select_hypothesis(
        self,
        hypotheses: Sequence[Hypothesis],
        experience: Experience | None,
    ) -> Hypothesis:
        if not hypotheses:
            raise ValueError("hypotheses must not be empty")

        if experience is not None:
            for hypothesis in hypotheses:
                if hypothesis.prediction == experience.actual_result:
                    return hypothesis

        return hypotheses[0]

    def cycle(
        self,
        observation: Any,
        hypotheses: Sequence[Hypothesis],
        actual_result: Any,
    ) -> CycleResult:
        self.cycle_count += 1

        related_experiences = self._find_related_experiences(
            observation
        )

        related = (
            related_experiences[-1]
            if related_experiences
            else None
        )

        selected = self._select_hypothesis(
            hypotheses,
            related,
        )

        prediction = selected.prediction
        matched = prediction == actual_result

        previous_results = {
            experience.actual_result
            for experience in related_experiences
        }

        conflict = bool(previous_results) and (
            actual_result not in previous_results
        )

        hypothesis_status = {
            hypothesis.id: (
                HypothesisStatus.CONFIRMED
                if hypothesis.prediction == actual_result
                else HypothesisStatus.REFUTED
            )
            for hypothesis in hypotheses
        }

        self.experiences.append(
            Experience(
                cycle=self.cycle_count,
                observation=deepcopy(observation),
                hypothesis_id=selected.id,
                prediction=prediction,
                actual_result=actual_result,
                matched=matched,
            )
        )

        status = (
            CycleStatus.CONFLICT
            if conflict
            else CycleStatus.UPDATED
        )

        return CycleResult(
            status=status,
            cycle=self.cycle_count,
            prediction=prediction,
            actual_result=actual_result,
            used_experience=related is not None,
            prediction_correct=matched,
            conflict=conflict,
            hypothesis_status=hypothesis_status,
        )


def normalize(result: CycleResult) -> dict[str, Any]:
    return {
        "status": result.status.value,
        "cycle": result.cycle,
        "prediction": result.prediction,
        "actual_result": result.actual_result,
        "used_experience": result.used_experience,
        "prediction_correct": result.prediction_correct,
        "conflict": result.conflict,
        "hypothesis_status": {
            key: value.value
            for key, value in result.hypothesis_status.items()
        },
    }
