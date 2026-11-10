from pathlib import Path
import shutil
import re

ROOT = Path(r"C:\Python")
PKG_ROOT = ROOT / "packages"
MPKG = PKG_ROOT / "mypackage"

def backup(p: Path):
    bak = p.with_suffix(p.suffix + ".bak")
    if not bak.exists():
        shutil.copy2(p, bak)

def replace_patterns_in_file(p: Path, patterns):
    text = p.read_text(encoding="utf-8")
    new = text
    for pat, repl in patterns:
        new = re.sub(pat, repl, new, flags=re.M)
    if new != text:
        backup(p)
        p.write_text(new, encoding="utf-8")
        print("Patched:", p)

# Fix packages/module_test.py
top_patterns = [
    (r'(?m)^\s*import\s+private\s*$', 'from packages.mypackage import private'),
]
if PKG_ROOT.exists():
    for py in PKG_ROOT.glob("*.py"):
        replace_patterns_in_file(py, top_patterns)

# Fix packages/mypackage modules
if MPKG.exists():
    patterns = []

    # remove problematic sys.path.append lines
    patterns.append((r'(?m)^\s*sys\.path\.append\([^\)]*\)\s*$', '# sys.path.append removed by reorganizer'))

    # convert import forms to package-safe forms
    patterns.append((r'(?m)^\s*import\s+private\s*$', 'from . import private'))
    patterns.append((r'(?m)^\s*import\s+module_test\s*$', 'from .. import module_test'))
    patterns.append((r'(?m)^\s*from\s+animal\s+import\s', 'from .animal import '))
    patterns.append((r'(?m)^\s*from\s+class_object\s+import\s', 'from .class_object import '))

    # remove print(sys.path)
    patterns.append((r'(?m)^\s*print\(sys\.path\)\s*$', '# print(sys.path) removed by reorganizer'))

    for py in MPKG.rglob("*.py"):
        if py.name == "__init__.py":
            continue
        replace_patterns_in_file(py, patterns)

print("Done. Backups saved as *.bak where files were changed.")