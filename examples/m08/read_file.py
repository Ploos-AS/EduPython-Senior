from pathlib import Path

sample_path = Path(__file__).with_name("sample.txt")

with open(sample_path, "r", encoding="utf-8") as file:
    content = file.read()

print(content)
