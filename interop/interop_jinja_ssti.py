"""IL-1 polyglot — Python → Jinja2 (CWE-1336 SSTI).

Host (Python) embeds a guest language (Jinja2 template) and feeds it untrusted
input via render_template_string, so the template engine evaluates attacker
markup. Expected today: likely FN (host-side template-eval not modeled as a sink).
"""
from flask import Flask, request
from jinja2 import Template

app = Flask(__name__)


@app.route("/hello")
def hello():
    name = request.args.get("name", "")  # SOURCE (HTTP param)
    # SINK (CWE-1336): tainted value concatenated into the template *source*,
    # so `{{7*7}}` / `{{config}}` payloads are evaluated by Jinja (SSTI).
    return Template("<h1>Hello " + name + "</h1>").render()
