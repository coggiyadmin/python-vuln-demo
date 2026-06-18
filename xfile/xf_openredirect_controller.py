"""Cross-file taint — SOURCE side (open redirect). Flask handler passes user
input into a sink defined in xf_openredirect_helper.py. The scanner MUST trace
taint across the import boundary; no finding = FALSE NEGATIVE (cross-file, cf. #74)."""
from flask import Flask, request

from xf_openredirect_helper import go

app = Flask(__name__)


@app.route("/login")
def login():
    nxt = request.args.get("next", "")   # SOURCE
    return go(nxt)                       # → xf_openredirect_helper.go sink (CWE-601)
