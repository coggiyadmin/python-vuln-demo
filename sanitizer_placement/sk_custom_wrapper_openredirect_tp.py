"""C1 custom wrapper — org helper strips javascript: scheme only."""
from flask import Flask, redirect, request
app = Flask(__name__)

def company_sanitize(v: str) -> str:
    return v.replace("javascript:", "")

@app.route("/go")
def go():
    nxt = company_sanitize(request.args.get("next", ""))
    return redirect(nxt)
