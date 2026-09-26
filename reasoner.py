from dataclasses import dataclass
from enum import Enum


class Decision(Enum):
    PASS = "PASS"
    HOLD = "HOLD"
    CONFLICT = "CONFLICT"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class ReasonerResult:
    decision: Decision
    reason: str


class Reasoner:
    """
    WorldModel -> Decision
    """

    def decide(self, knowledge):
        if knowledge.unknown:
            return ReasonerResult(
                decision=Decision.UNKNOWN,
                reason="no experience",
            )

        if knowledge.conflict:
            return ReasonerResult(
                decision=Decision.CONFLICT,
                reason="conflicting experience",
            )

        if knowledge.stable:
            return ReasonerResult(
                decision=Decision.PASS,
                reason="stable experience",
            )

        return ReasonerResult(
            decision=Decision.HOLD,
            reason="insufficient evidence",
        )
