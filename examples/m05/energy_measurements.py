total_kwh = 0

for day in range(1, 4):
    print("Day", day)
    kwh = float(input("Usage in kWh: "))

    total_kwh = total_kwh + kwh

    if kwh > 20:
        print("Usage was above 20 kWh on this day.")
    else:
        print("Usage was 20 kWh or lower on this day.")

print("Total usage:", total_kwh, "kWh")
