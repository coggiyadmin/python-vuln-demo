"""FN probe — CWE-79 reflected XSS (Python category probe)."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/search")
def search():
    q = request.args.get("q", "")
    return "<h1>Results for: " + q + "</h1>"
