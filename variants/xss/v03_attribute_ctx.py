# XSS variant: attribute context in template string.
from flask import Flask, request
app = Flask(__name__)
@app.route("/a")
def a():
    u = request.args.get("u", "")
    return f'<a href="{u}">x</a>'  # SINK CWE-79
