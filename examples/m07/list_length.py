days = ["Monday", "Tuesday", "Wednesday"]

print("Count:", len(days))

if len(days) > 0:
    last_index = len(days) - 1
    print("Last index:", last_index)
    print("Last item:", days[last_index])

empty = []
if len(empty) > 0:
    print(empty[len(empty) - 1])
else:
    print("The list is empty.")
