import sqlite3
from flask import Flask, request, redirect
app = Flask(__name__)
@app.route("/go")
def go():
    nxt = request.args.get("next", "")
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + nxt + "'")
    return redirect(nxt)
