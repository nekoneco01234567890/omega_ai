from reasoner import Reasoner, Decision
from world_model import Knowledge


print("=== REASONER RESPONSIBILITY AUDIT ===")

reasoner = Reasoner()

# 現在のWorldModelから直接導ける基本状態
cases = {
    "UNKNOWN": Knowledge(
        observation={"signal": "U"},
    ),
    "PASS": Knowledge(
        observation={"signal": "P"},
        results={"X"},
        history_count=1,
    ),
    "CONFLICT": Knowledge(
        observation={"signal": "C"},
        results={"X", "Y"},
        history_count=2,
    ),
}

for expected, knowledge in cases.items():
    result = reasoner.decide(knowledge)
    print(
        expected,
        "=>",
        result.decision.value,
        "|",
        result.reason,
    )
    assert result.decision.value == expected


# 現行Reasonerの責務を確認
required_decisions = {
    Decision.UNKNOWN,
    Decision.PASS,
    Decision.CONFLICT,
}

implemented_decisions = {
    reasoner.decide(k).decision
    for k in cases.values()
}

print()
print("REQUIRED_BY_CURRENT_KNOWLEDGE:",
      sorted(d.value for d in required_decisions))

print("IMPLEMENTED_BY_CURRENT_KNOWLEDGE:",
      sorted(d.value for d in implemented_decisions))

print(
    "BASIC_DECISION_COVERAGE:",
    required_decisions == implemented_decisions,
)

# HOLDについては、まだ正式要件として追加しない
print()
print("HOLD:")
print("  CURRENT_KNOWLEDGE_SUPPORT: NO")
print("  FORMAL_REQUIREMENT: UNCONFIRMED")
print("  IMPLEMENTATION: NOT_REQUIRED_YET")

print()
print("CONCLUSION:")
print("REASONER_CORE_CONTRACT: UNKNOWN / PASS / CONFLICT")
print("HOLD: OPEN_REQUIREMENT")
print("WORLD_MODEL_CHANGE: NO")
print("NO DESIGN CHANGE")
