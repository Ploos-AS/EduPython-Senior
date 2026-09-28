def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    return total


expenses = [
    {"description": "Bus", "amount": 45},
    {"description": "Coffee", "amount": 38},
    {"description": "Book", "amount": 249},
]

for expense in expenses:
    print(expense["description"], expense["amount"])

print("Total:", calculate_total(expenses))

expenses.append({"description": "Train", "amount": 120})
print("Entries:", len(expenses))
print("New total:", calculate_total(expenses))
