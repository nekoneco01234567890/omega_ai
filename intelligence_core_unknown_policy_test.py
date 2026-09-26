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


def main():
    print("=== UNKNOWN POLICY TEST ===")

    # K1: 完全未知
    core = IntelligenceCore()
    r1 = cycle(core, "A", "X")
    print("K1_UNKNOWN:", r1["prediction"], r1["conflict"])

    # K2: 安定経験
    core = IntelligenceCore()
    cycle(core, "A", "X")
    r2 = cycle(core, "A", "X")
    print("K2_STABLE:", r2["prediction"], r2["conflict"])

    # K3: 矛盾経験
    core = IntelligenceCore()
    cycle(core, "A", "X")
    cycle(core, "A", "Y")
    r3 = cycle(core, "A", "X")
    print("K3_CONFLICT:", r3["prediction"], r3["conflict"])

    print("=== UNKNOWN POLICY TEST COMPLETE ===")
    print("NO UNKNOWN POLICY SELECTED")


if __name__ == "__main__":
    main()
