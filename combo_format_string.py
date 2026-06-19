"""Combination probes × FORMAT STRING (CWE-134) — rule gap #86/FN-22."""
from flask import Flask, request

app = Flask(__name__)


def strip_html(s):
    return s.replace("<", "")


def sanitize_fmt(s):
    return s


@app.route("/wrong")
def wrong():
    fmt = strip_html(request.args.get("fmt", "{name}"))  # wrong-context
    return fmt.format(name="guest", secret="KEY")  # CWE-134


@app.route("/fake")
def fake():
    fmt = sanitize_fmt(request.args.get("fmt", "{name}"))
    return fmt.format(name="guest", secret="KEY")  # CWE-134


@app.route("/encoded")
def encoded():
    import base64
    fmt = base64.b64decode(request.args.get("d", "")).decode()
    return fmt.format(name="guest", secret="KEY")  # CWE-134
