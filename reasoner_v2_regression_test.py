from reasoner import Reasoner, Decision
from world_model import WorldModel
from intelligence_core import IntelligenceCore


HYPOTHESES = [
    {"id": "H1", "prediction": "X"},
    {"id": "H2", "prediction": "Y"},
]


def experience(core, observation, actual):
    core.cycle(
        observation=observation,
        hypotheses=HYPOTHESES,
        actual_result=actual,
    )
    return core.experiences[-1]


print("=== REASONER V2 REGRESSION TEST ===")

core = IntelligenceCore()
world = WorldModel()
()
reasoner = Reasoner()

# UNKNOWN
unknown = world.lookup({"signal": "UNKNOWN"})
result = reasoner.decide(unknown)

assert result.decision == Decision.UNKNOWN
assert result.reason == "no experience"
print("UNKNOWN: PASS")

# PASS
world.observe(experience(core, {"signal": "A"}, "X"))
world.observe(experience(core, {"signal": "A"}, "X"))

stable = world.lookup({"signal": "A"})
result = reasoner.decide(stable)

assert stable.stable
assert not stable.conflict
assert not stable.unknown
assert result.decision == Decision.PASS
assert result.reason == "stable experience"

print("PASS: PASS")

# CONFLICT
world.observe(experience(core, {"signal": "A"}, "Y"))

conflict = world.lookup({"signal": "A"})
result = reasoner.decide(conflict)

assert conflict.conflict
assert not conflict.stable
assert result.decision == Decision.CONFLICT
assert result.reason == "conflicting experience"

print("CONFLICT: PASS")

# Observation isolation
other = world.lookup({"signal": "B"})

assert other.unknown
assert reasoner.decide(other).decision == Decision.UNKNOWN

print("OBSERVATION ISOLATION: PASS")

# Minimal contract
observed_decisions = {
    Decision.UNKNOWN,
    Decision.PASS,
    Decision.CONFLICT,
}

assert {
    reasoner.decide(unknown).decision,
    reasoner.decide(stable).decision,
    reasoner.decide(conflict).decision,
} == observed_decisions

print("MINIMAL CONTRACT: PASS")
print("REASONER V2 REGRESSION: PASS")
print("NO DESIGN CHANGE")
