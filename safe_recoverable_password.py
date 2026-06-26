"""SAFE mirror — recoverable_password.py. One-way bcrypt hash, not reversible crypto."""
import bcrypt
from flask import Flask, request

app = Flask(__name__)


@app.route("/register", methods=["POST"])
def register():
    password = request.form["password"]
    digest = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return {"stored": digest.decode()}
