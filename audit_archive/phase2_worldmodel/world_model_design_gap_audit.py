from pathlib import Path

print("=== WORLD MODEL DESIGN GAP AUDIT ===")

targets = [
    "PHASE1_INTELLIGENCE_CORE_v1.0.md",
    "world_model_v2_code_map.py",
    "reasoner_v2_code_map.py",
    "code_map.py",
]

keywords = [
    "WorldModel",
    "Knowledge",
    "time",
    "condition",
    "state",
    "scope",
    "source",
    "evidence",
    "unknown",
    "conflict",
    "stable",
    "generalization",
    "confidence",
    "causal",
]

for filename in targets:
    path = Path(filename)

    print()
    print(f"=== {filename} ===")

    if not path.exists():
        print("FILE: MISSING")
        continue

    text = path.read_text(errors="replace")
    lower = text.lower()

    for keyword in keywords:
        count = lower.count(keyword.lower())
        if count:
            print(f"{keyword}: {count}")

print()
print("=== CURRENT IMPLEMENTATION ===")

from world_model import Knowledge

fields = list(Knowledge.__dataclass_fields__.keys())

print("Knowledge fields:", fields)

print()
print("=== CURRENT CODE MAP ===")

code_map = Path("world_model_v2_code_map.py")

if code_map.exists():
    print(code_map.read_text(errors="replace"))
else:
    print("world_model_v2_code_map.py: MISSING")

print()
print("=== CONCLUSION ===")
print("DESIGN_SOURCE_SCAN: COMPLETE")
print("IMPLEMENTATION_FIELDS: RECORDED")
print("DESIGN_GAP: REQUIRES INTERPRETATION")
print("NO DESIGN CHANGE")
