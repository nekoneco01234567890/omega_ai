print("=== WORLD MODEL STATE DISCRIMINATION AUDIT ===")

cases = [
    {
        "observation": {"signal": "A"},
        "latent_state": "NORMAL",
        "result": "X",
    },
    {
        "observation": {"signal": "A"},
        "latent_state": "STRESSED",
        "result": "Y",
    },
]

# 状態を無視した表現
collapsed = {}

for case in cases:
    key = repr(case["observation"])
    collapsed.setdefault(key, set()).add(case["result"])

# 状態を識別する表現
separated = {}

for case in cases:
    key = (
        repr(case["observation"]),
        case["latent_state"],
    )
    separated.setdefault(key, set()).add(case["result"])

print("COLLAPSED:", collapsed)
print("SEPARATED:", separated)

# 状態を無視すると X/Y が混ざる。
assert collapsed[repr({"signal": "A"})] == {"X", "Y"}

# 状態を識別すると結果が分離される。
assert len(separated) == 2
assert separated[
    (repr({"signal": "A"}), "NORMAL")
] == {"X"}
assert separated[
    (repr({"signal": "A"}), "STRESSED")
] == {"Y"}

print("STATE_INFORMATION_LOSS: CONFIRMED")
print("STATE_DISCRIMINATION: POSSIBLE")
print("REPRESENTATION_GAIN: CONFIRMED")
print("STATE_AXIS_REQUIREMENT: CANDIDATE")
print("FORMAL_WORLD_MODEL_CHANGE: NOT_YET_JUSTIFIED")
print("NO DESIGN CHANGE")
