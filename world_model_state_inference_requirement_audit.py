print("=== STATE INFERENCE REQUIREMENT AUDIT ===")

cases = [
    {
        "observation": {
            "signal": "A",
            "pressure": 10,
        },
        "result": "X",
    },
    {
        "observation": {
            "signal": "A",
            "pressure": 90,
        },
        "result": "Y",
    },
]

# 現在のObservationそのものには差が存在する。
assert cases[0]["observation"] != cases[1]["observation"]

# しかし現在のWorldModelはObservation全体をキーにできる。
from world_model import WorldModel

world = WorldModel()

world.observe({
    "observation": cases[0]["observation"],
    "actual_result": cases[0]["result"],
})

world.observe({
    "observation": cases[1]["observation"],
    "actual_result": cases[1]["result"],
})

k1 = world.lookup(cases[0]["observation"])
k2 = world.lookup(cases[1]["observation"])

print("OBSERVATION_LEVEL_SEPARATION:",
      k1.observation != k2.observation)

assert k1.observation != k2.observation

print("STATE_INFERENCE_REQUIRED_FOR_CURRENT_SEPARATION: NO")

# 重要：
# 状態を導入しなくても、Observationそのものが異なれば
# 現行WorldModelは既に別Knowledgeとして保持できる。
print("CURRENT_MODEL_CAN_PRESERVE_RAW_DISTINCTION: CONFIRMED")
print("STATE_LAYER_ADDS_INFORMATION: NOT_YET_PROVEN")
print("STATE_INFERENCE_REQUIREMENT: UNCONFIRMED")
print("WORLD_MODEL_CHANGE: NOT_YET_JUSTIFIED")
print("NO DESIGN CHANGE")
