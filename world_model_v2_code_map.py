"""
ΩAI Phase2 Code Map
WorldModel v2 (Design Fixed)
STATUS: DESIGN_FIXED
"""

PHASE = {
    "name": "WorldModel v2",
    "status": "DESIGN_FIXED",
    "depends_on": "Intelligence Core v1.0",
}

KNOWLEDGE_MODEL = {
    "FACT": "観測で確認済みの事実。",
    "CONFLICT": "矛盾している事実・仮説。",
    "UNKNOWN": "証拠不足で判断保留。",
}

RESPONSIBILITY = {
    "observe": [
        "ExperienceをKnowledgeへ変換",
        "history更新",
        "conflict保持",
    ],
    "lookup": [
        "Knowledge取得",
        "stable/conflict/unknown判定",
    ],
}

UPDATE_RULES = {
    "same_result": "FACTを強化（history_count増加）",
    "different_result": "CONFLICTへ追加",
    "no_evidence": "UNKNOWN維持",
}

NOT_IMPLEMENTED = [
    "confidence_score",
    "generalization",
    "causal_links",
    "planner",
    "learner",
]

NEXT_STEP = "world_model_fact_test.py"
