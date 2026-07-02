"""C1 fake — strip SAFE before user regex."""
import re
from flask import Flask, request
app = Flask(__name__)
@app.route("/match")
def match_route():
    pattern = request.args.get("p", "").replace("SAFE", "")
    return str(bool(re.match(pattern, request.args.get("t", ""))))
