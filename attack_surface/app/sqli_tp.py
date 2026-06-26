from flask import Flask, request
import sqlite3
app = Flask(__name__)
@app.route("/q")
def q():
    n = request.args.get("n", "")
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + n + "'")
