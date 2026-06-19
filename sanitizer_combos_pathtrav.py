"""Combinations #6/#7/#8 — SANITIZER × PATH TRAVERSAL (CWE-22, Python).
#8 wrapped route is in safe_sanitizer_wrapped_pathtrav.py (basename confuses this file — #77)."""
import os
from flask import Flask, request

app = Flask(__name__)
BASE = "/srv/app/data/"


def strip_html(s):
    return s.replace("<", "").replace(">", "")  # wrong-context — useless for paths


def sanitize_name(s):
    return s


@app.route("/wrong")
def wrong():
    name = strip_html(request.args.get("name", ""))
    open(BASE + name)  # CWE-22


@app.route("/fake")
def fake():
    name = sanitize_name(request.args.get("name", ""))
    open(BASE + name)  # CWE-22
