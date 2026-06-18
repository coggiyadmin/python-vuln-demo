"""Cross-file taint — SOURCE side (NoSQL injection). Flask handler passes user
input into a sink defined in xf_nosql_helper.py. The scanner MUST trace taint
across the import boundary; no finding = FALSE NEGATIVE (cross-file, cf. #74)."""
from flask import Flask, request

from xf_nosql_helper import find

app = Flask(__name__)


@app.route("/q")
def q():
    user = request.args.get("user", "")   # SOURCE
    list(find(user))                      # → xf_nosql_helper.find sink (CWE-943)
    return "ok"
