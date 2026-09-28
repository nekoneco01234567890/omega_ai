from world_model import WorldModel

print("=== CONDITION GENERALIZATION AUDIT ===")

# 現実上は異なる条件
normal_case = {
    "observation": {"signal": "A"},
    "actual_result": "X",
    "condition": "NORMAL",
}

stressed_case = {
    "observation": {"signal": "A"},
    "actual_result": "Y",
    "condition": "STRESSED",
}

# 現在のWorldModelにconditionを渡さない。
world = WorldModel()

world.observe({
    "observation": normal_case["observation"],
    "actual_result": normal_case["actual_result"],
})

world.observe({
    "observation": stressed_case["observation"],
    "actual_result": stressed_case["actual_result"],
})

knowledge = world.lookup({"signal": "A"})

print("RESULTS:", knowledge.results)
print("HISTORY_COUNT:", knowledge.history_count)

# 条件を区別できないため、X/Yは同一観測の結果として統合される。
assert knowledge.results == {"X", "Y"}
assert knowledge.conflict

print("CONDITION_DISTINCTION: LOST")
print("RESULTS_COLLAPSED_ACROSS_CONDITIONS: CONFIRMED")
print("GENERALIZATION_RISK: CANDIDATE")

# ただし、条件依存学習をΩAIが必須とする仕様はまだ未確定。
print("CONDITION_DEPENDENT_GENERALIZATION: UNCONFIRMED")
print("WORLD_MODEL_CHANGE: NOT_YET_JUSTIFIED")
print("NO DESIGN CHANGE")
