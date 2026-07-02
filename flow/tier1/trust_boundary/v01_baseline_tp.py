"""TP (CWE-501) — untrusted request value written into trusted session store."""
from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = "dev"


@app.route("/role")
def role():
    session["role"] = request.args.get("role")  # SINK (CWE-501)
