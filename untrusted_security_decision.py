"""CWE-807 — Reliance on Untrusted Inputs in a Security Decision. A client-supplied
header is trusted to grant admin access. (Engine gap.) FN probe."""
from flask import Flask, request

app = Flask(__name__)


@app.route("/admin")
def admin():
    # trusts an attacker-controllable request header for authorization → CWE-807
    if request.headers.get("X-Is-Admin") == "true":
        return "admin panel"
    return "denied", 403
