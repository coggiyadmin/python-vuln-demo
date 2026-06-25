"""Combination #3 — LOOP-CARRIED TAINT × LOGINJ (CWE-117, Python). Taint flows
through a loop into the sink. Any handler with NO finding is a FALSE NEGATIVE."""
import logging
from flask import Flask, request
app = Flask(__name__)
log = logging.getLogger('app')


# 3a. LIST BUILT IN LOOP — taint stored in a list, then sunk
@app.route("/list")
def via_list():
    items = []
    for x in request.args.getlist("user"):
        items.append(x)
    user = items[0] if items else ""
    log.warning("login attempt user=%s", user)  # CWE-117
    return "ok"


# 3b. STRING ACCUMULATOR — taint concatenated across iterations
@app.route("/accum")
def via_accum():
    acc = ""
    for x in request.args.getlist("user"):
        acc += x
    user = acc
    log.warning("login attempt user=%s", user)  # CWE-117
    return "ok"


# 3c. ITERATE-AND-SINK — sink invoked inside the loop body
@app.route("/iter")
def via_iter():
    for user in request.args.getlist("user"):
        log.warning("login attempt user=%s", user)  # CWE-117 per iteration
    return "ok"
