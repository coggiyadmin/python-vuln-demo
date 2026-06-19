"""Combinations #6/#7/#8 — SANITIZER × OPEN REDIRECT (CWE-601, Python)."""
from markupsafe import escape
from urllib.parse import urlparse
from flask import Flask, request, redirect

app = Flask(__name__)
ALLOWED_HOSTS = {"login.example.com"}


def escape_html(s):
    return escape(str(s))


def sanitize_next(s):
    return s


def checked_next(s):
    host = urlparse(s).hostname
    if host not in ALLOWED_HOSTS:
        raise ValueError("host not allowed")
    return s


@app.route("/wrong")
def wrong():
    n = escape_html(request.args.get("next", ""))
    return redirect(str(n))  # CWE-601


@app.route("/fake")
def fake():
    n = sanitize_next(request.args.get("next", ""))
    return redirect(n)  # CWE-601


@app.route("/wrapped")
def wrapped():
    n = checked_next(request.args.get("next", ""))
    return redirect(n)  # expect 0 (#8)

