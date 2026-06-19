"""CWE-523 — Unprotected Transport of Credentials. Credentials are POSTed over plain
HTTP (no TLS). Real vuln; NO finding = FALSE NEGATIVE."""
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    user = request.form["user"]
    password = request.form["password"]   # SOURCE (credential)
    # credentials sent over cleartext http:// → CWE-523
    requests.post("http://auth.internal/login", data={"u": user, "p": password})
    return "ok"
