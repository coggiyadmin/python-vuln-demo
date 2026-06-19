"""SAFE mirror — user_regex.py; the pattern is a fixed server-side constant and only the
text is user-supplied. Expect 0 security findings."""
import re
from flask import Flask, request

app = Flask(__name__)
ALLOWED = re.compile(r"^[a-z0-9_]{1,32}$")   # fixed, linear-time pattern


@app.route("/match")
def match():
    text = request.args.get("t", "")
    return str(bool(ALLOWED.match(text)))
