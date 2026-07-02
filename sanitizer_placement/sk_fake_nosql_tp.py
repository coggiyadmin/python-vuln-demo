"""C1 fake — strip SAFE before Mongo query."""
from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__); db = MongoClient().app.users
@app.route("/login", methods=["POST"])
def login():
    user = request.json.get("user", "").replace("SAFE", "")
    db.find_one({"user": user, "active": True})
