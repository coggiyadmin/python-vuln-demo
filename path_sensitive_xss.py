"""Combination #2 — PATH-SENSITIVITY × XSS (CWE-79, Python)."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/neg")
def neg():
    q = request.args.get("q", "")
    if "<" in q:
        return "<p>" + q + "</p>"  # CWE-79


@app.route("/onebranch")
def onebranch():
    q = request.args.get("q", "")
    if request.args.get("strict"):
        q = q.replace("<", "")
    return "<p>" + q + "</p>"  # CWE-79


@app.route("/early")
def early():
    q = request.args.get("q", "")
    if q == "":
        return "empty"
    return "<p>" + q + "</p>"  # CWE-79
