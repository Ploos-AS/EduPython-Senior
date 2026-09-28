power_watts = 1000
hours = 3
price_per_kwh = 1.20

power_kw = power_watts / 1000
consumption_kwh = power_kw * hours
cost = consumption_kwh * price_per_kwh

print("Consumption in kWh:")
print(consumption_kwh)
print("Cost:")
print(cost)
