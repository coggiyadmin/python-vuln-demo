import json
from flask import Flask, request
app = Flask(__name__)
@app.route("/load", methods=["POST"])
def load():
    return str(json.loads(request.get_data()))
