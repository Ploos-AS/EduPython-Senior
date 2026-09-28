temperature = float(input("Temperature: "))

if temperature < 0:
    print("Below zero.")
elif temperature < 20:
    print("From 0 to below 20.")
else:
    print("20 or above.")
