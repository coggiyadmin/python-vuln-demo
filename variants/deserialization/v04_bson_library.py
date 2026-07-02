from flask import Flask, request
from bson import BSON
app = Flask(__name__)
@app.route("/b", methods=["POST"])
def b():
    BSON.decode(request.get_data())  # SINK CWE-502 bson library
