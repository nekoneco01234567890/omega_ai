from intelligence_core import IntelligenceCore
from world_model import WorldModel

core = IntelligenceCore()
world = WorldModel()

for result in ["X", "Y"]:
    core.cycle(
        observation={"signal": "A"},
        hypotheses=[{"id": "H1", "prediction": result}],
        actual_result=result,
    )
    world.observe(core.experiences[-1])

k = world.lookup({"signal": "A"})

assert world.has_conflict({"signal": "A"}) is True
assert k.conflict is True

print("WORLD MODEL CONFLICT TEST: PASS")
