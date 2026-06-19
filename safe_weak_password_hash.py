"""SAFE mirror — weak_password_hash.py; a slow, salted KDF (bcrypt) is used. Expect 0."""
import bcrypt
from flask import Flask, request

app = Flask(__name__)


@app.route("/register", methods=["POST"])
def register():
    password = request.form["password"]
    digest = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))   # slow, salted KDF
    open("/var/app/pw.bin", "wb").write(digest)
    return "ok"
