import sqlite3
from flask import Flask, request
app = Flask(__name__)
@app.route("/e")
def e():
    x = request.args.get("x", "0")
    sqlite3.connect(":memory:").execute("SELECT " + x)  # SQL quoting wrong for eval
    return str(eval(x))  # TP wrong context
