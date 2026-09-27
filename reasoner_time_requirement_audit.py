print("=== REASONER TIME REQUIREMENT AUDIT ===")


cases = [
    {
        "name": "PAST_X_CURRENT_X",
        "past": "X",
        "current": "X",
        "required_decision": "PASS",
    },
    {
        "name": "PAST_X_CURRENT_UNKNOWN",
        "past": "X",
        "current": None,
        "required_decision": "UNKNOWN",
    },
    {
        "name": "PAST_X_CURRENT_CONFLICT",
        "past": "X",
        "current": "Y",
        "required_decision": "CONFLICT",
    },
]


for case in cases:
    print(
        case["name"],
        "past=", case["past"],
        "current=", case["current"],
        "required=", case["required_decision"],
    )


# 重要:
# 上記は「時間を考慮した場合にあり得る判断仕様」の候補であり、
# 現行ΩAIの正式な仕様としてはまだ確定していない。
#
# 時間を追加する根拠にするには、
# 「同じ観測結果でも時間によって判断を変える」
# という明示的な目的・契約が必要。

distinct_required = any(
    case["required_decision"] != "PASS"
    for case in cases
)

print()
print("TIME_CAN_CHANGE_REQUIRED_DECISION:", distinct_required)
print("TIME_REQUIREMENT_STATUS: CANDIDATE_ONLY")
print("SPECIFICATION_CONFIRMED: NO")
print("WORLD_MODEL_CHANGE: NO")
print("NO DESIGN CHANGE")
