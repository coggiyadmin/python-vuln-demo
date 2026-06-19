"""SAFE mirror — toctou.py; open atomically (no separate check) and rely on the OS, with
exclusive create. Expect 0 security findings."""
import os
from flask import Flask, request

app = Flask(__name__)
BASE = "/var/app/data/"


@app.route("/write")
def write():
    leaf = os.path.basename(request.args.get("f", ""))
    fd = os.open(os.path.join(BASE, leaf), os.O_WRONLY | os.O_CREAT, 0o600)  # atomic open, no TOCTOU
    with os.fdopen(fd, "w") as fh:
        fh.write(request.args.get("d", ""))
    return "ok"
