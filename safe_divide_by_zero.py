"""SAFE mirror — divide_by_zero.py; the divisor is checked for zero. Expect 0 findings."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/average")
def average():
    total = 1000
    n = int(request.args.get("n", "0"))
    if n == 0:                             # guarded
        return "n must be non-zero", 400
    return str(total / n)
