"""CWE-15 — External Control of System or Configuration Setting. A user-controlled key/value
writes directly into process configuration. Real vuln; NO finding = FALSE NEGATIVE."""
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/config")
def config():
    key = request.args.get("k", "")        # SOURCE — attacker-controlled setting name
    val = request.args.get("v", "")
    os.environ[key] = val                  # user controls arbitrary config → CWE-15
    return "ok"
