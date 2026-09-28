from world_model import WorldModel

print("=== WORLD MODEL CONTEXT COLLAPSE AUDIT ===")


def run_case(name, context1, context2):
    world = WorldModel()

    observation = {"signal": "A"}

    world.observe({
        "observation": observation,
        "actual_result": "X",
        "context": context1,
    })

    world.observe({
        "observation": observation,
        "actual_result": "Y",
        "context": context2,
    })

    knowledge = world.lookup(observation)

    print(f"{name}:")
    print("  CONTEXT_1:", context1)
    print("  CONTEXT_2:", context2)
    print("  HISTORY_COUNT:", knowledge.history_count)
    print("  RESULTS:", knowledge.results)

    return knowledge


cases = {
    "TIME": ("T1", "T2"),
    "CONDITION": ("NORMAL", "STRESSED"),
    "STATE": ("S1", "S2"),
    "SCOPE": ("LOCAL", "GLOBAL"),
    "SOURCE": ("SRC1", "SRC2"),
    "EVIDENCE": ("DIRECT", "REPORTED"),
}

results = {}

for name, pair in cases.items():
    results[name] = run_case(name, pair[0], pair[1])


print()
print("=== SUMMARY ===")

for name, knowledge in results.items():
    if knowledge.history_count == 2:
        print(f"{name}: CONTEXT_COLLAPSED")
    else:
        print(f"{name}: NOT_COLLAPSED")

print()
print("INTERPRETATION:")
print("The current WorldModel keys only on observation.")
print("External context is not part of the current Knowledge identity.")
print("This confirms information collapse at the current interface.")
print("It does NOT prove that every context axis must be implemented.")
print("NO DESIGN CHANGE")
