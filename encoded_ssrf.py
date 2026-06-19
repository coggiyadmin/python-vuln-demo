"""Combination #13 — ENCODED PAYLOAD × SSRF (CWE-918, Python)."""
import base64
import requests
from urllib.parse import unquote
from flask import Flask, request

app = Flask(__name__)


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    u = base64.b64decode(raw).decode()
    requests.get(u)  # CWE-918


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    u = unquote(raw)
    requests.get(u)  # CWE-918

