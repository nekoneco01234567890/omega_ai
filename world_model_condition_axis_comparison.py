print("=== WORLD MODEL AXIS COMPARISON ===")

cases = [
    {
        "observation": {"signal": "A"},
        "condition": "NORMAL",
        "state": "NORMAL",
        "context": "NORMAL",
        "result": "X",
    },
    {
        "observation": {"signal": "A"},
        "condition": "STRESSED",
        "state": "STRESSED",
        "context": "STRESSED",
        "result": "Y",
    },
]

axes = {
    "condition": lambda x: x["condition"],
    "state": lambda x: x["state"],
    "context": lambda x: x["context"],
}

for name, getter in axes.items():
    keys = {
        (
            repr(case["observation"]),
            getter(case),
        )
        for case in cases
    }

    separated = len(keys) == len(cases)

    print(f"{name.upper()}_SEPARATION:", separated)

    assert separated

print("ALL_CANDIDATE_AXES_CAN_SEPARATE: PASS")
print("BEST_AXIS: UNDETERMINED")
print("AXIS_SELECTION: NOT_YET_JUSTIFIED")
print("WORLD_MODEL_CHANGE: NOT_YET_JUSTIFIED")
print("NO DESIGN CHANGE")
