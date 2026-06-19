"""Combination #13 — ENCODED PAYLOAD × LOG INJECTION (CWE-117, Python)."""
import base64
import logging
from urllib.parse import unquote
from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger("combo")


@app.route("/b64")
def b64():
    raw = request.args.get("d", "")
    actor = base64.b64decode(raw).decode()
    log.info("actor " + actor)  # CWE-117


@app.route("/url")
def url():
    raw = request.args.get("d", "")
    actor = unquote(raw)
    log.info("actor " + actor)  # CWE-117

