"""
ΩAI Phase 2 Code Map
Reasoner v2
STATUS: DESIGN_REFINED
"""

PHASE = {
    "name": "Reasoner v2",
    "status": "DESIGN_REFINED",
    "depends_on": "WorldModel v1",
}

INPUT = {
    "knowledge": [
        "observation",
        "results",
        "history_count",
    ],
}

OUTPUT = {
    "UNKNOWN": "知識が存在しない。",
    "PASS": "観測結果が安定している。",
    "CONFLICT": "異なる結果が観測されている。",
}

REASONING_PIPELINE = [
    "Read Knowledge",
    "Check Unknown",
    "Check Conflict",
    "Check Stable",
    "Return Decision",
]

MINIMAL_CONTRACT = {
    "required_input": [
        "observation",
        "results",
        "history_count",
    ],
    "required_output": [
        "UNKNOWN",
        "PASS",
        "CONFLICT",
    ],
}

NOT_REQUIRED_BY_CURRENT_EVIDENCE = [
    "facts",
    "hypotheses",
    "HOLD",
    "confidence_score",
    "hypothesis_search",
    "counterfactual_reasoning",
    "causal_reasoning",
]

OPEN_REQUIREMENTS = [
    "HOLD requirement",
    "time-aware reasoning",
    "condition-aware reasoning",
    "scope-aware reasoning",
    "evidence-quality reasoning",
    "independence-aware reasoning",
]

NEXT_STEP = "reasoner_v2_regression_test.py"
