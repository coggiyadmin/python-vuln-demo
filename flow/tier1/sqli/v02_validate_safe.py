import sqlite3
from flask import Flask, request, abort
app = Flask(__name__)
@app.route("/u")
def u():
    name = request.args.get("name", "")
    if not name.isalnum(): abort(400)
    conn = sqlite3.connect("app.db")
    conn.execute("SELECT * FROM users WHERE name=?", (name,))
