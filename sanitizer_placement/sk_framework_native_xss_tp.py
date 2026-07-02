"""C1 framework-native bypass — Markup() disables Jinja autoescape."""
from flask import Flask, request, render_template_string
from markupsafe import Markup
app = Flask(__name__)
@app.route("/x")
def x():
    q = request.args.get("q", "")
    return render_template_string("<p>{{ name }}</p>", name=Markup(q))
