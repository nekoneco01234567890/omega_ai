from world_model import WorldModel

print("=== WORLD MODEL KNOWLEDGE SUFFICIENCY AUDIT ===")


def inspect_pair(name, obs1, obs2):
    world = WorldModel()

    world.observe({
        "observation": obs1,
        "actual_result": "X",
    })

    world.observe({
        "observation": obs2,
        "actual_result": "Y",
    })

    k1 = world.lookup(obs1)
    k2 = world.lookup(obs2)

    separated = (
        k1.history_count == 1
        and k2.history_count == 1
    )

    collapsed = (
        k1.history_count == 2
        and k2.history_count == 2
    )

    print(f"{name}:")
    print("  KNOWLEDGE_SEPARATED:", separated)
    print("  KNOWLEDGE_COLLAPSED:", collapsed)

    return {
        "separated": separated,
        "collapsed": collapsed,
    }


results = {}

results["TIME"] = inspect_pair(
    "TIME",
    {"signal": "A", "time": "T1"},
    {"signal": "A", "time": "T2"},
)

results["CONDITION"] = inspect_pair(
    "CONDITION",
    {"signal": "A", "condition": "NORMAL"},
    {"signal": "A", "condition": "STRESSED"},
)

results["STATE"] = inspect_pair(
    "STATE",
    {"signal": "A", "state": "S1"},
    {"signal": "A", "state": "S2"},
)

results["SCOPE"] = inspect_pair(
    "SCOPE",
    {"signal": "A", "scope": "LOCAL"},
    {"signal": "A", "scope": "GLOBAL"},
)

results["SOURCE"] = inspect_pair(
    "SOURCE",
    {"signal": "A", "source": "SRC1"},
    {"signal": "A", "source": "SRC2"},
)

results["EVIDENCE"] = inspect_pair(
    "EVIDENCE",
    {"signal": "A", "evidence": "DIRECT"},
    {"signal": "A", "evidence": "REPORTED"},
)

print()
print("=== SUMMARY ===")

for axis, result in results.items():
    if result["collapsed"]:
        status = "INFORMATION_COLLAPSE"
    elif result["separated"]:
        status = "REPRESENTABLE"
    else:
        status = "UNRESOLVED"

    print(f"{axis}: {status}")

print()
print("IMPORTANT:")
print("This audit measures representation loss only.")
print("It does NOT prove that any axis is required.")
print("NO DESIGN CHANGE")
