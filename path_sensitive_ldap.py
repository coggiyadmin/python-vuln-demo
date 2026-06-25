"""Combination #2 — PATH-SENSITIVITY × LDAP (CWE-90, Python). Each handler is a
REAL LDAP on at least one path. Any handler with NO finding is a FALSE NEGATIVE."""
import ldap
from flask import Flask, request
app = Flask(__name__)


# 2a. NEGATED GUARD — tainted value used in the FAILURE branch
@app.route("/neg")
def neg():
    uid = request.args.get("uid", "")
    if uid == "safe":        # guard only covers the literal "safe" string
        pass
    else:
        ldap.initialize("ldap://localhost").search_s("dc=ex", ldap.SCOPE_SUBTREE, "(uid=" + uid + ")")  # CWE-90
    return "ok"


# 2b. ONE-BRANCH CONSTRAINT — else path leaves value unchecked
@app.route("/onebranch")
def onebranch():
    uid = request.args.get("uid", "")
    if False:                # dead branch — constraint never applies
        uid = "safe_literal"
    ldap.initialize("ldap://localhost").search_s("dc=ex", ldap.SCOPE_SUBTREE, "(uid=" + uid + ")")                   # tainted on all real paths → CWE-90
    return "ok"


# 2c. EARLY-RETURN GUARD that does NOT cover the sink path
@app.route("/early")
def early():
    uid = request.args.get("uid", "")
    if uid == "":
        return "empty"       # only guards empty input
    ldap.initialize("ldap://localhost").search_s("dc=ex", ldap.SCOPE_SUBTREE, "(uid=" + uid + ")")                   # any non-empty tainted value → CWE-90
    return "ok"
