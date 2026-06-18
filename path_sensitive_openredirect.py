"""Combination #2 — PATH-SENSITIVITY × OPEN REDIRECT (CWE-601, Python). Each
handler is a REAL open redirect on at least one path. Any handler with NO finding
is a FALSE NEGATIVE."""
from flask import Flask, request, redirect

app = Flask(__name__)


# 2a. NEGATED GUARD — tainted target redirected in the FAILURE branch
@app.route("/neg")
def neg():
    nxt = request.args.get("next", "")
    if not nxt.startswith("/"):        # only relative paths should be allowed...
        return redirect(nxt)            # ...yet an absolute URL is honored anyway → CWE-601
    return "ok"


# 2b. ONE-BRANCH CONSTRAINT — else path leaves the target unchecked
@app.route("/onebranch")
def onebranch():
    nxt = request.args.get("next", "")
    if request.args.get("strict"):
        nxt = "/" + nxt.lstrip("/")     # constrained to same-site ONLY here
    return redirect(nxt)                # else path redirects tainted target → CWE-601


# 2c. EARLY-RETURN GUARD that does NOT cover the sink path
@app.route("/early")
def early():
    nxt = request.args.get("next", "")
    if nxt == "":
        return "empty"                  # only guards the empty case
    return redirect(nxt)                # any non-empty tainted target reaches sink → CWE-601
