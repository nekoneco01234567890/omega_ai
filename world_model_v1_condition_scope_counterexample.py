from world_model import WorldModel
from reasoner import Reasoner

print("=== WORLDMODEL V1 CONDITION / SCOPE COUNTEREXAMPLE ===")

reasoner = Reasoner()


def make_model(observation, result):
    world = WorldModel()
    world.observe({
        "observation": observation,
        "actual_result": result,
    })
    return world


# CONDITION
# 条件だけが違うケース
condition_a = make_model(
    {"signal": "A"},
    "X",
)

condition_b = make_model(
    {"signal": "A"},
    "X",
)

ka = condition_a.lookup({"signal": "A"})
kb = condition_b.lookup({"signal": "A"})

da = reasoner.decide(ka)
db = reasoner.decide(kb)

assert ka.results == kb.results
assert ka.history_count == kb.history_count
assert da.decision == db.decision

print("CONDITION_ONLY_DIFFERENCE: NOT_REPRESENTABLE")
print("CONDITION_DECISION_DIFFERENCE: NOT_OBSERVED")


# SCOPE
# 判断対象の範囲だけが違うケース
scope_a = make_model(
    {"signal": "A"},
    "X",
)

scope_b = make_model(
    {"signal": "A"},
    "X",
)

sa = scope_a.lookup({"signal": "A"})
sb = scope_b.lookup({"signal": "A"})

dsa = reasoner.decide(sa)
dsb = reasoner.decide(sb)

assert sa.results == sb.results
assert sa.history_count == sb.history_count
assert dsa.decision == dsb.decision

print("SCOPE_ONLY_DIFFERENCE: NOT_REPRESENTABLE")
print("SCOPE_DECISION_DIFFERENCE: NOT_OBSERVED")


print("CONDITION_REQUIREMENT: UNCONFIRMED")
print("SCOPE_REQUIREMENT: UNCONFIRMED")
print("WORLD_MODEL_CHANGE: NOT_JUSTIFIED")
print("NO DESIGN CHANGE")
