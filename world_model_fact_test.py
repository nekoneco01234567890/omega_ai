from intelligence_core import IntelligenceCore
from world_model import WorldModel

core = IntelligenceCore()
world = WorldModel()

for result in ["X", "X"]:
    core.cycle(
        observation={"signal": "A"},
        hypotheses=[{"id": "H1", "prediction": result}],
        actual_result=result,
    )
    world.observe(core.experiences[-1])

k = world.lookup({"signal": "A"})

assert k.results == {"X"}
assert k.history_count == 2
assert world.has_conflict({"signal": "A"}) is False

print("WORLD MODEL FACT TEST: PASS")
