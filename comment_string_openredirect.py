"""Combination #9 — COMMENT / STRING-LITERAL × OPEN REDIRECT (CWE-601, Python). Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    n = request.args.get("next", "")
    # redirect(n)  # commented
    example = "redirect(next)"
    return str(len(example) + len(n))

