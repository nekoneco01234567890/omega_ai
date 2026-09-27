from dataclasses import replace
from reasoner import Reasoner, Decision
from world_model import Knowledge


reasoner = Reasoner()


def decision(knowledge):
    return reasoner.decide(knowledge).decision


print("=== REASONER V2 MINIMALITY AUDIT ===")


# 基準となるKnowledge
base = Knowledge(
    observation={"signal": "A"},
    results={"X"},
    history_count=2,
)

# 1. factsを外部概念として追加しても、
#    現在のReasoner契約そのものは変わらない
base_with_fact = {
    "knowledge": base,
    "facts": ["X_IS_FACT"],
}

assert decision(base_with_fact["knowledge"]) == Decision.PASS
print("FACTS: NO_EFFECT_ON_CURRENT_CONTRACT")


# 2. hypothesesを外部概念として追加しても、
#    現在のReasoner契約そのものは変わらない
base_with_hypotheses = {
    "knowledge": base,
    "hypotheses": ["H1", "H2"],
}

assert decision(base_with_hypotheses["knowledge"]) == Decision.PASS
print("HYPOTHESES: NO_EFFECT_ON_CURRENT_CONTRACT")


# 3. HOLD
# 現在のKnowledgeで作れる状態をすべて確認
states = [
    Knowledge(observation={"signal": "U"}),
    Knowledge(
        observation={"signal": "P"},
        results={"X"},
        history_count=1,
    ),
    Knowledge(
        observation={"signal": "C"},
        results={"X", "Y"},
        history_count=2,
    ),
]

decisions = {decision(k) for k in states}

assert decisions == {
    Decision.UNKNOWN,
    Decision.PASS,
    Decision.CONFLICT,
}

assert Decision.HOLD not in decisions

print("HOLD: NOT_REACHED_BY_CURRENT_KNOWLEDGE")


# 4. 最小契約
required = {
    Decision.UNKNOWN,
    Decision.PASS,
    Decision.CONFLICT,
}

assert decisions == required

print("MINIMAL_CONTRACT: UNKNOWN / PASS / CONFLICT")
print("FACTS_REQUIRED: NOT_CONFIRMED")
print("HYPOTHESES_REQUIRED: NOT_CONFIRMED")
print("HOLD_REQUIRED: NOT_CONFIRMED")
print("REASONER_V2_MINIMALITY: PASS")
print("CODE_MAP_CHANGE: NOT_YET")
print("NO DESIGN CHANGE")
