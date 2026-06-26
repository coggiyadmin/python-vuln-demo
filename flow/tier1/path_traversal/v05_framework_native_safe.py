# framework_native mirror — path_traversal
import os
from flask import Flask, request, abort
app = Flask(__name__)
ROOT = "/data"
@app.route("/r")
def r():
    p = request.args.get("p", "")
    full = os.path.realpath(os.path.join(ROOT, p))
    if not full.startswith(ROOT): abort(403)
    return open(full).read()
