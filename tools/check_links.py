from pathlib import Path
import re

ROOTS = [Path("README.md"), Path("README.en.md"), Path("ROADMAP.md"), Path("content"), Path("docs")]
files = []
for root in ROOTS:
    if root.is_file():
        files.append(root)
    elif root.is_dir():
        files.extend(root.rglob("*.md"))

if not files:
    raise SystemExit("No Markdown content found")

errors = []
link_re = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

for path in sorted(files):
    text = path.read_text(encoding="utf-8")

    if "\x00" in text:
        errors.append(f"{path}: contains NUL byte")

    for match in link_re.finditer(text):
        target = match.group(1).strip()
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = target.split("#", 1)[0].split("?", 1)[0]
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(Path.cwd().resolve())
        except ValueError:
            errors.append(f"{path}: local link escapes repository: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{path}: broken local link: {target}")

if errors:
    raise SystemExit("\n".join(errors))

print(f"OK: content/link checks passed for {len(files)} Markdown file(s)")
