"""Combinations #6/#7/#8 — SANITIZER × SSRF (CWE-918, Python)."""
import requests
from markupsafe import escape
from urllib.parse import urlparse
from flask import Flask, request

app = Flask(__name__)
ALLOWED = {"api.internal.example.com"}


def escape_html(s):
    return escape(str(s))


def sanitize_url(u):
    return u


def checked_url(u):
    host = urlparse(u).hostname
    if host not in ALLOWED:
        raise ValueError("host not allowed")
    return u


@app.route("/wrong")
def wrong():
    u = escape_html(request.args.get("url", ""))  # wrong-context for SSRF
    requests.get(str(u))  # CWE-918


@app.route("/fake")
def fake():
    u = sanitize_url(request.args.get("url", ""))
    requests.get(u)  # CWE-918


@app.route("/wrapped")
def wrapped():
    u = checked_url(request.args.get("url", ""))
    requests.get(u)  # expect 0 (#8 custom wrapper)

