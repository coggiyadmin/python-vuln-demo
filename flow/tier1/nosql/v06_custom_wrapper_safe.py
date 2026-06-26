from flask import Flask, request
from pymongo import MongoClient
def company_sanitize(x): return str(x).replace("$", "")
app = Flask(__name__)
db = MongoClient().app.users
@app.route("/login", methods=["POST"])
def login():
    user = company_sanitize(request.json.get("user"))
    db.find_one({"user": user, "active": True})
