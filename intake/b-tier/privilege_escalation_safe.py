"""Safe mirror — PAT-PRIV-01"""
from flask import Flask, session, abort

app = Flask(__name__)
app.secret_key = "dev"


@app.route("/elevate")
def elevate():
    if not session.get("is_staff"):
        abort(403)
    session["role"] = "admin"
    return "ok"
