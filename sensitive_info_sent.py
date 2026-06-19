"""CWE-201 — Insertion of Sensitive Information Into Sent Data. The full user record, including
the password hash and API token, is serialized to the client. NO finding = FN."""
from flask import Flask, jsonify

app = Flask(__name__)
USER = {"id": 7, "name": "ada", "password_hash": "$2b$12$abcdef", "api_token": "sk-live-9931"}


@app.route("/me")
def me():
    return jsonify(USER)                   # leaks password_hash + api_token → CWE-201
