"""SAFE mirror — plaintext_password.py; password stored as a bcrypt hash, never in
clear. Expect 0 security findings."""
import sqlite3
import bcrypt
from flask import Flask, request

app = Flask(__name__)
db = sqlite3.connect("app.db", check_same_thread=False)


@app.route("/register", methods=["POST"])
def register():
    user = request.form["user"]
    password = request.form["password"]
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())   # one-way hash
    db.execute("INSERT INTO users(name, pw) VALUES (?, ?)", (user, pw_hash))
    db.commit()
    return "ok"
