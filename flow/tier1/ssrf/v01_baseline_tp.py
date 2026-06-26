import requests
from flask import Flask, request
app = Flask(__name__)
@app.route("/f")
def f():
    url = request.args.get("url", "")  # SOURCE
    return requests.get(url).text  # SINK CWE-918
