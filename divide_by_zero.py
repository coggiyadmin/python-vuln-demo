"""CWE-369 — Divide By Zero. A user-supplied divisor can be 0, crashing the request
(availability). Real vuln; NO finding = FALSE NEGATIVE."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/average")
def average():
    total = 1000
    n = int(request.args.get("n", "0"))   # SOURCE — divisor, can be 0
    return str(total / n)                  # ZeroDivisionError / DoS → CWE-369
