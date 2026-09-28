from pathlib import Path
from world_model import Knowledge

print("=== WORLD MODEL CONTRACT CONSISTENCY AUDIT ===")

fields = list(Knowledge.__dataclass_fields__.keys())

print("IMPLEMENTED_KNOWLEDGE_FIELDS:", fields)

design = Path("world_model_v2_code_map.py").read_text(errors="replace")

claims = {
    "FACT": "FACT" in design,
    "HYPOTHESIS": "HYPOTHESIS" in design,
    "CONFLICT": "CONFLICT" in design,
    "UNKNOWN": "UNKNOWN" in design,
    "new_hypothesis_rule": "new_hypothesis" in design,
}

print()
print("DESIGN_CLAIMS:")
for name, value in claims.items():
    print(f"  {name}: {value}")

implemented_capabilities = {
    "observation": "observation" in fields,
    "results": "results" in fields,
    "history_count": "history_count" in fields,
    "hypothesis_storage": (
        "hypothesis" in fields
        or "hypotheses" in fields
    ),
}

print()
print("IMPLEMENTED_CAPABILITIES:")
for name, value in implemented_capabilities.items():
    print(f"  {name}: {value}")

print()
print("=== GAP ANALYSIS ===")

if claims["HYPOTHESIS"] and not implemented_capabilities["hypothesis_storage"]:
    print("HYPOTHESIS_CONTRACT_GAP: CONFIRMED")
else:
    print("HYPOTHESIS_CONTRACT_GAP: NOT_CONFIRMED")

if claims["new_hypothesis_rule"] and not implemented_capabilities["hypothesis_storage"]:
    print("HYPOTHESIS_UPDATE_GAP: CONFIRMED")
else:
    print("HYPOTHESIS_UPDATE_GAP: NOT_CONFIRMED")

print()
print("=== STATUS ===")
print("CODE_MAP_IMPLEMENTATION_ALIGNMENT: REQUIRES_REVIEW")
print("WORLD_MODEL_IMPLEMENTATION_CHANGE: NOT_PERFORMED")
print("DESIGN_DECISION: HOLD")
