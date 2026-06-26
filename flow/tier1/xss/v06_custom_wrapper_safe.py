from flask import Flask, request
def company_sanitize(v: str) -> str:
    return v.replace("<", "").replace(">", "")
app = Flask(__name__)
@app.route("/s")
def s():
    return "<h1>" + company_sanitize(request.args.get("q", "")) + "</h1>"
