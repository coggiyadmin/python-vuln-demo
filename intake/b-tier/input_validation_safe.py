"""Safe mirror — PAT-INPUT-01"""
import sqlite3
from flask import Flask, request, abort

app = Flask(__name__)
db = sqlite3.connect("app.db", check_same_thread=False)
MAX_TRANSFER = 1000


@app.route("/transfer")
def transfer():
    amount = int(request.args["amount"])
    if amount <= 0 or amount > MAX_TRANSFER:
        abort(400)
    to_user = request.args["to"]
    db.execute(
        "UPDATE accounts SET balance = balance - ? WHERE user = ?",
        (amount, to_user),
    )
    db.commit()
    return "ok"
