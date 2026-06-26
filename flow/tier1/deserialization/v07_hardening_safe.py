import json
from flask import Flask, request, abort
app = Flask(__name__)
@app.route("/load", methods=["POST"])
def load():
    raw = request.get_data()
    if len(raw) > 65536:
        abort(413)
    return str(json.loads(raw))
