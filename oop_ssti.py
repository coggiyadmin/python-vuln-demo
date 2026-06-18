"""Combination #5 — OOP OBJECT FLOW × SSTI (CWE-1336, Python). Taint injected via
__init__, stored on self, concatenated into a Jinja2 template string (directly and
via a property). Each is a REAL template injection; NO finding = FALSE NEGATIVE."""
from flask import Flask, request, render_template_string

app = Flask(__name__)


class Greeting:
    def __init__(self, name):
        self.name = name                    # constructor-injected taint

    @property
    def who(self):
        return self.name                    # property exposes tainted field

    def render_direct(self):
        return render_template_string("<p>Hello " + self.name + "</p>")  # 5a → SSTI sink (CWE-1336)

    def render_via_property(self):
        return render_template_string("<p>Hi " + self.who + "</p>")      # 5b via property → sink (CWE-1336)


@app.route("/hello")
def hello():
    g = Greeting(request.args.get("name", ""))  # SOURCE → constructor
    g.render_via_property()
    return g.render_direct()
