"""Combination #13 — ENCODED PAYLOAD × DESERIALIZE (CWE-502, Python)."""
import base64
import pickle
from urllib.parse import unquote
from flask import Flask, request

app = Flask(__name__)


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    blob = base64.b64decode(raw)
    pickle.loads(blob)  # CWE-502


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    blob = unquote(raw).encode()
    pickle.loads(blob)  # CWE-502

