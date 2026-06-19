"""CWE-256 — Plaintext Storage of a Password. The password is persisted as-is, with
no hashing. Real vuln; NO finding = FALSE NEGATIVE."""
import sqlite3
from flask import Flask, request

app = Flask(__name__)
db = sqlite3.connect("app.db", check_same_thread=False)


@app.route("/register", methods=["POST"])
def register():
    user = request.form["user"]
    password = request.form["password"]   # SOURCE
    db.execute("INSERT INTO users(name, pw) VALUES (?, ?)", (user, password))  # plaintext → CWE-256
    db.commit()
    return "ok"
