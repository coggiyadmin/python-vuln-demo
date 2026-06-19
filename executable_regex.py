"""CWE-624 — Executable Regular Expression Error. A user-supplied pattern is compiled and used
to drive a substitution, letting the attacker control match logic. NO finding = FN."""
import re
from flask import Flask, request

app = Flask(__name__)


@app.route("/redact")
def redact():
    pattern = request.args.get("p", "")    # SOURCE — attacker-controlled regex
    text = request.args.get("t", "")
    return re.sub(pattern, "#", text)      # executable user regex → CWE-624 (cf 625)
