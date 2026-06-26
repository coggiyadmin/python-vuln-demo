from flask import Flask, request
import subprocess
import sqlite3
app = Flask(__name__)
@app.route("/x")
def h():
    parts = []
    for x in request.args.getlist("q"):
        parts.append(x)
    t = "".join(parts)
    import sqlite3
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + t + "'")  # PRP-10 collect
