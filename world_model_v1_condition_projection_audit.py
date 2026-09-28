from world_model import WorldModel

print("=== WORLDMODEL V1 CONDITION PROJECTION AUDIT ===")

# 現実世界では条件が異なる2状態を仮想的に定義する。
# ただしWorldModelにはconditionを渡さない。
case_a = {
    "observation": {"signal": "A"},
    "actual_result": "X",
    "condition": "NORMAL",
}

case_b = {
    "observation": {"signal": "A"},
    "actual_result": "X",
    "condition": "STRESSED",
}

# 現在のWorldModelが実際に保持する情報だけを入力する。
world_a = WorldModel()
world_b = WorldModel()

world_a.observe({
    "observation": case_a["observation"],
    "actual_result": case_a["actual_result"],
})

world_b.observe({
    "observation": case_b["observation"],
    "actual_result": case_b["actual_result"],
})

ka = world_a.lookup({"signal": "A"})
kb = world_b.lookup({"signal": "A"})

# 条件だけが違うのに、現在のKnowledgeは完全に同一になる。
same_representation = (
    ka.observation == kb.observation
    and ka.results == kb.results
    and ka.history_count == kb.history_count
)

print("REAL_WORLD_CONDITION_DIFFERENCE: PRESENT")
print("CURRENT_KNOWLEDGE_DIFFERENCE:", not same_representation)

assert same_representation

print("CONDITION_INFORMATION_COLLAPSE: CONFIRMED")
print("CONDITION_IS_NOT_REPRESENTED: CONFIRMED")
print("CONDITION_REQUIREMENT: NOT_YET_PROVEN")
print("FALSE_NEGATIVE_RISK: CANDIDATE")
print("WORLD_MODEL_CHANGE: NOT_YET_JUSTIFIED")
print("NO DESIGN CHANGE")
