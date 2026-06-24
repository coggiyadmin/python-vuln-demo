"""TP control (CWE-94) — eval of UNTRUSTED HTTP input. Proves the engine fires on the genuine
code-exec sink, so the constant-expr twin in safe_expr_constant.py staying clean is meaningful."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/calc")
def calc():
    expr = request.args.get("expr")  # attacker-controlled HTTP source
    return str(eval(expr))  # SINK — arbitrary code execution
