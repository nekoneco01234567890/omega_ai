from world_model import WorldModel

print("=== WORLD MODEL AXIS SEMANTIC ROLE AUDIT ===")

AXES = {
    "TIME": ("T1", "T2"),
    "CONDITION": ("NORMAL", "STRESSED"),
    "STATE": ("S1", "S2"),
    "SCOPE": ("LOCAL", "GLOBAL"),
    "SOURCE": ("SRC1", "SRC2"),
    "EVIDENCE": ("DIRECT", "REPORTED"),
}


def same_result_collapse(axis):
    world = WorldModel()
    observation = {"signal": "A"}
    a, b = AXES[axis]

    world.observe({
        "observation": observation,
        "actual_result": "X",
        "context": a,
    })

    world.observe({
        "observation": observation,
        "actual_result": "X",
        "context": b,
    })

    knowledge = world.lookup(observation)

    return {
        "history_count": knowledge.history_count,
        "results": knowledge.results,
        "stable": knowledge.stable,
        "conflict": knowledge.conflict,
    }


def hypothetical_context_decision(axis):
    """
    Audit-only.
    Ask whether the axis itself can define a different
    applicability/decision context even when the observed
    result is identical.
    """
    a, b = AXES[axis]

    return {
        a: {
            "result": "X",
            "applicable": True,
        },
        b: {
            "result": "X",
            "applicable": False,
        },
    }


for axis in AXES:
    current = same_result_collapse(axis)
    hypothetical = hypothetical_context_decision(axis)

    print(f"{axis}:")
    print("  SAME_RESULT_COLLAPSE:", current)
    print(
        "  CONTEXT_CAN_AFFECT_APPLICABILITY:",
        hypothetical[AXES[axis][0]]["applicable"]
        != hypothetical[AXES[axis][1]]["applicable"],
    )

print()
print("=== ROLE CLASSIFICATION STATUS ===")
print("TIME: NEEDS TEMPORAL SEMANTICS AUDIT")
print("CONDITION: NEEDS CONDITION-DEPENDENT DECISION AUDIT")
print("STATE: NEEDS STATE-DEPENDENT DECISION AUDIT")
print("SCOPE: NEEDS APPLICABILITY-SCOPE AUDIT")
print("SOURCE: NEEDS PROVENANCE INDEPENDENCE AUDIT")
print("EVIDENCE: NEEDS EVIDENCE-QUALITY AUDIT")

print()
print("=== CONCLUSION ===")
print("CURRENT COLLAPSE: CONFIRMED")
print("SEMANTIC ROLE: NOT_YET_DETERMINED")
print("NO DESIGN CHANGE")
