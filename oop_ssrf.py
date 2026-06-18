"""Combination #5 — OOP OBJECT FLOW × SSRF (CWE-918, Python). Taint injected via
__init__, stored on self, used in a method sink (directly and via a property).
Each is a REAL server-side request forgery; NO finding = FALSE NEGATIVE."""
import requests
from flask import Flask, request

app = Flask(__name__)


class Fetcher:
    def __init__(self, url):
        self.url = url                     # constructor-injected taint

    @property
    def target(self):
        return self.url                    # property exposes tainted field

    def fetch_direct(self):
        return requests.get(self.url)       # 5a: field → SSRF sink (CWE-918)

    def fetch_via_property(self):
        return requests.get(self.target)    # 5b: field via property → sink (CWE-918)


@app.route("/fetch")
def fetch():
    f = Fetcher(request.args.get("url", ""))  # SOURCE → constructor
    f.fetch_direct()
    f.fetch_via_property()
    return "ok"
