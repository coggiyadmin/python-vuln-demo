import os
from flask import Flask, request, abort
app = Flask(__name__)
ROOT = "/data"
@app.route("/r")
def r():
    full = os.path.realpath(os.path.join(ROOT, request.args.get("p", "")))
    if not full.startswith(ROOT): abort(403)
    return open(full).read()
