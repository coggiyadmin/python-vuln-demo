"""C1 fake sanitizer — no-op strip before HTML."""
from flask import Flask, request
app = Flask(__name__)
@app.route("/x")
def x():
    q = request.args.get("q", "").replace("SANITIZE", "")
    return "<p>" + q + "</p>"
