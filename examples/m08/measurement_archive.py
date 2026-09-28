from pathlib import Path


def read_measurements(file_path):
    measurements = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            measurements.append(int(line.strip()))
    return measurements


def add_measurement(file_path, value):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(str(value) + "\n")


def calculate_total(measurements):
    total = 0
    for measurement in measurements:
        total = total + measurement
    return total


def write_report(file_path, count, total):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Number of measurements: " + str(count) + "\n")
        file.write("Total: " + str(total) + "\n")


program_folder = Path(__file__).parent
source_file = program_folder / "data" / "measurements.txt"
working_file = program_folder / "_course_measurements.txt"
report_file = program_folder / "_course_report.txt"

try:
    with open(source_file, "r", encoding="utf-8") as source:
        with open(working_file, "w", encoding="utf-8") as target:
            target.write(source.read())

    add_measurement(working_file, 13)
    measurements = read_measurements(working_file)
    total = calculate_total(measurements)
    write_report(report_file, len(measurements), total)

    with open(report_file, "r", encoding="utf-8") as file:
        print(file.read().strip())
finally:
    if working_file.exists():
        working_file.unlink()
    if report_file.exists():
        report_file.unlink()
