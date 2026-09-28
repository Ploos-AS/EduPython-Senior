from pathlib import Path
import sys

if len(sys.argv) != 2 or sys.argv[1] not in {"no", "en"}:
    raise SystemExit("usage: book_inputs.py no|en")

lang = sys.argv[1]
manifest = Path("book") / f"{lang}.txt"
paths = []
for raw in manifest.read_text(encoding="utf-8").splitlines():
    raw = raw.strip()
    if not raw or raw.startswith("#"):
        continue
    path = Path(raw)
    if not path.is_file():
        raise SystemExit(f"Missing book input: {path}")
    paths.append(str(path))

if not paths:
    raise SystemExit(f"Empty book manifest: {manifest}")

print(" ".join(paths))
