"""SAFE mirror — path_equivalence.py; canonicalize first, then enforce the real
extension and base-dir prefix on the resolved path. Expect 0 security findings."""
import os
from flask import Flask, request

app = Flask(__name__)
BASE = "/srv/app/data/"


@app.route("/get")
def get():
    leaf = os.path.basename(request.args.get("name", ""))
    full = os.path.realpath(os.path.join(BASE, leaf))   # canonical form
    if not full.startswith(os.path.realpath(BASE)) or not full.endswith(".txt"):
        return "blocked", 403
    return open(full).read()
