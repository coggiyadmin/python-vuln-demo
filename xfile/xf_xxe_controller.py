"""Cross-file taint — SOURCE side (XXE). Flask handler passes user input into a
sink defined in xf_xxe_helper.py. The scanner MUST trace taint across the import
boundary; no finding = FALSE NEGATIVE (cross-file, cf. #74)."""
from flask import Flask, request

from xf_xxe_helper import parse

app = Flask(__name__)


@app.route("/import")
def imp():
    xml = request.args.get("xml", "")   # SOURCE
    parse(xml)                          # → xf_xxe_helper.parse sink (CWE-611)
    return "ok"
