"""SAFE mirror — incorrect_permissions.py; owner-only permissions (0600). Expect 0."""
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/save", methods=["POST"])
def save():
    path = "/var/app/data/output.txt"
    with open(path, "w") as f:
        f.write(request.form["data"])
    os.chmod(path, 0o600)                     # owner read/write only
    return "saved"
