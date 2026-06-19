"""Combination #3 — LOOP-CARRIED × XSS (CWE-79, Python)."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/loop")
def loop():
    parts = []
    for item in request.args.getlist("q"):
        parts.append("<span>" + item + "</span>")  # CWE-79
    return "".join(parts)
