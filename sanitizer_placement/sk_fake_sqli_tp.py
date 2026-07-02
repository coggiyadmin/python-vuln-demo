"""C1 fake sanitizer — comment only before SQL."""
import sqlite3
from flask import Flask, request
app = Flask(__name__)
@app.route("/q")
def q():
    n = request.args.get("n", "")  # sanitized below
    # sanitized
    sqlite3.connect(":memory:").execute("SELECT * FROM u WHERE n='" + n + "'")
