from intelligence_core import IntelligenceCore


def cycle(core, signal, result):
    return core.cycle(
        observation={"signal": signal},
        hypotheses=[
            {"id": "H1", "prediction": "X"},
            {"id": "H2", "prediction": "Y"},
        ],
        actual_result=result,
    )


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def main():

    print("=== INTELLIGENCE CORE DIAGNOSTIC ===")

    # ============================================================
    # H1: 安定
    # 同一観測 → 同一結果
    # ============================================================
    stable = IntelligenceCore()

    s1 = cycle(stable, "A", "X")
    s2 = cycle(stable, "A", "X")
    s3 = cycle(stable, "A", "X")

    print("H1_STABLE:",
          [s1["actual_result"], s2["actual_result"], s3["actual_result"]])

    check(
        all(r["actual_result"] == "X" for r in [s1, s2, s3]),
        "H1 setup failed"
    )

    # ============================================================
    # H2: 観測状態が不足している可能性
    #
    # 表面上は A だが、実際には A1 / A2 が違うと仮定した
    # 場合に、コアへ異なる観測を与えると区別できるかを見る。
    # ============================================================
    state = IntelligenceCore()

    a1 = cycle(state, "A1", "X")
    a2 = cycle(state, "A2", "Y")
    a3 = cycle(state, "A1", "X")
    a4 = cycle(state, "A2", "Y")

    print("H2_STATE_SPLIT:",
          a1["actual_result"],
          a2["actual_result"],
          a3["actual_result"],
          a4["actual_result"])

    check(
        a3["prediction"] == "X",
        "H2: state A1 did not retain its own experience"
    )

    check(
        a4["prediction"] == "Y",
        "H2: state A2 did not retain its own experience"
    )

    # ============================================================
    # H3: 時間変化
    #
    # 同一観測だが、環境が変化したケース。
    # ============================================================
    changing = IntelligenceCore()

    t1 = cycle(changing, "A", "X")
    t2 = cycle(changing, "A", "X")
    t3 = cycle(changing, "A", "Y")
    t4 = cycle(changing, "A", "Y")

    print("H3_TIME_CHANGE:",
          [t1["actual_result"],
           t2["actual_result"],
           t3["actual_result"],
           t4["actual_result"]])

    # ここでは正解を決めない。
    # 「最新経験を使った」という結果だけ観測する。
    print("H3_PREDICTIONS:",
          [t1["prediction"],
           t2["prediction"],
           t3["prediction"],
           t4["prediction"]])

    # ============================================================
    # H4: ノイズ / 不安定環境
    #
    # X/Yが交互に発生するケース。
    # ============================================================
    noisy = IntelligenceCore()

    n1 = cycle(noisy, "A", "X")
    n2 = cycle(noisy, "A", "Y")
    n3 = cycle(noisy, "A", "X")
    n4 = cycle(noisy, "A", "Y")
    n5 = cycle(noisy, "A", "X")
    n6 = cycle(noisy, "A", "Y")

    print("H4_NOISE_RESULTS:",
          [n["actual_result"] for n in [n1, n2, n3, n4, n5, n6]])

    print("H4_PREDICTIONS:",
          [n["prediction"] for n in [n1, n2, n3, n4, n5, n6]])

    # ============================================================
    # H5: 経験品質差
    #
    # 現在のAPIには品質情報がない。
    # したがって「品質差を扱えるか」は今は検証不能。
    # ここでは現在の経験表現を観測するだけ。
    # ============================================================
    quality = IntelligenceCore()

    q1 = cycle(quality, "A", "X")
    q2 = cycle(quality, "A", "Y")

    print("H5_EXPERIENCE_FIELDS:",
          sorted(q1.keys()))

    print("H5_STORED_FIELDS:",
          sorted(quality.experiences[0].keys()))

    print()
    print("=== DIAGNOSTIC COMPLETE ===")
    print("NO DESIGN CHANGE")
    print("NO CONFLICT POLICY SELECTED")


if __name__ == "__main__":
    main()
