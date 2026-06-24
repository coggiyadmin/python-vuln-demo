import sqlite3
from flask import Flask, request
app = Flask(__name__)
@app.route("/q")
def q():
    uid = request.args.get("id", "")
    db = sqlite3.connect(":memory:")
    db.execute("SELECT * FROM u WHERE id=" + uid)  # SINK CWE-89
