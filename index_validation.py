"""CWE-1285 — Improper Validation of Specified Index/Position/Offset. A user-supplied index
is used to access an array with no bounds check. Real vuln; NO finding = FALSE NEGATIVE."""
from flask import Flask, request

app = Flask(__name__)
ACCOUNTS = [{"id": 0}, {"id": 1}, {"id": 2}]


@app.route("/account")
def account():
    i = int(request.args.get("i", "0"))   # SOURCE — unchecked index
    return ACCOUNTS[i]                      # out-of-range / negative index → CWE-1285
