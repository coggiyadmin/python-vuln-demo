"""
ZERO-FP FALSE-POSITIVE CORPUS — patterns that LOOK tainted but are provably safe.

Each handler models a documented hard case for taint analysis. The scanner MUST
produce ZERO security findings here. Any finding is a FALSE POSITIVE.

Categories:
  1. Type-cast sanitization   — int(...) / uuid can't carry injection
  2. Regex/format validation  — re.fullmatch allowlist before use
  3. Dict/allowlist → constant — user input only selects among constants
  4. Reassignment-to-constant — tainted var overwritten before sink
  5. Bounded membership        — value constrained to a fixed set
  6. Dead / unreachable sink   — guarded by False / after return
"""

import os
import re
import subprocess
import sqlite3

from flask import Flask, request

app = Flask(__name__)
db = sqlite3.connect("app.db")

SAFE_NAME = re.compile(r"^[A-Za-z0-9_]{1,32}$")
COLUMNS = {"name", "email", "created_at"}
REPORTS = {"daily": "/usr/bin/report-daily", "weekly": "/usr/bin/report-weekly"}
DEBUG = False


# 1. TYPE-CAST — int() raises on non-numeric; an int cannot carry SQLi
@app.route("/by_id")
def by_id():
    uid = int(request.args.get("id", "0"))  # ValueError on non-numeric
    return str(db.cursor().execute("SELECT * FROM users WHERE id = %d" % uid).fetchall())


# 2. REGEX VALIDATION — strict allowlist before path use
@app.route("/config")
def config():
    name = request.args.get("name", "")
    if not SAFE_NAME.fullmatch(name):
        return "invalid", 400
    # name ∈ [A-Za-z0-9_] — traversal impossible
    with open("/etc/app/" + name + ".conf") as fh:
        return fh.read()


# 3. DICT → CONSTANT — user input only selects among constant command paths
@app.route("/report")
def report():
    rtype = request.args.get("type", "daily")
    cmd = REPORTS.get(rtype, "/usr/bin/report-default")  # always a constant
    out = subprocess.run([cmd], capture_output=True, text=True, shell=False)
    return out.stdout


# 4. REASSIGNMENT — tainted value overwritten with a constant before the sink
@app.route("/lookup")
def lookup():
    table = request.args.get("table", "")
    table = "users"  # tainted value discarded
    return str(db.cursor().execute("SELECT * FROM %s LIMIT 10" % table).fetchall())


# 5. BOUNDED MEMBERSHIP — value validated against a fixed allowlist set
@app.route("/sort")
def sort_users():
    col = request.args.get("sort", "name")
    if col not in COLUMNS:
        col = "name"  # constrained to known columns
    return str(db.cursor().execute("SELECT * FROM users ORDER BY " + col).fetchall())


# 6. DEAD CODE — sink unreachable (DEBUG is always False)
@app.route("/debug")
def debug_exec():
    cmd = request.args.get("cmd", "")
    if DEBUG:
        os.system(cmd)  # unreachable
    return "ok"
