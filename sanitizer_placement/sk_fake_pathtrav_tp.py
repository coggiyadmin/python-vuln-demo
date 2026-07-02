"""C1 fake sanitizer — strips only leading slash."""
from flask import Flask, request
app = Flask(__name__)
@app.route("/f")
def f():
    p = request.args.get("p", "").lstrip("/")
    open("/data/" + p).read()
