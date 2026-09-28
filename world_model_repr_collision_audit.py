from world_model import WorldModel

print("=== WORLD MODEL CANONICAL KEY REGRESSION AUDIT ===")


def history_count(obs1, obs2):
    world = WorldModel()

    world.observe({
        "observation": obs1,
        "actual_result": "X",
    })

    world.observe({
        "observation": obs2,
        "actual_result": "X",
    })

    return (
        world.lookup(obs1).history_count,
        world.lookup(obs2).history_count,
    )


# 1. 辞書キー順だけ違う → 同一
case1 = history_count(
    {"signal": "A", "pressure": 10},
    {"pressure": 10, "signal": "A"},
)

# 2. ネスト辞書のキー順だけ違う → 同一
case2 = history_count(
    {"signal": {"a": 1, "b": 2}},
    {"signal": {"b": 2, "a": 1}},
)

# 3. リスト順が違う → 別
case3 = history_count(
    {"signal": ["A", "B"]},
    {"signal": ["B", "A"]},
)

print("CASE1_DICT_ORDER:", case1)
print("CASE2_NESTED_DICT_ORDER:", case2)
print("CASE3_LIST_ORDER:", case3)

assert case1 == (2, 2)
assert case2 == (2, 2)
assert case3 == (1, 1)

print("DICT_KEY_ORDER_NORMALIZATION: PASS")
print("NESTED_DICT_KEY_ORDER_NORMALIZATION: PASS")
print("LIST_ORDER_PRESERVED: PASS")
print("CANONICAL_KEY_REGRESSION: PASS")
