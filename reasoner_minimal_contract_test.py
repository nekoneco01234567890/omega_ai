from reasoner import Reasoner, Decision
from world_model import WorldModel
from intelligence_core import IntelligenceCore


HYPOTHESES = [
    {"id": "H1", "prediction": "X"},
    {"id": "H2", "prediction": "Y"},
]


def exp(core, observation, actual):
    core.cycle(
        observation=observation,
        hypotheses=HYPOTHESES,
        actual_result=actual,
    )
    return core.experiences[-1]


core = IntelligenceCore()
world = WorldModel()
reasoner = Reasoner()

# UNKNOWN:
# 経験が存在しないKnowledgeだけで判断できるか
unknown = world.lookup({"signal": "UNKNOWN"})
result = reasoner.decide(unknown)
assert result.decision == Decision.UNKNOWN

# PASS:
# 単一結果だけで安定した知識として判断できるか
world.observe(exp(core, {"signal": "A"}, "X"))
world.observe(exp(core, {"signal": "A"}, "X"))

stable = world.lookup({"signal": "A"})
result = reasoner.decide(stable)
assert result.decision == Decision.PASS

# CONFLICT:
# 複数結果だけで矛盾として判断できるか
world.observe(exp(core, {"signal": "A"}, "Y"))

conflict = world.lookup({"signal": "A"})
result = reasoner.decide(conflict)
assert result.decision == Decision.CONFLICT

# HOLD:
# 現行Knowledgeの状態空間で、HOLDが必要なケースを確認
# v1 Knowledgeでは UNKNOWN / STABLE / CONFLICT に完全分類されるため、
# HOLDが自然に発生するケースが存在するかを明示確認する。
hold_candidates = []

for knowledge in [unknown, stable, conflict]:
    decision = reasoner.decide(knowledge).decision
    hold_candidates.append(decision)

assert Decision.HOLD not in hold_candidates

print("REASONER MINIMAL CONTRACT: PASS")
print("UNKNOWN / PASS / CONFLICT: PASS")
print("HOLD_CASE: NOT_REPRESENTED_BY_CURRENT_KNOWLEDGE")
print("FACTS_REQUIRED: NOT_CONFIRMED")
print("HYPOTHESES_REQUIRED: NOT_CONFIRMED")
print("NO DESIGN CHANGE")
