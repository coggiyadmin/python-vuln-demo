"""Combination #2 — PATH-SENSITIVITY × DESERIALIZE (CWE-502, Python). Each handler is a
REAL DESERIALIZE on at least one path. Any handler with NO finding is a FALSE NEGATIVE."""
import pickle
from flask import Flask, request
app = Flask(__name__)


# 2a. NEGATED GUARD — tainted value used in the FAILURE branch
@app.route("/neg", methods=["POST"])
def neg():
    body = request.get_data()
    if body == "safe":        # guard only covers the literal "safe" string
        pass
    else:
        pickle.loads(body)  # CWE-502
    return "ok"


# 2b. ONE-BRANCH CONSTRAINT — else path leaves value unchecked
@app.route("/onebranch", methods=["POST"])
def onebranch():
    body = request.get_data()
    if False:                # dead branch — constraint never applies
        body = "safe_literal"
    pickle.loads(body)                   # tainted on all real paths → CWE-502
    return "ok"


# 2c. EARLY-RETURN GUARD that does NOT cover the sink path
@app.route("/early", methods=["POST"])
def early():
    body = request.get_data()
    if body == "":
        return "empty"       # only guards empty input
    pickle.loads(body)                   # any non-empty tainted value → CWE-502
    return "ok"
