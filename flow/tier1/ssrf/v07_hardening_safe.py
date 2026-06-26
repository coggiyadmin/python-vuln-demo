import requests
from flask import Flask, request, abort
from urllib.parse import urlparse
app = Flask(__name__)
BLOCK = {"127.0.0.1", "169.254.169.254"}
@app.route("/f")
def f():
    url = request.args.get("url", "")
    host = urlparse(url).hostname or ""
    if host in BLOCK or not host.endswith(".example.com"):
        abort(403)
    return requests.get(url).text
