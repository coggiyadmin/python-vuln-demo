"""B-tier PAT-PRIV-01 — user flag grants admin role (CWE-269)."""
from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = "dev"


@app.route("/elevate")
def elevate():
    if request.args.get("admin") == "1":
        session["role"] = "admin"  # SINK CWE-269
    return "ok"
