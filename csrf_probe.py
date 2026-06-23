"""FN probe — CWE-352 CSRF: state-changing POST with no anti-CSRF token (FN-16)."""
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/transfer", methods=["POST"])
def transfer():
    # SOURCE: cross-site forgeable form POST — no CSRF token / SameSite check
    to = request.form["to"]
    amt = request.form["amount"]
    # SINK (CWE-352): state-changing action executed with no anti-CSRF defense
    return jsonify({"transferred": amt, "to": to})
