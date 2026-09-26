from intelligence_core import IntelligenceCore


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def run_cycle(core, actual_result):
    return core.cycle(
        observation={"signal": "A"},
        hypotheses=[
            {"id": "H1", "prediction": "X"},
            {"id": "H2", "prediction": "Y"},
        ],
        actual_result=actual_result,
    )


def main():

    # ============================================================
    # A: 安定した経験
    # A -> X
    # A -> X
    # A -> X
    #
    # 安定した経験は通常どおり利用できる必要がある。
    # ============================================================
    stable = IntelligenceCore()

    run_cycle(stable, "X")
    run_cycle(stable, "X")
    r1 = run_cycle(stable, "X")

    check(
        r1["prediction"] == "X",
        "A: stable experience was not retained"
    )

    # ============================================================
    # B: 矛盾する経験
    #
    # A -> X
    # A -> Y
    #
    # この時点で「Xが真」「Yが真」と一意に確定してはいけない。
    # 矛盾そのものを状態として観測可能でなければならない。
    # ============================================================
    conflict = IntelligenceCore()

    run_cycle(conflict, "X")
    r2 = run_cycle(conflict, "Y")

    print("CONFLICT_RESULT:", r2)

    check(
        r2.get("conflict") is True,
        "B: conflict was not detected"
    )

    check(
        r2.get("status") == "CONFLICT",
        "B: conflict status was not exposed"
    )

    # ============================================================
    # C: 矛盾中に新しい観測を与えても、
    #    古い経験だけを根拠に確定してはいけない。
    # ============================================================
    r3 = run_cycle(conflict, "X")

    print("POST_CONFLICT_RESULT:", r3)

    check(
        r3.get("conflict") is True,
        "C: conflict state disappeared without resolution"
    )

    print("=== CONFLICT EXPERIENCE TEST ===")
    print("STABLE:", r1["prediction"])
    print("CONFLICT:", r2["status"])
    print("POST_CONFLICT:", r3["status"])
    print("PASS")


if __name__ == "__main__":
    main()
