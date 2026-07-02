"""TP (CWE-79 / cognium-dev#153) — user input in HTML attribute context without encoding."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/link")
def link():
    url = request.args.get("url", "")
    return f'<a href="{url}">click</a>'  # SINK (attribute context)
