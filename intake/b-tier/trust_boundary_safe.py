"""Safe mirror — PAT-TRUST-01"""
from flask import Flask, session, request, abort

app = Flask(__name__)
app.secret_key = "dev"
ALLOWED = {"user", "viewer"}


@app.route("/role")
def role():
    role = request.args.get("role")
    if role not in ALLOWED:
        abort(400)
    session["role"] = role
    return "ok"
