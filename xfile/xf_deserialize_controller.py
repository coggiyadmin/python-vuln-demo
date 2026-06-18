"""Cross-file taint — SOURCE side (insecure deserialization). Flask handler passes
user input into a sink defined in xf_deserialize_helper.py. The scanner MUST trace
taint across the import boundary; no finding = FALSE NEGATIVE (cross-file, cf. #74)."""
from flask import Flask, request

from xf_deserialize_helper import load

app = Flask(__name__)


@app.route("/restore")
def restore():
    s = request.args.get("s", "")   # SOURCE
    load(s)                         # → xf_deserialize_helper.load sink (CWE-502)
    return "ok"
