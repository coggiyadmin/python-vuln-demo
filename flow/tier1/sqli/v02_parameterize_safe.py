import sqlite3
from flask import Flask, request
app = Flask(__name__)
@app.route("/u")
def u():
    conn = sqlite3.connect("app.db")
    conn.execute("SELECT * FROM users WHERE name=?", (request.args.get("name", ""),))
