"""Cross-file taint — SINK side (SSTI). Imported by xf_ssti_controller.py."""
from flask import render_template_string


def render(name: str):
    # SINK: `name` arrives tainted across the file boundary → SSTI (CWE-1336)
    return render_template_string("<p>Hello " + name + "</p>")
