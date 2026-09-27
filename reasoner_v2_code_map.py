"""
ΩAI Phase2 Code Map
Reasoner v2 (Design Fixed)
STATUS: DESIGN_FIXED
"""

PHASE = {
    "name": "Reasoner v2",
    "status": "DESIGN_FIXED",
    "depends_on": "WorldModel v2",
}

INPUT = {
    "knowledge": [
        "facts",
        "hypotheses",
        "conflicts",
        "history_count",
    ],
}

OUTPUT = {
    "PASS": "十分な根拠がある。",
    "HOLD": "証拠不足で保留。",
    "CONFLICT": "矛盾が残っている。",
    "UNKNOWN": "知識が存在しない。",
}

REASONING_PIPELINE = [
    "Read Knowledge",
    "Check Conflict",
    "Check Stable Fact",
    "Check Unknown",
    "Return Decision",
]

NOT_IMPLEMENTED = [
    "hypothesis_search",
    "counterfactual_reasoning",
    "confidence_score",
    "causal_reasoning",
]

NEXT_STEP = "reasoner_v2_test.py"
