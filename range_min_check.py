"""CWE-839 — Numeric Range Comparison Without Minimum Check. The index is checked against the
upper bound only, so a negative index wraps to the tail of the list. NO finding = FN."""
from flask import Flask, request

app = Flask(__name__)
RECORDS = ["public-a", "public-b", "secret-tail"]


@app.route("/record")
def record():
    i = int(request.args.get("i", "0"))    # SOURCE
    if i < len(RECORDS):                    # upper-bound only, NO i >= 0 check → CWE-839
        return RECORDS[i]                   # i=-1 leaks the last (secret) element
    return "out of range", 400
