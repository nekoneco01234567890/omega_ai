from pathlib import Path
import re

ROOT = Path(".")

TARGETS = [
    "time",
    "condition",
    "state",
    "scope",
    "source",
    "evidence",
]

EXCLUDE = {
    ".git",
    "__pycache__",
    "audit_archive",
}

FILES = []
for p in ROOT.glob("*.py"):
    if p.name != Path(__file__).name:
        FILES.append(p)

print("=== WORLD MODEL DOWNSTREAM REQUIREMENT AUDIT ===")

for target in TARGETS:
    print(f"\n[{target}]")
    hits = []

    for path in FILES:
        text = path.read_text(errors="replace")
        lines = text.splitlines()

        for i, line in enumerate(lines, 1):
            if re.search(rf"\b{re.escape(target)}\b", line, re.IGNORECASE):
                hits.append((path.name, i, line.strip()))

    if not hits:
        print("  NO_DIRECT_REFERENCE")
        continue

    for name, line_no, line in hits:
        print(f"  {name}:{line_no}: {line}")

print("\n=== KNOWLEDGE FIELD REFERENCES ===")

patterns = [
    r"\.observation\b",
    r"\.results\b",
    r"\.history_count\b",
    r"\.stable\b",
    r"\.conflict\b",
    r"\.unknown\b",
]

for pattern in patterns:
    print(f"\nPATTERN: {pattern}")
    found = False

    for path in FILES:
        text = path.read_text(errors="replace")
        for i, line in enumerate(text.splitlines(), 1):
            if re.search(pattern, line):
                print(f"  {path.name}:{i}: {line.strip()}")
                found = True

    if not found:
        print("  NONE")

print("\n=== CONCLUSION ===")
print("EXISTING_CODE_EVIDENCE: COLLECTED")
print("HYPOTHETICAL_CASES: NOT_USED")
print("WORLD_MODEL_CHANGE: NONE")
print("NEXT: CLASSIFY_ACTUAL_REQUIREMENTS")
