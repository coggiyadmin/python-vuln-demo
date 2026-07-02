"""C1 wrong-context — HTML escape before Mongo query."""
import html
from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__); db = MongoClient().app.users
@app.route("/login", methods=["POST"])
def login():
    user = html.escape(request.json.get("user", ""))
    db.find_one({"user": user, "active": True})
