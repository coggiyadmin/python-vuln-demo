"""Combination #11 — FAN-OUT × SSRF (CWE-918, Python). One source → multiple SSRF sinks."""
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/fanout")
def fanout():
    u = request.args.get("u", "")  # SOURCE
    requests.get(u)  # sink 1
    requests.get("http://proxy/?url=" + u)  # sink 2
    requests.post(u)  # sink 3

