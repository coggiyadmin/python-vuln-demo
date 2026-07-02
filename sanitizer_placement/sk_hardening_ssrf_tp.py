"""C1 hardening — substring block only; URL still attacker-controlled."""
import urllib.request
from flask import Flask, request, abort
app = Flask(__name__)
@app.route("/u")
def u():
    url = request.args.get("url", "")
    if "127.0.0.1" in url or "169.254.169.254" in url:
        abort(403)
    urllib.request.urlopen(url)
