from world_model import WorldModel

print("=== WORLD MODEL AXIS ROLE AUDIT ===")

AXES = {
    "TIME": ("T1", "T2"),
    "CONDITION": ("NORMAL", "STRESSED"),
    "STATE": ("S1", "S2"),
    "SCOPE": ("LOCAL", "GLOBAL"),
    "SOURCE": ("SRC1", "SRC2"),
    "EVIDENCE": ("DIRECT", "REPORTED"),
}


def current_collapse(axis):
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
        "actual_result": "Y",
        "context": b,
    })

    return world.lookup(observation).conflict


def identity_candidate(axis):
    """
    Audit-only representation:
    axis is treated as part of Knowledge identity.
    """
    a, b = AXES[axis]

    return {
        a: {"X"},
        b: {"Y"},
    }


def attribute_candidate(axis):
    """
    Audit-only representation:
    one Knowledge identity, axis retained as metadata.
    """
    a, b = AXES[axis]

    return {
        "results": {"X", "Y"},
        "contexts": {a, b},
    }


for axis in AXES:
    collapsed = current_collapse(axis)
    identity = identity_candidate(axis)
    attribute = attribute_candidate(axis)

    identity_separates = (
        len(identity) == 2
        and all(len(v) == 1 for v in identity.values())
    )

    attribute_preserves_axis = (
        len(attribute["contexts"]) == 2
    )

    print(f"{axis}:")
    print("  CURRENT_COLLAPSE:", collapsed)
    print("  IDENTITY_SEPARATION_POSSIBLE:", identity_separates)
    print("  ATTRIBUTE_PRESERVATION_POSSIBLE:", attribute_preserves_axis)

print()
print("=== ROLE HYPOTHESES ===")
print("TIME: identity / history candidate")
print("CONDITION: identity / state-context candidate")
print("STATE: identity / world-state candidate")
print("SCOPE: applicability candidate")
print("SOURCE: provenance candidate")
print("EVIDENCE: evidence-quality candidate")

print()
print("=== CONCLUSION ===")
print("CURRENT_COLLAPSE: CONFIRMED")
print("ROLE_ASSIGNMENT: NOT_YET_PROVEN")
print("IDENTITY_VS_ATTRIBUTE: UNRESOLVED")
print("NO DESIGN CHANGE")
