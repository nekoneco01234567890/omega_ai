print("=== CONDITION MINIMAL REPRESENTATION TEST ===")

# 現在失われている情報を最小限だけ追加した仮想表現。
normal = {
    "observation": {"signal": "A"},
    "condition": "NORMAL",
    "result": "X",
}

stressed = {
    "observation": {"signal": "A"},
    "condition": "STRESSED",
    "result": "Y",
}

# conditionを識別軸として使えば、
# 現在混ざっている2ケースを分離できる。
normal_key = (
    repr(normal["observation"]),
    normal["condition"],
)

stressed_key = (
    repr(stressed["observation"]),
    stressed["condition"],
)

assert normal_key != stressed_key

print("NORMAL_KEY:", normal_key)
print("STRESSED_KEY:", stressed_key)
print("CONDITION_SEPARATION: POSSIBLE")
print("MINIMAL_ADDITIONAL_AXIS: condition")
print("WORLD_MODEL_CHANGE: NOT_YET_JUSTIFIED")
print("NO DESIGN CHANGE")
