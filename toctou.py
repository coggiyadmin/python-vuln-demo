"""CWE-367 — Time-of-check Time-of-use (TOCTOU) Race Condition. The file is checked, then
opened in a separate step; an attacker can swap it in the window. NO finding = FN."""
import os
from flask import Flask, request

app = Flask(__name__)
BASE = "/var/app/data/"


@app.route("/write")
def write():
    path = BASE + request.args.get("f", "")
    if os.access(path, os.W_OK):                 # CHECK
        with open(path, "w") as fh:              # USE — race window between check and use → CWE-367
            fh.write(request.args.get("d", ""))
    return "ok"
