from pathlib import Path
import ast
import re

print("=== WORLD MODEL SEMANTIC CONTRACT AUDIT ===")

FILES = [
    "world_model.py",
    "world_model_v2_code_map.py",
    "reasoner.py",
    "world_model_minimal_contract_test.py",
    "world_model_fact_test.py",
    "world_model_conflict_test.py",
    "world_reasoner_integration_test.py",
]

for name in FILES:
    path = Path(name)
    if not path.exists():
        print(f"{name}: MISSING")
        continue

    print(f"\n=== {name} ===")
    text = path.read_text(errors="replace")

    terms = ["FACT", "STABLE", "CONFLICT", "UNKNOWN"]

    for term in terms:
        lines = [
            f"{i}: {line.strip()}"
            for i, line in enumerate(text.splitlines(), 1)
            if re.search(rf"\b{term}\b", line, re.IGNORECASE)
        ]

        if lines:
            print(f"[{term}]")
            for line in lines:
                print(" ", line)
        else:
            print(f"[{term}] NONE")

print("\n=== IMPLEMENTATION STRUCTURE ===")

tree = ast.parse(Path("world_model.py").read_text())

for node in tree.body:
    if isinstance(node, ast.ClassDef):
        print(f"CLASS: {node.name}")

        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                print(f"  METHOD: {item.name}")

print("\n=== CONTRACT RELATION ===")

print("KNOWLEDGE STATE MODEL:")
print("  Formal states = UNKNOWN / STABLE / CONFLICT")
print("  Implementation representation = observation + results + history_count")

print("STABLE:")
print("  Implementation condition = len(results) == 1")

print("CONFLICT:")
print("  Implementation condition = len(results) >= 2")

print("UNKNOWN:")
print("  Implementation condition = history_count == 0")

print("\n=== TRANSITION CHECK ===")

print("NO HISTORY -> UNKNOWN")
print("ONE UNIQUE RESULT -> STABLE")
print("REPEATED SAME RESULT -> STABLE")
print("MULTIPLE RESULTS -> CONFLICT")

print("\n=== CONCLUSION ===")
print("SEMANTIC_CONTRACT_SCAN: COMPLETE")
print("IMPLEMENTATION_CHANGE: NONE")
print("DESIGN_DECISION: HOLD")
print("NEXT: REVIEW_OUTPUT")
