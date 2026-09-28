temperature = float(input("Temperature: "))

if temperature < 0:
    message = "Below zero"
elif temperature >= 0 and temperature < 10:
    message = "Cool"
elif temperature >= 10 and temperature < 20:
    message = "Mild"
else:
    message = "20 or above"

print("Assessment:")
print(message)
