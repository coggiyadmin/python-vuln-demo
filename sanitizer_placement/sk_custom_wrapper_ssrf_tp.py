"""C1 custom wrapper — org helper strips scheme only before fetch."""
import urllib.request
from flask import Flask, request
app = Flask(__name__)

def company_sanitize(v: str) -> str:
    return v.replace("http://", "").replace("https://", "")

@app.route("/fetch")
def fetch_route():
    url = company_sanitize(request.args.get("url", ""))
    urllib.request.urlopen("http://" + url)
