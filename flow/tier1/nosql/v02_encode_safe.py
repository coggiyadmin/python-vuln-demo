# Phase-3 encode mirror
from flask import Flask, request, abort
from pymongo import MongoClient
app = Flask(__name__); db = MongoClient().app.users
@app.route("/login", methods=["POST"])
def login():
    user = request.json.get("user")
    if not isinstance(user, str):
        abort(400)
    db.find_one({"user": user, "active": True})
