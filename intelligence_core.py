from copy import deepcopy
from enum import Enum


class CycleStatus(Enum):
    UPDATED = "UPDATED"
    CONFLICT = "CONFLICT"

from copy import deepcopy
from dataclasses import dataclass
from enum import Enum


class CycleStatus(Enum):
    UPDATED = "UPDATED"
    CONFLICT = "CONFLICT"


class HypothesisStatus(Enum):
    CONFIRMED = "CONFIRMED"
    REFUTED = "REFUTED"


@dataclass(frozen=True)
class Experience:
    cycle: int
    observation: object
    hypothesis_id: str
    prediction: object
    actual_result: object
    matched: bool


class IntelligenceCore:
    def __init__(self):
        self.experiences = []
        self.cycle_count = 0

    def _find_related_experiences(self, observation):
        return [
            exp
            for exp in self.experiences
            if exp.observation == observation
        ]

    def _select_hypothesis(self, hypotheses, experience):
        if not hypotheses:
            raise ValueError("hypotheses must not be empty")

        if experience is not None:
            for hypothesis in hypotheses:
                if hypothesis["prediction"] == experience.actual_result:
                    return hypothesis

        return hypotheses[0]

    def cycle(self, observation, hypotheses, actual_result):
        self.cycle_count += 1

        related_experiences = self._find_related_experiences(observation)
        related = related_experiences[-1] if related_experiences else None

        selected = self._select_hypothesis(hypotheses, related)

        prediction = selected["prediction"]
        matched = prediction == actual_result

        previous_results = {
            exp.actual_result
            for exp in related_experiences
        }

        observed_results = previous_results | {actual_result}
        conflict = len(observed_results) >= 2

        hypothesis_status = {}

        for hypothesis in hypotheses:
            hypothesis_status[hypothesis["id"]] = (
                HypothesisStatus.CONFIRMED.value
                if hypothesis["prediction"] == actual_result
                else HypothesisStatus.REFUTED.value
            )

        self.experiences.append(
            Experience(
                cycle=self.cycle_count,
                observation=deepcopy(observation),
                hypothesis_id=selected["id"],
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

        return {
            "status": status.value,
            "cycle": self.cycle_count,
            "prediction": prediction,
            "actual_result": actual_result,
            "used_experience": related is not None,
            "prediction_correct": matched,
            "conflict": conflict,
            "hypothesis_status": hypothesis_status,
        }
class HypothesisStatus(Enum):
    CONFIRMED = "CONFIRMED"
    REFUTED = "REFUTED"


class IntelligenceCore:
    """
    Minimal intelligence core.

    Keeps experience, evaluates hypotheses, and explicitly exposes
    conflicting experience for the same observation.
    """

    def __init__(self):
        self.experiences = []
        self.cycle_count = 0

    def _find_related_experiences(self, observation):
        return [
            experience
            for experience in self.experiences
            if experience["observation"] == observation
        ]

    def _find_related_experience(self, observation):
        related = self._find_related_experiences(observation)

        if not related:
            return None

        return related[-1]

    def _select_hypothesis(self, hypotheses, experience):
        if not hypotheses:
            raise ValueError("hypotheses must not be empty")

        if experience is not None:
            for hypothesis in hypotheses:
                if hypothesis["prediction"] == experience["actual_result"]:
                    return hypothesis

        return hypotheses[0]

    def cycle(self, observation, hypotheses, actual_result):
        self.cycle_count += 1

        related_experiences = self._find_related_experiences(observation)

        related = (
            related_experiences[-1]
            if related_experiences
            else None
        )

        selected = self._select_hypothesis(
            hypotheses,
            related,
        )

        prediction = selected["prediction"]
        matched = prediction == actual_result

        previous_results = {
            experience["actual_result"]
            for experience in related_experiences
        }

        observed_results = previous_results | {actual_result}
        conflict = len(observed_results) >= 2

        hypothesis_status = {}

        for hypothesis in hypotheses:
            hypothesis_status[hypothesis["id"]] = (
                HypothesisStatus.CONFIRMED.value
                if hypothesis["prediction"] == actual_result
                else HypothesisStatus.REFUTED.value
            )

        experience = {
            "cycle": self.cycle_count,
            "observation": deepcopy(observation),
            "hypothesis_id": selected["id"],
            "prediction": prediction,
            "actual_result": actual_result,
            "matched": matched,
        }

        self.experiences.append(experience)

        status = (
            CycleStatus.CONFLICT
            if conflict
            else CycleStatus.UPDATED
        )

        return {
            "status": status.value,
            "cycle": self.cycle_count,
            "prediction": prediction,
            "actual_result": actual_result,
            "used_experience": related is not None,
            "prediction_correct": matched,
            "conflict": conflict,
            "hypothesis_status": hypothesis_status,
        }
from copy import deepcopy


class IntelligenceCore:
    """
    Minimal intelligence core.

    Keeps experience, evaluates hypotheses, and explicitly exposes
    conflicting experience for the same observation.
    """

    def __init__(self):
        self.experiences = []
        self.cycle_count = 0

    def _find_related_experiences(self, observation):
        return [
            experience
            for experience in self.experiences
            if experience["observation"] == observation
        ]

    def _find_related_experience(self, observation):
        related = self._find_related_experiences(observation)

        if not related:
            return None

        return related[-1]

    def _select_hypothesis(self, hypotheses, experience):
        if not hypotheses:
            raise ValueError("hypotheses must not be empty")

        if experience is not None:
            for hypothesis in hypotheses:
                if hypothesis["prediction"] == experience["actual_result"]:
                    return hypothesis

        return hypotheses[0]

    def cycle(self, observation, hypotheses, actual_result):
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

        prediction = selected["prediction"]
        matched = prediction == actual_result

        previous_results = {
            experience["actual_result"]
            for experience in related_experiences
        }

        observed_results = previous_results | {actual_result}
        conflict = len(observed_results) >= 2

        hypothesis_status = {}

        for hypothesis in hypotheses:
            hypothesis_status[hypothesis["id"]] = (
                "CONFIRMED"
                if hypothesis["prediction"] == actual_result
                else "REFUTED"
            )

        experience = {
            "cycle": self.cycle_count,
            "observation": deepcopy(observation),
            "hypothesis_id": selected["id"],
            "prediction": prediction,
            "actual_result": actual_result,
            "matched": matched,
        }

        self.experiences.append(experience)

        if conflict:
            status = "CONFLICT"
        else:
            status = "UPDATED"

        return {
            "status": status,
            "cycle": self.cycle_count,
            "prediction": prediction,
            "actual_result": actual_result,
            "used_experience": related is not None,
            "prediction_correct": matched,
            "conflict": conflict,
            "hypothesis_status": hypothesis_status,
        }
