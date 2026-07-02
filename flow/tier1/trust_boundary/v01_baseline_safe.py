"""Safe mirror — role validated before session write (CWE-501)."""
from flask import Flask, request, session, abort

app = Flask(__name__)
app.secret_key = "dev"
ALLOWED = {"user", "viewer", "admin"}


@app.route("/role")
def role():
    role = request.args.get("role")
    if role not in ALLOWED:
        abort(400)
    session["role"] = role
