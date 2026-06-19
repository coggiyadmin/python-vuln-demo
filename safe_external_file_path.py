"""SAFE mirror — external_file_path.py; basename-only, confined under a fixed base
dir with a realpath prefix check. Expect 0 security findings."""
import os
from flask import Flask, request

app = Flask(__name__)
BASE = "/srv/app/public/"


@app.route("/read")
def read():
    leaf = os.path.basename(request.args.get("path", ""))   # strip dirs/traversal
    full = os.path.realpath(os.path.join(BASE, leaf))
    if not full.startswith(os.path.realpath(BASE)):
        return "denied", 403
    return open(full).read()
