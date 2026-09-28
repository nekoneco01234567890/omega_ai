from pathlib import Path

print("=== PHASE 2 AUDIT ARTIFACT AUDIT ===")

files = sorted(Path(".").glob("world_model_*audit.py"))
files += sorted(Path(".").glob("hypothesis_*audit.py"))
files = sorted(set(files))

for path in files:
    text = path.read_text(errors="replace")

    print()
    print(f"=== {path.name} ===")

    if "NO DESIGN CHANGE" in text:
        print("DESIGN_CHANGE: NO")
    elif "DESIGN CHANGE" in text:
        print("DESIGN_CHANGE: PRESENT")
    else:
        print("DESIGN_CHANGE: NOT_STATED")

    if "CONCLUSION" in text:
        print("CONCLUSION: PRESENT")
    else:
        print("CONCLUSION: ABSENT")

    if "AUDIT" in text:
        print("AUDIT_MARKER: PRESENT")
    else:
        print("AUDIT_MARKER: ABSENT")

print()
print("=== CURRENT TRACKED STATUS ===")

import subprocess

result = subprocess.run(
    ["git", "status", "--short"],
    capture_output=True,
    text=True,
)

print(result.stdout)

print()
print("=== CONCLUSION ===")
print("ARTIFACT_INVENTORY: COMPLETE")
print("AUTO_DELETE: NO")
print("DESIGN_CHANGE: NONE")
print("NEXT: CLASSIFY_KEEP_ARCHIVE_DISCARD")
