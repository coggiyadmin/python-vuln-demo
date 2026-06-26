"""c08 SAFE — custom wrapper × SSRF (CWE-918). Expect clean."""
import requests
from urllib.parse import urlparse
from flask import Flask, request

app = Flask(__name__)
ALLOWED = {"api.internal.example.com"}


def checked_url(u):
    host = urlparse(u).hostname
    if host not in ALLOWED:
        raise ValueError("host not allowed")
    return u


@app.route("/wrapped")
def wrapped():
    u = checked_url(request.args.get("url", ""))
    requests.get(u)
