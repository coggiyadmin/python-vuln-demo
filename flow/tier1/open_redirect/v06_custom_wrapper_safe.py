from flask import Flask, request, redirect
def company_sanitize(x: str) -> str:
    return x.replace("//evil", "")
app = Flask(__name__)
@app.route("/go")
def go():
    return redirect(company_sanitize(request.args.get("next", "/")))
