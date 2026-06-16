"""Combination #11 — FAN-OUT / dedup (Python). One tainted source reaches
multiple distinct sinks; the engine should report one finding per sink type
(3 findings), not collapse to one or duplicate per source path."""
import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)
db = sqlite3.connect("app.db")


@app.route("/fanout")
def fanout():
    u = request.args.get("u", "")        # single SOURCE
    os.system("echo " + u)                # sink 1 — command_injection (CWE-78)
    open("/var/app/data/" + u)            # sink 2 — path_traversal (CWE-22)
    db.cursor().execute("SELECT * FROM t WHERE id = " + u)  # sink 3 — sql_injection (CWE-89)
    return "ok"
