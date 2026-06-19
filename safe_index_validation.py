"""SAFE mirror — index_validation.py; the index is range-checked before use. Expect 0."""
from flask import Flask, request

app = Flask(__name__)
ACCOUNTS = [{"id": 0}, {"id": 1}, {"id": 2}]


@app.route("/account")
def account():
    i = int(request.args.get("i", "0"))
    if not 0 <= i < len(ACCOUNTS):         # bounds-checked
        return "not found", 404
    return ACCOUNTS[i]
