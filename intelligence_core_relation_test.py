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


def main():

    print("=== INTELLIGENCE CORE RELATION TEST ===")

    # ------------------------------------------------------------
    # R1:
    # 「色」が結果を決める関係を経験
    #
    # A + RED  -> X
    # A + BLUE -> Y
    #
    # その後、未知の対象Bについて
    #
    # B + RED  -> ?
    #
    # を与える。
    #
    # もし「RED -> X」という関係を抽出できれば、
    # Bそのものを経験していなくてもXを予測できる。
    # ------------------------------------------------------------

    core = IntelligenceCore()

    cycle(
        core,
        {"object": "A", "color": "RED"},
        "X",
    )

    cycle(
        core,
        {"object": "A", "color": "BLUE"},
        "Y",
    )

    r1 = cycle(
        core,
        {"object": "B", "color": "RED"},
        "X",
    )

    print("R1_RELATION_TRANSFER:")
    print("  prediction:", r1["prediction"])
    print("  used_experience:", r1["used_experience"])
    print("  actual:", r1["actual_result"])

    # ------------------------------------------------------------
    # R2:
    # 逆方向
    #
    # B + RED -> X
    # B + BLUE -> Y
    #
    # 未知のA + RED。
    #
    # 対象そのものではなく色との関係を抽出できるか。
    # ------------------------------------------------------------

    core = IntelligenceCore()

    cycle(
        core,
        {"object": "B", "color": "RED"},
        "X",
    )

    cycle(
        core,
        {"object": "B", "color": "BLUE"},
        "Y",
    )

    r2 = cycle(
        core,
        {"object": "A", "color": "RED"},
        "X",
    )

    print("R2_REVERSE_TRANSFER:")
    print("  prediction:", r2["prediction"])
    print("  used_experience:", r2["used_experience"])
    print("  actual:", r2["actual_result"])

    # ------------------------------------------------------------
    # R3:
    # 対象と色の両方が未知。
    #
    # ここでは一般化不能であることが期待される。
    # 「何でもXとする」ことを一般化とは認めない。
    # ------------------------------------------------------------

    core = IntelligenceCore()

    cycle(
        core,
        {"object": "A", "color": "RED"},
        "X",
    )

    cycle(
        core,
        {"object": "A", "color": "BLUE"},
        "Y",
    )

    r3 = cycle(
        core,
        {"object": "C", "color": "GREEN"},
        "Y",
    )

    print("R3_BOTH_UNKNOWN:")
    print("  prediction:", r3["prediction"])
    print("  used_experience:", r3["used_experience"])
    print("  actual:", r3["actual_result"])

    # ------------------------------------------------------------
    # R4:
    # 経験なしとの比較
    #
    # B + RED を、
    # 経験あり / 経験なしで比較する。
    # ------------------------------------------------------------

    no_memory = IntelligenceCore()

    no_memory_result = cycle(
        no_memory,
        {"object": "B", "color": "RED"},
        "X",
    )

    with_memory = IntelligenceCore()

    cycle(
        with_memory,
        {"object": "A", "color": "RED"},
        "X",
    )

    cycle(
        with_memory,
        {"object": "A", "color": "BLUE"},
        "Y",
    )

    with_memory_result = cycle(
        with_memory,
        {"object": "B", "color": "RED"},
        "X",
    )

    print("R4_MEMORY_TRANSFER_EFFECT:")
    print("  no_memory_prediction:",
          no_memory_result["prediction"])
    print("  no_memory_used_experience:",
          no_memory_result["used_experience"])

    print("  with_memory_prediction:",
          with_memory_result["prediction"])
    print("  with_memory_used_experience:",
          with_memory_result["used_experience"])

    print()
    print("=== RELATION TEST COMPLETE ===")
    print("NO DESIGN CHANGE")
    print("NO GENERALIZATION CLAIM")


if __name__ == "__main__":
    main()
