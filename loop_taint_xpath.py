"""Combination #3 — LOOP-CARRIED TAINT × XPATH (CWE-643, Python). Taint flows
through a loop into the sink. Any handler with NO finding is a FALSE NEGATIVE."""
from flask import Flask, request
from lxml import etree
app = Flask(__name__)
doc = etree.fromstring(b'<users/>')


# 3a. LIST BUILT IN LOOP — taint stored in a list, then sunk
@app.route("/list")
def via_list():
    items = []
    for x in request.args.getlist("name"):
        items.append(x)
    name = items[0] if items else ""
    doc.xpath("//user[name='" + name + "']")  # CWE-643
    return "ok"


# 3b. STRING ACCUMULATOR — taint concatenated across iterations
@app.route("/accum")
def via_accum():
    acc = ""
    for x in request.args.getlist("name"):
        acc += x
    name = acc
    doc.xpath("//user[name='" + name + "']")  # CWE-643
    return "ok"


# 3c. ITERATE-AND-SINK — sink invoked inside the loop body
@app.route("/iter")
def via_iter():
    for name in request.args.getlist("name"):
        doc.xpath("//user[name='" + name + "']")  # CWE-643 per iteration
    return "ok"
