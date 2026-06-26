from flask import Flask, request
import subprocess
import sqlite3
app = Flask(__name__)
CACHE = {}
@app.route("/a")
def a():
    CACHE["v"] = request.args.get("q", "")
    return "ok"
@app.route("/b")
def b():
    t = CACHE.get("v", "")
    import sqlite3
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + t + "'")  # PRP-09 stored2
