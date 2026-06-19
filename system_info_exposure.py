"""CWE-497 — Exposure of Sensitive System Information. A debug endpoint returns the full
environment and platform details to the client. Real vuln; NO finding = FALSE NEGATIVE."""
import os
import platform
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/debug")
def debug():
    # leaks env vars (secrets), versions, paths to an unauthorized actor → CWE-497
    return jsonify({"env": dict(os.environ), "platform": platform.platform(), "cwd": os.getcwd()})
