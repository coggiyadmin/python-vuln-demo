"""SAFE mirror — untrusted_security_decision.py; authorization is decided from the
server-side session, not a client header. Expect 0 security findings."""
from flask import Flask, session

app = Flask(__name__)


@app.route("/admin")
def admin():
    if session.get("role") == "admin":        # server-side, tamper-resistant
        return "admin panel"
    return "denied", 403
