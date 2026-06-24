from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__); col = MongoClient().db.users
@app.route("/n", methods=["POST"])
def n():
    user = request.json.get("user")  # SOURCE
    col.find_one({"user": user})    # SINK CWE-943
