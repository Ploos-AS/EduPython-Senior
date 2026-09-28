from pathlib import Path

log_path = Path(__file__).with_name("_course_log.txt")


def add_log(message):
    with open(log_path, "a", encoding="utf-8") as file:
        file.write(message + "\n")


try:
    with open(log_path, "w", encoding="utf-8") as file:
        file.write("Start\n")

    add_log("Check completed")
    add_log("Finished")

    with open(log_path, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())
finally:
    if log_path.exists():
        log_path.unlink()
