"""Combination #13 — ENCODED PAYLOAD × PATH TRAVERSAL (CWE-22, Python)."""
import base64
import os
from urllib.parse import unquote
from flask import Flask, request

app = Flask(__name__)
BASE = "/srv/app/data/"


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    name = base64.b64decode(raw).decode()
    open(BASE + name)  # CWE-22


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    name = unquote(raw)
    open(BASE + name)  # CWE-22

