"""CWE-306 — Missing Authentication for Critical Function. A destructive admin endpoint
has no authentication/authorization check. (Engine gap / partial.) FN probe."""
import sqlite3
from flask import Flask

app = Flask(__name__)
db = sqlite3.connect("app.db", check_same_thread=False)


@app.route("/admin/purge", methods=["POST"])
def purge():
    # no auth check on a destructive, privileged action → CWE-306
    db.execute("DELETE FROM users")
    db.commit()
    return "purged"
