"""Combination #2 — PATH-SENSITIVITY × SSTI (CWE-1336, Python). Each handler is a
REAL SSTI on at least one path. Any handler with NO finding is a FALSE NEGATIVE."""
from jinja2 import Template
from flask import Flask, request
app = Flask(__name__)


# 2a. NEGATED GUARD — tainted value used in the FAILURE branch
@app.route("/neg")
def neg():
    t = request.args.get("t", "")
    if t == "safe":        # guard only covers the literal "safe" string
        pass
    else:
        Template(t).render()  # CWE-1336
    return "ok"


# 2b. ONE-BRANCH CONSTRAINT — else path leaves value unchecked
@app.route("/onebranch")
def onebranch():
    t = request.args.get("t", "")
    if False:                # dead branch — constraint never applies
        t = "safe_literal"
    Template(t).render()                   # tainted on all real paths → CWE-1336
    return "ok"


# 2c. EARLY-RETURN GUARD that does NOT cover the sink path
@app.route("/early")
def early():
    t = request.args.get("t", "")
    if t == "":
        return "empty"       # only guards empty input
    Template(t).render()                   # any non-empty tainted value → CWE-1336
    return "ok"
