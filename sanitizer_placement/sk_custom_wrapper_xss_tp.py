"""C1 custom wrapper — org helper strips only angle brackets before HTML."""
from flask import Flask, request
app = Flask(__name__)

def company_sanitize(v: str) -> str:
    return v.replace("<", "").replace(">", "")

@app.route("/x")
def x():
    q = company_sanitize(request.args.get("q", ""))
    return "<p>" + q + "</p>"
