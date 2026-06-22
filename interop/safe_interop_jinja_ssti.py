"""IL-1 polyglot — SAFE mirror of interop_jinja_ssti.py.
The untrusted value is passed as template *data* (a context variable), so Jinja's
autoescaping treats it as text, never as template source. The scanner MUST produce
ZERO security findings.
"""
from flask import Flask, request
from jinja2 import Template

app = Flask(__name__)


@app.route("/hello")
def hello():
    name = request.args.get("name", "")  # SOURCE
    # Safe: constant template; `name` bound as autoescaped data, not concatenated
    # into the template source — `{{7*7}}` is rendered literally, not evaluated.
    return Template("<h1>Hello {{ name }}</h1>").render(name=name)
