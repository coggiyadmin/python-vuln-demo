"""Combinations #6/#7/#8 — SANITIZER × DESERIALIZATION (CWE-502, Python)."""
import base64
import json
import pickle
from markupsafe import escape
from flask import Flask, request

app = Flask(__name__)


def escape_html(s):
    return escape(str(s))


def sanitize_blob(s):
    return s


@app.route("/wrong")
def wrong():
    blob = escape_html(request.args.get("s", ""))
    pickle.loads(base64.b64decode(str(blob)))  # CWE-502


@app.route("/fake")
def fake():
    blob = sanitize_blob(request.args.get("s", ""))
    pickle.loads(base64.b64decode(blob))  # CWE-502


@app.route("/wrapped")
def wrapped():
    blob = request.args.get("s", "")
    json.loads(base64.b64decode(blob))  # expect 0 (#8 — json not pickle)

