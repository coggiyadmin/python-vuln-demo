"""Combination #3 — LOOP-CARRIED TAINT × LDAP (CWE-90, Python). Taint flows
through a loop into the sink. Any handler with NO finding is a FALSE NEGATIVE."""
import ldap
from flask import Flask, request
app = Flask(__name__)


# 3a. LIST BUILT IN LOOP — taint stored in a list, then sunk
@app.route("/list")
def via_list():
    items = []
    for x in request.args.getlist("uid"):
        items.append(x)
    uid = items[0] if items else ""
    ldap.initialize("ldap://localhost").search_s("dc=ex", ldap.SCOPE_SUBTREE, "(uid=" + uid + ")")  # CWE-90
    return "ok"


# 3b. STRING ACCUMULATOR — taint concatenated across iterations
@app.route("/accum")
def via_accum():
    acc = ""
    for x in request.args.getlist("uid"):
        acc += x
    uid = acc
    ldap.initialize("ldap://localhost").search_s("dc=ex", ldap.SCOPE_SUBTREE, "(uid=" + uid + ")")  # CWE-90
    return "ok"


# 3c. ITERATE-AND-SINK — sink invoked inside the loop body
@app.route("/iter")
def via_iter():
    for uid in request.args.getlist("uid"):
        ldap.initialize("ldap://localhost").search_s("dc=ex", ldap.SCOPE_SUBTREE, "(uid=" + uid + ")")  # CWE-90 per iteration
    return "ok"
