"""CWE-242 — Use of Inherently Dangerous Function. `eval` executes arbitrary code in-process
and is dangerous by design. Real vuln; NO finding = FALSE NEGATIVE."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/calc")
def calc():
    expr = request.args.get("e", "")       # SOURCE
    return str(eval(expr))                  # inherently dangerous function → CWE-242
