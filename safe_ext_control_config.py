"""SAFE mirror — ext_control_config.py; only an allow-listed setting may be changed. Expect 0."""
import os
from flask import Flask, request

app = Flask(__name__)
ALLOWED = {"locale", "theme"}


@app.route("/config")
def config():
    key = request.args.get("k", "")
    if key not in ALLOWED:                  # allow-listed keys only
        return "forbidden key", 400
    os.environ["APP_" + key] = request.args.get("v", "")
    return "ok"
