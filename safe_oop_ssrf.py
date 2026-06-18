"""SAFE mirror — oop_ssrf.py; the tainted host is validated against an allowlist
inside the object before the request is made. Expect 0 security findings."""
from urllib.parse import urlparse
import requests
from flask import Flask, request

app = Flask(__name__)
ALLOWED_HOSTS = {"api.internal.example.com"}


class Fetcher:
    def __init__(self, url):
        self.url = url

    def _checked(self):
        host = urlparse(self.url).hostname
        if host not in ALLOWED_HOSTS:        # allowlist enforced before sink
            raise ValueError("host not allowed")
        return self.url

    def fetch_direct(self):
        return requests.get(self._checked())  # only allowlisted hosts reach the sink


@app.route("/fetch")
def fetch():
    f = Fetcher(request.args.get("url", ""))
    f.fetch_direct()
    return "ok"
