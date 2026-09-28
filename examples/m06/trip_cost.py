def calculate_cost(kilometres, price_per_km):
    return kilometres * price_per_km


def show_result(kilometres, cost):
    print("Distance:", kilometres, "km")
    print("Cost:", cost)


kilometres = 120
price_per_km = 1.50

cost = calculate_cost(kilometres, price_per_km)
show_result(kilometres, cost)
