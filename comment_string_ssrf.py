"""Combination #9 — COMMENT / STRING-LITERAL × SSRF (CWE-918, Python). Expect 0 findings."""
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/x")
def x():
    url = request.args.get("url", "")
    # requests.get(url)  # commented sink — must not fire
    example = "requests.get(url)"  # string literal
    return str(len(example) + len(url))

