from pathlib import Path

print("=== WORLD MODEL CONTEXT DEPENDENCY AUDIT ===")

targets = [
    "reasoner.py",
    "world_model.py",
    "world_reasoner_integration_test.py",
    "reasoner_v2_regression_test.py",
]

terms = [
    "time",
    "condition",
    "state",
    "scope",
    "source",
    "evidence",
    "observation",
    "results",
    "history_count",
]

for filename in targets:
    path = Path(filename)

    print()
    print(f"[{filename}]")

    if not path.exists():
        print("  FILE: MISSING")
        continue

    text = path.read_text()

    for term in terms:
        count = text.lower().count(term.lower())
        print(f"  {term}: {count}")

print()
print("=== CURRENT KNOWLEDGE CONTRACT ===")

from world_model import Knowledge

fields = list(Knowledge.__dataclass_fields__.keys())

print("KNOWLEDGE_FIELDS:", fields)

expected_core = [
    "observation",
    "results",
    "history_count",
]

print(
    "CORE_CONTRACT:",
    "PASS" if fields == expected_core else "CHANGED",
)

print()
print("=== CONCLUSION ===")
print("DOWNSTREAM_CONTEXT_REQUIREMENT: AUDIT_REQUIRED")
print("CURRENT_KNOWLEDGE_CONTRACT: RECORDED")
print("CONTEXT_AXIS_IMPLEMENTATION: NOT_JUSTIFIED")
print("NO DESIGN CHANGE")
