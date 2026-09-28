from world_model import WorldModel
from reasoner import Reasoner, Decision

print("=== CONDITION DECISION IMPACT AUDIT ===")

reasoner = Reasoner()

# 本来は条件によって判断を変えたい仮想ケース。
# 現在のWorldModelにはconditionを渡さない。
normal = WorldModel()
stressed = WorldModel()

normal.observe({
    "observation": {"signal": "A"},
    "actual_result": "X",
})

stressed.observe({
    "observation": {"signal": "A"},
    "actual_result": "X",
})

normal_k = normal.lookup({"signal": "A"})
stressed_k = stressed.lookup({"signal": "A"})

normal_d = reasoner.decide(normal_k)
stressed_d = reasoner.decide(stressed_k)

print("NORMAL_DECISION:", normal_d.decision.value)
print("STRESSED_DECISION:", stressed_d.decision.value)

# 現在の契約では同じKnowledgeなので同じDecisionになる。
assert normal_d.decision == stressed_d.decision

print("CURRENT_DECISION_DIFFERENCE: NOT_OBSERVED")
print("CONDITION_INFORMATION_LOST_BEFORE_REASONING: CONFIRMED")

# 重要：
# 「条件によって本来判断を変えるべき」という仕様自体は
# 現在のΩAI契約では未確定。
print("CONDITION_DEPENDENT_DECISION_REQUIREMENT: UNCONFIRMED")
print("CONDITION_WORLD_MODEL_CHANGE: NOT_YET_JUSTIFIED")
print("NO DESIGN CHANGE")
