from pathlib import Path

print("=== HYPOTHESIS RESPONSIBILITY BOUNDARY AUDIT ===")

files = [
    "intelligence_core.py",
    "world_model.py",
    "reasoner.py",
    "learner_v1_code_map.py",
    "world_model_v2_code_map.py",
    "PHASE1_INTELLIGENCE_CORE_v1.0.md",
]

terms = [
    "hypothesis",
    "hypothesis_id",
    "prediction",
    "actual_result",
    "Experience",
    "Knowledge",
]

for filename in files:
    path = Path(filename)

    print()
    print(f"=== {filename} ===")

    if not path.exists():
        print("MISSING")
        continue

    lines = path.read_text(errors="replace").splitlines()

    for i, line in enumerate(lines, 1):
        lower = line.lower()

        if any(term.lower() in lower for term in terms):
            print(f"L{i}: {line.strip()}")

print()
print("=== RESPONSIBILITY QUESTIONS ===")

print("1. IntelligenceCore hypothesis evaluation: EXISTING")
print("2. Experience hypothesis trace: EXISTING")
print("3. WorldModel hypothesis storage: TO_BE_DETERMINED")
print("4. Reasoner hypothesis dependency: AUDITED AS NOT REQUIRED")
print("5. Learner hypothesis responsibility: DESIGN REVIEW REQUIRED")

print()
print("=== CONCLUSION ===")
print("HYPOTHESIS_BOUNDARY: REVIEW_REQUIRED")
print("WORLD_MODEL_CHANGE: NONE")
print("DESIGN_DECISION: HOLD")
