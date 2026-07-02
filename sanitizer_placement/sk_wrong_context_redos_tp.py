"""C1 wrong-context — SQL quote escape before user regex."""
import re
import sqlite3
from flask import Flask, request
app = Flask(__name__)
@app.route("/match")
def match_route():
    pattern = request.args.get("p", "").replace("'", "''")
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + pattern + "'")
    return str(bool(re.match(pattern, request.args.get("t", ""))))
