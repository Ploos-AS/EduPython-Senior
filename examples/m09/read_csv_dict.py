import csv
from pathlib import Path

path = Path(__file__).with_name("energy.csv")

with open(path, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["month"], ":", row["kwh"], "kWh")
