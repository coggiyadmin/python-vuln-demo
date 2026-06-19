"""Combination #9 — COMMENT / STRING × XSS (CWE-79, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    q = request.args.get("q", "")
    example = "<p>" + q + "</p>"  # string building doc only
    return str(len(example))
