"""Combination #5 — OOP × XSS (CWE-79, Python). NO finding = FN (#78)."""
from flask import Flask, request

app = Flask(__name__)


class Page:
    def __init__(self, title):
        self.title = title

    def render_direct(self):
        return "<h1>" + self.title + "</h1>"  # CWE-79

    def render_via_property(self):
        return "<h1>" + self.title + "</h1>"  # CWE-79


@app.route("/page")
def page():
    p = Page(request.args.get("q", ""))
    return p.render_direct() + p.render_via_property()
