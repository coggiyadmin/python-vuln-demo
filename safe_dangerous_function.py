"""SAFE mirror — dangerous_function.py; a constrained numeric add replaces eval. Expect 0."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/calc")
def calc():
    try:
        a = int(request.args.get("a", ""))
        b = int(request.args.get("b", ""))
    except ValueError:
        return "bad input", 400
    return str(a + b)                       # no dynamic evaluation
