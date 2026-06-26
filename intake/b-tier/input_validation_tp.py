"""B-tier PAT-INPUT-01 — unbounded user amount in transfer (CWE-20)."""
import sqlite3
from flask import Flask, request

app = Flask(__name__)
db = sqlite3.connect("app.db", check_same_thread=False)


@app.route("/transfer")
def transfer():
    amount = int(request.args["amount"])  # SINK CWE-20 — no bounds check
    to_user = request.args["to"]
    db.execute(
        "UPDATE accounts SET balance = balance - ? WHERE user = ?",
        (amount, to_user),
    )
    db.commit()
    return "ok"
