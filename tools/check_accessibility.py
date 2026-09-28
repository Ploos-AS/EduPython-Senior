from pathlib import Path
import re

files = sorted(Path("content").rglob("*.md"))
if not files:
    raise SystemExit("No course Markdown found")

errors = []
for path in files:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Images with an empty alt text are not accepted in course content.
    for n, line in enumerate(lines, 1):
        if re.search(r"!\[\]\(", line):
            errors.append(f"{path}:{n}: image has empty alt text")

    # Avoid web-position-only instructions that do not survive book output.
    for n, line in enumerate(lines, 1):
        low = line.lower()
        if any(p in low for p in ("knappen over", "knappen under", "button above", "button below")):
            errors.append(f"{path}:{n}: web-position-dependent instruction")

if errors:
    raise SystemExit("\n".join(errors))

print(f"OK: accessibility structure checked in {len(files)} course file(s)")
