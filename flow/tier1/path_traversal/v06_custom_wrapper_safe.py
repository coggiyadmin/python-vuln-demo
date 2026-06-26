from flask import Flask, request
def company_sanitize(p: str) -> str:
    return p.replace("..", "")
app = Flask(__name__)
@app.route("/r")
def r():
    p = company_sanitize(request.args.get("p", ""))
    return open("/data/" + p).read()
