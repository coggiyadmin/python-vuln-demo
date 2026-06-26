"""IL-1 polyglot — Python → Jinja2 via Markup|safe bypass (CWE-79).

Host disables auto-escaping by marking tainted input as safe markup before the
template render. Expected today: FN (template context bypass).
"""
from flask import Flask, render_template_string, request
from markupsafe import Markup

app = Flask(__name__)


@app.route("/hello")
def hello():
    name = request.args.get("name", "")  # SOURCE
    # SINK (CWE-79): Markup() tells Jinja the value is pre-escaped HTML.
    return render_template_string("<h1>{{ name }}</h1>", name=Markup(name))
