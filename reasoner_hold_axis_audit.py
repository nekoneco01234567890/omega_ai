print("=== REASONER HOLD AXIS AUDIT ===")

axes = {
    "EVIDENCE_QUALITY": "根拠そのものの質が違う",
    "TIME": "古い観測と現在の観測で適用可能性が違う",
    "CONDITION": "観測時と現在で条件が違う",
    "SCOPE": "観測対象と判断対象の範囲が違う",
    "SAMPLE": "観測回数が少なく代表性が不明",
    "DEPENDENCE": "複数観測が独立していない",
}

for name, description in axes.items():
    print(f"{name}: {description}")

print()
print("CURRENT_KNOWLEDGE_FIELDS:")
print("  observation")
print("  results")
print("  history_count")

print()
print("AXIS_REPRESENTATION:")

represented = {
    "EVIDENCE_QUALITY": False,
    "TIME": False,
    "CONDITION": False,
    "SCOPE": False,
    "SAMPLE": "PARTIAL",
    "DEPENDENCE": False,
}

for name, value in represented.items():
    print(f"{name}: {value}")

print()
print("CONCLUSION:")
print("HOLD_CAUSES: MULTIPLE_POSSIBLE_AXES")
print("SINGLE_CAUSE_NOT_CONFIRMED")
print("WORLD_MODEL_CHANGE: NOT_YET_JUSTIFIED")
print("NEXT: TEST_MINIMAL_DISTINGUISHING_INFORMATION")
