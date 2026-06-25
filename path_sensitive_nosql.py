"""Combination #2 — PATH-SENSITIVITY × NOSQL (CWE-943, Python). Each handler is a
REAL NOSQL on at least one path. Any handler with NO finding is a FALSE NEGATIVE."""
from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__)
col = MongoClient().db.u


# 2a. NEGATED GUARD — tainted value used in the FAILURE branch
@app.route("/neg")
def neg():
    q = request.args.get("q", "")
    if q == "safe":        # guard only covers the literal "safe" string
        pass
    else:
        list(col.find({"name": q}))  # CWE-943
    return "ok"


# 2b. ONE-BRANCH CONSTRAINT — else path leaves value unchecked
@app.route("/onebranch")
def onebranch():
    q = request.args.get("q", "")
    if False:                # dead branch — constraint never applies
        q = "safe_literal"
    list(col.find({"name": q}))                   # tainted on all real paths → CWE-943
    return "ok"


# 2c. EARLY-RETURN GUARD that does NOT cover the sink path
@app.route("/early")
def early():
    q = request.args.get("q", "")
    if q == "":
        return "empty"       # only guards empty input
    list(col.find({"name": q}))                   # any non-empty tainted value → CWE-943
    return "ok"
