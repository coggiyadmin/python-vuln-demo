import sqlite3
from flask import Flask, request
app = Flask(__name__)
@app.route("/o")
def o():
    sort = request.args.get("sort", "")
    db = sqlite3.connect(":memory:")
    db.execute("SELECT * FROM u ORDER BY " + sort)  # SINK CWE-89
