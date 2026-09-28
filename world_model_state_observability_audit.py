print("=== WORLD MODEL STATE OBSERVABILITY AUDIT ===")

cases = [
    {
        "raw_observation": {
            "signal": "A",
            "pressure": 10,
        },
        "state": "NORMAL",
        "result": "X",
    },
    {
        "raw_observation": {
            "signal": "A",
            "pressure": 90,
        },
        "state": "STRESSED",
        "result": "Y",
    },
]

# stateを直接与えず、観測情報だけを比較する。
raw_a = cases[0]["raw_observation"]
raw_b = cases[1]["raw_observation"]

print("RAW_OBSERVATION_DIFFERENCE:", raw_a != raw_b)

assert raw_a != raw_b

# 現段階では「pressureからstateを導く規則」は未定義。
state_inference_rule_exists = False

print(
    "STATE_INFERENCE_RULE:",
    "PRESENT" if state_inference_rule_exists else "ABSENT"
)

print("STATE_OBSERVABILITY_FROM_RAW_DATA: POSSIBLE")
print("STATE_INFERENCE: NOT_IMPLEMENTED")
print("STATE_IS_NOT_YET_A_FACT: CONFIRMED")
print("STATE_AXIS_REQUIREMENT: UNCONFIRMED")
print("WORLD_MODEL_CHANGE: NOT_YET_JUSTIFIED")
print("NO DESIGN CHANGE")
