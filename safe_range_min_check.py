"""SAFE mirror — range_min_check.py; both lower and upper bounds are enforced. Expect 0."""
from flask import Flask, request

app = Flask(__name__)
RECORDS = ["public-a", "public-b", "secret-tail"]


@app.route("/record")
def record():
    try:
        i = int(request.args.get("i", "0"))
    except ValueError:
        return "bad index", 400
    if i < 0 or i >= len(RECORDS):          # both bounds enforced
        return "out of range", 400
    return RECORDS[i]
