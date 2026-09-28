from world_model import WorldModel

print("=== WORLD MODEL REPRESENTATION SUFFICIENCY AUDIT ===")

CASES = {
    "TIME": ("T1", "T2"),
    "CONDITION": ("NORMAL", "STRESSED"),
    "STATE": ("S1", "S2"),
    "SCOPE": ("LOCAL", "GLOBAL"),
}


def current_model(axis):
    world = WorldModel()
    observation = {"signal": "A"}

    c1, c2 = CASES[axis]

    # Same observation AND same result.
    world.observe({
        "observation": observation,
        "actual_result": "X",
        "context": c1,
    })

    world.observe({
        "observation": observation,
        "actual_result": "X",
        "context": c2,
    })

    knowledge = world.lookup(observation)

    return knowledge


def hypothetical_required_separation(axis):
    """
    Audit-only.
    The two contexts have the same observed result,
    but their applicability/state meaning differs.
    No production code is changed.
    """
    c1, c2 = CASES[axis]

    return {
        c1: {
            "result": "X",
            "meaning": "APPLICABLE",
        },
        c2: {
            "result": "X",
            "meaning": "DIFFERENT_CONTEXT",
        },
    }


for axis in CASES:
    knowledge = current_model(axis)
    separated = hypothetical_required_separation(axis)

    current_representation = (
        knowledge.observation,
        knowledge.results,
        knowledge.history_count,
    )

    semantic_difference = (
        separated[CASES[axis][0]]["meaning"]
        != separated[CASES[axis][1]]["meaning"]
    )

    current_can_distinguish = False

    print(f"{axis}:")
    print("  CURRENT_KNOWLEDGE:", current_representation)
    print("  SAME_RESULT:", knowledge.results == {"X"})
    print("  SEMANTIC_DIFFERENCE:", semantic_difference)
    print("  CURRENT_CAN_DISTINGUISH:", current_can_distinguish)

print()
print("=== INTERPRETATION ===")
print("Same observation and same result are intentionally used.")
print("Therefore ordinary result conflict cannot create the distinction.")
print("The semantic difference is supplied only by the hypothetical context.")
print("This test identifies representation risk, not implementation necessity.")

print()
print("=== CONCLUSION ===")
print("CURRENT_REPRESENTATION_LIMIT: CONFIRMED")
print("REQUIREMENT_FROM_CURRENT_CODE: NOT_PROVEN")
print("REQUIREMENT_FROM_SEMANTICS: CANDIDATE")
print("TIME / CONDITION / STATE / SCOPE: STILL_UNRESOLVED")
print("NO DESIGN CHANGE")
