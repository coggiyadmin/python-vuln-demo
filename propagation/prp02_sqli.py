from flask import Flask, request
import subprocess
import sqlite3
app = Flask(__name__)
@app.route("/x")
def h():
    t = request.args.get("q", "")  # SOURCE
    u = t
    v = u
    import sqlite3
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + v + "'")  # PRP-02 alias
