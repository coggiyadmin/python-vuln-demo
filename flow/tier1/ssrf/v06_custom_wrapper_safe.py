# custom_wrapper mirror — ssrf
import requests
from flask import Flask, request
from urllib.parse import urlparse
app = Flask(__name__)
ALLOWED = {"api.internal.example.com"}
@app.route("/f")
def f():
    url = request.args.get("url", "")
    if urlparse(url).hostname not in ALLOWED:
        return "forbidden", 403
    return requests.get(url).text
