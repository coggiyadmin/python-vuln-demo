import sqlite3
from flask import Flask, request, abort
app = Flask(__name__)
@app.route("/u")
def u():
    n = request.args.get("name", "")
    if not n.isalnum():
        abort(400)
    sqlite3.connect(":memory:").execute("SELECT * FROM users WHERE name=?", (n,))
