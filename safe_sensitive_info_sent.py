"""SAFE mirror — sensitive_info_sent.py; only non-sensitive fields are projected. Expect 0."""
from flask import Flask, jsonify

app = Flask(__name__)
USER = {"id": 7, "name": "ada", "password_hash": "$2b$12$abcdef", "api_token": "sk-live-9931"}


@app.route("/me")
def me():
    return jsonify({"id": USER["id"], "name": USER["name"]})  # secrets excluded
