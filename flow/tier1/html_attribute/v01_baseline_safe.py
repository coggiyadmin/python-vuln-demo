"""Safe mirror (cognium-dev#153) — attribute-encoded href."""
import html
from flask import Flask, request

app = Flask(__name__)


@app.route("/link")
def link():
    url = html.escape(request.args.get("url", ""), quote=True)
    return f'<a href="{url}">click</a>'
