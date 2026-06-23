"""SAFE mirror — csrf_probe.py; state-changing POST gated by a per-session CSRF token."""
import secrets

from flask import Flask, jsonify, request, session

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


@app.route("/transfer", methods=["POST"])
def transfer():
    token = request.form.get("csrf_token", "")
    if not token or token != session.get("csrf_token"):
        return jsonify({"error": "forbidden"}), 403
    to = request.form["to"]
    amt = request.form["amount"]
    return jsonify({"transferred": amt, "to": to})
