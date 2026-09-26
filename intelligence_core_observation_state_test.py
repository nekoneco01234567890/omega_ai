from intelligence_core import IntelligenceCore


HYPOTHESES = [
    {"id": "H1", "prediction": "X"},
    {"id": "H2", "prediction": "Y"},
]


def run_case(name, history, current):
    core = IntelligenceCore()

    for observation, result in history:
        core.cycle(
            observation=observation,
            hypotheses=HYPOTHESES,
            actual_result=result,
        )

    result = core.cycle(
        observation=current,
        hypotheses=HYPOTHESES,
        actual_result=current.get("_actual"),
    )

    print(name)
    print("  observation:", current)
    print("  prediction:", result["prediction"])
    print("  used_experience:", result["used_experience"])
    print("  conflict:", result["conflict"])
    print("  status:", result["status"])
    print()


def main():
    print("=== OBSERVATION / STATE SEPARATION TEST ===")

    # A: 完全同一観測
    run_case(
        "A_SAME_OBSERVATION",
        [({"signal": "A"}, "X")],
        {"signal": "A", "_actual": "X"},
    )

    # B: 時間だけ違う
    run_case(
        "B_TIME_ONLY",
        [({"signal": "A", "time": 1}, "X")],
        {"signal": "A", "time": 2, "_actual": "Y"},
    )

    # C: 状態だけ違う
    run_case(
        "C_STATE_ONLY",
        [({"signal": "A", "state": "old"}, "X")],
        {"signal": "A", "state": "new", "_actual": "Y"},
    )

    # D: 文脈だけ違う
    run_case(
        "D_CONTEXT_ONLY",
        [({"signal": "A", "context": "C1"}, "X")],
        {"signal": "A", "context": "C2", "_actual": "Y"},
    )

    # E: signalそのものが違う
    run_case(
        "E_DIFFERENT_OBSERVATION",
        [({"signal": "A"}, "X")],
        {"signal": "B", "_actual": "Y"},
    )

    print("=== TEST COMPLETE ===")
    print("NO DESIGN CHANGE")


if __name__ == "__main__":
    main()
