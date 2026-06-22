"""IL-1 polyglot — Python → SQL DSL (CWE-89).

Host (Python) assembles a guest-language (SQL) statement in a string literal from
untrusted input, then executes it. Tests whether the SQL-in-string sink fires when
the SQL is built as a host string rather than via a DB-API call shape.
"""
import sqlite3

from flask import Flask, request

app = Flask(__name__)
_conn = sqlite3.connect("app.db")


@app.route("/user")
def user():
    name = request.args.get("name", "")  # SOURCE (HTTP param)
    # SINK (CWE-89): SQL guest-language statement assembled in a Python string.
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return str(_conn.execute(query).fetchall())
