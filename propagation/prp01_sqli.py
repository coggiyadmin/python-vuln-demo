from flask import Flask, request
import subprocess
import sqlite3
app = Flask(__name__)
@app.route("/x")
def h():
    import sqlite3
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + request.args.get("q", "") + "'")  # PRP-01 inline
