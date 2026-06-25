"""Combination #3 — LOOP-CARRIED TAINT × SSTI (CWE-1336, Python). Taint flows
through a loop into the sink. Any handler with NO finding is a FALSE NEGATIVE."""
from jinja2 import Template
from flask import Flask, request
app = Flask(__name__)


# 3a. LIST BUILT IN LOOP — taint stored in a list, then sunk
@app.route("/list")
def via_list():
    items = []
    for x in request.args.getlist("t"):
        items.append(x)
    t = items[0] if items else ""
    Template(t).render()  # CWE-1336
    return "ok"


# 3b. STRING ACCUMULATOR — taint concatenated across iterations
@app.route("/accum")
def via_accum():
    acc = ""
    for x in request.args.getlist("t"):
        acc += x
    t = acc
    Template(t).render()  # CWE-1336
    return "ok"


# 3c. ITERATE-AND-SINK — sink invoked inside the loop body
@app.route("/iter")
def via_iter():
    for t in request.args.getlist("t"):
        Template(t).render()  # CWE-1336 per iteration
    return "ok"
