from intelligence_core import IntelligenceCore
from world_model import WorldModel
from reasoner import Reasoner, Decision

HYPOTHESES = [
    {"id": "H1", "prediction": "X"},
    {"id": "H2", "prediction": "Y"},
]

core = IntelligenceCore()
world = WorldModel()
reasoner = Reasoner()


def learn(signal, actual):
    result = core.cycle(
        observation={"signal": signal},
        hypotheses=HYPOTHESES,
        actual_result=actual,
    )
    world.observe(core.experiences[-1])
    return result


print("=== WORLD + REASONER INTEGRATION TEST ===")

# 1. UNKNOWN
k = world.lookup({"signal": "NEW"})
print("UNKNOWN:", reasoner.decide(k).decision.value)

# 2. PASS
learn("A", "X")
learn("A", "X")
k = world.lookup({"signal": "A"})
print("PASS:", reasoner.decide(k).decision.value)

# 3. CONFLICT
learn("B", "X")
learn("B", "Y")
k = world.lookup({"signal": "B"})
print("CONFLICT:", reasoner.decide(k).decision.value)

print("=== INTEGRATION TEST COMPLETE ===")
