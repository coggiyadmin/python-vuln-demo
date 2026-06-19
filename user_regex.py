"""CWE-625 — Permissive/Attacker-Controlled Regular Expression. A user-supplied pattern is
compiled and run, enabling catastrophic backtracking (ReDoS). Real vuln; NO finding = FN."""
import re
from flask import Flask, request

app = Flask(__name__)


@app.route("/match")
def match():
    pattern = request.args.get("p", "")   # SOURCE — attacker-controlled regex
    text = request.args.get("t", "")
    return str(bool(re.match(pattern, text)))   # user regex → ReDoS / CWE-625/1333
