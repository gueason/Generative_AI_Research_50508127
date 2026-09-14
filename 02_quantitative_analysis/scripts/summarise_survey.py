"""Summarise the synthetic, de-identified survey example."""

import csv
from pathlib import Path
from statistics import mean


DATA_FILE = Path(__file__).parents[1] / "data" / "2026-09-14_deidentified_survey_sample_v01.csv"


with DATA_FILE.open(encoding="utf-8", newline="") as source:
    rows = list(csv.DictReader(source))

print(f"Responses: {len(rows)}")
print(f"Mean productivity rating: {mean(int(row['productivity_rating']) for row in rows):.2f}")
print(f"Mean inaccuracy concern: {mean(int(row['inaccuracy_concern']) for row in rows):.2f}")

