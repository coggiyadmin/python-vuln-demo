"""Combination #3 — LOOP-CARRIED TAINT × NOSQL (CWE-943, Python). Taint flows
through a loop into the sink. Any handler with NO finding is a FALSE NEGATIVE."""
from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__)
col = MongoClient().db.u


# 3a. LIST BUILT IN LOOP — taint stored in a list, then sunk
@app.route("/list")
def via_list():
    items = []
    for x in request.args.getlist("q"):
        items.append(x)
    q = items[0] if items else ""
    list(col.find({"name": q}))  # CWE-943
    return "ok"


# 3b. STRING ACCUMULATOR — taint concatenated across iterations
@app.route("/accum")
def via_accum():
    acc = ""
    for x in request.args.getlist("q"):
        acc += x
    q = acc
    list(col.find({"name": q}))  # CWE-943
    return "ok"


# 3c. ITERATE-AND-SINK — sink invoked inside the loop body
@app.route("/iter")
def via_iter():
    for q in request.args.getlist("q"):
        list(col.find({"name": q}))  # CWE-943 per iteration
    return "ok"
