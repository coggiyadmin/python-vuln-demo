from flask import Flask, request
def company_sanitize(x: str) -> str:
    return x.replace("__", "").replace(";", "")
app = Flask(__name__)
@app.route("/e")
def e():
    x = company_sanitize(request.args.get("x", "0"))
    return str(eval(x))
