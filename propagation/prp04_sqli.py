from flask import Flask, request
import subprocess
import sqlite3
app = Flask(__name__)
class Box:
    pass
@app.route("/x")
def h():
    b = Box()
    b.t = request.args.get("q", "")
    import sqlite3
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + b.t + "'")  # PRP-04 field
