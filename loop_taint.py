"""Combination #3 — LOOP-CARRIED TAINT (Python). Each handler is a REAL command
injection where taint flows through a loop. Any handler with NO finding is a
FALSE NEGATIVE."""
import os
from flask import Flask, request

app = Flask(__name__)


# 3a. LIST BUILT IN LOOP — taint stored in a list element, then sunk
@app.route("/list")
def via_list():
    parts = []
    for p in request.args.getlist("p"):   # SOURCE (getlist)
        parts.append(p)
    os.system("echo " + parts[0])          # taint via list element → CWE-78


# 3b. STRING ACCUMULATOR — taint concatenated across iterations
@app.route("/accum")
def via_accum():
    acc = "echo "
    for p in request.args.getlist("p"):
        acc += p                            # accumulate tainted parts
    os.system(acc)                          # → CWE-78


# 3c. ITERATE-AND-SINK — sink invoked inside the loop body
@app.route("/iter")
def via_iter():
    for p in request.args.getlist("p"):     # each element tainted
        os.system("echo " + p)              # → CWE-78 per iteration
