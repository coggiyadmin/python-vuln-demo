from html import escape
import sqlite3
from flask import Flask, request
app = Flask(__name__)
@app.route("/u")
def u():
    n = escape(request.args.get("name", ""))
    sqlite3.connect(":memory:").execute("SELECT * FROM users WHERE name='" + n + "'")  # TP
