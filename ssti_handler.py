"""
DEMO FILE — intentional vulnerabilities for security scanner showcase.

CVE classes covered:
  CWE-1336 / SSTI    Jinja2 server-side template injection (render_template_string)
  CWE-94   / eval    Python expression injection
  CWE-95   / exec    Python code injection via exec
  CWE-502  / yaml    Unsafe YAML deserialization (yaml.load without SafeLoader)
"""

import yaml
from flask import Flask, request, render_template_string
from jinja2 import Template

app = Flask(__name__)


# CWE-1336 — Jinja2 SSTI via render_template_string (Flask SSTI → RCE)
@app.route("/render")
def render():
    name = request.args.get("name", "")
    # Attacker sends name={{ ''.__class__.__mro__[1].__subclasses__() }} → RCE
    template = "<h1>Hello " + name + "</h1>"
    return render_template_string(template)


# CWE-1336 — Jinja2 SSTI via Template(user_input)
@app.route("/preview")
def preview():
    body = request.args.get("body", "")
    # Attacker sends body={{ config.__class__.__init__.__globals__['os'].popen('id').read() }}
    tmpl = Template(body)
    return tmpl.render()


# CWE-94 — eval on user input
@app.route("/calc")
def calc():
    expr = request.args.get("expr", "0")
    # Attacker sends expr=__import__('os').system('id')
    return str(eval(expr))


# CWE-95 — exec on user input
@app.route("/run", methods=["POST"])
def run_code():
    code = request.form.get("code", "")
    exec(code)  # Attacker sends arbitrary Python
    return "executed"


# CWE-502 — unsafe yaml.load (NOT safe_load) → arbitrary object construction
@app.route("/import", methods=["POST"])
def import_config():
    raw = request.get_data(as_text=True)
    # yaml.load without SafeLoader instantiates arbitrary Python objects
    cfg = yaml.load(raw, Loader=yaml.Loader)
    return str(cfg)
