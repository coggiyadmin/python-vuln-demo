from html import escape
from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__)
db = MongoClient().app.users
@app.route("/login", methods=["POST"])
def login():
    user = escape(str(request.json.get("user", "")))
    db.find_one({"user": user, "active": True})
