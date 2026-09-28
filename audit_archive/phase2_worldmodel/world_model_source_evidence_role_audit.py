from world_model import WorldModel

print("=== WORLD MODEL SOURCE / EVIDENCE ROLE AUDIT ===")


def run_case(context1, context2, result1, result2):
    world = WorldModel()
    observation = {"signal": "A"}

    world.observe({
        "observation": observation,
        "actual_result": result1,
        "context": context1,
    })

    world.observe({
        "observation": observation,
        "actual_result": result2,
        "context": context2,
    })

    knowledge = world.lookup(observation)

    return {
        "history_count": knowledge.history_count,
        "results": knowledge.results,
        "stable": knowledge.stable,
        "conflict": knowledge.conflict,
    }


cases = {
    "SOURCE_SAME_FACT": {
        "context1": "SRC1",
        "context2": "SRC2",
        "result1": "X",
        "result2": "X",
    },

    "EVIDENCE_SAME_FACT": {
        "context1": "DIRECT",
        "context2": "REPORTED",
        "result1": "X",
        "result2": "X",
    },

    "SOURCE_CONFLICT": {
        "context1": "SRC1",
        "context2": "SRC2",
        "result1": "X",
        "result2": "Y",
    },

    "EVIDENCE_CONFLICT": {
        "context1": "DIRECT",
        "context2": "REPORTED",
        "result1": "X",
        "result2": "Y",
    },
}


for name, case in cases.items():
    result = run_case(
        case["context1"],
        case["context2"],
        case["result1"],
        case["result2"],
    )

    print(f"{name}:")
    print("  CONTEXT_1:", case["context1"])
    print("  CONTEXT_2:", case["context2"])
    print("  RESULT_1:", case["result1"])
    print("  RESULT_2:", case["result2"])
    print("  HISTORY_COUNT:", result["history_count"])
    print("  RESULTS:", result["results"])
    print("  STABLE:", result["stable"])
    print("  CONFLICT:", result["conflict"])


print()
print("=== INTERPRETATION ===")
print("Same-result cases test whether SOURCE/EVIDENCE alone creates a world-state difference.")
print("Different-result cases test whether SOURCE/EVIDENCE can coincide with contradictory observations.")
print("The current WorldModel cannot distinguish either context because context is external to observation.")
print("Therefore this audit tests behavior, not a predetermined role assignment.")

print()
print("=== CONCLUSION ===")
print("SOURCE_IDENTITY_ROLE: UNRESOLVED")
print("EVIDENCE_IDENTITY_ROLE: UNRESOLVED")
print("PROVENANCE_SEPARATION: CANDIDATE")
print("EVIDENCE_LAYER_SEPARATION: CANDIDATE")
print("NO DESIGN CHANGE")
