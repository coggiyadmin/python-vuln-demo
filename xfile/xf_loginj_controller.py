"""Cross-file taint — SOURCE side (log injection). Flask handler passes user input
into a sink defined in xf_loginj_helper.py. The scanner MUST trace taint across the
import boundary; no finding = FALSE NEGATIVE (cross-file, cf. #74)."""
from flask import Flask, request

from xf_loginj_helper import record

app = Flask(__name__)


@app.route("/audit")
def audit():
    user = request.args.get("user", "")   # SOURCE
    record(user)                          # → xf_loginj_helper.record sink (CWE-117)
    return "ok"
