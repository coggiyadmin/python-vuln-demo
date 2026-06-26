import sqlite3
from flask import Flask, request
app = Flask(__name__)
@app.route("/greet")
def greet():
    name = request.args.get("name", "")
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + name + "'")
    return "Hello %s" % name
