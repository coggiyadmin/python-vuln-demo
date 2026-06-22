"""IL-1 polyglot — SAFE mirror of interop_sql_in_string.py.
The SQL text is a constant with a bound `?` placeholder; the untrusted value is
passed as a parameter, never concatenated into the statement. The scanner MUST
produce ZERO security findings.
"""
import sqlite3

from flask import Flask, request

app = Flask(__name__)
_conn = sqlite3.connect("app.db")


@app.route("/user")
def user():
    name = request.args.get("name", "")  # SOURCE
    # Safe: parameterized query — `name` bound, not interpolated into the SQL.
    return str(_conn.execute("SELECT * FROM users WHERE name = ?", (name,)).fetchall())
