"""SAFE mirror — interop_flask_jinja_safe_filter.py. Plain text, no Markup bypass."""
from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.route("/hello")
def hello():
    name = request.args.get("name", "")
    return render_template_string("<h1>{{ name }}</h1>", name=name)
