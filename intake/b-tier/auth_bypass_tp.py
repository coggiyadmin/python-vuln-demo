"""B-tier PAT-AUTH-01 — missing auth on destructive admin route (CWE-306)."""
import sqlite3
from flask import Flask

app = Flask(__name__)
db = sqlite3.connect("app.db", check_same_thread=False)


@app.route("/admin/purge", methods=["POST"])
def purge():
    db.execute("DELETE FROM users")  # SINK CWE-306
    db.commit()
    return "purged"
