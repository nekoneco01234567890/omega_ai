from world_model import WorldModel
from world_model import Knowledge

print("=== WORLD MODEL CONTEXT DECISION IMPACT AUDIT ===")


def current_model(context1, context2):
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

    return world.lookup(observation)


def separated_model(context1, context2):
    """
    Audit-only hypothetical representation.
    This is NOT a WorldModel implementation change.
    """
    entries = {
        context1: {"X"},
        context2: {"Y"},
    }

    return {
        context1: Knowledge(
            observation={"signal": "A"},
            results=set(entries[context1]),
            history_count=1,
        ),
        context2: Knowledge(
            observation={"signal": "A"},
            results=set(entries[context2]),
            history_count=1,
        ),
    }


cases = {
    "TIME": ("T1", "T2"),
    "CONDITION": ("NORMAL", "STRESSED"),
    "STATE": ("S1", "S2"),
    "SCOPE": ("LOCAL", "GLOBAL"),
    "SOURCE": ("SRC1", "SRC2"),
    "EVIDENCE": ("DIRECT", "REPORTED"),
}

for name, (context1, context2) in cases.items():
    current = current_model(context1, context2)
    separated = separated_model(context1, context2)

    current_decision = (
        "CONFLICT"
        if current.conflict
        else "PASS"
        if current.stable
        else "UNKNOWN"
    )

    separated_decisions = [
        (
            "PASS"
            if knowledge.stable
            else "CONFLICT"
            if knowledge.conflict
            else "UNKNOWN"
        )
        for knowledge in separated.values()
    ]

    decision_changes = (
        current_decision != "PASS"
        and separated_decisions == ["PASS", "PASS"]
    )

    print(f"{name}:")
    print("  CURRENT_DECISION:", current_decision)
    print("  SEPARATED_DECISIONS:", separated_decisions)
    print("  DECISION_IMPACT:", decision_changes)

print()
print("=== INTERPRETATION ===")
print("Current WorldModel collapses the contexts.")
print("The audit-only separated representation can preserve distinct stable results.")
print("This demonstrates a potential decision impact of context preservation.")
print("It does NOT identify which axis should be implemented.")
print("It does NOT prove that context separation is universally required.")
print("NO DESIGN CHANGE")
