import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

for candidate in (
    ROOT,
    ROOT / "packages",
    ROOT / "basics",
    ROOT / "functions",
    ROOT / "oop",
    ROOT / "games",
):
    if candidate.exists() and str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))
