from world_model import Knowledge


print("=== REASONER HOLD TIME AUDIT ===")


def classify(k):
    if k.unknown:
        return "UNKNOWN"
    if k.conflict:
        return "CONFLICT"
    if k.stable:
        return "PASS"
    return "HOLD"


# 時間情報を持たない現在のKnowledge
past = Knowledge(
    observation={"signal": "A"},
    results={"X"},
    history_count=1,
)

recent = Knowledge(
    observation={"signal": "A"},
    results={"X"},
    history_count=1,
)

# 「過去」と「現在」という意味を外部的に与えても、
# Knowledge内部には時間情報がない。
past_decision = classify(past)
recent_decision = classify(recent)

print("PAST:", past_decision)
print("RECENT:", recent_decision)

# 構造が同一なら現モデルは同じ判断しか返せない
assert past_decision == recent_decision

# つまり時間だけを変数にした判断分離は現在できない
print("TIME_ONLY_DISTINCTION: NOT_REPRESENTABLE")

# ただし、時間がReasonerに必要だとはまだ断定しない
print("TIME_REQUIRED_FOR_REASONING: UNCONFIRMED")
print("WORLD_MODEL_CHANGE: NOT_YET_JUSTIFIED")
print("NO DESIGN CHANGE")
