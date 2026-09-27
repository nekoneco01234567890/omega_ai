"""
ΩAI CODE MAP
Phase 1 : Intelligence Core v1.0
STATUS : PASS / FIXED
"""

PHASE = {
    "name": "Intelligence Core v1.0",
    "status": "PASS",
    "fixed": True,
}

MODULES = {
    "observation.py": "観測を構造化",
    "intelligence_core.py": "経験・仮説評価・矛盾保持",
    "world_model.py": "経験→知識(stable/conflict/unknown)",
    "reasoner.py": "PASS/HOLD/CONFLICT/UNKNOWN 判定",
    "runtime.py": "実行・復旧・二重実行防止",
    "store.py": "状態永続化(SQLite)",
    "state_store.py": "AI状態保存・復元",
    "event_journal.py": "イベント記録・改ざん検証",
}

PIPELINE = [
    "Observation",
    "IntelligenceCore",
    "WorldModel",
    "Reasoner",
    "Runtime",
]

STATE_MODEL = {
    "knowledge": ["stable", "conflict", "unknown"],
    "decision": ["PASS", "HOLD", "CONFLICT", "UNKNOWN"],
}

TEST_STATUS = {
    "intelligence_core": "PASS",
    "conflict": "PASS",
    "world_reasoner_integration": "PASS",
    "runtime_integration": "PASS",
    "recovery": "PASS",
    "event_journal": "PASS",
    "world_model_v1_audit": "PASS",
}

NOT_IMPLEMENTED = [
    "Generalization",
    "Confidence Model",
    "Causal Reasoning",
    "Planner",
    "Learner",
    "Long-term Memory Compression",
]

NEXT_PHASE = "WorldModel v2 / Reasoner v2 / Planner / Learner"
