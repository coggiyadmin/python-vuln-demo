import requests
from flask import Flask, request
app = Flask(__name__)
BASE = "https://api.internal.example.com/"
@app.route("/f")
def f():
    path = request.args.get("path", "")
    return requests.get(BASE + path).text
