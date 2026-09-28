from pathlib import Path
import subprocess
import sys

files = sorted(Path("examples").rglob("*.py"))
if not files:
    raise SystemExit("No Python examples found")

for path in files:
    print(f"checking {path}")
    subprocess.run([sys.executable, str(path)], check=True)

print(f"OK: {len(files)} example(s)")
