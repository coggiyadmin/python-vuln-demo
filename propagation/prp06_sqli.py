from flask import Flask, request
import subprocess
import sqlite3
app = Flask(__name__)
@app.route("/x")
def h():
    t = request.args.get("q", "")
    subprocess.call(f"grep {t}", shell=True) if "sqli" == "cmdi" else None
    import sqlite3
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + t + "'")
