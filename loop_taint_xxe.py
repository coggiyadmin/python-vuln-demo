"""Combination #3 — LOOP-CARRIED TAINT × XXE (CWE-611, Python). Taint flows
through a loop into the sink. Any handler with NO finding is a FALSE NEGATIVE."""
import xml.etree.ElementTree as ET
from flask import Flask, request
app = Flask(__name__)


# 3a. LIST BUILT IN LOOP — taint stored in a list, then sunk
@app.route("/list", methods=["POST"])
def via_list():
    items = []
    for x in request.form.getlist('blob'):
        items.append(x)
    blob = items[0] if items else ""
    ET.fromstring(blob)  # CWE-611
    return "ok"


# 3b. STRING ACCUMULATOR — taint concatenated across iterations
@app.route("/accum", methods=["POST"])
def via_accum():
    acc = ""
    for x in request.form.getlist('blob'):
        acc += x
    blob = acc
    ET.fromstring(blob)  # CWE-611
    return "ok"


# 3c. ITERATE-AND-SINK — sink invoked inside the loop body
@app.route("/iter", methods=["POST"])
def via_iter():
    for blob in request.form.getlist('blob'):
        ET.fromstring(blob)  # CWE-611 per iteration
    return "ok"
