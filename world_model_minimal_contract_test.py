from intelligence_core import IntelligenceCore
from world_model import WorldModel


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


core = IntelligenceCore()
world = WorldModel()

# 1. 未観測
unknown = world.lookup({"signal": "NEW"})
assert unknown.unknown
assert not unknown.stable
assert not unknown.conflict

# 2. 同一観測・同一結果
world.observe(experience(core, {"signal": "A"}, "X"))
world.observe(experience(core, {"signal": "A"}, "X"))

stable = world.lookup({"signal": "A"})
assert stable.results == {"X"}
assert stable.history_count == 2
assert stable.stable
assert not stable.conflict
assert not stable.unknown

# 3. 同一観測・異なる結果
world.observe(experience(core, {"signal": "A"}, "Y"))

conflict = world.lookup({"signal": "A"})
assert conflict.results == {"X", "Y"}
assert conflict.history_count == 3
assert conflict.conflict
assert not conflict.stable

# 4. 別観測は混ざらない
world.observe(experience(core, {"signal": "B"}, "X"))

other = world.lookup({"signal": "B"})
assert other.results == {"X"}
assert other.stable
assert not world.lookup({"signal": "A"}).stable

# 5. 未観測と既観測を区別
assert world.lookup({"signal": "C"}).unknown
assert not world.lookup({"signal": "B"}).unknown

print("WORLD MODEL MINIMAL CONTRACT: PASS")
print("UNKNOWN / STABLE / CONFLICT / OBSERVATION SEPARATION: PASS")
print("NO DESIGN CHANGE")
