import csv
from pathlib import Path

path = Path(__file__).with_name("_course_output.csv")
fieldnames = ["month", "kwh"]
measurements = [
    {"month": "January", "kwh": 820},
    {"month": "February", "kwh": 760},
    {"month": "March", "kwh": 640},
]

try:
    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(measurements)

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row["month"], row["kwh"])
finally:
    if path.exists():
        path.unlink()
