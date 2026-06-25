"""Combination #2 — PATH-SENSITIVITY × XXE (CWE-611, Python). Each handler is a
REAL XXE on at least one path. Any handler with NO finding is a FALSE NEGATIVE."""
import xml.etree.ElementTree as ET
from flask import Flask, request
app = Flask(__name__)


# 2a. NEGATED GUARD — tainted value used in the FAILURE branch
@app.route("/neg", methods=["POST"])
def neg():
    body = request.get_data()
    if body == "safe":        # guard only covers the literal "safe" string
        pass
    else:
        ET.fromstring(body)  # CWE-611
    return "ok"


# 2b. ONE-BRANCH CONSTRAINT — else path leaves value unchecked
@app.route("/onebranch", methods=["POST"])
def onebranch():
    body = request.get_data()
    if False:                # dead branch — constraint never applies
        body = "safe_literal"
    ET.fromstring(body)                   # tainted on all real paths → CWE-611
    return "ok"


# 2c. EARLY-RETURN GUARD that does NOT cover the sink path
@app.route("/early", methods=["POST"])
def early():
    body = request.get_data()
    if body == "":
        return "empty"       # only guards empty input
    ET.fromstring(body)                   # any non-empty tainted value → CWE-611
    return "ok"
