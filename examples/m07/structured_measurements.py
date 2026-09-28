def calculate_total(measurements):
    total = 0
    for measurement in measurements:
        total = total + measurement["kwh"]
    return total


measurements = [
    {"day": "Monday", "kwh": 12.4},
    {"day": "Tuesday", "kwh": 10.8},
    {"day": "Wednesday", "kwh": 13.1},
]

for measurement in measurements:
    print(measurement["day"], measurement["kwh"])

print("Total:", calculate_total(measurements))

new_measurement = {"day": "Thursday", "kwh": 11.7}
measurements.append(new_measurement)
print("Entries:", len(measurements))
