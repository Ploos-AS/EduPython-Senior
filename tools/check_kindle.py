from pathlib import Path
from zipfile import ZipFile
import sys

if len(sys.argv) < 2:
    raise SystemExit("usage: check_kindle.py EPUB...")

for name in sys.argv[1:]:
    path = Path(name)
    if not path.is_file() or path.stat().st_size == 0:
        raise SystemExit(f"Missing or empty EPUB: {path}")
    with ZipFile(path) as z:
        names = set(z.namelist())
        if "mimetype" not in names:
            raise SystemExit(f"{path}: missing mimetype")
        if z.read("mimetype") != b"application/epub+zip":
            raise SystemExit(f"{path}: invalid EPUB mimetype")
        if "META-INF/container.xml" not in names:
            raise SystemExit(f"{path}: missing META-INF/container.xml")
        html = [n for n in names if n.lower().endswith((".xhtml", ".html"))]
        if not html:
            raise SystemExit(f"{path}: no readable HTML/XHTML content")
    print(f"Kindle profile OK: {path}")
