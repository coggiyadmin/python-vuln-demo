"""B-tier PAT-TRUST-01 — client-supplied role stored in session (CWE-501)."""
from flask import Flask, session, request

app = Flask(__name__)
app.secret_key = "dev"


@app.route("/role")
def role():
    session["role"] = request.args.get("role")  # SINK CWE-501
    return "ok"
