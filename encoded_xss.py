"""Combination #13 — ENCODED × XSS (CWE-79, Python)."""
import base64
from urllib.parse import unquote
from flask import Flask, request

app = Flask(__name__)


@app.route("/b64")
def b64():
    q = base64.b64decode(request.args.get("d", "")).decode()
    return "<p>" + q + "</p>"  # CWE-79


@app.route("/url")
def url():
    q = unquote(request.args.get("d", ""))
    return "<p>" + q + "</p>"  # CWE-79
