from pathlib import Path

required = [
    Path("README.md"),
    Path("README.en.md"),
    Path("ROADMAP.md"),
    Path("content/no"),
    Path("content/en"),
]
missing = [str(p) for p in required if not p.exists()]
if missing:
    raise SystemExit("Missing required paths: " + ", ".join(missing))

print("OK: bilingual course structure present")
