"""CWE-276 — Incorrect Default Permissions. A file is created world-writable (0777).
Real vuln; NO finding = FALSE NEGATIVE. (CWE-732 family.)"""
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/save", methods=["POST"])
def save():
    path = "/var/app/data/output.txt"
    with open(path, "w") as f:
        f.write(request.form["data"])
    os.chmod(path, 0o777)                     # world-writable/readable → CWE-276
    return "saved"
