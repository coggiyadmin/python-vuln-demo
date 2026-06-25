"""Combination #2 — PATH-SENSITIVITY × XPATH (CWE-643, Python). Each handler is a
REAL XPATH on at least one path. Any handler with NO finding is a FALSE NEGATIVE."""
from flask import Flask, request
from lxml import etree
app = Flask(__name__)
doc = etree.fromstring(b'<users/>')


# 2a. NEGATED GUARD — tainted value used in the FAILURE branch
@app.route("/neg")
def neg():
    name = request.args.get("name", "")
    if name == "safe":        # guard only covers the literal "safe" string
        pass
    else:
        doc.xpath("//user[name='" + name + "']")  # CWE-643
    return "ok"


# 2b. ONE-BRANCH CONSTRAINT — else path leaves value unchecked
@app.route("/onebranch")
def onebranch():
    name = request.args.get("name", "")
    if False:                # dead branch — constraint never applies
        name = "safe_literal"
    doc.xpath("//user[name='" + name + "']")                   # tainted on all real paths → CWE-643
    return "ok"


# 2c. EARLY-RETURN GUARD that does NOT cover the sink path
@app.route("/early")
def early():
    name = request.args.get("name", "")
    if name == "":
        return "empty"       # only guards empty input
    doc.xpath("//user[name='" + name + "']")                   # any non-empty tainted value → CWE-643
    return "ok"
