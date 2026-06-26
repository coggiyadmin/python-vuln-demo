# wrong_context mirror — deserialization
import json
from flask import Flask, request
app = Flask(__name__)
@app.route("/p", methods=["POST"])
def p():
    json.loads(request.get_data())  # SAFE JSON only
