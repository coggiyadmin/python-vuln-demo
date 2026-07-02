"""C1 hardening — pattern length cap only; catastrophic backtracking remains."""
import re
from flask import Flask, request, abort
app = Flask(__name__)
@app.route("/match")
def match_route():
    pattern = request.args.get("p", "")
    if len(pattern) > 64:
        abort(400)
    re.match(pattern, request.args.get("t", ""))
