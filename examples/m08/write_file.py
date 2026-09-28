from pathlib import Path

output_path = Path(__file__).with_name("_course_output.txt")

try:
    places = ["Tonstad", "Grimstad", "Oslo"]

    with open(output_path, "w", encoding="utf-8") as file:
        for place in places:
            file.write(place + "\n")

    with open(output_path, "r", encoding="utf-8") as file:
        content = file.read()

    print(content)
finally:
    if output_path.exists():
        output_path.unlink()
