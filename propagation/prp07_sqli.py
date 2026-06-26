from flask import Flask, request
import subprocess
import sqlite3
app = Flask(__name__)
@app.route("/x")
def h():
    t = (request.args.get("q") or "") if request.args else ""
    import sqlite3
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + t + "'")  # PRP-07
