from pathlib import Path
import subprocess
import sys

files = sorted(Path("examples").rglob("*.py"))
if not files:
    raise SystemExit("No Python examples found")

stdin_by_example = {
    "examples/m03/text_input.py": "Ada\nGrimstad\n",
    "examples/m03/numeric_input.py": "3\n19.95\n",
    "examples/m03/energy_calculator.py": "6\n1.25\n",
    "examples/m04/first_if.py": "-5\n",
    "examples/m04/if_else.py": "0\n",
    "examples/m04/if_elif_else.py": "20\n",
    "examples/m04/logical_operators.py": "15\n",
    "examples/m04/decision_program.py": "10\n",
    "examples/m05/energy_measurements.py": "10\n25\n15\n",
}

for path in files:
    print(f"checking {path}")
    subprocess.run(
        [sys.executable, str(path)],
        input=stdin_by_example.get(path.as_posix(), ""),
        text=True,
        check=True,
        timeout=10,
    )

print(f"OK: {len(files)} example(s)")
