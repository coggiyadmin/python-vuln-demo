"""Combinations #6/#7/#8 — SANITIZER × SSTI (CWE-1336, Python)."""
from markupsafe import escape
from flask import Flask, request, render_template_string

app = Flask(__name__)


def escape_html(s):
    return escape(str(s))


def sanitize_name(s):
    return s


@app.route("/wrong")
def wrong():
    name = escape_html(request.args.get("name", ""))
    render_template_string("<p>Hello " + str(name) + "</p>")  # CWE-1336


@app.route("/fake")
def fake():
    name = sanitize_name(request.args.get("name", ""))
    render_template_string("<p>Hello " + name + "</p>")  # CWE-1336


@app.route("/wrapped")
def wrapped():
    name = request.args.get("name", "")
    render_template_string("<p>Hello {{ name }}</p>", name=name)  # expect 0 (#8)

