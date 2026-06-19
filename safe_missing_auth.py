"""SAFE mirror — missing_auth.py; the critical action requires an authenticated admin
session. Expect 0 security findings."""
import sqlite3
from flask import Flask, session, abort

app = Flask(__name__)
db = sqlite3.connect("app.db", check_same_thread=False)


@app.route("/admin/purge", methods=["POST"])
def purge():
    if not session.get("is_admin"):           # server-side authz check
        abort(403)
    db.execute("DELETE FROM users")
    db.commit()
    return "purged"
