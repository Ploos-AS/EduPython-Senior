from pathlib import Path

path = Path(__file__).with_name("energy.csv")

with open(path, "r", encoding="utf-8") as file:
    print(file.read())
