import requests
from flask import Flask, request
app = Flask(__name__)
@app.route("/b")
def b():
    cb = request.args.get("cb", "")
    requests.get(cb)  # SINK CWE-918 blind
    return "ok"
