"""Cross-file taint — SINK side (open redirect). Imported by
xf_openredirect_controller.py."""
from flask import redirect


def go(url: str):
    # SINK: `url` arrives tainted across the file boundary → open redirect (CWE-601)
    return redirect(url)
