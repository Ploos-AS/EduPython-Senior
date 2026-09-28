from pathlib import Path

missing_path = Path(__file__).with_name("_this_file_should_not_exist.txt")

try:
    with open(missing_path, "r", encoding="utf-8") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("Expected: practice file was not found.")
