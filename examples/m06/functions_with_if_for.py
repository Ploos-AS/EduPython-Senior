def temperature_message(temperature):
    if temperature < 0:
        return "Below zero"
    elif temperature < 20:
        return "From 0 to below 20"
    else:
        return "20 or above"

temperatures = [-5, 4, 18, 23]

for temperature in temperatures:
    message = temperature_message(temperature)
    print(temperature, ":", message)
