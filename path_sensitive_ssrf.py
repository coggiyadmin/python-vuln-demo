"""Combination #2 — PATH-SENSITIVITY × SSRF (CWE-918, Python). Each handler is a
REAL SSRF on at least one path. Any handler with NO finding is a FALSE NEGATIVE."""
import requests
from flask import Flask, request

app = Flask(__name__)


# 2a. NEGATED GUARD — tainted URL fetched in the FAILURE branch
@app.route("/neg")
def neg():
    url = request.args.get("url", "")
    if not url.startswith("https://api.internal/"):  # guard fails for malicious input...
        requests.get(url)                             # ...yet the URL is fetched anyway → CWE-918
    return "ok"


# 2b. ONE-BRANCH ALLOWLIST — else path leaves the URL unchecked
@app.route("/onebranch")
def onebranch():
    url = request.args.get("url", "")
    if request.args.get("strict"):
        url = "https://api.internal/" + url.rsplit("/", 1)[-1]  # constrained ONLY here
    requests.get(url)                                           # else path fetches tainted URL → CWE-918


# 2c. EARLY-RETURN GUARD that does NOT cover the sink path
@app.route("/early")
def early():
    url = request.args.get("url", "")
    if url == "":
        return "empty"                  # only guards the empty case
    requests.get(url)                   # any non-empty tainted URL reaches sink → CWE-918
