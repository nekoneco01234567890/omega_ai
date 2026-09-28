from pathlib import Path

print("=== WORLD MODEL HYPOTHESIS TRACE AUDIT ===")

root = Path(".")

targets = [
    "world_model.py",
    "world_model_v2_code_map.py",
    "reasoner.py",
    "reasoner_v2_code_map.py",
    "intelligence_core.py",
    "learner_v1_code_map.py",
    "planner_v1_code_map.py",
    "code_map.py",
    "PHASE1_INTELLIGENCE_CORE_v1.0.md",
]

keywords = [
    "hypothesis",
    "hypotheses",
    "HYPOTHESIS",
    "new_hypothesis",
]

print()
print("=== TARGET FILE TRACE ===")

for name in targets:
    path = root / name

    if not path.exists():
        print(f"{name}: MISSING")
        continue

    hits = []

    for i, line in enumerate(
        path.read_text(errors="replace").splitlines(),
        start=1,
    ):
        if any(k in line for k in keywords):
            hits.append((i, line.strip()))

    print()
    print(f"[{name}]")
    if not hits:
        print("  NO_HYPOTHESIS_REFERENCE")
    else:
        for line_no, line in hits:
            print(f"  L{line_no}: {line}")

print()
print("=== REPOSITORY IMPLEMENTATION TRACE ===")

skip_dirs = {
    ".git",
    "__pycache__",
}

found = []

for path in root.rglob("*"):
    if not path.is_file():
        continue

    if any(part in skip_dirs for part in path.parts):
        continue

    if path.name == "world_model_hypothesis_trace_audit.py":
        continue

    try:
        lines = path.read_text(errors="replace").splitlines()
    except Exception:
        continue

    for i, line in enumerate(lines, start=1):
        lower = line.lower()

        if "hypothesis" in lower or "hypotheses" in lower:
            found.append((str(path), i, line.strip()))

for path, line_no, line in found:
    print(f"{path}:L{line_no}: {line}")

print()
print("=== CONCLUSION ===")
print("HYPOTHESIS_TRACE: RECORDED")
print("IMPLEMENTATION_CHANGE: NONE")
print("DESIGN_DECISION: HOLD")
