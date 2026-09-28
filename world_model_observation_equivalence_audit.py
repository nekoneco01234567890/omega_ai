from world_model import WorldModel

print("=== WORLD MODEL OBSERVATION EQUIVALENCE AUDIT ===")

cases = [
    {
        "observation": {"signal": "A", "pressure": 10},
        "result": "X",
    },
    {
        "observation": {"pressure": 10, "signal": "A"},
        "result": "X",
    },
]

world = WorldModel()

for case in cases:
    world.observe({
        "observation": case["observation"],
        "actual_result": case["result"],
    })

k1 = world.lookup(cases[0]["observation"])
k2 = world.lookup(cases[1]["observation"])

print("OBSERVATION_1:", k1.observation)
print("OBSERVATION_2:", k2.observation)
print("HISTORY_1:", k1.history_count)
print("HISTORY_2:", k2.history_count)

print(
    "PYTHON_EQUALITY:",
    cases[0]["observation"] == cases[1]["observation"]
)

print(
    "WORLD_MODEL_SAME_KNOWLEDGE:",
    k1.history_count == 2
)

print("IDENTITY_MECHANISM: canonical_key(observation)")
print("EQUIVALENCE_POLICY: DICT_KEYS_ORDER_INSENSITIVE")
print("SEMANTIC_EQUIVALENCE: NOT_REPRESENTED")
print("WORLD_MODEL_CHANGE: NOT_YET_JUSTIFIED")
print("NO DESIGN CHANGE")
