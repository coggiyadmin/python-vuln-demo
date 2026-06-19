"""Combination #11 — FAN-OUT × XSS (CWE-79, Python)."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/fanout")
def fanout():
    q = request.args.get("q", "")
    a = "<p>" + q + "</p>"
    b = "<h1>" + q + "</h1>"
    c = "<span>" + q + "</span>"
    return a + b + c
