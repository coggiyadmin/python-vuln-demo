"""Cross-file taint — SOURCE side (LDAP injection). Flask handler passes user input
into a sink defined in xf_ldap_helper.py. The scanner MUST trace taint across the
import boundary; no finding = FALSE NEGATIVE (cross-file, cf. #74)."""
from flask import Flask, request

from xf_ldap_helper import search

app = Flask(__name__)


@app.route("/dir")
def directory():
    user = request.args.get("user", "")   # SOURCE
    search(user)                          # → xf_ldap_helper.search sink (CWE-90)
    return "ok"
