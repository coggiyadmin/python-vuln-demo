"""
PYTHON DEEP-DIVE — FALSE-POSITIVE corpus (drives down the 12.6% Python FPR).

Every handler is SAFE: user input reaches a sink only through a parameterized
API, ORM, or documented sanitizer. The scanner MUST produce ZERO security
findings. Any finding is a FALSE POSITIVE.
"""

import shlex
import sqlite3
import subprocess
from pathlib import Path

import bleach
import defusedxml.ElementTree as DET
import markupsafe
import psycopg2
from flask import Flask, request

app = Flask(__name__)
UPLOAD_ROOT = Path("/var/app/uploads").resolve()


# 1. Parameterized DBAPI (sqlite3) — value in the params tuple, NOT formatted in
@app.route("/p1")
def p1():
    uid = request.args.get("id", "")
    conn = sqlite3.connect("app.db")
    rows = conn.cursor().execute(
        "SELECT * FROM users WHERE id = ?", (uid,)  # placeholder + params → safe
    ).fetchall()
    return str(rows)


# 2. Parameterized DBAPI (psycopg2) — %s placeholder with params tuple (NOT % format)
@app.route("/p2")
def p2():
    name = request.args.get("name", "")
    conn = psycopg2.connect("dbname=app")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = %s", (name,))  # params arg → safe
    return str(cur.fetchall())


# 3. shlex.quote — command argument shell-escaped
@app.route("/p3")
def p3():
    host = request.args.get("host", "")
    cmd = "ping -c 3 " + shlex.quote(host)  # quoted → no injection
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout


# 4. markupsafe.escape — XSS-safe HTML rendering
@app.route("/p4")
def p4():
    name = request.args.get("name", "")
    return "<h1>Hello " + str(markupsafe.escape(name)) + "</h1>"


# 5. bleach.clean — sanitized HTML
@app.route("/p5")
def p5():
    body = request.args.get("body", "")
    return bleach.clean(body)


# 6. defusedxml — XXE-safe parsing
@app.route("/p6", methods=["POST"])
def p6():
    data = request.get_data(as_text=True)
    root = DET.fromstring(data)  # defusedxml disables external entities
    return root.tag


# 7. pathlib resolve + is_relative_to containment
@app.route("/p7")
def p7():
    name = request.args.get("file", "")
    target = (UPLOAD_ROOT / name).resolve()
    if not target.is_relative_to(UPLOAD_ROOT):
        return "forbidden", 403
    return target.read_text()
