from world_model import WorldModel
from reasoner import Reasoner, Decision

print("=== WORLDMODEL V1 TIME COUNTEREXAMPLE ===")

reasoner = Reasoner()

# 過去と現在で同じ観測・同じ結果だが、
# 時間だけが異なるケースを作る。
past = WorldModel()
current = WorldModel()

past.observe({
    "observation": {"signal": "A"},
    "actual_result": "X",
})

current.observe({
    "observation": {"signal": "A"},
    "actual_result": "X",
})

past_k = past.lookup({"signal": "A"})
current_k = current.lookup({"signal": "A"})

past_d = reasoner.decide(past_k)
current_d = reasoner.decide(current_k)

print("PAST:", past_d.decision.value)
print("CURRENT:", current_d.decision.value)

# 現在のWorldModelでは時間情報が存在しないため、
# 同じ観測・結果ならKnowledgeは同型になる。
assert past_k.results == current_k.results
assert past_k.history_count == current_k.history_count
assert past_d.decision == current_d.decision

print("TIME_ONLY_DIFFERENCE: NOT_REPRESENTABLE")
print("DECISION_DIFFERENCE: NOT_OBSERVED")
print("TIME_REQUIREMENT: UNCONFIRMED")
print("WORLD_MODEL_CHANGE: NOT_JUSTIFIED")
print("NO DESIGN CHANGE")
