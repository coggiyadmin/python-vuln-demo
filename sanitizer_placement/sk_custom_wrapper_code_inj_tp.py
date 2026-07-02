"""C1 custom wrapper — org helper strips semicolon only before eval."""
from flask import Flask, request
app = Flask(__name__)

def company_sanitize(v: str) -> str:
    return v.replace(";", "")

@app.route("/run")
def run_route():
    code = company_sanitize(request.args.get("code", ""))
    eval(code)
