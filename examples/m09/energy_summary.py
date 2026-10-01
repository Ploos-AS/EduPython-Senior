import csv
from pathlib import Path

path = Path(__file__).with_name("energy.csv")
values = []

with open(path, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        kwh = int(row["kwh"])
        values.append(kwh)

count = len(values)
total = sum(values)
lowest = min(values)
highest = max(values)
average = total / count

print("Count:", count)
print("Total:", total, "kWh")
print("Minimum:", lowest, "kWh")
print("Maximum:", highest, "kWh")
print("Average:", average, "kWh")
