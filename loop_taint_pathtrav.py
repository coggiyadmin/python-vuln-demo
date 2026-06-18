"""Combination #3 — LOOP-CARRIED TAINT × PATH TRAVERSAL (CWE-22, Python). Each
handler is a REAL path traversal where taint flows through a loop. Any handler
with NO finding is a FALSE NEGATIVE."""
from flask import Flask, request

app = Flask(__name__)
BASE = "/srv/app/data/"


# 3a. LIST BUILT IN LOOP — taint stored in a list element, then sunk
@app.route("/list")
def via_list():
    names = []
    for n in request.args.getlist("n"):   # SOURCE (getlist)
        names.append(n)
    open(BASE + names[0])                  # taint via list element → CWE-22


# 3b. STRING ACCUMULATOR — taint concatenated across iterations
@app.route("/accum")
def via_accum():
    path = BASE
    for seg in request.args.getlist("seg"):
        path += seg                        # accumulate tainted path segments
    open(path)                             # → CWE-22


# 3c. ITERATE-AND-SINK — sink invoked inside the loop body
@app.route("/iter")
def via_iter():
    for n in request.args.getlist("n"):    # each element tainted
        open(BASE + n)                     # → CWE-22 per iteration
