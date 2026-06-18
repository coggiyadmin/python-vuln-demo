"""Cross-file taint — SOURCE side (SSRF). Flask handler passes user input into a
sink defined in xf_ssrf_helper.py. The scanner MUST trace taint across the import
boundary; no finding = FALSE NEGATIVE (cross-file, cf. #74)."""
from flask import Flask, request

from xf_ssrf_helper import fetch_url

app = Flask(__name__)


@app.route("/fetch")
def fetch():
    url = request.args.get("url", "")   # SOURCE
    fetch_url(url)                      # → xf_ssrf_helper.fetch_url sink (CWE-918)
    return "ok"
