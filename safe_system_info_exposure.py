"""SAFE mirror — system_info_exposure.py; returns only a static health status, no system
details. Expect 0 security findings."""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/debug")
def debug():
    return jsonify({"status": "ok"})       # no system/env information disclosed
