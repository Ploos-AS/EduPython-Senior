import csv
from pathlib import Path

path = Path(__file__).with_name("energy_with_errors.csv")
valid_values = []

with open(path, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        month = row["month"]
        text = row["kwh"].strip()

        if text == "":
            print(month, ": missing value")
            continue

        try:
            kwh = int(text)
        except ValueError:
            print(month, ": invalid number:", text)
            continue

        valid_values.append(kwh)
        print(month, ":", kwh, "kWh")

print("Valid values:", len(valid_values))
