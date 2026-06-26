"""TP — dynamic eval of admin expression (CWE-94). CVE-2026-33017 B-tier class."""
from flask import Flask, request

app = Flask(__name__)


@app.post("/admin/eval")
def eval_expr():
    expr = request.form.get("expr", "")
    return str(eval(expr))  # SINK CWE-94
