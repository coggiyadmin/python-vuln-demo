"""Combination #2 — PATH-SENSITIVITY (Python). Each handler is a REAL vuln on
at least one path. Any handler with NO finding is a FALSE NEGATIVE."""
import os
import shlex
from flask import Flask, request

app = Flask(__name__)


# 2a. NEGATED GUARD — tainted value used in the FAILURE branch
@app.route("/neg")
def neg():
    host = request.args.get("host", "")
    if not host.isalnum():            # validation fails for malicious input...
        os.system("echo " + host)      # ...yet the value is used anyway → CWE-78
    return "ok"


# 2b. ONE-BRANCH SANITIZER — else path leaves the value tainted
@app.route("/onebranch")
def onebranch():
    host = request.args.get("host", "")
    if request.args.get("fast"):
        host = shlex.quote(host)       # sanitized ONLY on this branch
    os.system("echo " + host)          # on the else path host is tainted → CWE-78


# 2c. EARLY-RETURN GUARD that does NOT cover the sink path
@app.route("/early")
def early():
    cmd = request.args.get("cmd", "")
    if cmd == "":
        return "empty"                 # only guards the empty case
    os.system(cmd)                     # any non-empty tainted cmd reaches sink → CWE-78
