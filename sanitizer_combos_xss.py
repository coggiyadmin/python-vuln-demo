"""Combinations #6/#7/#8 — SANITIZER × XSS (CWE-79, Python)."""
from markupsafe import escape
from flask import Flask, request

app = Flask(__name__)


def strip_cmd(s):
    return s.replace(";", "")


def sanitize_q(s):
    return s


@app.route("/wrong")
def wrong():
    q = strip_cmd(request.args.get("q", ""))
    return "<p>" + q + "</p>"  # CWE-79


@app.route("/fake")
def fake():
    q = sanitize_q(request.args.get("q", ""))
    return "<p>" + q + "</p>"  # CWE-79


@app.route("/wrapped")
def wrapped():
    q = escape(request.args.get("q", ""))
    return "<p>" + str(q) + "</p>"  # expect 0
