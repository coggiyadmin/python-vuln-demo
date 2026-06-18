"""Combination #2 — PATH-SENSITIVITY × PATH TRAVERSAL (CWE-22, Python). Each
handler is a REAL path traversal on at least one path. Any handler with NO finding
is a FALSE NEGATIVE."""
import os
from flask import Flask, request

app = Flask(__name__)
BASE = "/srv/app/data/"


# 2a. NEGATED GUARD — tainted name used in the FAILURE branch
@app.route("/neg")
def neg():
    name = request.args.get("name", "")
    if ".." in name or "/" in name:    # traversal detected...
        open(BASE + name)               # ...yet the file is opened anyway → CWE-22
    return "ok"


# 2b. ONE-BRANCH SANITIZER — else path leaves the name tainted
@app.route("/onebranch")
def onebranch():
    name = request.args.get("name", "")
    if request.args.get("strict"):
        name = os.path.basename(name)   # sanitized ONLY on this branch
    open(BASE + name)                   # on the else path name is tainted → CWE-22


# 2c. EARLY-RETURN GUARD that does NOT cover the sink path
@app.route("/early")
def early():
    name = request.args.get("name", "")
    if name == "":
        return "empty"                  # only guards the empty case
    open(BASE + name)                   # any non-empty tainted name reaches sink → CWE-22
