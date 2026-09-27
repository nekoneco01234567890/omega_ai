"""
ΩAI Phase2 Code Map
Planner v1 (Design Fixed)
STATUS: DESIGN_FIXED
"""

PHASE = {
    "name": "Planner v1",
    "status": "DESIGN_FIXED",
    "depends_on": "Reasoner v2",
}

PURPOSE = {
    "goal": "目的から行動候補を生成する。",
    "rule": "実行はしない。候補だけ生成する。",
}

INPUT = {
    "goal": "達成したい目的",
    "decision": "Reasonerの判断結果",
    "knowledge": "WorldModelの知識",
}

OUTPUT = {
    "candidate_actions": "実行候補一覧",
    "hold": "証拠不足なら保留",
}

PIPELINE = [
    "Receive Goal",
    "Read Decision",
    "Read Knowledge",
    "Generate Candidates",
    "Return Plan",
]

NOT_IMPLEMENTED = [
    "search_strategy",
    "cost_estimation",
    "priority_selection",
    "execution",
]

NEXT_STEP = "planner_v1_test.py"
