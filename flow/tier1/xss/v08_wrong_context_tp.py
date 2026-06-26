import sqlite3
from flask import Flask, request
app = Flask(__name__)
@app.route("/s")
def s():
    n = request.args.get("q", "")
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + n + "'")  # SQL param wrong for XSS page
    return "<h1>" + n + "</h1>"
