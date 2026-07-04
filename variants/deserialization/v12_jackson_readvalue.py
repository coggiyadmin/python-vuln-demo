import json
from flask import Flask, request
app = Flask(__name__)
@app.route("/j", methods=["POST"])
def j():
    json.loads(request.get_data())  # SINK CWE-502 json.loads untyped
