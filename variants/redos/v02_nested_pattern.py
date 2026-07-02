import re
from flask import Flask, request
app = Flask(__name__)
@app.route("/search")
def search():
    outer = request.args.get("outer", "")
    inner = request.args.get("inner", "")
    combined = f"({outer})+{inner}"  # SOURCE (nested construction)
    return str(bool(re.match(combined, request.args.get("t", ""))))
