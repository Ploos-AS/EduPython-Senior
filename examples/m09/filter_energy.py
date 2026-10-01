import csv
from pathlib import Path

path = Path(__file__).with_name("energy.csv")
limit = 700
selected = []

with open(path, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        kwh = int(row["kwh"])

        if kwh >= limit:
            selected.append(row)

for row in selected:
    print(row["month"], row["kwh"], "kWh")
