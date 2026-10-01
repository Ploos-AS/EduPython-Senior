import csv
from pathlib import Path


def read_measurements(path):
    measurements = []

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            month = row["month"]
            text = row["kwh"].strip()

            if text == "":
                print("Skipped", month, "- missing value")
                continue

            try:
                kwh = int(text)
            except ValueError:
                print("Skipped", month, "- invalid number:", text)
                continue

            measurements.append({"month": month, "kwh": kwh})

    return measurements


def print_report(measurements, limit):
    if len(measurements) == 0:
        print("No valid measurements")
        return

    values = []

    for measurement in measurements:
        values.append(measurement["kwh"])

    print("Valid measurements:", len(measurements))
    print("Total:", sum(values), "kWh")
    print("Minimum:", min(values), "kWh")
    print("Maximum:", max(values), "kWh")
    print("Average:", sum(values) / len(values), "kWh")
    print("At least", limit, "kWh:")

    for measurement in measurements:
        if measurement["kwh"] >= limit:
            print("-", measurement["month"], measurement["kwh"], "kWh")


path = Path(__file__).with_name("energy_report.csv")
measurements = read_measurements(path)
print_report(measurements, 700)
