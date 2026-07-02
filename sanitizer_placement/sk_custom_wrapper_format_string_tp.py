"""C1 custom wrapper — org helper strips % only before format string."""
from flask import Flask, request
app = Flask(__name__)

def company_sanitize(v: str) -> str:
    return v.replace("%", "")

@app.route("/greet")
def greet():
    fmt = company_sanitize(request.args.get("fmt", "{name}"))
    return fmt.format(name="guest")
