from pathlib import Path


def read_measurements(file_path):
    measurements = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            measurements.append(int(line.strip()))
    return measurements


def calculate_total(measurements):
    total = 0
    for measurement in measurements:
        total = total + measurement
    return total


def write_result(file_path, total):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Total: " + str(total) + "\n")


program_folder = Path(__file__).parent
input_file = program_folder / "data" / "measurements.txt"
output_file = program_folder / "_course_result.txt"

try:
    measurements = read_measurements(input_file)
    total = calculate_total(measurements)
    write_result(output_file, total)

    with open(output_file, "r", encoding="utf-8") as file:
        saved_result = file.read().strip()

    print("Measurements:", measurements)
    print(saved_result)
finally:
    if output_file.exists():
        output_file.unlink()
