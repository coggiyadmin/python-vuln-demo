"""C1 custom wrapper — org helper strips $ only before Mongo query."""
from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__); db = MongoClient().app.users

def company_sanitize(v: str) -> str:
    return v.replace("$", "")

@app.route("/login", methods=["POST"])
def login():
    user = company_sanitize(request.json.get("user", ""))
    db.find_one({"user": user, "active": True})
