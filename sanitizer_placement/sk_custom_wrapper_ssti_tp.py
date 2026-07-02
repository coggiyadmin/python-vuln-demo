"""C1 custom wrapper — org helper strips {{ only before template render."""
from flask import Flask, request, render_template_string
app = Flask(__name__)

def company_sanitize(v: str) -> str:
    return v.replace("{{", "").replace("}}", "")

@app.route("/hello")
def hello():
    name = company_sanitize(request.args.get("name", ""))
    return render_template_string("<p>Hello " + name + "</p>")
