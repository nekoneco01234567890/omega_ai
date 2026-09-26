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


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def main():

    print("=== INTELLIGENCE CORE GENERALIZATION TEST ===")

    # ------------------------------------------------------------
    # G1: 同一条件の再現
    # ------------------------------------------------------------
    core = IntelligenceCore()

    cycle(core, "A", "X")
    r = cycle(core, "A", "X")

    print("G1_SAME_STATE:", r["prediction"])

    # ------------------------------------------------------------
    # G2: 未知状態
    #
    # A -> X を経験した後、
    # 未知のBに遭遇したとき何をするかを見る。
    # ------------------------------------------------------------
    core = IntelligenceCore()

    cycle(core, "A", "X")
    r = cycle(core, "B", "Y")

    print("G2_UNKNOWN_STATE:")
    print("  prediction:", r["prediction"])
    print("  used_experience:", r["used_experience"])
    print("  actual:", r["actual_result"])

    # ------------------------------------------------------------
    # G3: 表面的に似た未知状態
    #
    # A1 -> X
    # A2 -> Y
    #
    # A3 は未経験。
    # ------------------------------------------------------------
    core = IntelligenceCore()

    cycle(core, "A1", "X")
    cycle(core, "A2", "Y")
    r = cycle(core, "A3", "X")

    print("G3_UNSEEN_VARIANT:")
    print("  prediction:", r["prediction"])
    print("  used_experience:", r["used_experience"])

    # ------------------------------------------------------------
    # G4: 条件依存
    #
    # A + C -> X
    # A + D -> Y
    #
    # 表現上の条件を分けた場合に、
    # コアが条件差を保持できるかを見る。
    # ------------------------------------------------------------
    core = IntelligenceCore()

    cycle(core, "A_C", "X")
    cycle(core, "A_D", "Y")

    r1 = cycle(core, "A_C", "X")
    r2 = cycle(core, "A_D", "Y")

    print("G4_CONDITION_DEPENDENCE:")
    print("  A_C prediction:", r1["prediction"])
    print("  A_D prediction:", r2["prediction"])

    # ------------------------------------------------------------
    # G5: 経験なし vs 経験あり
    #
    # 同じ未知ケースについて、
    # 過去経験の有無で判断が変わるかを見る。
    # ------------------------------------------------------------
    no_memory = IntelligenceCore()
    with_memory = IntelligenceCore()

    no_memory_result = cycle(no_memory, "B", "Y")

    cycle(with_memory, "A", "X")
    with_memory_result = cycle(with_memory, "B", "Y")

    print("G5_MEMORY_EFFECT:")
    print("  no_memory_prediction:",
          no_memory_result["prediction"])
    print("  with_memory_prediction:",
          with_memory_result["prediction"])

    print()
    print("=== GENERALIZATION TEST COMPLETE ===")
    print("NO DESIGN CHANGE")
    print("NO PASS/FAIL CLAIM FOR GENERALIZATION")


if __name__ == "__main__":
    main()
