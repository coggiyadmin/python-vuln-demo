import re
from flask import Flask, request
app = Flask(__name__)
@app.route("/match")
def match_route():
    pattern = request.args.get("p", ".*")  # SOURCE
    return str(bool(re.match(pattern, request.args.get("t", ""))))  # SINK CWE-1333
