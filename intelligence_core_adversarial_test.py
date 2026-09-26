from intelligence_core import IntelligenceCore


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    core = IntelligenceCore()

    # 1. 最初の経験
    r1 = core.cycle(
        observation={"signal": "A"},
        hypotheses=[
            {"id": "H1", "prediction": "X"},
            {"id": "H2", "prediction": "Y"},
        ],
        actual_result="X",
    )

    check(r1["prediction"] == "X",
          "initial learning failed")

    # 2. 同じ状況だが、現実が変化した
    #    古い経験 X を盲目的に使うならここで失敗する
    r2 = core.cycle(
        observation={"signal": "A"},
        hypotheses=[
            {"id": "H1", "prediction": "X"},
            {"id": "H2", "prediction": "Y"},
        ],
        actual_result="Y",
    )

    print("OLD_EXPERIENCE:", r1["actual_result"])
    print("NEW_RESULT:", r2["actual_result"])
    print("NEW_PREDICTION:", r2["prediction"])

    # 3. さらに同じ状況で新しい結果が続く
    r3 = core.cycle(
        observation={"signal": "A"},
        hypotheses=[
            {"id": "H1", "prediction": "X"},
            {"id": "H2", "prediction": "Y"},
        ],
        actual_result="Y",
    )

    print("LATEST_PREDICTION:", r3["prediction"])

    # 現在の最小実装が本当に経験を更新できるなら、
    # 新しい証拠 Y を受けて次回は Y を選ぶ必要がある。
    check(
        r3["prediction"] == "Y",
        "stale experience was not overridden"
    )

    print("=== ADVERSARIAL EXPERIENCE TEST ===")
    print("PASS")


if __name__ == "__main__":
    main()
