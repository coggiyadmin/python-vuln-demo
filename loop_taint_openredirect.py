"""Combination #3 — LOOP-CARRIED TAINT × OPEN REDIRECT (CWE-601, Python). Each
handler is a REAL open redirect where taint flows through a loop. Any handler with
NO finding is a FALSE NEGATIVE."""
from flask import Flask, request, redirect

app = Flask(__name__)


# 3a. LIST BUILT IN LOOP — taint stored in a list element, then sunk
@app.route("/list")
def via_list():
    targets = []
    for t in request.args.getlist("t"):   # SOURCE (getlist)
        targets.append(t)
    return redirect(targets[0])            # taint via list element → CWE-601


# 3b. STRING ACCUMULATOR — taint concatenated across iterations
@app.route("/accum")
def via_accum():
    dest = ""
    for p in request.args.getlist("p"):
        dest += p                          # accumulate tainted target
    return redirect(dest)                  # → CWE-601


# 3c. ITERATE-AND-SINK — sink invoked inside the loop body
@app.route("/iter")
def via_iter():
    for t in request.args.getlist("t"):    # each element tainted
        return redirect(t)                 # → CWE-601
