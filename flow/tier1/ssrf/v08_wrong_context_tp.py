import requests
from html import escape
from flask import Flask, request
app = Flask(__name__)
@app.route("/f")
def f():
    url = escape(request.args.get("url", ""))  # HTML escape wrong for URL fetch
    return requests.get(url).text  # TP wrong context
