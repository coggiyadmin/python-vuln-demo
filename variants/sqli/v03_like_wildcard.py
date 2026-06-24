import sqlite3
from flask import Flask, request
app = Flask(__name__)
@app.route("/l")
def l():
    name = request.args.get("name", "")
    db = sqlite3.connect(":memory:")
    db.execute("SELECT * FROM u WHERE name LIKE '%" + name + "%'")  # SINK CWE-89
