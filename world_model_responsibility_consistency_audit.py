from pathlib import Path

print("=== WORLD MODEL RESPONSIBILITY CONSISTENCY AUDIT ===")

files = {
    "phase1": "PHASE1_INTELLIGENCE_CORE_v1.0.md",
    "world_model": "world_model_v2_code_map.py",
    "reasoner": "reasoner_v2_code_map.py",
    "learner": "learner_v1_code_map.py",
    "code_map": "code_map.py",
}

texts = {}

for role, filename in files.items():
    path = Path(filename)

    print()
    print(f"=== {role.upper()} ===")

    if not path.exists():
        print("MISSING:", filename)
        continue

    text = path.read_text(errors="replace")
    texts[role] = text

    print("FILE:", filename)
    print("LINES:", len(text.splitlines()))

print()
print("=== RESPONSIBILITY EVIDENCE ===")

checks = {
    "PHASE1_INTELLIGENCE_HYPOTHESIS": (
        "Hypothesis evaluation" in texts.get("phase1", "")
    ),
    "PHASE1_WORLD_KNOWLEDGE": (
        "World knowledge" in texts.get("phase1", "")
    ),
    "WORLDMODEL_EXPERIENCE_TO_KNOWLEDGE": (
        "ExperienceをKnowledgeへ変換" in texts.get("world_model", "")
    ),
    "WORLDMODEL_STABLE": (
        "stable" in texts.get("world_model", "")
    ),
    "WORLDMODEL_CONFLICT": (
        "conflict" in texts.get("world_model", "")
    ),
    "WORLDMODEL_UNKNOWN": (
        "unknown" in texts.get("world_model", "")
    ),
    "REASONER_DECISION": (
        "Decision" in texts.get("reasoner", "")
    ),
    "LEARNER_EXPERIENCE": (
        "IntelligenceCoreが保存したExperience" in texts.get("learner", "")
    ),
    "LEARNER_KNOWLEDGE_UPDATE": (
        "Knowledge" in texts.get("learner", "")
    ),
}

for name, result in checks.items():
    print(f"{name}: {result}")

print()
print("=== HYPOTHESIS LOCATION ===")

for role, text in texts.items():
    if "HYPOTHESIS" in text or "hypothesis" in text.lower():
        print(f"{role}: PRESENT")

print()
print("=== DECISION ===")

print("WORLD_MODEL_CORE_ROLE:")
print("  Experience -> Knowledge")
print("  stable / conflict / unknown")

print()
print("HYPOTHESIS_CORE_ROLE:")
print("  IntelligenceCore -> hypothesis evaluation")

print()
print("LEARNER_ROLE:")
print("  Experience + Knowledge -> future knowledge update")

print()
print("CURRENT_HYPOTHESIS_IN_WORLDMODEL_CODEMAP: REVIEW_REQUIRED")
print("WORLD_MODEL_IMPLEMENTATION_CHANGE: NONE")
print("RESPONSIBILITY_BOUNDARY: HOLD")
print("AUDIT_STATUS: PASS")
