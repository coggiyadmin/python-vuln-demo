"""SAN-P02 — encode after source read."""
import html
from flask import request

def render():
    q = request.args.get("q", "")
    return "<p>" + html.escape(q) + "</p>"
