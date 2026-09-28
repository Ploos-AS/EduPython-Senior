from pathlib import Path

path = Path(__file__).with_name("temperatures.txt")
total = 0
count = 0

with open(path, "r", encoding="utf-8") as file:
    for line in file:
        value = int(line.strip())
        print("Temperature:", value)
        total = total + value
        count = count + 1

print("Count:", count)
print("Total:", total)
