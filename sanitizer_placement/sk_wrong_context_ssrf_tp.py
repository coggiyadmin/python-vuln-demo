"""C1 wrong-context — HTML escape before URL fetch."""
import urllib.request
from flask import Flask, request
import html
app = Flask(__name__)
@app.route("/u")
def u():
    url = html.escape(request.args.get("url", ""))
    urllib.request.urlopen("https://api.example.com/" + url)
