"""Cross-file taint — SINK side (path traversal). Imported by
xf_pathtrav_controller.py."""

BASE = "/srv/app/data/"


def read_file(name: str):
    # SINK: `name` arrives tainted across the file boundary → path traversal (CWE-22)
    return open(BASE + name).read()
