"""
FALSE-NEGATIVE PROBE CORPUS — every handler is a REAL SQL injection.

User input (request.args) reaches an unparameterized cursor.execute via a flow
pattern that taint engines commonly drop. Any handler that produces NO
sql_injection finding is a FALSE NEGATIVE.

direct() is the control: it MUST fire.
"""

import sqlite3
from flask import Flask, request

app = Flask(__name__)
db = sqlite3.connect("app.db")

_stored = {}


def _run(query: str):
    return db.cursor().execute(query).fetchall()


# CONTROL — direct flow, must fire
@app.route("/direct")
def direct():
    u = request.args.get("u", "")
    return str(db.cursor().execute("SELECT * FROM users WHERE name = '" + u + "'").fetchall())


# 1. INTERPROCEDURAL — taint passed into a helper that holds the sink
@app.route("/inter")
def inter():
    u = request.args.get("u", "")
    return str(_run("SELECT * FROM users WHERE name = '" + u + "'"))


# 2. CONTAINER (list) — taint stored in a list element, retrieved
@app.route("/list")
def via_list():
    names = []
    names.append(request.args.get("u", ""))
    return str(_run("SELECT * FROM users WHERE name = '" + names[0] + "'"))


# 3. CONTAINER (dict) — taint stored as a dict value
@app.route("/dict")
def via_dict():
    _stored["name"] = request.args.get("u", "")
    return str(_run("SELECT * FROM users WHERE name = '" + _stored["name"] + "'"))


# 4. STRING TRANSFORM — .upper().strip() preserves taint
@app.route("/transform")
def via_transform():
    u = request.args.get("u", "").upper().strip()
    return str(_run("SELECT * FROM users WHERE name = '" + u + "'"))


# 5. ALIASING — taint copied through intermediate variables
@app.route("/alias")
def via_alias():
    a = request.args.get("u", "")
    b = a
    c = b
    return str(_run("SELECT * FROM users WHERE name = '" + c + "'"))


# 6. F-STRING — taint interpolated via f-string
@app.route("/fstring")
def via_fstring():
    u = request.args.get("u", "")
    return str(_run(f"SELECT * FROM users WHERE name = '{u}'"))


# 7. % FORMAT — taint via percent formatting
@app.route("/percent")
def via_percent():
    u = request.args.get("u", "")
    return str(_run("SELECT * FROM users WHERE name = '%s'" % u))


# 8. .format() — taint via str.format
@app.route("/format")
def via_format():
    u = request.args.get("u", "")
    return str(_run("SELECT * FROM users WHERE name = '{}'".format(u)))
