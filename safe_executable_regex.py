"""SAFE mirror — executable_regex.py; a fixed server-side pattern; only a count is returned."""
import re
from flask import Flask, request

app = Flask(__name__)
DIGITS = re.compile(r"\d")


@app.route("/redact")
def redact():
    text = request.args.get("t", "")
    return str(len(DIGITS.findall(text)))  # static pattern; no user text reflected
