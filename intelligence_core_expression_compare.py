from intelligence_core import IntelligenceCore
from intelligence_core_typed_experiment import (
    IntelligenceCoreTyped,
    Hypothesis,
    normalize,
)


def run_original(cases):
    core = IntelligenceCore()
    results = []

    for observation, hypotheses, actual in cases:
        results.append(
            core.cycle(
                observation,
                hypotheses,
                actual,
            )
        )

    return results


def run_typed(cases):
    core = IntelligenceCoreTyped()
    results = []

    for observation, hypotheses, actual in cases:
        typed_hypotheses = [
            Hypothesis(
                id=h["id"],
                prediction=h["prediction"],
            )
            for h in hypotheses
        ]

        result = core.cycle(
            observation,
            typed_hypotheses,
            actual,
        )

        results.append(normalize(result))

    return results


CASES = [
    (
        {"signal": "A"},
        [
            {"id": "H1", "prediction": "X"},
            {"id": "H2", "prediction": "Y"},
        ],
        "X",
    ),
    (
        {"signal": "A"},
        [
            {"id": "H1", "prediction": "X"},
            {"id": "H2", "prediction": "Y"},
        ],
        "X",
    ),
    (
        {"signal": "A"},
        [
            {"id": "H1", "prediction": "X"},
            {"id": "H2", "prediction": "Y"},
        ],
        "Y",
    ),
    (
        {"signal": "B"},
        [
            {"id": "H1", "prediction": "X"},
            {"id": "H2", "prediction": "Y"},
        ],
        "Y",
    ),
]


original = run_original(CASES)
typed = run_typed(CASES)

original_normalized = [
    result
    for result in original
]

print("=== ORIGINAL ===")
for result in original_normalized:
    print(result)

print()
print("=== TYPED ===")
for result in typed:
    print(result)

print()
print("=== COMPARISON ===")

for i, (a, b) in enumerate(
    zip(original_normalized, typed),
    start=1,
):
    same = a == b
    print(f"CASE {i}: {'MATCH' if same else 'DIFF'}")

    if not same:
        print("  ORIGINAL:", a)
        print("  TYPED:   ", b)

print()
print(
    "FINAL:",
    "BEHAVIOR MATCH"
    if original_normalized == typed
    else "BEHAVIOR DIFFERENCE",
)
