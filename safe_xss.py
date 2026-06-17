"""SAFE mirror — xss_probe.py; markupsafe.escape before HTML render."""
import markupsafe
from flask import Flask, request

app = Flask(__name__)


@app.route("/search")
def search():
    q = request.args.get("q", "")
    return "<h1>Results for: " + str(markupsafe.escape(q)) + "</h1>"
