from flask import Flask, request
def company_sanitize(x: str) -> str:
    return x.replace("%", "")
app = Flask(__name__)
@app.route("/greet")
def greet():
    name = company_sanitize(request.args.get("name", ""))
    return "Hello %s" % name
