"""Cross-file taint — SOURCE side (path traversal). Flask handler passes user
input into a sink defined in xf_pathtrav_helper.py. The scanner MUST trace taint
across the import boundary; no finding = FALSE NEGATIVE (cross-file, cf. #74)."""
from flask import Flask, request

from xf_pathtrav_helper import read_file

app = Flask(__name__)


@app.route("/doc")
def doc():
    name = request.args.get("name", "")   # SOURCE
    return read_file(name)                # → xf_pathtrav_helper.read_file sink (CWE-22)
