from flask import Flask, request
import sqlite3
app = Flask(__name__)
@app.route("/x")
def h():
    from html import escape
    n = escape(request.args.get("n", ""))  # wrong context for SQL
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + n + "'")  # SK-06 TP
