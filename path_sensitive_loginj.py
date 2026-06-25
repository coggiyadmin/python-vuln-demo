"""Combination #2 — PATH-SENSITIVITY × LOGINJ (CWE-117, Python). Each handler is a
REAL LOGINJ on at least one path. Any handler with NO finding is a FALSE NEGATIVE."""
import logging
from flask import Flask, request
app = Flask(__name__)
log = logging.getLogger('app')


# 2a. NEGATED GUARD — tainted value used in the FAILURE branch
@app.route("/neg")
def neg():
    user = request.args.get("user", "")
    if user == "safe":        # guard only covers the literal "safe" string
        pass
    else:
        log.warning("login attempt user=%s", user)  # CWE-117
    return "ok"


# 2b. ONE-BRANCH CONSTRAINT — else path leaves value unchecked
@app.route("/onebranch")
def onebranch():
    user = request.args.get("user", "")
    if False:                # dead branch — constraint never applies
        user = "safe_literal"
    log.warning("login attempt user=%s", user)                   # tainted on all real paths → CWE-117
    return "ok"


# 2c. EARLY-RETURN GUARD that does NOT cover the sink path
@app.route("/early")
def early():
    user = request.args.get("user", "")
    if user == "":
        return "empty"       # only guards empty input
    log.warning("login attempt user=%s", user)                   # any non-empty tainted value → CWE-117
    return "ok"
