from flask import Flask, request, render_template_string
def company_sanitize(x: str) -> str:
    return x.replace("{", "").replace("}", "")
app = Flask(__name__)
@app.route("/hello")
def hello():
    name = company_sanitize(request.args.get("name", ""))
    return render_template_string("<p>Hello " + name + "</p>")
