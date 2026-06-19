"""Combination #13 — ENCODED PAYLOAD × OPEN REDIRECT (CWE-601, Python)."""
import base64
from urllib.parse import unquote
from flask import Flask, request, redirect

app = Flask(__name__)


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    n = base64.b64decode(raw).decode()
    return redirect(n)  # CWE-601


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    n = unquote(raw)
    return redirect(n)  # CWE-601

