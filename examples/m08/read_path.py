from pathlib import Path

program_folder = Path(__file__).parent
file_path = program_folder / "data" / "places.txt"

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
