# Python workspace reorganized

This workspace has been reorganized into topic-based folders so the Python examples, package exercises, and notes are easier to browse.

## Structure

- basics/: foundational scripts and simple exercises
- functions/: function-related examples, decorators, and higher-order functions
- oop/: object-oriented examples and class exercises
- games/: game scripts and small demos
- packages/: package and module examples; this is also the package root used by the import helper
- docs/: notes, markdown files, and generated HTML content

## Runtime folders kept at the root

The local Python installation directories remain at the workspace root and should be treated as runtime infrastructure:

- DLLs/
- Lib/
- Scripts/
- include/
- tcl/
- Python tool/
- Python-base/

## Import note

A startup helper named sitecustomize.py is placed at the workspace root. When Python starts from this workspace, it adds the workspace root and the package folders to sys.path so imports such as packages.mypackage continue to work after the reorganization.
