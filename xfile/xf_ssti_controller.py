"""Cross-file taint — SOURCE side (SSTI). Flask handler passes user input into a
sink defined in xf_ssti_helper.py. The scanner MUST trace taint across the import
boundary; no finding = FALSE NEGATIVE (cross-file, cf. #74)."""
from flask import Flask, request

from xf_ssti_helper import render

app = Flask(__name__)


@app.route("/hello")
def hello():
    name = request.args.get("name", "")   # SOURCE
    return render(name)                   # → xf_ssti_helper.render sink (CWE-1336)
