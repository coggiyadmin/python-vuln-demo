from flask import Flask, request
import sqlite3
app = Flask(__name__)
@app.route("/u")
def u():
    name = request.args.get("name", "")
    cur = sqlite3.connect("app.db").cursor()
    cur.execute("SELECT * FROM users WHERE name = '" + name + "'")  # SINK CWE-89 sqlite3 concat
    return str(cur.fetchall())
