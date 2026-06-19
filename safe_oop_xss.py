"""SAFE mirror — oop_xss.py; markupsafe escape before echo. Expect 0."""
from markupsafe import escape
from flask import Flask, request

app = Flask(__name__)


class Page:
    def __init__(self, title):
        self.title = title

    def render(self):
        return "<h1>" + escape(self.title) + "</h1>"


@app.route("/page")
def page():
    p = Page(request.args.get("q", ""))
    return p.render()
