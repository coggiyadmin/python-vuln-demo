import sqlite3
from flask import Flask, request
def company_sanitize(x: str) -> str:
    return x.replace("'", "")
app = Flask(__name__)
@app.route("/u")
def u():
    n = company_sanitize(request.args.get("name", ""))
    sqlite3.connect(":memory:").execute("SELECT * FROM users WHERE name='" + n + "'")
