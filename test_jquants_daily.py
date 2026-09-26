import os
import csv
import json
import urllib.request
from datetime import datetime

API_KEY = os.environ.get("JQUANTS_API_KEY")
CODE = "7203"
FROM = "20260301"
TO = "20260331"
OUT = "7203_202603_daily.csv"

if not API_KEY:
    raise SystemExit("ERROR: JQUANTS_API_KEY is not set")

url = (
    "https://api.jquants.com/v2/equities/bars/daily"
    f"?code={CODE}&from={FROM}&to={TO}"
)

req = urllib.request.Request(
    url,
    headers={"x-api-key": API_KEY}
)

with urllib.request.urlopen(req) as response:
    data = json.load(response)["data"]

if not data:
    raise SystemExit("ERROR: no data")

fields = [
    "Date",
    "Code",
    "AdjO",
    "AdjH",
    "AdjL",
    "AdjC",
    "AdjVo",
]

with open(OUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()

    for row in data:
        writer.writerow({k: row.get(k) for k in fields})

dates = [row["Date"] for row in data]
codes = [row["Code"] for row in data]

print("=== RESULT ===")
print(f"rows       = {len(data)}")
print(f"first_date = {min(dates)}")
print(f"last_date  = {max(dates)}")
print(f"codes      = {sorted(set(codes))}")
print(f"duplicates = {len(dates) - len(set(dates))}")
print(f"output     = {OUT}")

required = ["AdjO", "AdjH", "AdjL", "AdjC", "AdjVo"]

missing = 0
for row in data:
    for key in required:
        if row.get(key) is None:
            missing += 1

print(f"missing_required_fields = {missing}")

if (
    len(data) > 0
    and len(dates) == len(set(dates))
    and missing == 0
):
    print("PASS")
else:
    print("FAIL")
