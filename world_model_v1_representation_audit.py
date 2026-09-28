from world_model import WorldModel, Knowledge

print("=== WORLDMODEL V1 REPRESENTATION AUDIT ===")

world = WorldModel()

# 1. UNKNOWN
unknown = world.lookup({"signal": "A"})

assert isinstance(unknown, Knowledge)
assert unknown.unknown
assert not unknown.stable
assert not unknown.conflict

print("UNKNOWN: REPRESENTABLE")

# 2. STABLE
world.observe({
    "observation": {"signal": "B"},
    "actual_result": "X",
})

stable = world.lookup({"signal": "B"})

assert stable.stable
assert not stable.conflict
assert not stable.unknown
assert stable.results == {"X"}
assert stable.history_count == 1

print("STABLE: REPRESENTABLE")

# 3. Repeated same result
world.observe({
    "observation": {"signal": "B"},
    "actual_result": "X",
})

stable_repeat = world.lookup({"signal": "B"})

assert stable_repeat.stable
assert stable_repeat.results == {"X"}
assert stable_repeat.history_count == 2

print("REPEATED STABLE: REPRESENTABLE")

# 4. CONFLICT
world.observe({
    "observation": {"signal": "B"},
    "actual_result": "Y",
})

conflict = world.lookup({"signal": "B"})

assert conflict.conflict
assert conflict.results == {"X", "Y"}
assert conflict.history_count == 3

print("CONFLICT: REPRESENTABLE")

# 5. Observation isolation
other = world.lookup({"signal": "C"})

assert other.unknown
assert other.results == set()
assert other.history_count == 0

print("OBSERVATION ISOLATION: PASS")

# 6. Current representation fields
fields = [
    "observation",
    "results",
    "history_count",
]

for field in fields:
    assert hasattr(conflict, field)

print("CORE_FIELDS: PASS")

# 7. Candidate missing axes
missing_axes = {
    "time": not hasattr(conflict, "time"),
    "condition": not hasattr(conflict, "condition"),
    "scope": not hasattr(conflict, "scope"),
    "evidence_quality": not hasattr(conflict, "evidence_quality"),
    "source": not hasattr(conflict, "source"),
    "dependence": not hasattr(conflict, "dependence"),
    "confidence": not hasattr(conflict, "confidence"),
}

print("MISSING_AXES:")
for name, missing in missing_axes.items():
    print(f"  {name}: {missing}")

print("=== CONCLUSION ===")
print("UNKNOWN / STABLE / CONFLICT: REPRESENTABLE")
print("OBSERVATION ISOLATION: PASS")
print("CURRENT_CORE_FIELDS: PASS")
print("MISSING_AXES: CANDIDATES_ONLY")
print("WORLD_MODEL_CHANGE: NOT_YET_JUSTIFIED")
print("NO DESIGN CHANGE")
