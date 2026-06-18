"""Cross-file taint — SOURCE side (XPath injection). Flask handler passes user
input into a sink defined in xf_xpath_helper.py. The scanner MUST trace taint
across the import boundary; no finding = FALSE NEGATIVE (cross-file, cf. #74)."""
from flask import Flask, request

from xf_xpath_helper import find

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    name = request.args.get("name", "")   # SOURCE
    find(name)                            # → xf_xpath_helper.find sink (CWE-643)
    return "ok"
