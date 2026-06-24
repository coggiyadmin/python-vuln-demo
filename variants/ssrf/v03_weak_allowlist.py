import requests
from flask import Flask, request
app = Flask(__name__)
@app.route("/w")
def w():
    url = request.args.get("url", "")
    if "trusted" in url:
        return requests.get(url).text  # SINK CWE-918 weak allowlist
