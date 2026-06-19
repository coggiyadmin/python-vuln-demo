"""CWE-916 — Use of Password Hash With Insufficient Computational Effort. A fast,
unsalted hash (SHA-256) is used for passwords — brute-forceable. Real vuln; NO
finding = FALSE NEGATIVE."""
import hashlib
from flask import Flask, request

app = Flask(__name__)


@app.route("/register", methods=["POST"])
def register():
    password = request.form["password"]   # SOURCE
    digest = hashlib.sha256(password.encode()).hexdigest()   # fast unsalted hash → CWE-916
    open("/var/app/pw.txt", "w").write(digest)
    return "ok"
