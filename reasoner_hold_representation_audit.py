from dataclasses import fields
from world_model import Knowledge


print("=== REASONER HOLD REPRESENTATION AUDIT ===")

field_names = [f.name for f in fields(Knowledge)]

print("KNOWLEDGE_FIELDS:", field_names)

required_concepts = [
    "observation",
    "results",
    "history_count",
]

for name in required_concepts:
    assert name in field_names

# 現在のKnowledgeに「根拠の質」を表す情報があるか確認
quality_fields = [
    "evidence",
    "evidence_quality",
    "reliability",
    "source",
    "confidence",
]

present_quality_fields = [
    name for name in quality_fields
    if name in field_names
]

print("EVIDENCE_QUALITY_FIELDS:", present_quality_fields)

if not present_quality_fields:
    print("HOLD_REPRESENTATION: NOT_AVAILABLE")
else:
    print("HOLD_REPRESENTATION: AVAILABLE")

# 現在の3状態がKnowledgeの情報だけで区別可能か確認
unknown = Knowledge(observation={"signal": "U"})
stable = Knowledge(
    observation={"signal": "S"},
    results={"X"},
    history_count=1,
)
conflict = Knowledge(
    observation={"signal": "C"},
    results={"X", "Y"},
    history_count=2,
)

assert unknown.unknown
assert stable.stable
assert conflict.conflict

print("UNKNOWN: REPRESENTABLE")
print("STABLE: REPRESENTABLE")
print("CONFLICT: REPRESENTABLE")

print("HOLD: UNRESOLVED")
print("NO DESIGN CHANGE")
