from pathlib import Path
import ast

TARGET = Path("world_model.py")

print("=== WORLD MODEL PRODUCTION DEPENDENCY AUDIT ===")

production_files = [
    "core.py",
    "engine.py",
    "reasoner.py",
    "runtime.py",
    "observation.py",
    "state.py",
    "store.py",
    "state_store.py",
    "event_journal.py",
    "learner_v1_code_map.py",
    "planner_v1_code_map.py",
    "world_model_v2_code_map.py",
    "reasoner_v2_code_map.py",
]

axes = [
    "time",
    "condition",
    "state",
    "scope",
    "source",
    "evidence",
]

print("\n=== DIRECT AXIS DEPENDENCIES ===")

for axis in axes:
    found = []

    for filename in production_files:
        path = Path(filename)

        if not path.exists():
            continue

        text = path.read_text(errors="replace")

        for lineno, line in enumerate(text.splitlines(), 1):
            stripped = line.strip()

            if axis in stripped.lower():
                found.append(
                    f"{filename}:{lineno}: {stripped}"
                )

    print(f"\n[{axis}]")

    if found:
        for item in found:
            print(" ", item)
    else:
        print("  NO_PRODUCTION_REFERENCE")

print("\n=== WORLD MODEL PUBLIC INTERFACE ===")

tree = ast.parse(TARGET.read_text())

for node in tree.body:
    if isinstance(node, ast.ClassDef):
        print(f"CLASS: {node.name}")

        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                print(f"  METHOD: {item.name}")

                args = [
                    arg.arg
                    for arg in item.args.args
                ]

                if args:
                    print(f"    ARGS: {args}")

print("\n=== CURRENT KNOWLEDGE CONTRACT ===")

for node in tree.body:
    if isinstance(node, ast.ClassDef) and node.name == "Knowledge":
        for item in node.body:
            if isinstance(item, ast.AnnAssign):
                if isinstance(item.target, ast.Name):
                    print("FIELD:", item.target.id)

            if isinstance(item, ast.FunctionDef):
                print("PROPERTY/METHOD:", item.name)

print("\n=== CONCLUSION ===")
print("PRODUCTION_DEPENDENCY_SCAN: COMPLETE")
print("AXIS_REQUIREMENT: NOT_AUTO_PROMOTED")
print("WORLD_MODEL_CHANGE: NONE")
