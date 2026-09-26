from intelligence_core import IntelligenceCore


HYPOTHESES = [
    {"id": "H1", "prediction": "X"},
    {"id": "H2", "prediction": "Y"},
]


def cycle(core, observation, result):
    return core.cycle(
        observation=observation,
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
    print("=== STATE SEPARATION TEST ===")

    # S1: 完全未知
    core = IntelligenceCore()
    r1 = cycle(core, {"signal": "A"}, "X")
    show("S1_UNKNOWN", r1)

    # S2: 同一条件で安定
    core = IntelligenceCore()
    cycle(core, {"signal": "A"}, "X")
    r2 = cycle(core, {"signal": "A"}, "X")
    show("S2_STABLE", r2)

    # S3: 明示的な結果衝突
    core = IntelligenceCore()
    cycle(core, {"signal": "A"}, "X")
    r3 = cycle(core, {"signal": "A"}, "Y")
    show("S3_CONFLICT", r3)

    # S4: 条件が変化した可能性
    core = IntelligenceCore()
    cycle(core, {"signal": "A", "time": 1}, "X")
    r4 = cycle(core, {"signal": "A", "time": 2}, "Y")
    show("S4_TIME_CHANGE", r4)

    # S5: 同じ結果だが情報量が不足
    core = IntelligenceCore()
    cycle(core, {"signal": "A"}, "X")
    r5 = cycle(core, {"signal": "A", "extra": "UNKNOWN"}, "X")
    show("S5_INSUFFICIENT_CONTEXT", r5)

    # S6: 過去経験が現在状態に適用できない可能性
    core = IntelligenceCore()
    cycle(core, {"signal": "A", "state": "old"}, "X")
    r6 = cycle(core, {"signal": "A", "state": "new"}, "Y")
    show("S6_POSSIBLE_STALE", r6)

    print()
    print("=== STATE SEPARATION COMPLETE ===")
    print("NO DESIGN CHANGE")
    print("NO STATE POLICY SELECTED")


if __name__ == "__main__":
    main()
