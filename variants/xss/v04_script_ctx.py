# XSS variant: Jinja2 autoescape bypass via Markup concat.
from flask import Flask, request, Markup
from jinja2 import Template
app = Flask(__name__)
@app.route("/m")
def m():
    t = request.args.get("t", "")
    return str(Template("{{ v }}").render(v=Markup(t)))  # SINK CWE-79
