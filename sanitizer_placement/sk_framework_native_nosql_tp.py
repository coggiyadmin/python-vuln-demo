"""C1 framework-native bypass — JSON parse then Mongo $eq."""
from flask import Flask, request
from pymongo import MongoClient
import json
app = Flask(__name__); db = MongoClient().app.users
@app.route("/login", methods=["POST"])
def login():
    user = json.loads(request.get_data() or b"{}").get("user", "")
    db.find_one({"user": {"$eq": user}, "active": True})
