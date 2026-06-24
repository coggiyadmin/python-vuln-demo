import requests
from flask import Flask, request
app = Flask(__name__)
@app.route("/meta")
def meta():
    path = request.args.get("path", "")
    return requests.get("http://169.254.169.254/" + path).text  # SINK CWE-918
