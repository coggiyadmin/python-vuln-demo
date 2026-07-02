"""C1 fake — comment-only before URL fetch."""
import urllib.request
from flask import Flask, request
app = Flask(__name__)
@app.route("/u")
def u():
    url = request.args.get("url", "")
    urllib.request.urlopen("https://api.example.com/" + url)
