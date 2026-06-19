"""Combination #13 — ENCODED PAYLOAD × SSTI (CWE-1336, Python)."""
import base64
from urllib.parse import unquote
from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    name = base64.b64decode(raw).decode()
    render_template_string("<p>" + name + "</p>")  # CWE-1336


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    name = unquote(raw)
    render_template_string("<p>" + name + "</p>")  # CWE-1336

