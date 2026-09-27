from world_model import Knowledge


print("=== HOLD COUNTEREXAMPLE AUDIT ===")


def classify(k):
    if k.unknown:
        return "UNKNOWN"
    if k.conflict:
        return "CONFLICT"
    if k.stable:
        return "PASS"
    return "HOLD"


cases = [
    (
        "A: 同じ結果だが経験1回",
        Knowledge(
            observation={"signal": "A"},
            results={"X"},
            history_count=1,
        ),
    ),
    (
        "B: 同じ結果を多数観測",
        Knowledge(
            observation={"signal": "B"},
            results={"X"},
            history_count=10,
        ),
    ),
    (
        "C: 同じ結果だが別条件の可能性",
        Knowledge(
            observation={"signal": "C"},
            results={"X"},
            history_count=2,
        ),
    ),
    (
        "D: 過去はX、現在条件が変化",
        Knowledge(
            observation={"signal": "D"},
            results={"X"},
            history_count=5,
        ),
    ),
    (
        "E: X/Yの両方を観測",
        Knowledge(
            observation={"signal": "E"},
            results={"X", "Y"},
            history_count=2,
        ),
    ),
]


for name, knowledge in cases:
    print(name, "=>", classify(knowledge))


# 現行Knowledgeで区別できる情報量を確認
same_structure_a = Knowledge(
    observation={"signal": "S"},
    results={"X"},
    history_count=1,
)

same_structure_b = Knowledge(
    observation={"signal": "S"},
    results={"X"},
    history_count=1,
)

assert classify(same_structure_a) == classify(same_structure_b)

# ここでは「HOLDが必要」とは断定しない。
# 現行モデルから導ける状態だけを確認する。
assert classify(same_structure_a) == "PASS"

print()
print("CURRENT_MODEL_STATES: UNKNOWN / PASS / CONFLICT")
print("HOLD: NOT_DERIVABLE_FROM_CURRENT_FIELDS")
print("HOLD_REQUIREMENT: UNCONFIRMED")
print("NO DESIGN CHANGE")
