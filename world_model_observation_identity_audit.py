from world_model import WorldModel

print("=== WORLD MODEL OBSERVATION IDENTITY AUDIT ===")

cases = [
    {
        "observation": {"signal": "A", "pressure": 10},
        "result": "X",
    },
    {
        "observation": {"signal": "A", "pressure": 11},
        "result": "X",
    },
    {
        "observation": {"signal": "A", "pressure": 90},
        "result": "Y",
    },
]

world = WorldModel()

for case in cases:
    world.observe({
        "observation": case["observation"],
        "actual_result": case["result"],
    })

k10 = world.lookup({"signal": "A", "pressure": 10})
k11 = world.lookup({"signal": "A", "pressure": 11})
k90 = world.lookup({"signal": "A", "pressure": 90})

print("10_HISTORY:", k10.history_count)
print("11_HISTORY:", k11.history_count)
print("90_HISTORY:", k90.history_count)

print("OBSERVATION_KEYS_DISTINCT:",
      len({
          repr(k10.observation),
          repr(k11.observation),
          repr(k90.observation),
      }))

assert k10.history_count == 1
assert k11.history_count == 1
assert k90.history_count == 1

print("RAW_IDENTITY_RULE: EXACT_OBSERVATION_MATCH")
print("SEMANTIC_SIMILARITY: NOT_REPRESENTED")
print("GENERALIZATION_FROM_SIMILAR_OBSERVATIONS: NOT_REPRESENTED")
print("OBSERVATION_IDENTITY_LIMIT: CONFIRMED")
print("WORLD_MODEL_CHANGE: NOT_YET_JUSTIFIED")
print("NO DESIGN CHANGE")
