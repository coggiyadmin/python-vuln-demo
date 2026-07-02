"""C1 wrong-context — SQL quote escape before HTML sink."""
import sqlite3
from flask import Flask, request
app = Flask(__name__)
@app.route("/x")
def x():
    q = request.args.get("q", "").replace("'", "''")
    return "<p>" + q + "</p>"
