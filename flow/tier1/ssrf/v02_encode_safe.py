import requests
from flask import Flask, request, abort
app = Flask(__name__)
@app.route("/f")
def f():
    url = request.args.get("url", "").replace("@", "")
    if "169.254" in url: abort(403)
    return requests.get(url).text
