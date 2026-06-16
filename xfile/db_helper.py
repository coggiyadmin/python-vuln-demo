"""Cross-file taint — the SINK side. Imported by controller.py."""
import os
import sqlite3

_conn = sqlite3.connect("app.db")


def run_user_query(name: str):
    # SINK: `name` arrives tainted from controller.py across the file boundary
    return _conn.cursor().execute(
        "SELECT * FROM users WHERE name = '" + name + "'"
    ).fetchall()


def run_command(arg: str):
    # SINK: command injection across files (arg tainted at end — no #62 confound)
    os.system("echo " + arg)
