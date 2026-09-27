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
    "observation.py": {
        "role": "Observation Layer",
        "responsibility": "観測を構造化してイベント化する。",
    },

    "intelligence_core.py": {
        "role": "Intelligence Core",
        "responsibility": [
            "Experience保存",
            "Hypothesis評価",
            "Prediction生成",
            "Conflict保持",
        ],
    },

    "world_model.py": {
        "role": "Knowledge Layer",
        "responsibility": [
            "Experience→Knowledge変換",
            "stable判定",
            "conflict判定",
            "unknown判定",
        ],
    },

    "reasoner.py": {
        "role": "Decision Layer",
        "responsibility": [
            "PASS",
            "HOLD",
            "CONFLICT",
            "UNKNOWN",
        ],
    },

    "runtime.py": {
        "role": "Execution Layer",
        "responsibility": [
            "Effect実行",
            "Recovery",
            "二重実行防止",
        ],
    },

    "store.py": {
        "role": "Persistence Layer",
        "responsibility": [
            "SQLite状態保存",
            "Effect状態管理",
        ],
    },

    "state_store.py": {
        "role": "State Persistence",
        "responsibility": "AI状態保存・復元",
    },

    "event_journal.py": {
        "role": "Audit Layer",
        "responsibility": [
            "イベント記録",
            "チェーン検証",
            "改ざん検知",
        ],
    },
}

PIPELINE = [
    "Observation",
    "IntelligenceCore",
    "WorldModel",
    "Reasoner",
    "Runtime",
]

STATE_MODEL = {
    "knowledge": [
        "stable",
        "conflict",
        "unknown",
    ],
    "decision": [
        "PASS",
        "HOLD",
        "CONFLICT",
        "UNKNOWN",
    ],
}

TEST_STATUS = {
    "intelligence_core": "PASS",
    "conflict": "PASS",
    "world_reasoner_integration": "PASS",
    "runtime_integration": "PASS",
    "recovery": "PASS",
    "event_journal": "PASS",
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
