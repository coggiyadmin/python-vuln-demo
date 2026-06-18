"""Combination #3 — LOOP-CARRIED TAINT × SSRF (CWE-918, Python). Each handler is
a REAL SSRF where taint flows through a loop. Any handler with NO finding is a
FALSE NEGATIVE."""
import requests
from flask import Flask, request

app = Flask(__name__)


# 3a. LIST BUILT IN LOOP — taint stored in a list element, then sunk
@app.route("/list")
def via_list():
    urls = []
    for u in request.args.getlist("u"):   # SOURCE (getlist)
        urls.append(u)
    requests.get(urls[0])                  # taint via list element → CWE-918


# 3b. STRING ACCUMULATOR — taint concatenated across iterations
@app.route("/accum")
def via_accum():
    acc = "https://"
    for p in request.args.getlist("p"):
        acc += p                           # accumulate tainted parts into URL
    requests.get(acc)                      # → CWE-918


# 3c. ITERATE-AND-SINK — sink invoked inside the loop body
@app.route("/iter")
def via_iter():
    for u in request.args.getlist("u"):    # each element tainted
        requests.get(u)                    # → CWE-918 per iteration
