from intelligence_core import IntelligenceCore


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    core = IntelligenceCore()

    # A: 経験なし
    r1 = core.cycle(
        observation={"signal": "A"},
        hypotheses=[
            {"id": "H1", "prediction": "X"},
            {"id": "H2", "prediction": "Y"},
        ],
        actual_result="X",
    )

    check(r1["status"] == "UPDATED", "A: update failed")
    check(r1["prediction"] == "X", "A: prediction mismatch")

    # B: 関連経験あり
    r2 = core.cycle(
        observation={"signal": "A"},
        hypotheses=[
            {"id": "H1", "prediction": "X"},
            {"id": "H2", "prediction": "Y"},
        ],
        actual_result="X",
    )

    check(r2["used_experience"] is True,
          "B: related experience was not used")

    # C: 無関係経験は判断を変える根拠にならない
    core2 = IntelligenceCore()
    core2.cycle(
        observation={"signal": "B"},
        hypotheses=[
            {"id": "H1", "prediction": "X"},
            {"id": "H2", "prediction": "Y"},
        ],
        actual_result="Y",
    )

    r3 = core2.cycle(
        observation={"signal": "A"},
        hypotheses=[
            {"id": "H1", "prediction": "X"},
            {"id": "H2", "prediction": "Y"},
        ],
        actual_result="X",
    )

    check(r3["used_experience"] is False,
          "C: unrelated experience affected decision")

    # D: 反証
    core3 = IntelligenceCore()

    r4 = core3.cycle(
        observation={"signal": "C"},
        hypotheses=[
            {"id": "H1", "prediction": "X"},
        ],
        actual_result="Y",
    )

    check(r4["hypothesis_status"]["H1"] == "REFUTED",
          "D: hypothesis was not refuted")

    # E: 未知ケース
    r5 = core3.cycle(
        observation={"signal": "D"},
        hypotheses=[
            {"id": "H1", "prediction": "X"},
            {"id": "H2", "prediction": "Y"},
        ],
        actual_result="Y",
    )

    check(r5["status"] == "UPDATED",
          "E: unknown case failed")

    print("=== INTELLIGENCE CORE MINIMUM TEST ===")
    print("RELATED_EXPERIENCE:", r2["used_experience"])
    print("UNRELATED_EXPERIENCE:", r3["used_experience"])
    print("REFUTATION:", r4["hypothesis_status"]["H1"])
    print("UNKNOWN_CASE:", r5["status"])
    print("PASS")


if __name__ == "__main__":
    main()
