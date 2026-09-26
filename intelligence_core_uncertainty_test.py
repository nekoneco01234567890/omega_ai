from intelligence_core import IntelligenceCore


HYPOTHESES = [
    {"id": "H1", "prediction": "X"},
    {"id": "H2", "prediction": "Y"},
]


def cycle(core, signal, result):
    return core.cycle(
        observation={"signal": signal},
        hypotheses=HYPOTHESES,
        actual_result=result,
    )


def show(name, result):
    print(name)
    print("  prediction:", result["prediction"])
    print("  actual:", result["actual_result"])
    print("  used_experience:", result["used_experience"])
    print("  conflict:", result["conflict"])
    print("  status:", result["status"])


def main():

    print("=== INTELLIGENCE CORE UNCERTAINTY TEST ===")

    # U1: 完全未知
    core = IntelligenceCore()

    r = cycle(core, "UNKNOWN_A", "X")
    show("U1_UNKNOWN", r)

    # U2: 安定した既知
    core = IntelligenceCore()

    cycle(core, "A", "X")
    r = cycle(core, "A", "X")
    show("U2_KNOWN_STABLE", r)

    # U3: 明確な矛盾
    core = IntelligenceCore()

    cycle(core, "A", "X")
    r = cycle(core, "A", "Y")
    show("U3_CONFLICT", r)

    # U4: 同じ観測で結果が交互に変わる
    core = IntelligenceCore()

    cycle(core, "A", "X")
    cycle(core, "A", "Y")
    cycle(core, "A", "X")
    r = cycle(core, "A", "Y")
    show("U4_OSCILLATION", r)

    # U5: 未知だが、過去経験から完全には決められないケース
    core = IntelligenceCore()

    cycle(core, "A", "X")
    cycle(core, "B", "Y")

    r = cycle(core, "C", "X")
    show("U5_UNSEEN_WITH_HISTORY", r)

    print()
    print("=== UNCERTAINTY TEST COMPLETE ===")
    print("NO DESIGN CHANGE")
    print("NO UNKNOWN POLICY SELECTED")


if __name__ == "__main__":
    main()
