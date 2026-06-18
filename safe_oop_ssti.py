"""SAFE mirror — oop_ssti.py; the tainted value is passed as a template context
variable (auto-escaped, never parsed as template source). Expect 0 findings."""
from flask import Flask, request, render_template_string

app = Flask(__name__)


class Greeting:
    def __init__(self, name):
        self.name = name

    def render_direct(self):
        # constant template; user value is data passed via context, not template source
        return render_template_string("<p>Hello {{ n }}</p>", n=self.name)


@app.route("/hello")
def hello():
    g = Greeting(request.args.get("name", ""))
    return g.render_direct()
